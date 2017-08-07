import requests
import mtranslate as gt
import urllib
import os

if not os.path.exists('images'):
    os.makedirs('images')

API_KEY = '6102150-5ea971838fc8caa06e2afab2d';


english_words = open("english-words.txt",'r')

for word in english_words.read().split('\n'):
	r = requests.get("https://pixabay.com/api/?key="+API_KEY+"&q="+word)
	img_url = r.json()['hits'][0]['webformatURL']
	urllib.urlretrieve(img_url, "images/"+word.replace(" ","")+".jpg")
 	print word, gt.translate(word,"fr","auto").encode('utf-8')

