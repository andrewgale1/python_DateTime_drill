#Scenario: The company you work for just opened two new branches,
#one is in New York City, the other in London.
#They need a very simple program to find out if the branches are open or closed
#based on the current time of the Headquarters here in Portland. The hours of both
#branches are 9:00AM - 9:00PM in their own time zone. What is asked of you:
#Create code that will use the current time of the Portland HQ to find out
#the time in the NYC & London branches, then compare that time with the branches
#hours to see if they are open or closed. Print out if each of the two branches
#are open or closed.
#Guidelines: Use Python 2.7 IDLE, Use Datetime Module, Execute program on the Shell.

import datetime
from datetime import *
import pytz
from pytz import timezone
import time
now_utc = datetime.now(timezone('UTC'))


def getCurrentTimePdx():
    now_utc = datetime.now(timezone('UTC'))
    now_western = now_utc.astimezone(timezone('US/Pacific'))
    pdx_Time = now_western.strftime('%H : %M : %S')
    print ('The current time at Portland HQ is  '+ pdx_Time)
    if now_western.hour > 9 and now_western.hour < 21:
        print ("  -HQ is now Open.")
    else:
        print ("  -HQ is now Closed.")

def nycTime():
    now_utc = datetime.now(timezone('UTC'))
    now_eastern = now_utc.astimezone(timezone('US/Eastern'))
    nyc_Time = now_eastern.strftime('%H : %M : %S')
    print ('The current time at the NYC branch is  '+ nyc_Time)
    if now_eastern.hour > 9 and now_eastern.hour < 21:
        print ("  -this branch is now Open.")
    else:
        print ("  -this branch is now Closed.")

def londonTime():
    now_utc = datetime.now(timezone('UTC'))
    now_europe = now_utc.astimezone(timezone('Europe/London'))
    london_Time = now_europe.strftime('%H : %M : %S')
    print ('The current time at the London branch is  '+ london_Time)
    if now_europe.hour > 9 and now_europe.hour < 21:
        print ("  -this branch is now Open.")
    else:
        print ("  -this branch is now Closed.")


getCurrentTimePdx()
nycTime()
londonTime()

