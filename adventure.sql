use adventure;

drop table if exists `userinfo`;
create table `userinfo` (
`username` varchar(16) not null,
`story_id` tinyint(2) not null default '1',
`current_life` tinyint(3) not null default '100',
`current_gold` tinyint(3) not null default '100',
primary key (`username`)
)ENGINE=MyISAM DEFAULT CHARSET=utf8;








drop table if exists `questions`;
create table `questions` (
`story_id` tinyint(2) not null default '0', 
`story_question_text` text,
`answer_id` tinyint(2) not null default'0', 
`answer_text` text, 
`notes` text,
`goes_to_story_id` tinyint(2) not null default '0',
`health_changes` tinyint(4) not null default '0', 
`gold_changes` tinyint(4) not null default '0',
foreign key userinfo(story_id) references userinfo (story_id)
)ENGINE=MyISAM DEFAULT CHARSET=utf8;


insert into `questions` (`story_id`, `story_question_text`, `answer_id`, `answer_text`, `notes`, `goes_to_story_id`, `health_changes`, `gold_changes`)
values ('1', "You're alone in the woods. There's no one around and your phone is dead. Out of the corner of your eye you spot him. Shia LaBeouf. What do you do?", '1', 'Fawn over him! You loved him in Transformers!', 'Not aggressive, but you drop your guard and lose some money.', '2', -20, -30),
('1', "You're alone in the woods. There's no one around and your phone is dead. Out of the corner of your eye you spot him. Shia LaBeouf. What do you do?", '2', 'Get into a powerful stance and shout "JUST DO IT!" ', 'Aggressive. Shia attacks and you suffer a fatal blow. Game over.', '9', -100, -100),
('1', "You're alone in the woods. There's no one around and your phone is dead. Out of the corner of your eye you spot him. Shia LaBeouf. What do you do?", '3', 'You keep walking. Something tells you that something is wrong.', 'Not aggressive, but pushes the story forward safely.', '3', 0, 0),
('1', "You're alone in the woods. There's no one around and your phone is dead. Out of the corner of your eye you spot him. Shia LaBeouf. What do you do?", '4', 'Break into a run. You have seen enough horror movies and late night TV to know that you should not be alone with anyone in the woods.','Aggressive. Leads into chase segment and drops money. Triggers combat', '3', -10, -20),
('2', "You're starstruck feelings blind you to your surroundings. As the two of you get closer, you suddenly find yourself on the ground. You've been suckerpunched by Shia LaBeouf! What's next?!", '1', 'Stand up and hug it out. He seems like a lovable guy, maybe it was a mistake?', 'Aggressive. Shia bites your jugular and you lose consciousness. Game over.', '9', -100, -100),
('2', "You're starstruck feelings blind you to your surroundings. As the two of you get closer, you suddenly find yourself on the ground. You've been suckerpunched by Shia LaBeouf! What's next?!", '2', "Get up and run! He's out of is mind!", 'Not aggressive, triggers combat.', '3', 0, 0),
('2', "You're starstruck feelings blind you to your surroundings. As the two of you get closer, you suddenly find yourself on the ground. You've been suckerpunched by Shia LaBeouf! What's next?!", '3', "Return the favor and punch him back! You ain't no sucka!", 'Aggressive. Triggers combat.', '4', -20, +20),
('2', "You're starstruck feelings blind you to your surroundings. As the two of you get closer, you suddenly find yourself on the ground. You've been suckerpunched by Shia LaBeouf! What's next?!", '4', 'Start insulting him. His modern art is trash and transformers was only good because of Megan Fox.', 'Aggressive. Triggers combat', '4', -40, 0),
('3', "He's following you about 30 feet back. He gets down on all fours and breaks into a sprint. He's gaining on you. Shia LaBeouf. You're looking for your car, but you're all turned around. He's almost upon you now and you can see there's blood on his face! My god, there's blood everywhere!",'1', "Run for your life! He's crazed and must be escaped at all costs! Is that a knife in his hands? Is this REALLY Hollywood superstar Shia LaBeouf?!", 'Not aggressive. Safely passes story, lose some health out of fear.', '5', -5, 0),
('3', "He's following you about 30 feet back. He gets down on all fours and breaks into a sprint. He's gaining on you. Shia LaBeouf. You're looking for your car, but you're all turned around. He's almost upon you now and you can see there's blood on his face! My god, there's blood everywhere!", '2', "Turn back and take him head on. He's just a regular guy with a drinking problem!", 'Aggressive. Triggers combat.', '4', -20, 0),
('3', "He's following you about 30 feet back. He gets down on all fours and breaks into a sprint. He's gaining on you. Shia LaBeouf. You're looking for your car, but you're all turned around. He's almost upon you now and you can see there's blood on his face! My god, there's blood everywhere!", '3', "Run! Run far away! You let the adrenaline in your body push you faster and farther than you can imagine!", 'Not aggressive. Lose health out of fear.', '5', -10, 0),
('3', "He's following you about 30 feet back. He gets down on all fours and breaks into a sprint. He's gaining on you. Shia LaBeouf. You're looking for your car, but you're all turned around. He's almost upon you now and you can see there's blood on his face! My god, there's blood everywhere!", '4', "You've been waiting your entire life for this moment. The day you can take Shia LaBeouf head on! You want your money back from all the Holes merchandise you bought. You got an old beat up Camaro because of him that didn't even make it to the summer. This is your revenge!", 'Aggressive. Triggers combat.', '4', -10, 20),
('4', "The adrenaline flowing through you, you plan take your stand against Shia LaBeouf. He's coming at you, what's your plan?!", '1', "Run up to him and fake him out. Have him collide face first with your fist. Show him who's the boss!", 'Aggressive. Stuns Shia, leads into option to either run or continue fighting.', '6', 0, 20),
('4', "The adrenaline flowing through you, you plan take your stand against Shia LaBeouf. He's coming at you, what's your plan?!", '2', "You notice the knife in his pocket. You take the first hit just so you can get close enough to steal it. Turn the tables and attack!", 'Aggressive. Continues combat, gain money, lose health.', '7', -20, 20),
('4', "The adrenaline flowing through you, you plan take your stand against Shia LaBeouf. He's coming at you, what's your plan?!", '3', "Run! Run far away! You let the adrenaline in your body push you faster and farther than you can imagine!", 'Not aggressive. Lose health out of fear.', '5', -10, 20),
('4', "The adrenaline flowing through you, you plan take your stand against Shia LaBeouf. He's coming at you, what's your plan?!", '4', "Grab him by his rat tail! Not gonna let some weirdo get the best of you!", 'Aggressive. Stuns Shia, leads into option to either run or continue fighting.', '6', -10, 0);