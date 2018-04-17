#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup
import json

import dlpage

def parsePSHWsrc(html):
	tagRe = re.compile(r'<.*?>')

	bsObj = BeautifulSoup(html, "lxml")
	rows = bsObj.findAll("tr")

	homeworks = []
	for row in rows:
		rowObj = BeautifulSoup(str(row), "lxml")
		units = rowObj.findAll("td")
		if len(units) != 0:
			for i in range(0, len(units)):
				units[i] = re.sub(tagRe, "", str(units[i]))
			homework = {
				'date' : units[0],
				'topic' : units[1],
				'target' : units[2],
				'preview' : units[3],
				'guide' : units[4],
				'homework' : units[5],
				'ot' : units[6],
			}
			homeworks += [homework]
	return homeworks

if __name__ == '__main__':
	url = r"http://cslabcms.nju.edu.cn/problem_solving/index.php/2017%E7%BA%A7--%E5%AD%A6%E6%9C%9F%E5%AE%89%E6%8E%92_(%E7%AC%AC%E4%BA%8C%E5%AD%A6%E6%9C%9F)"

	print(json.dumps(parsePSHWsrc(dlpage.download(url)), indent=4))