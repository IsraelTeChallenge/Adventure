from bottle import route, run, template, static_file, request
import json
import pymysql
from sys import argv

# Local
# connection = pymysql.connect(host = 'localhost',
#                              user = 'root',
#                              password = 'root',
#                              db = 'adventure',
#                              charset = 'utf8',
#                              cursorclass=pymysql.cursors.DictCursor)

#database
connection = pymysql.connect(host = 'sql9.freesqldatabase.com',
                           user = 'sql9157879',
                           password = '8HnCSPBpkI',
                           db = 'sql9157879',
                           charset = 'utf8',
                           cursorclass=pymysql.cursors.DictCursor)


@route("/", method="GET")
def index():
    return template("adventure.html")


def get_user_info(cursor, username):
    try:
        get_user_sql = "SELECT * FROM userinfo WHERE username = '{}'".format(username)
        cursor.execute(get_user_sql)
        get_user_result = cursor.fetchone()
    except Exception as e:
        print(repr(e))
        get_user_result = None

    return get_user_result


def get_story_sql(cursor, story_id):
    try:
        pull_user_story_sql = "select distinct story_question_text from questions where story_id = '{}'".format(story_id)
        cursor.execute(pull_user_story_sql)
        user_story_pull = cursor.fetchone()
        user_story_text = list(user_story_pull.values())

    except Exception as e:
        print(repr(e))
        user_story_text = None

    return user_story_text


def get_story_questions(cursor, story_id):
    try:
        pull_story_questions_sql = "select answer_text, goes_to_story_id from questions where story_id ='{}'".format(story_id)
        cursor.execute(pull_story_questions_sql)
        story_questions = cursor.fetchall()
    except Exception as e:
        print(repr(e))
        story_questions = None

    return story_questions


def get_story_image(cursor, story_id):
    try:
        pull_images_sql = "select distinct image_used from questions where story_id = '{}'".format(story_id)
        cursor.execute(pull_images_sql)
        image = cursor.fetchall()
        image_show = (image[0]['image_used'])
    except Exception as e:
        print(repr(e))
        image_show = None

    return image_show


@route("/start", method="POST")
def start():
    username = request.POST.get("user")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT username FROM userinfo WHERE username = '{}'".format(username)
            cursor.execute(sql)
            result = cursor.fetchone()
            user_info_sql = None

            if not result:
                resgister_sql = "INSERT INTO userinfo (username) VALUE ('{}')".format(username)
                cursor.execute(resgister_sql)

            user_info_sql = get_user_info(cursor, username)
            if not user_info_sql:
                if not result:
                    raise Exception("Registration failed")
                else:
                    raise Exception("User info pull failed")

            user_story_text = get_story_sql(cursor, user_info_sql['story_id'])
            if not user_story_text:
                raise Exception("Couldn't get story text")

            story_questions = get_story_questions(cursor, user_info_sql['story_id'])
            if not story_questions:
                raise Exception("Couldn't get story questions")

            image_show = get_story_image(cursor, user_info_sql['story_id'])
            if not image_show:
                raise Exception("Couldn't get the picture")
    except Exception as e:
        print(repr(e))


    return json.dumps({"user": username,
                       "text": user_story_text,
                       "image": image_show,
                       "options": story_questions
                       })

@route("/story", method="POST")
def story():
    username = request.POST.get("user")
    current_adv_id = request.POST.get("adventure")
    next_story_id = request.POST.get("next") #this is what the user chose - use it!
    try:
        with connection.cursor() as cursor:

            next_story_text = get_story_sql(cursor, next_story_id)
            if not next_story_text:
                raise Exception("Couldn't get story text")

            story_questions = get_story_questions(cursor, next_story_id)
            if not story_questions:
                raise Exception("Couldn't get story questions")

            image_show = get_story_image(cursor, next_story_id)
            if not image_show:
                raise Exception("Couldn't get the picture")

            update_user_story_sql = "update userinfo set story_id = '{}' where username = '{}'".format(next_story_id,username)
            cursor.execute(update_user_story_sql)
    except Exception as e:
        print(repr(e))

    return json.dumps({"user": username,
                       "text": next_story_text,
                       "image": image_show,
                       "options": story_questions
                       })
# ,
# "next": next_story_id

@route('/js/<filename:re:.*\.js$>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


# Local testing
# def main():
#     run(host='localhost', port=9001)

# Remote server
def main():
    run(host='0.0.0.0', port=argv[1])


if __name__ == '__main__':
    main()
