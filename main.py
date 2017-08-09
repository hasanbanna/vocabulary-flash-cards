import requests
import mtranslate as gt
import urllib
import os
import os.path
from config import API_KEY
from config import USER_COLLECTION_MEDIA_PATH

def main():
	flash_cards_image_path = USER_COLLECTION_MEDIA_PATH
	english_words = open("english-words.txt",'r')
	output_csv = open('flashcards.csv', 'w')
	for word in english_words.read().split('\n'):
		r = requests.get("https://pixabay.com/api/?key="+API_KEY+"&q="+word)
		if not r.json()['hits']:
			print "No image found for " + word
		else:
			img_url = r.json()['hits'][0]['webformatURL']
		word_image_filename = word.replace(" ","_")
		new_file_path = os.path.join(flash_cards_image_path, word_image_filename +".jpg")
		print "word added: "  + word 
		urllib.urlretrieve(img_url, new_file_path)
		output_str = "%s <br /> <img src='%s.jpg'>, %s\n"%(word, word_image_filename,gt.translate(word,"fr","auto").encode('utf-8'))
	 	output_csv.write(output_str)
	output_csv.close()
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	print "All images that were found have been added to the collection media folder."
	print "flashcards.csv file created."
if __name__ == '__main__':
	main()
