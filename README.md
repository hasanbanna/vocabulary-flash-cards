# Vocabulary Flashcard Generator for Anki

A python script which creates vocabulary flash cards for Anki. Currently, only tested on Macs.

## How to use

Before you can use the script, you need to get the API key from pixabay which you can get by signing up [here](https://pixabay.com/). It is used to search for images related to the word.

You also need to know the absolute path to your Anki collection.media so the images can be downloaded to this folder.

`Users/{mac_username}/Library/Application\ Support/Anki2/{anki_username}/collection.media`

*notice you have to escape the space with a  ' \ ' between Application and Support when copying the address in the terminal on Mac.*


Copy the api key and the path to the config.py file make sure they are inside quotes.

```python
#config.py

API_KEY =  "ADD_API_KEY_HERE"
USER_COLLECTION_MEDIA_PATH = "COPY_PATH_HERE"
```

1. Create a text file which contain english words
	**make sure to put one word per line*.
	```
	cat
	dog
	man
	strawberries
	peach
	```
2. Save the text file as english-words.txt in the same directory as the script. 
3. Run the script using the terminal make sure you are in the script's directory
	`python main.py`
4. Import the newly created .csv file to Anki
