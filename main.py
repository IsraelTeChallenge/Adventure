from bottle import route, run, template, static_file, request
import json
import pymysql


connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'root',
                             db = 'adventure',
                             charset = 'utf8',
                             cursorclass=pymysql.cursors.DictCursor)


@route("/", method="GET")
def index():
    return template("adventure.html")


@route("/start", method="POST")
def start():
    username = request.POST.get("user")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT username FROM userinfo WHERE username = '{}'".format(username)
            cursor.execute(sql)
            result = cursor.fetchone()
            if not result:
                resgister_sql = "INSERT INTO userinfo (username) VALUE ('{}')".format(username)
                cursor.execute(resgister_sql)
                get_user_sql = "SELECT * FROM userinfo WHERE username = '{}'".format(username)
                cursor.execute(get_user_sql)
                register_result = cursor.fetchone()
                print(register_result)
                print("Registering works")
            pull_user_info_sql = "SELECT * from userinfo where username = '{}'".format(username)
            cursor.execute(pull_user_info_sql)
            user_info_sql = cursor.fetchone()
            print(user_info_sql)
            print(type(user_info_sql['story_id']))
            pull_user_story_sql = "select distinct story_question_text from questions inner join userinfo on questions.story_id = userinfo.story_id where username = '{}'".format(username)
            cursor.execute(pull_user_story_sql)
            user_story_pull = cursor.fetchone()
            user_story_text = list(user_story_pull.values())
            print(user_story_text)
            pull_story_questions_sql = "select answer_text, goes_to_story_id from questions inner join userinfo on questions.story_id = userinfo.story_id where username = '{}'".format(username)
            cursor.execute(pull_story_questions_sql)
            story_questions = cursor.fetchall()
            pull_images_sql = "select distinct questions.image_used from questions inner join userinfo on questions.story_id = userinfo.story_id where username = '{}'".format(username)
            cursor.execute(pull_images_sql)
            image = cursor.fetchall()
            #image_list = list(image.values())
            print(image)
            image_show = (image[0]['image_used'])
    except Exception as e:
        print(repr(e))


    #todo add the next step based on db
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
            get_next_story_sql = "select distinct story_question_text from questions where story_id = '{}'".format(next_story_id)
            cursor.execute(get_next_story_sql)
            next_story_pull = cursor.fetchone()
            next_story_text = list(next_story_pull.values())
            print(next_story_text)
            pull_story_questions_sql = "select answer_text, goes_to_story_id from questions where story_id ='{}'".format(next_story_id)
            cursor.execute(pull_story_questions_sql)
            story_questions = cursor.fetchall()
            update_user_story_sql = "update userinfo set story_id = '{}' where username = '{}'".format(next_story_id,username)
            cursor.execute(update_user_story_sql)
            pull_images_sql = "select distinct image_used from questions where story_id = '{}'".format(next_story_id)
            cursor.execute(pull_images_sql)
            image = cursor.fetchall()
            #image_list = list(image.values())
            print(image)
            image_show = (image[0]['image_used'])
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

def main():
    run(host='localhost', port=9001)

if __name__ == '__main__':
    main()
