# -*- coding: utf-8 -*-

from util import hook, textgen, text
import random
from random import randint
import json

color_codes = {
    "<r>": "\x02\x0305",
    "<g>": "\x02\x0303",
    "<y>": "\x02"
}

with open("plugins/data/8ball_responses.txt") as f:
    responses = [line.strip() for line in f.readlines() if not line.startswith("//")]


with open("plugins/data/larts.txt") as f:
    larts = [line.strip() for line in f.readlines() if not line.startswith("//")]


with open("plugins/data/insults.txt") as f:
    insults = [line.strip() for line in f.readlines() if not line.startswith("//")]


with open("plugins/data/flirts.txt") as f:
    flirts = [line.strip() for line in f.readlines() if not line.startswith("//")]


with open("plugins/data/fishboles.txt") as f:
    lewds = [line.strip() for line in f.readlines() if not line.startswith("//")]


def get_generator(_json, variables):
    data = json.loads(_json)
    return textgen.TextGenerator(data["templates"], data["parts"], variables=variables)


def send_phrase(inp,attack,nick,conn,me,notice,chan):
    target = inp.strip()
    if " " in target:
        notice("Invalid username!")
        return

    # if the user is trying to make the bot slap itself, slap them
    if target.lower() == conn.nick.lower() or target.lower() == "itself": target = nick

    values = {"user": target,"nick": conn.nick, "channel": chan, "yiffer": nick}
    #if inp.split(" ")[-1].isdigit: phrase = attack[int(inp.split(" ")[-1].strip())-1]
    #else:
    phrase = random.choice(attack)
    # act out the message
    me(phrase.format(**values).decode('utf-8', "ignore"))
    return


@hook.command('8ball')
def eightball(input, me=None):
    """8ball <question> -- The all knowing magic eight ball,
    =in electronic form. Ask and it shall be answered!"""
    magic = text.multiword_replace(random.choice(responses), color_codes)
    me("shakes the magic 8 ball... {}".format(magic))
    return


@hook.command
def lart(inp, me=None, nick=None, conn=None, notice=None, chan=None):
    """lart <user> -- LARTs <user>."""
    send_phrase(inp,larts,nick,conn,me,notice, chan)
    return


@hook.command
def insult(inp, me=None, nick=None, conn=None, notice=None, chan=None):
    """insult <user> -- Makes the bot insult <user>."""
    send_phrase(inp,insults,nick,conn,me,notice, chan)
    return


@hook.command(autohelp=False)
def yiff(inp, me=None, nick=None, conn=None, notice=None, chan=None):
    """yiff <user> -- yiffs <user>."""
    send_phrase(inp,yiffs,nick,conn,me,notice, chan)
    return


@hook.command
def kill(inp, me=None, nick=None, conn=None, notice=None):
    """kill <user> -- Makes the bot kill <user>."""
    target = inp.strip()

    if " " in target:
        notice("Invalid username!")
        return

    # if the user is trying to make the bot kill itself, kill them
    if target.lower() == conn.nick.lower() or target.lower() == "itself":
        target = nick

    variables = {
        "user": target
    }

    with open("plugins/data/kills.json") as f:
        generator = get_generator(f.read(), variables)

    # act out the message
    me(generator.generate_string())
    return


@hook.command
def slap(inp, me=None, nick=None, conn=None, notice=None):
    """slap <user> -- Makes the bot slap <user>."""
    target = inp.strip()

    if " " in target:
        notice("Invalid username!")
        return

    # if the user is trying to make the bot slap itself, slap them
    if target.lower() == conn.nick.lower() or target.lower() == "itself":
        target = nick

    variables = {
        "user": target
    }

    with open("plugins/data/slaps.json") as f:
        generator = get_generator(f.read(), variables)

    # act out the message
    me(generator.generate_string())
    return

@hook.command
def cookie(inp, me=None, nick=None, conn=None, notice=None):
    """cookie <user> -- Gives <user> a cookie."""
    target = inp.strip()

    if " " in target:
        notice("Invalid username!")
        return

    # if the user is trying to make the bot cookie itself, cookie them
    if target.lower() == conn.nick.lower() or target.lower() == "itself":
        target = nick

    variables = {
        "user": target
    }

    with open("plugins/data/cookies.json") as f:
        generator = get_generator(f.read(), variables)

    # act out the message
    me(generator.generate_string())
    return

@hook.command
def rekt(inp, me=None, nick=None, conn=None, notice=None):
    """rekt <user> -- Makes the bot rekt <user>."""
    target = inp.strip()

    if " " in target:
        notice("Invalid username!")
        return

    # if the user is trying to make the bot rekt itself, rekt them
    if target.lower() == conn.nick.lower() or target.lower() == "itself":
        target = nick

    variables = {
        "user": target
    }

    with open("plugins/data/rekt.json") as f:
        generator = get_generator(f.read(), variables)

    # act out the message
    me(generator.generate_string())
    return

