# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect
from ask.models import Question, Answer, Tag
import json
import datetime
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def paginateObjects(request, all_objects, num_on_page):
	#print(all_objects)
	paginator = Paginator(all_objects, num_on_page)
	try:
		page = request.GET['page']
	except:
		page = 1
	#try:
	#page = paginator.num_pages
	try:
		pag_obj = paginator.page(page)
	except PageNotAnInteger:
		pag_obj = paginator.page(1)
	#except EmptyPage:
	#	pag_obj = paginator.page(1)
	#except InvalidPage:
	#	pag_obj = paginator.page(1)
	return pag_obj

def getPrev(num):
	n = []
	if num - 2 >= 1:
		n += [str(num - 2)]
	if num - 1 >= 1:
		n += [str(num - 1)]
	return n
	
def getNext(num, last):
	n = []
	if num + 1 <= last:
		n += [str(num + 1)]
	if num + 2 <= last:
		n += [str(num + 2)]
	return n
	
def dotFirst(num):
	n = ''
	if num - 4 >= 1:
		n += str(num - 4)
	elif num - 3 >= 1:
		n += str(num - 3)
	return n
	
def dotLast(num, last):
	n = ''
	if num + 4 <= last:
		n += str(num + 4)
	elif num + 3 <= last:
		n += str(num + 3)
	return n
	
def paginatorIndex(num, last, tag = None):
	if tag == None:
		tag = ''
	else:
		tag = 'tag=' + tag
	r = {
		'number': num,
		'pr': getPrev(num),
		'ne': getNext(num, last),
		'dotFirst': dotFirst(num),
		'dotLast': dotLast(num, last),
		'last': last,
		'tag': tag,
	}
	return r