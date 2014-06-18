# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import cPickle
from os import walk
from itertools import combinations

odds = {}
data_path = '../data/'
for (dirpath, dirnames, filenames) in walk(data_path):
    for filename in filenames:
        if filename.startswith('odds_'):
            with open(data_path + filename, 'rb') as f:
                hh_kickoff = cPickle.load(f)
                [home_country, away_country] = cPickle.load(f)
                [p_home_win, p_tie, p_away_win] = cPickle.load(f)
                odds[hh_kickoff] = [ [home_country, away_country], [p_home_win, p_tie, p_away_win] ]
    break;

print odds

##with open('../data/odds_' + str(hh_kickoff), 'rb') as f:

file = open(u'../data/竞彩足球.htm', 'r')
doc = file.read()
file.close();

soup = BeautifulSoup(doc)
##print(soup.prettify())

money_table = {}
game_items = soup.body.findAll('div', attrs = {'class':'game-hd'})
for game_item in game_items:
    if game_item.find('span', attrs = {'class':'title'}).text == u'世界杯':
        hh_ko = (int(game_item.find('span', attrs = {'class':'meta'}).text.split(':')[0]) + 1) % 24
        if hh_ko not in odds:
            break;
        magnis = game_item.findAll('span', attrs = {'class':'odds'})
        print magnis
        print ' '
        money_table[(hh_ko, 'home_win')] = float(magnis[0].text) * odds[hh_ko][1][0]
        money_table[(hh_ko, 'tie')] = float(magnis[1].text) * odds[hh_ko][1][1]
        money_table[(hh_ko, 'away_win')] = float(magnis[2].text) * odds[hh_ko][1][2]
        del(odds[hh_ko])


print(len(money_table))
max_money = 0.
max_bet1 = ()
max_bet2 = ()
sum_money = 0.
for bets in combinations(money_table, 2):
    if bets[0][0] == bets[1][0]:
        continue;
    money = money_table[bets[0]] * money_table[bets[1]]
    sum_money += money
    if money > max_money:
        max_money = money
        max_bet1 = bets[0]
        max_bet2 = bets[1]

print('best bet: ' + str(max_bet1) + ' ' + str(max_bet2))
print('expected money earned if bet 1: ' + str(max_money))
