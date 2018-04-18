import urllib.request
import time
import json
import re
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.http import HttpResponse

from PSHWparser.models import Homework
# Create your views here.

def PSHWmod2dic(mod):
	dic = {
		'date' : mod.date,
		'ot' : mod.opentopic,
		'topic' : mod.topic,
		'homework' : mod.homework,
		'preview' : mod.preview,
		'target' : mod.target,
		'guide' : mod.guide,
	}
	return dic

def PSHWdic2mod(dic):
	mod = Homework()
	mod.date = dic['date']
	mod.homework = dic['homework']
	mod.preview = dic['preview']
	mod.topic = dic['topic']
	mod.guide = dic['guide']
	mod.target = dic['target']
	mod.opentopic = dic['ot']
	return mod

def downloadPage(url):
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
	flag = "nothing updated"
	for homework in homeworks:
		try:
			Homework.objects.get(date=homework['date'])
		except Homework.DoesNotExist:
			# newhw = Homework()
			# newhw.date = homework['date']
			# newhw.homework = homework['homework']
			# newhw.preview = homework['preview']
			# newhw.topic = homework['topic']
			# newhw.guide = homework['guide']
			# newhw.target = homework['target']
			# newhw.opentopic = homework['ot']
			newhw = PSHWdic2mod(homework)
			newhw.save()
			flag = "updated"
	return flag

def startParse(req):
	name = req.GET.get('name', 0)
	if name == 'PSHW':
		url = r"http://cslabcms.nju.edu.cn/problem_solving/index.php/2017%E7%BA%A7--%E5%AD%A6%E6%9C%9F%E5%AE%89%E6%8E%92_(%E7%AC%AC%E4%BA%8C%E5%AD%A6%E6%9C%9F)"
		html = downloadPage(url)
		homeworks = parsePSHW(html)
		info = dumpPSHW(homeworks)
		return HttpResponse(str(info))
	else:
		return HttpResponse(str("nothing to do"))

def getAll(req):
	name = req.GET.get('name', 0)
	if name == 'PSHW':
		try:
			homeworks = Homework.objects.all().order_by('date')
		except Homework.DoesNotExist:
			return startParse(req)
		homeworksArr = []
		for homework in homeworks:
			homeworkDic = PSHWmod2dic(homework)
			homeworksArr += [homeworkDic]
		jsonfile = json.dumps(homeworksArr, indent=4, ensure_ascii=False)		
		return HttpResponse(jsonfile)
	else:
		return HttpResponse("nothing")

def getLast(req):
	name = req.GET.get('name', 0)
	if name == 'PSHW':
		try:
			homeworks = Homework.objects.all().order_by('-date')
		except Homework.DoesNotExist:
			return startParse(req)
		homeworkLastMod = homeworks[0]
		homeworkLastDic = PSHWmod2dic(homeworkLastMod)
		jsonfile = json.dumps([homeworkLastDic], indent=4, ensure_ascii=False)
		return HttpResponse(jsonfile)
	else:
		return HttpResponse("nothing")