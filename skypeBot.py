import Skype4Py
import time
import sys
import random


class SkypeBot(object):
    def __init__(self):
        self.skype = Skype4Py.Skype(Events=self)
        self.skype.name = "Skype Bot"
        self.skype.Attach()

    def MessageStatus(self, message, status):
        if status == Skype4Py.cmsReceived or status == Skype4Py.cmsSent:
            print "message: ", message.Body #debug
            m = message.Body.split()
            for command, function in self.commands.items():
                if command in m[0]:
                    function(self, message)
                    break
                
    def commandxD(self, message):
        message.Chat.SendMessage("/me xD")

    def commandRandom(self, message):
        value = random.randint(0,10)
        message.Chat.SendMessage("/me " + str(value))

    def commandCommands(self, message):
        msg = "| "
        for command, function in self.commands.items():
            msg = msg + str(command) + " "
        message.Chat.SendMessage("/me " + msg)

    def commandGenji(self, message):
        message.Chat.SendMessage("/me MonsterMan1 is the best Genji (flex)")

    def commandDoIt(self, message):
        answer = "YES"
        if (random.randint(0,1)) == 0:
            answer = "NO"
        message.Chat.SendMessage("/me " + answer)

    def commandIMDB(self, message):
        movie = message.Body[6:]
        message.Chat.SendMessage("test: " + movie)
        # http://www.omdbapi.com/?t=mad+max+fury+road&y=&plot=short&r=json

    def commandYouTube(self, message):
        message.Chat.SendMessage("/me under construction")
        

    commands = {
        '!xD': commandxD,
        '!random': commandRandom,
        '!commands': commandCommands,
        '!genji': commandGenji,
        '!doit': commandDoIt,
        '!imdb': commandIMDB,
        '!youtube': commandYouTube
    }



if __name__ == "__main__":
    bot = SkypeBot()
    print("MonsterMannen SkypeBot running")

    while True:
        time.sleep(1.0)
        
