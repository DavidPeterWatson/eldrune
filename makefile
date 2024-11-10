install:
	pip install pyttsx3
	pip install SpeechRecognition
	brew install portaudio
	pip install pyaudio
	pip install pydub
	pip install anthropic-sdk
	pip install openai
	pip install google-cloud-texttospeech
	pip install pygame
	pip install pymongo
install_mongo:
	brew tap mongodb/brew
	brew install mongodb-community
	brew services start mongodb-community
	mongod --version
run:
	python game-master.py
