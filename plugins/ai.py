import re
import random
from util import hook

responses = (
    ("hi.*{name}.*",              ("Hi!", "Hello!", "Greetings!", "Howdy!", "How are you?", "'sup", "Hey!","Time to abandon ship!")),
    (".*hello.*{name}.*",         ("Hi!", "Hello!", "Greetings!", "Howdy!", "How are you?", "'sup", "Hey!","Time to abandon ship!")),
    # (".*how are you.*",         ("I'm fine, thank you.","Tired","Leave me alone!","Bored.")),
    ("thanks {name}",             ("You're welcome!", "No problem, it was easy","Eh, it wasn't much","I didn't do anything...")),
    (".*kock",                   ("dem kock","dem kock")),
    (".*>dj",                   ("Join #DontJoinItsATrap, the most entertaining channel on Rizon!","Join #DontJoinItsATrap, the most entertaining channel on Rizon!")),
    (".*>nightmode",                   ("Check out KiwiIRC night mode: http://bit.ly/1W3mr4Z","Check out KiwiIRC night mode: http://bit.ly/1W3mr4Z")),
    (".*>msg",                   ("Play the lottery to win a prize! Signup by typing: 10/msg GOD xdcc list","Play the lottery to win a prize! Sign up by typing: 10/msg GOD xdcc list")),
    (".*>kek",                   ("4kekekekekekeke","7kek","9kek!","11KEK!")),
    (".*>rekt",                  ("4REKT!","4REKT!")),
    (".*>rip",                  ("1Rest in Peace","1RIP")),
    (".*>color",                  ("1C2o3l4o5r6!","1C2o3l4o5r6!")),
    (".*>wbnc",                  ("10Check out WBNC! #WBNC","10Check out WBNC! #WBNC")),
    (".*>website",                  ("4W24 has made a website! Check it out here: http://bit.ly/20P0cjJ","4W24 has made a website! Check it out here: http://bit.ly/20P0cjJ")),


)
    # ("yeah",                    ("yeah","yeah")),

# wise/smart
# 7205566175 - frankie

pronouns = {
    "i'm": "you're",
    "i": "you",
    "me": "you",
    "yours": "mine",
    "you": "I",
    "am": "are",
    "my": "your",
    "you're": "I'm",
    "was": "were"
}


