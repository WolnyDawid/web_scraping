import requests
from bs4 import BeautifulSoup
import collections

text = []
URL = "https://megalotto.pl/wyniki/mini-lotto/losowania-od-9-Stycznia-2019-do-28-Marca-2023#"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="list_of_last_drawings_wyniki_lotto")
tags = soup.find_all("li", class_="numbers_in_list")

for i in tags:
    p = str(i)
    p = p.replace('\n', '')
    text.append(int(p.split('>')[1].split(' <')[0]))

counter = collections.Counter(text)
for key in sorted(counter):
    variable = (counter[key] * 100) / len(text)
    print(key, ":", "%.2f" % variable, "%")
