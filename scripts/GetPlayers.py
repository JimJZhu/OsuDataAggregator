#import the library used to query a website
import urllib2
mouse_list = []
tablet_list = []
#specify the url
for page_number in range(196, 200):
    url = "https://osu.ppy.sh/p/pp/?m=0&s=3&o=1&f=&page=" + str(page_number)
    #Query the website and return the html to the variable 'page'
    leaderboard_page = urllib2.urlopen(url)
    #import the Beautiful soup functions to parse the data returned from the website
    from bs4 import BeautifulSoup
    #Parse the html in the 'leaderboard_page' variable, and store it in Beautiful Soup format
    soup = BeautifulSoup(leaderboard_page, "lxml")
    for player in soup.find_all("tr"):
        player_url = player.get("onclick")
        if player_url is not None:
            player_url = player_url[20:len(player_url)-1]
            player_page = urllib2.urlopen("https://osu.ppy.sh/" + player_url)
            player_soup = BeautifulSoup(player_page, "lxml")
            #check playstyle
            if player_soup.find_all("div", class_="playstyle mouse using") and not player_soup.find_all("div", class_="playstyle tablet using"):
                #mouse
                print "Checking: " + player_soup.title.string + "...Mouse"
                mouse_list.append(player_url)
            elif player_soup.find_all("div", class_="playstyle tablet using"):
                #tablet
                print "Checking: " + player_soup.title.string + "...Tablet"
                tablet_list.append(player_url)

print "writing to mouse file..."
mouse_file = open('mouselist.txt', 'w')
for item in mouse_list:
      mouse_file.write(item + ", ")
mouse_file.close()

print "writing to tablet file..."
tablet_file = open('tabletlist.txt', 'w')
for item in tablet_list:
      tablet_file.write(item + ", ")
tablet_file.close()

print "done"