@hook.command
def tslap(inp, me=None, nick=None, conn=None, notice=None):
    """tslap <user> -- Slaps <user> with a trout."""
    target = inp.strip()

    if " " in target:
        notice("Invalid username!")
        return

    # if the user is trying to make the bot trout itself, trout them
    if target.lower() == conn.nick.lower() or target.lower() == "itself":
        target = nick

    variables = {
        "user": target
    }

    with open("plugins/data/trouts.json") as f:
        generator = get_generator(f.read(), variables)

    # act out the message
    me(generator.generate_string())
    return


def get_filename(action,notice):
    if 'loli' in action: action = 'lolis'
    elif 'insult' in action: action = 'insults'
    elif 'kek' in action: action = 'keks'
    elif 'flirt' in action: action = 'flirts'
    elif 'moist' in action: action = 'moists'
    elif 'lewd' in action: action = 'lewds'
    elif 'qt' in action: action = 'qts'
    elif 'urmom' in action: action = 'urmom'
    elif 'honry' in action: action = 'old'
    elif 'old' in action: action = 'old'
    elif 'fortune' in action: action = 'fortunes'
    elif 'fishbole' in action: action = 'fishboles'
    elif 'troll' in action: action = 'troll'
    elif 'gain' in action: action = 'gainz'
    elif 'nsfw' in action: action = 'nsfw'
    elif 'rekt' in action: action = 'rekt'
    else:
        notice('Invalid action')
        return
    return action

@hook.command
def add(inp,notice=None, channeladminonly=True):
    """add <type> <data> -- appends <data> to <type>.txt"""
    #inp = inp.split('add')[1]
    action = inp.split(' ')[0]
    text = inp.replace(action,'').strip()
    action=get_filename(action,notice)

    with open('plugins/data/{}.txt'.format(action), 'a') as file:
        file.write(u'{}\n'.format(text).encode('utf-8'))

    notice('{} added.'.format(action))
    file.close()
    return

def process_text(inp,name,notice):
    # if not inp or inp is int:
    if 'add' in inp:
        add(inp,name,notice)
    else:
        with open("plugins/data/{}.txt".format(name)) as file:
            lines = [line.strip() for line in file.readlines() if not line.startswith("//")]
        linecount = len(lines) - 1

        if inp and inp.isdigit(): num = int(inp) - 1
        else: num = randint(0,linecount)

        if num > linecount or num < 0:
            return "Theres nothing there baka"

        reply='\x02[{}/{}]\x02 {}'.format(num+1,linecount+1,lines[num]).decode('utf-8')

        file.close()
        lines = []
        return reply


    # else:
    #     action = inp.split(' ')[0]
    #     text = inp.replace(action,'').strip()
    #     if "add" in inp and text:
    #         with open('plugins/data/{}.txt'.format(name), 'a') as file:
    #             file.write(u'{}\n'.format(text).encode('utf-8'))
    #         file.close()


# def process_text(inp,name,notice):
#     num = -1
#     if inp:
#         action = inp.split(' ')[0]
#         text = inp.replace(action,'').strip()

#         if action.isdigit(): num = int(action) - 1
#         elif text.isdigit(): num = int(text) - 1

#         elif 'add' in action:
#             if 'http:' in text:
#                 with open('plugins/data/{}.txt'.format(name), 'a') as file:
#                     file.write(u'{}\n'.format(text).encode('utf-8'))
#                 notice('{} added.'.format(action))
#                 file.close()
#                 return
#             else:
#                 notice('No image to add.')
#                 return
#         elif 'del' in action:
#             num = int(text) - 1
#             notice('Deleted {}: {}.'.format(action,text))
#             with open("plugins/data/{}.txt".format(name)) as file:
#                 lines = [line.strip() for line in file.readlines() if not line.startswith("//")]
#                 lines = lines.replace(lines[num],'')
#             print "deleting"


#     with open("plugins/data/{}.txt".format(name)) as file:
#         lines = [line.strip() for line in file.readlines() if not line.startswith("//")]
#     linecount = len(lines) - 1
#     if num < 0: num = randint(0,linecount)
#     reply='\x02[{}/{}]\x02 {}'.format(num+1,linecount+1,lines[num]).decode('utf-8')


#     file.close()
#     lines =[]
#     return reply

@hook.command('wailord', autohelp=False)
@hook.command(autohelp=False)
def troll(inp, say=None,notice=None):
    """troll -- Trolls on demand"""
    say(process_text(inp,"trolls",notice))
    return

@hook.command(autohelp=False)
def fortune(inp,say=None,notice=None):
    """fortune -- Fortune cookies on demand."""
    say(process_text(inp,"fortunes",notice))
    return

@hook.command("fishbole", autohelp=False)
@hook.command(autohelp=False)
def fishbole(inp,say=None,notice=None):
    """fishbole -- Displays a random fishbole quote."""
    say(process_text(inp,"fishboles",notice))
    return








