from time import *
import random as r
# print(time()) -- this show seconds from 1971 to the present time.
def mistake(par,user):
        error = 0
        for i in range(len(par)):
                try:
                   if par[i]!=user[i]:
                        error=error+1
                except:
                        error=error+1
        return error

def speedDelay(time_start,time_end,userinput):
        time_delay = time_end - time_start
        roundofftime = round(time_delay,2)
        speed = len(userinput)/roundofftime
        return round(speed)


while True:
  Qs = input("Ready to check your Speed ? yes/no : ")
  if Qs == 'yes':
    test = ["Hey this is presently a console application Ankit will transform this application into WebApp after this Semester",
        "Ankit is Genius","Ankit is ANN & DL Researcher","hey"]
    test1 = r.choice(test)

    print("testing...................")
    print(test1)
    print() # For giving line breaks -
    print()

    initialTime = time()
    testInput = input("Enter >> ")
    EndTime = time()

    print("Speed : ",speedDelay(initialTime,EndTime,testInput),"word per second..")
    print("Errors : ",mistake(test1,testInput))

  elif Qs =="no":
         print("thank you for visiting the algorithm")
         break
  else:
          print("Invalid Input ")

#  1st we want speed calculation
#  2nd we want Errors

