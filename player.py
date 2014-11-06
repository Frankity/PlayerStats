__module_name__ = "Player Stats"
__module_version__ = "0.9 "
__module_description__ = "Show the player stats and another shiets..."
__autor__ = "Douglas Brunal (AKA) Frankity"
 
import json
import urllib2
import xchat as XC
 
def players(word, word_eol, userdata):
    command = word[0]
    name = word[1]
    if command == "player":
        response = urllib2.urlopen('http://api.emulatornexus.com/v1/rome/persona/'+ name +'/stats')
        jdata = json.load(response)
        rank = '\002' + 'Rank: ' + '\002' + '\00307' + str(jdata['data']['rank']) + '\00302' 
        score = '\002' + '\00301' + 'Score: ' + '\00301' + '\002' + '\00307' + str(jdata['data']['score']) + '\00302' 
        kills = '\002' + '\00301' + 'Kills: ' + '\00301' + '\002' + '\00307' + str(jdata['data']['kills']) + '\00302' 
        deaths = '\002' + '\00301' + 'Deaths: ' + '\00301' + '\002' + '\00307' + str(jdata['data']['deaths']) + '\00302' 
                        
        try:
            print name +" - " + rank + " " + score + " " + kills + " " + deaths 
        except IOError, er:
            print er

XC.hook_command("player", players)
XC.prnt(__module_name__ + ' vesion ' + __module_version__ + 'loaded')