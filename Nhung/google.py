from urllib2 import urlopen
from urllib2 import Request
from bs4 import BeautifulSoup
import unicodecsv as csv

myfile = open('links.csv', 'w')
myData = [['link', 'title']]

url = "https://www.google.com/search?q=ocean%278+b%C4%83ng+c%C6%B0%E1%BB%9Bp+th%E1%BA%BF+k%E1%BB%B7+%C4%91%E1%BA%B3ng+c%E1%BA%A5p+qu%C3%BD+c%C3%B4&num=100&tbs=cdr:1,cd_min:4/14/2018,cd_max:6/21/2018&filter=0&biw=1440&bih=759"
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,}

request= Request(url,None,headers)
# page = urlopen("https://www.google.com/search?q=%22ocean+8%22&lr=&hl=vi&tbs=qdr:m&ei=GIEqW-3UD8KAvQTC9ajwCw&start=0&sa=N&biw=1920&bih=983")
page = urlopen(request)
soup = BeautifulSoup(page.read())
links = soup.findAll("a")
count = 0

for link in links:
	s = link["href"]
	if (not s.startswith('/url?q=http://webcache')):
		if (s.startswith('/url?q')):
			t = s.find("&sa=U&ved")
			print(s[7:t])
			print(link.getText())
			myData.append([s[7:t], link.getText()])

with myfile:
	writer = csv.writer(myfile)
	writer.writerows(myData)
