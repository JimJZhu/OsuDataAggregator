import csv
import urllib2
from bs4 import BeautifulSoup
total_pp_file = open('total_pp_tablet_lowtier.csv', 'w')
total_aim_file = open('total_aim_tablet_lowtier.csv', 'w')
aim_jump_file = open('aim_jump_tablet_lowtier.csv', 'w')
aim_flow_file = open('aim_flow_tablet_lowtier.csv', 'w')
aim_precision_file = open('aim_precision_tablet_lowtier.csv', 'w')
speed_file = open('speed_tablet_lowtier.csv', 'w')
stamina_file = open('stamina_tablet_lowtier.csv', 'w')
accuracy_file = open('accuracy_tablet_lowtier.csv', 'w')
with open('tabletlist.csv', 'rb') as tablet_list_file:
    tablet_reader = csv.reader(tablet_list_file, delimiter=',')
    tablet_list = list(tablet_reader)
    count = 0
    for player in tablet_list[0]:
        count += 1
        if count < 100:
            continue
        if count > 500:
            break
        player_id = player.strip()
        player_url = 'https://syrin.me/pp+/' + player_id
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        while True:
            try: 
                req = urllib2.Request(player_url, headers=hdr)
                player_page = urllib2.urlopen(req).read()
                player_soup = BeautifulSoup(player_page, "lxml")
                print 'Checking ' + player_soup.title.contents[0][:-6] + '...'
                if player_soup.title.contents[0][:-6] == 'Oops!' or player_soup.title.contents[0][:-6] == 'Welcome ':
                    break
                total_pp = player_soup.find('tr', 'perform-total').contents[2].contents[0][:-2].replace(',','')
                total_aim_pp = player_soup.find_all('tr', 'perform-aim')[0].contents[2].contents[0][:-2].replace(',','')
                jump_pp = player_soup.find_all('tr', 'perform-aim')[1].contents[2].contents[0][:-2].replace(',','')
                flow_pp = player_soup.find_all('tr', 'perform-aim')[2].contents[2].contents[0][:-2].replace(',','')
                precision_pp = player_soup.find_all('tr', 'perform-aim')[3].contents[2].contents[0][:-2].replace(',','')
                speed_pp = player_soup.find_all('tr', 'perform-speed')[0].contents[2].contents[0][:-2].replace(',','')
                stamina_pp = player_soup.find_all('tr', 'perform-speed')[1].contents[2].contents[0][:-2].replace(',','')
                accuracy_pp = player_soup.find('tr', 'perform-acc').contents[2].contents[0][:-2].replace(',','')
                total_pp_file.write(total_pp + ',')
                total_aim_file.write(total_aim_pp + ',')
                aim_jump_file.write(jump_pp + ',')
                aim_flow_file.write(flow_pp + ',')
                aim_precision_file.write(precision_pp + ',')
                speed_file.write(speed_pp + ',')
                stamina_file.write(stamina_pp + ',')
                accuracy_file.write(accuracy_pp + ',')
                print "Total PP: " + total_pp
                print "Total Aim PP: " + total_aim_pp
                print "Jump PP: " + jump_pp
                print "Flow PP: " + flow_pp
                print "Precision PP: " + precision_pp
                print "Speed PP: " + speed_pp
                print "Stamina PP: " + stamina_pp
                print "Accuracy PP: " + accuracy_pp
            except KeyboardInterrupt:
                pass
            except:
                continue
            break