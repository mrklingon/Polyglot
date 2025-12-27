import time
import random
import neopixel
import board
import touchio
from prt import *

vowels = ""
consonants = ""
rules = []

def setWookie():
    cmpthink
    prt("Wookie",REPL)
    global vowels
    global consonants
    global rules

    vowels = "OUA"
    consonants = "WWRRRHHHWWWRR"
    rules = ["CvvvvC", "CVC", "VVCV", "VCVVVVC","VCVVC"]



grn = (0,20,0)
red = (20,0,0)
blue = (0,0,20)
colors=[grn,red,blue]
blank = (0,0,0)

REPL = True

def mkword():
    rule = rules[random.randrange(len(rules))]
    word = ""
    for i in range(len(rule)):
        r=rule[i]
        if r == "V":
            word = word + pickChar(vowels)
        if r == "v":
            if (random.randrange(100)>49):
                word = word + pickChar(vowels)
        if r == "C":
            con = pickChar(consonants)
            if (con == "g" and lang == 2):
                con = "gh"
            word = word + con
        if r == "c":
            if (random.randrange(100)>49):
                con = pickChar(consonants)
                if (con == "g" and lang == 2):
                    con = "gh"
                word = word + con

    return word

def setKlin():
    global vowels
    global consonants
    global rules
    prt("Klingon",REPL)
    vowels = "aeIouy"
    consonants = "bcDgHjlmnpqQStvwy'"
    rules = ["CVVC", "CVC", "CCVVC", "CVVC","CV"]

def setVul():
    prt("Vulcan",REPL)
    cmpthink()
    global vowels
    global consonants
    global rules

    vowels = "'iaei'uaiyaoia"
    consonants = "whltrkltkt'khthtrvttsnzh"
    rules = ["CVcvcv", "Cvcv", "Ccv", "Cvvcv","CvVccvcv"]


def setMando():
    prt("Mando'a",REPL)
    cmpthink()
    global vowels
    global consonants
    global rules

    vowels = "ouaaoaaaaeaeeeauiueaaeaeeaeoaeeaoaeooeaeaaeaeeeaeueeaieaaaoeeieiioaiaiaiae"
    consonants = "slstryshlntryshlntddthnhntcrcrtryshshtryshlnsh'''''''rslrl't'tdtd'tsh'hnshhn'tsh'cshk'tlsr'chkrvrrsrmsrmrdsnrrnrnrmjycrmjyc"

    rules = ["Cvvc", "CvCvC", "vCCvc", "cvVvCv","cvCCvc"]

def setRom():
    prt("Romulan",REPL)
    cmpthink()
    global vowels
    global consonants
    global rules

    vowels = "'eiueeeiia''"
    consonants = "skfhvhlnvhdhmnhl'rh"

    rules = ["cvCCv", "cvVCv", "cVvCC", "cvVvCv","cVvCCv"]
def pickChar(inp):
    return (inp[random.randrange(len(inp))])

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, auto_write=True)
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)


touched = time.monotonic()
Val = 0

def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1
def cmpthink():
    for i in range(3):
        for j in range(4):
            pixels[j]=random.choice(colors)
            time.sleep(.1)
    time.sleep(.2)
    pixels.fill(blank)

def wisdom(num,filename):
    global REPL
    qs = open(filename)
    for i in range(num+1):
        quote = qs.readline()
    cmpthink()
    prt(quote,REPL)
    qs.close()
    return quote

lines = file_len("sagan")
cmpthink()
setWookie()
lang=1
while True:

    if time.monotonic() - touched < 0.15:
        continue
    if touch1.value:

        Val = Val +1
        touched = time.monotonic()
    if touch2.value:
        Val = Val +2
        touched = time.monotonic()

    touched = time.monotonic()
    if Val == 1:
        dict = {}
        num = random.randrange(lines)
        quote = wisdom(num,"sagan")
        quote = quote.lower()
        q = ""
        for c in quote:
            if c >= "a" and c<="z":
                q = q+c
            else:
                q = q+ " "
        for w in q.split():
#prt(w,REPL)
            dict[w] = mkword()
        t = ""
        for w in q.split():
            t = t + " " + dict[w]

#prt(q,REPL)
        prt(t,REPL)

    time.sleep(.1)

    if Val == 2:
        lang = lang + 1
        if lang > 5:
            lang = 1

        if lang == 1:
            setWookie()

        if lang == 2:
            setKlin()

        if lang == 3:
            setVul()

        if lang == 4:
            setMando()

        if lang == 5:
            setRom()

        time.sleep(.25)
    if Val == 3:
        setKlin()
        lang = 2
    Val = 0
    time.sleep(.1)