@hook.singlethread
@hook.event('PRIVMSG')
def ai_sieve(paraml, input=None, notice=None, db=None, bot=None, nick=None, conn=None, server=None):
    server = server.split('.')[1]
    full_reply = ''

    # replace = {
    #     'nick':input.nick
    # }
    # process all aif

    # process uguu ai

    for pattern in responses:
        wildcards = []
        match = pattern[0].replace('{name}', bot.config['connections'][server.title()]['user'].lower())
        if re.match(match, input.msg.lower()):
            # print "Matched: {}".format(pattern[0])
            wildcards = filter(bool, re.split(pattern[0], input.msg.lower()))
            # replace pronouns
            wildcards = [' '.join(pronouns.get(word, word) for word in wildcard.split()) for wildcard in wildcards]

            response = random.choice(pattern[1])
            response = response.replace('{nick}',input.nick).replace('{name}', bot.config['connections'][server.title()]['user'].lower())
            response = response.format(*wildcards)
            full_reply+=response+' '
            return full_reply



    # ("(.*)",                 ("Can you please elaborate?", "I don't fully understand.", "Let's stop talking about this.", "How are you feeling about this?")),
    # ("i need (.*)",          ("Why do you need {}?", "Would it really help you to get {}?", "Are you sure you need {}?")),
    # ("why don't you (.*)",   ("Do you really think I don't {}?", "Perhaps eventually I will {}.", "Do you really want me to {}?")),
    # ("why can't I (.*)",     ("Do you think you should be able to {}?", "If you could {}, what would you do?", "I don't know -- why can't you {}?", "Have you really tried?")),
    # ("i can't (.*)",         ("How do you know you can't {}?", "Perhaps you could {}if you tried.", "What would it take for you to {}?")),
    # ("i am (.*)",            ("Did you come to me because you are {}?", "How long have you been {}?", "How do you feel about being {}?")),
    # ("are you (.*)",         ("Why does it matter whether I am {}?", "Would you prefer it if I were not {}?", "Perhaps you believe I am {}.", "I may be {}-- what do you think?")),
    # ("how (.*)",             ("How do you suppose?", "Perhaps you can answer your own question.", "Why can't you answer your question?", "What is it you're really asking?")),
    # ("i think (.*)",         ("Do you doubt {}?", "Do you really think so?", "But you're not sure {}?")),
    # ("(.*) friend (.*)",     ("Tell me more about your friends.", "What do you value in a friend?")),
    # ("yes",                  ("Okay, but can you tell me more?", "Can you actually be sure?", "You seem quite certain.")),
    # ("no",                   ("Why not?", "Can you tell me why you say no?", "Are you sure?")),
    # ("is it (.*)",           ("Do you think it is {}?", "Perhaps it's {}-- what do you think?", "If it were {}, what would you do?", "It could well be that {}.")),
    # ("can you (.*)",         ("If I could {}, then what?", "Why do you ask if I can {}?")),
    # ("can i (.*)",           ("Do you want to be able to {}?", "If you could {}, would you?")),
    # ("you are (.*)",         ("Why do you think I am {}?", "Perhaps you would like me to be {}.", "Are you really talking about yourself?")),
    # ("you're (.*)",          ("Why do you say I am {}?", "Why do you think I am {}?", "Are we talking about you, or me?")),
    # ("i don't (.*)",         ("Why don't you {}?", "DO you want to {}?")),
    # ("i feel (.*)",          ("Tell me more about these feelings.", "Do you often feel {}?", "When do you usually feel {}?", "When you feel {}, what do you do?")),
    # ("i have (.*)",          ("Why do you tell me that you've {}?", "Have you really {}?", "Now that you have {}, what will you do next?")),
    # ("i would (.*)",         ("Could you explain why you would {}?", "Why would you {}?", "Who else knows that you would {}?")),
    # ("is there (.*)",        ("Do you think there is {}?", "Is it likely that there is {}?", "Would you like there to be {}?")),
    # ("my name is (.*)",      ("Hi, {}",)),
    # ("my (.*)",              ("Why do you say that your {}?", "When your {}, how do you feel?")),
    # ("you (.*)",             ("We should be discussing you, not me.", "Why do you say that about me?", "Why do you care whether I {}?")),
    # ("i want (.*)",          ("What would it mean to you if you got {}?", "Why do you want {}?", "What would you do if you got {}?", "If you got {}, then what you do?")),
    # ("i don't know (.*)",    ("Perhaps you should learn.", "I don't know either.")),
    # ("i'm (.*)",             ("Why are you {}?",)),
    # ("because (.*)",         ("if {}, what else is true?", "Is that a good reason?", "Are there any other good reasons?", "Is that the only reason?", "Why do you think {}?")),
    # ("i (.*)",               ("Why do you {}?",)),
    # ("(.*) is (.*)",         ("Why is {} {}?",)),
    # ("(.*) can't (.*)",      ("Why can't {}, {}")),
    # ("why (.*)",             ("What do you think?", "Why do you think {}?", "Why don't you know the answer yourself?")),
    # ("(.*) are (.*)",        ("Why are {} {}?",)),
    # ("hi",                   ("Hi!", "Hello!", "Greetings!", "Howdy!", "how are you?", "I missed you!", ";_; its you again...","time to abandon ship")),



    #if re.match(r'^(s|S)/.*/.*\S*$', input.msg):
    #    correction(input,db,notice,say)
    #    return


    # print "running"
    # #random.seed()
    # #print "I'm psychiatrist bot. I can make you feel better. Tell me how you're feeling!"


    # input = re.split("[\.!?]",raw_input("> ").lower().rstrip('.!?'))
    # print input
    # full_reply=' '

    # for sentence in input:
    #     sentence=sentence.lstrip()
    #     for pattern in responses:
    #         wildcards = []
    #         if re.match(pattern[0], sentence):
    #             wildcards = filter(bool, re.split(pattern[0], sentence))
    #             # replace pronouns
    #             wildcards = [' '.join(pronouns.get(word, word) for word in wildcard.split()) for wildcard in wildcards]

    #             response = random.choice(pattern[1])
    #             response = response.format(*wildcards)
    #             full_reply+=response+' '

    #             break

    # print full_reply
