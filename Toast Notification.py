from win10toast import ToastNotifier
import time

toast = ToastNotifier()


annoyingAF = ["hi.", "ahem, hello", "hello??", "yooooo dude", "hey check mail",
              "check the mail please", "CHECK IT NOW!", "WILL YOU FUCKING....",
              "Fuck off then...."]

annoyingAFBody = ["you have received a new mail", "a new mail arrived", "check the mailbox",
                  "seriously...", "PLEASE DO IT", "JUST DO IT", "FUCKING CHECK THE MAILBOX",
                  "Im done with you man....", "im not getting paid enought for this..."]

for each in range(9):
    toast.show_toast(
        annoyingAF[each],
        annoyingAFBody[each],
        duration = 4,
        threaded = True)
    time.sleep(5)

#me discovering the cool toast notification function
    
