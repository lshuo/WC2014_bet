# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import cPickle

file = open(u'../data/竞彩足球.htm', 'r')
doc = file.read()
file.close();

soup = BeautifulSoup(doc)
##print(soup.prettify())

game_items = soup.body.findAll('li', attrs = {'class':'cpm-game-item'})
print(game_items)
