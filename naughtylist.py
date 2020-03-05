from lxml import html
import requests

page = requests.get('https://royaleapi.com/clan/PGYGQ0PL')
tree = html.fromstring(page.content)
allplayers = tree.xpath('//a[@class="block member_link"]/text()')
page = requests.get('https://royaleapi.com/clan/PGYGQ0PL/war/analytics')
tree = html.fromstring(page.content)
warplayers = tree.xpath('//a[@class="member_link"]/text()')
print("-----------Begin-------------")
for player in allplayers:
    if player not in warplayers:
        player = player.strip()
        if player != "" :
          print(player)

print("-----------END-------------")
