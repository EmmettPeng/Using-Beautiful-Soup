#!/bin/python3
#coding=utf-8

#from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup as bs
#from selenium.webdriver.chrome.options import Options
#from selenium.common.exceptions import NoSuchElementException

def get_result(formula):
	requests.adapters.DEFAULT_RETRIES = 5
	s = requests.session()
	s.keep_alive = False
	r = s.get("http://www.chemspider.com/Search.aspx?q=" + formula)
	soup = bs(r.content, 'html.parser')
	h3_tag = soup.select('h3')
	result = h3_tag[0].string

	return result

def process_file(file):

	formula_list = [line.rstrip('\n') for line in open(file)]
	length = len(formula_list)
	#print(formula_list, length)
	return formula_list, length

def main():
	formula_list, length = process_file('E:/Denglab/代码整理/查看网页中元素/lists all.txt')
	count = 0
	for formula in formula_list:
		result = get_result(formula)
		count = count + 1
		with open('E:/Denglab/代码整理/查看网页中元素/output_bs.txt', 'a+') as f:
			f.write(formula)
			f.write('\t')
			f.write(result)
			f.write('\n')
		print('Output: ' + str(count) + '/' + str(length))


if __name__ =="__main__":
	main()