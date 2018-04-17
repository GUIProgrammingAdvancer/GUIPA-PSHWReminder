#!/usr/bin/env python3
"""
DO NOT USE THIS, USE parser.py INSTEAD!
"""
import re
from bs4 import BeautifulSoup

import dlpage

def getPSHWsrc(html):
	BSobj = BeautifulSoup(html, "lxml")
	return str(BSobj.findAll("textarea")[0])

def parsePSHWsrc(html):
	src = getPSHWsrc(html)
	src = re.sub("\n", "", src)

	pastRe = re.compile(r'20[12]\d-\d{2}-\d{2}\|(.*?)\|\-\|')
	pastHW = re.findall(pastRe, src)

	lastRe = re.compile(r'20[12]\d-\d{2}-\d{2}\|(.*?)# # # ')
	lastHW = re.findall(lastRe, re.sub(pastRe, "", src))
	# return re.findall(dateRe, src)
	return {
		'past' : pastHW,
		'last' : lastHW,
	}

if __name__ == '__main__':
	url = r"http://cslabcms.nju.edu.cn/problem_solving/index.php?title=2017%E7%BA%A7--%E5%AD%A6%E6%9C%9F%E5%AE%89%E6%8E%92_(%E7%AC%AC%E4%BA%8C%E5%AD%A6%E6%9C%9F)&action=edit"
	# print(dlpage.download(url))
	print(parsePSHWsrc(dlpage.download(url)))