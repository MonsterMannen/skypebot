import Skype4Py
import time
import sys
import random
import requests


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
        movieTitle = message.Body[6:]
        url = "http://www.omdbapi.com/?t=" + movieTitle + "&y=&plot=short&r=json"
        r = requests.get(url)
        json = r.json()
        if json["Response"] == "True":
            imdbID = json["imdbID"]
            # Can only request info on a movie once to stop spammers
            if imdbID not in self.imdbIDs:
                title = json["Title"]
                year = json["Year"]
                rating = json["imdbRating"]
                self.imdbIDs.append(imdbID)
                # ghetto fix ascii character problem when printing
                if len(year) == 9:
                    year = year[:4] + "-" + year[5:]
                elif len(year) == 5:
                    year = year[:4] + "-"
                msg = title + "\n" + year + "\n" + rating
                decoded_string = msg.decode('string_escape')
                message.Chat.SendMessage(msg)
        else:
            print "response false"
            message.Chat.SendMessage(json["Error"])
        
    def commandYouTube(self, message):
        message.Chat.SendMessage("/me under construction")

    def commandClear(self, message):
        message.Chat.ClearRecentMessages()
        print "commandClear"

    def commandAidi(self, message):
        for i in range(69):
            message.Chat.SendMessage("aidi homo")
        

    commands = {
        '!xD': commandxD,
        '!random': commandRandom,
        '!commands': commandCommands,
        '!genji': commandGenji,
        '!doit': commandDoIt,
        '!imdb': commandIMDB,
        '!youtube': commandYouTube,
        '!clear': commandClear,
        '!aidi': commandAidi
    }

    # Cache all imdb results
    imdbIDs = []



if __name__ == "__main__":
    bot = SkypeBot()
    print("MonsterMannen SkypeBot running")

    while True:
        time.sleep(1.0)
