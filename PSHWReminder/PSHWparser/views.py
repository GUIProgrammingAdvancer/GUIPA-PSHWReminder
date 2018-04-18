from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import time
import json
import re
from bs4 import BeautifulSoup
# Create your views here.

def downloadpage(url):
	print("Start downloading " + url)
	i = 0
	html = None
	while i < 10 and html is None:
		try:
			html = urllib.request.urlopen(url).read()
			print("Downloading done")
		except urllib.request.URLError as errinfo:
			print("Error occor when downloading " + url + " with ")
			print(errinfo.reason)
			html = None
			i += 1
			time.sleep(5)
	return html

def parsePSHW(html):
	tagRe = re.compile(r'<.*?>')
	nlRe = re.compile(r'\n')

	bsObj = BeautifulSoup(html, "lxml")
	rows = bsObj.findAll("tr")

	homeworks = []
	for row in rows:
		rowObj = BeautifulSoup(str(row), "lxml")
		units = rowObj.findAll("td")
		if len(units) != 0:
			for i in range(0, len(units)):
				units[i] = re.sub(tagRe, "", str(units[i]))
				units[i] = re.sub(nlRe, "", str(units[i]))
			homework = {
				'date' : re.findall(r'(20[12]\d-\d{2}-\d{2})', units[0])[0],
				'topic' : units[1],
				'target' : units[2],
				'preview' : units[3],
				'guide' : units[4],
				'homework' : units[5],
				'ot' : units[6],
			}
			homeworks += [homework]
	return homeworks

def dumpPSHW(homeworks):
	return 1

def startparse(req):
	name = req.GET.get('name', 0)
	if name == 'PSHW':
		url = r"http://cslabcms.nju.edu.cn/problem_solving/index.php/2017%E7%BA%A7--%E5%AD%A6%E6%9C%9F%E5%AE%89%E6%8E%92_(%E7%AC%AC%E4%BA%8C%E5%AD%A6%E6%9C%9F)"
		html = downloadpage(url)
		homeworks = parsePSHW(html)
		info = dumpPSHW(homeworks)
		return HttpResponse(str(info))
	else:
		return HttpResponse(str("nothing to do"))

