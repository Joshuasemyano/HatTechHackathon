wlecMsg = [0, "welcome msg", "hi"]
langMenu = [1, "languge menu", ""]
MenuPersInfoEN = [2, "personal information menu", ""]
langInsureEN = [3, "insurence menu", ""]
catgMenuEN = [4, "department menu", ""]
durMenuEN = [5, "duration menu", ""]
issuDetlMenuEN = [6, "issue details menu", ""]
docMenuEN = [7, "doctor list menu", ""]
genrDocMenuEN = [8, "general Doctors menu", ""]
dateDayMenuEN = [9, "date by day menu", ""]
dateTimMenuEN = [10, "date by time menu", ""]
bayMSgEN = [11, "bay message", ""]

MenuPersInfoAR = [2, "personal information menu",  "" ,  "Ar"]
langInsureAR = [3, "insurence menu",   "",  "Ar"]
catgMenuAR = [4, "department menu",   "",  "Ar"]
durMenuAR = [5, "duration menu",   "",  "Ar"]
issuDetlMenuAR = [6, "issue details menu", "",  "Ar"]
docMenuAR = [7, "doctor list menu",   "",  "Ar"]
genrDocMenuAR = [8, "general Doctors menu",   "",  "Ar"]
dateDayMenuAR = [9, "date by day menu",   "",  "Ar"]
dateTimMenuAR = [10, "date by time menu",   "",  "Ar"]
bayMSgAR = [11, "bay message",  "" ,  "Ar"]


def mainFun(menuNum):
    if menuNum ==str(1):
        print (wlecMsg[0])
        print(wlecMsg[2])
    elif menuNum == str(2):
        print("Hello")
      # print ("hihihihih")

user_msg = input("Please insert a number: ")
mainFun(user_msg)
# print(wlecMsg)

    


#run. mainFun()