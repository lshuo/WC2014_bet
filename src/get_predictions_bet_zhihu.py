from bs4 import BeautifulSoup
import cPickle

file = open('../data/BSports Match Analysis.htm', 'r')
doc = file.read()
file.close();

soup = BeautifulSoup(doc)
# print(soup.prettify())

##dfg = soup.body.find('div', attrs = {'class':'forecast-group'})
##print (dfg.prettify())
##home_country = dfg.find('div', attrs = {'class':'forecast-item'}).findAll('div')
##print (home_country)

f_items = soup.body.findAll('div', attrs = {'class':'forecast-item'})
home_country = f_items[0].contents[3].text.strip()
away_country = f_items[2].contents[3].text.strip()
p_home_win = float(f_items[0].contents[1].text.strip('%'))/100.
p_tie = float(f_items[1].contents[1].text.strip('%'))/100.
p_away_win = float(f_items[2].contents[1].text.strip('%'))/100.
##print(home_country + away_country)
##print(p_home_win)
##print(p_tie)
##print(p_away_win)

##td_home_odds = soup.body.findAll('td', attrs = {'class':'home odds-none'})
##print(td_home_odds)
##print td_home_odds[-2].previous_element

d_table = soup.body.findAll('div', attrs = {'id':'correct-score-final'})[0].contents[1].contents[1].contents
##print type(d_table[3]).__name__  == 'NavigableString'
del(d_table[0:2])

zhihu_p_diff_distrib = {-4:0,-3:0,-2:0,-1:0,0:0,1:0,2:0,3:0,4:0}
for row in d_table:
    if type(row).__name__ != 'Tag' :
        continue;
    s_home_win_score = row.contents[1].text.strip()    
    s_away_win_score = row.contents[5].text.strip()
    s_tie = row.contents[9].text.strip()

    Other = 4
    home_win_diff = eval(s_home_win_score)
    zhihu_p_diff_distrib[home_win_diff] += float(row.contents[3].text.strip().strip('%'))/100.

    away_win_diff = eval(s_away_win_score)
    zhihu_p_diff_distrib[-away_win_diff] += float(row.contents[7].text.strip().strip('%'))/100.

    if len(s_tie) > 0:
        zhihu_p_diff_distrib[0] += float(row.contents[11].text.strip().strip('%'))/100.

zhihu_p_diff_distrib[4] /= 3.
zhihu_p_diff_distrib[-4] /= 3.
print zhihu_p_diff_distrib

point_table = cPickle.load(open('../data/point_table.cpickle', 'rb'))

point_exp = {}
for guess in range(-4, 5):
    point_exp[guess] = 0.
    for diff in range(-4, 5):
        point_exp[guess] += point_table[(diff, guess)] * zhihu_p_diff_distrib[diff]

print point_exp
print(home_country + " vs " + away_country)
print("bet on " + str(max(point_exp, key = point_exp.get)))

##with open('../data/aaa', 'wb') as f:

