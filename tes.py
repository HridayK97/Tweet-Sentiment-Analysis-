import csv
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
import string
from feature_extraction import num_of_positives
from feature_extraction import num_of_negatives
from feature_extraction import pratio
from feature_extraction import nratio
from feature_extraction import sentiment_score
#from vectorizer import vectorizer

data=[]
affinlist=[]
words=[]


datafile = open('dataset.csv', 'r')
for i in datafile:
	data.append(i.split(","))
#print data[27][1]

wordfile = open('affin.csv', 'r')
for i in wordfile:
	affinlist.append(i.split(","))


for i in range(1,30000):
	if len(data[i])>2:
		temp=""
		for j in range(1,len(data[i])):
			temp=temp+data[i][j]
		data[i][1]=temp
	print i

for i in range(1,30000):
	print data[i][1]
#print data[8822][1]

def cleanupDoc(s):
     stopset = set(stopwords.words('english'))
     tokens = nltk.word_tokenize(s)	
     cleanup = " ".join(filter(lambda word: word not in stopset, s.split()))
     return cleanup

def check(w):
	affin=open('affin.txt', 'r')
	for line in affin:
		if line.find(w)!=-1:
			return 1
	return 0

def stem(words):
	for i in range(len(words)):
		for j in range(len(words[i])):
			if not check(words[i][j]):
				n=re.sub(r'(\w)\1+',r'\1',words[i][j])
				#only changing if new n exists in affin				
				if check(n): 
					words[i][j]=n
	return words

def checkmultiwords(words):
	for i in range(len(words)):
		tbd = []
		for j in range(len(words[i])):
			if (j+1)<len(words[i]):		
				if words[i][j]=="not" and words[i][j+1]=="good":
					words[i][j]="not good"
					tbd.append(j+1)
				elif words[i][j]=="not" and words[i][j+1]=="working":
					words[i][j]="not working"
					tbd.append(j+1)
				elif words[i][j]=="does" and words[i][j+1]=="not" and words[i][j+2]=="work":
					words[i][j]="does not work"
					tbd.append(j+1)
				elif words[i][j]=="dont" and words[i][j+1]=="like":
					words[i][j]="dont like"
					tbd.append(j+1)
				elif words[i][j]=="cant" and words[i][j+1]=="stand":
					words[i][j]="cant stand"
					tbd.append(j+1)
				elif words[i][j]=="cashing" and words[i][j+1]=="in":
					words[i][j]="cashing in"
					tbd.append(j+1)
				elif words[i][j]=="cool" and words[i][j+1]=="stuff":
					words[i][j]="cool stuff"
					tbd.append(j+1)
				elif words[i][j]=="fed" and words[i][j+1]=="up":
					words[i][j]="fed up"
					tbd.append(j+1)
				elif words[i][j]=="messing" and words[i][j+1]=="up":
					words[i][j]="messing up"
					tbd.append(j+1)
				elif words[i][j]=="no" and words[i][j+1]=="fun":
					words[i][j]="no fun"
					tbd.append(j+1)
				elif words[i][j]=="screwed" and words[i][j+1]=="up":
					words[i][j]="screwed up"
					tbd.append(j+1)
				elif words[i][j]=="some" and words[i][j+1]=="kind":
					words[i][j]="some kind"
					tbd.append(j+1)
				elif words[i][j]=="green" and words[i][j+1]=="wash":
					words[i][j]="green wash"
					tbd.append(j+1)
				elif words[i][j]=="green" and words[i][j+1]=="washing":
					words[i][j]="green washing"
					tbd.append(j+1)
		for d in reversed(tbd):
			words[i].pop(d)
				
				
	return words

def points(w):
	for i in range(len(affinlist)):
		if '"'+w+'\t"' == affinlist[i][0]:
			return int(affinlist[i][1])
	return 0

def getScore(word):
	temp=[]
	for i in range(len(word)):
		temp1=[]
		for j in range(len(word[i])):
			temp1.append(points(word[i][j]))
		temp.append(temp1)
	return temp
	
def affin(l):
	temp=[]
	for i in range(len(affinlist)):
		temp.append(0)
	for w in l:
		for i in range(len(affinlist)):
			if '"'+w+'\t"' == affinlist[i][0]:
				temp[i]+=int(affinlist[i][1])
				break
	return temp
			
def clss(s):
	if s == "happiness":
		return 0
	if s == "love":
		return 1
	if s == "fun":
		return 2
	if s == "enthusiasm":
		return 3
	if s == "surprise":
		return 4
	if s == "neutral":
		return 5
	if s == "empty":
		return 6
	if s == "worry":
		return 7
	if s == "sadness":
		return 8
	if s == "hate":
		return 9
	if s == "boredom":
		return 10
	if s == "relief":
		return 11
	if s == "anger":
		return 12
	print s
	return 13

print "Started Pre-Processing\n"
for i in range(1,30000):
	data[i][1]=re.sub("http\S*\s",'',data[i][1])
	data[i][1]=re.sub("http\S*\z",'',data[i][1])
	data[i][1]=re.sub("-",'',data[i][1])
	data[i][1]=re.sub("@\w*\s",'',data[i][1])
	data[i][1]=re.sub("@\w*\z",'',data[i][1])
	data[i][1]=re.sub("&\w*\s",'',data[i][1])
	data[i][1]=re.sub("(\.|\!|\?|\'s|\'|\")",'',data[i][1])
	data[i][1]=re.sub("\(",'',data[i][1])
	data[i][1]=re.sub("\)",'',data[i][1])
	#print data[i][1]
	tokens = nltk.word_tokenize(data[i][1])
	x = cleanupDoc(data[i][1])
	words.append(x.split())
	#print x
	print i

words=stem(words)
'''
for i in words:
	print i
'''
words = checkmultiwords(words)
for i in words:
	print i

score=getScore(words)

for i in score:
	print i

print "\n*****************FEATURE - EXTRACTION ******************\n"
k=[]
def feature_ext(lists,words,s):
	features=[]
	temp=affin(words)
	for i in range(len(temp)):
		features.append(temp[i])
	pos = num_of_positives(lists)
	features.append(pos)
	neg = num_of_negatives(lists)
	features.append(neg)
	prat = pratio(lists)
	features.append(prat)
	nrat = nratio(lists)
	features.append(nrat)
	score = sentiment_score(lists)
	features.append(score)	
	features.append(clss(s))
	k.append(features)

for i in range(len(score)):
	feature_ext(score[i],words[i],data[i][0])

# for i in range(len(score)):
# 	print words[i]
# 	print k[i]

with open('myfile.csv','w') as f:
    for i in range(len(k)):
        for j in range(len(k[i])):
            f.write(str(k[i][j]) + ',')
	f.write(str(data[i][0]))
        f.write('\n')

