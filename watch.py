import sys
import pyak
from time import sleep
from datetime import datetime

if len(sys.argv) != 3:
    print "Usage: {} long lat".format(sys.argv[0])

loc = pyak.Location(sys.argv[1], sys.argv[2])

yakker = pyak.Yakker(location=loc)

while 1:
    yaks = yakker.get_yaks()
    for i in yaks[::-1]:
        print(i.message + "   " + str(i.likes))
    print datetime.now()
    sleep(10)
