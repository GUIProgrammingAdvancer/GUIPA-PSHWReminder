#!/usr/bin/env python3
import urllib.request
import time
def download(url):
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

if __name__ == '__main__':
	url1 = r"http://cslabcms.nju.edu.cn/problem_solving/index.php?title=2017%E7%BA%A7--%E5%AD%A6%E6%9C%9F%E5%AE%89%E6%8E%92_(%E7%AC%AC%E4%BA%8C%E5%AD%A6%E6%9C%9F)&action=edit"
	# url1 = r"https://www.v2ex.comdsfa/t/338457adsfadsfsa"
	print(download(url1))