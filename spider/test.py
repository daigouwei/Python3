#!/usr/bin/env
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import re

html = '''
<td id="d1" class="dt" bgcolor=""></td>
<td id="d2" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">1</td>
<td id="d3" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">2</td>
<td id="d4" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">3</td>
<td id="d5" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">4</td>
<td id="d6" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">5</td>
<td id="d7" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">6</td>
<td id="d8" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">7</td>
<td id="d9" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">8</td>
<td id="d10" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">9</td>
<td id="d11" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">10</td>
<td id="d12" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">11</td>
<td id="d13" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">12</td>
<td id="d14" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">13</td>
<td id="d15" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">14</td>
<td id="d16" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">15</td>
<td id="d17" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">16</td>
<td id="d18" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">17</td>
<td id="d19" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">18</td>
<td id="d20" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">19</td>
<td id="d21" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">20</td>
<td id="d22" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">21</td>
<td id="d23" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">22</td>
<td id="d24" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">23</td>
<td id="d25" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">24</td>
<td id="d26" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">25</td>
<td id="d27" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">26</td>
<td id="d28" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">27</td>
<td id="d29" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">28</td>
<td id="d30" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">29</td>
<td id="d31" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">30</td>
<td id="d32" class="dt" bgcolor="white" style="font-weight: bold; cursor: pointer; color: blue;">31</td>
<td id="d33" class="dt" bgcolor="" style="font-weight: bold; cursor: pointer; color: blue;"></td>
<td id="d34" class="dt" bgcolor="" style="font-weight: bold; cursor: pointer; color: blue;"></td>
<td id="d35" class="dt" bgcolor=""></td>
<td id="d36" class="dt" bgcolor=""></td>
<td id="d37" class="dt" bgcolor=""></td>
<td id="d38" class="dt" bgcolor=""></td>
<td id="d39" class="dt" bgcolor=""></td>
<td id="d40" class="dt" bgcolor=""></td>
<td id="d41" class="dt" bgcolor=""></td>
<td id="d42" class="dt" bgcolor=""></td>
'''
soup = BeautifulSoup(html, 'lxml')
soupLists = soup.find_all('td', bgcolor='white')
# print(soupList[0])
# print(soupList[1])
dataList = {}
for soupList in soupLists:
    data = re.findall(re.compile(r'<td bgcolor="white" class="dt" id="(.*?)" style="font-weight: bold; cursor: pointer; color: blue;">(.*?)</td>', re.S), str(soupList))
    # print(data)
    dataList[data[0][1]] = data[0][0]
print(dataList)
