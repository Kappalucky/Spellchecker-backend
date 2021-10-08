# Spellchecker-backend

This folder contains the Django built backend for the Spellchecker application

## Getting Started

Typically I remove all secret keys and place important information within ENV files but for this application I left everything in. I strongly recommend for you to do so [remove sensitive data] if you plan on forking this repository for personal use.

> **P.S:** If your python virtual environment is running version 3+ there is no need to specify "*python3*" or "*pip3*". "*python/pip*" will do.

#### Prerequisites

-  [Python 3.0+](https://www.python.org/)

-  [Pip3](https://pypi.org/project/pip/)

-  [Virtualenv](https://virtualenv.pypa.io/en/latest/) * Optional

#### Installation

1. Install prerequisites

2. Create a Python environment or Virtualenv environment

	```
	python3 -m venv <name/path of environment folder>
	```
	or
	```
	virtualenv venv
	```

3. Activate environment
	```
	source <name/path of environment folder>/bin/activate
	```

4. Install requirements file from repository

	```
	pip3 install -r requirements.txt
	```

5. (./manage.py or python3 manage.py) makemigrations and migrate before running server

	```
	python3 manage.py makemigrations

	python3 manage.py migrate
	```

7. Run the development server. Server defaults to localhost:31337. You can manually change the port if needed.

	```
	python3 manage.py runserver
	```
	Change port
	```
	python3 manage.py runserver 8000
	```



## Methodology

The spellchecker can accept GET request with the query parameter being "word". Spellchecker can also accept POST request with the parameter "word" passed in the request body. I included both options in the event a developer wants to change how the frontend functions.

|Request |Endpoint                              |Params              |
|------- |--------------------------------------|--------------------|
|GET	 	 |`'http://localhost/spellcheck/?word='`|user-word           |
|POST    |`'http://localhost/spellcheck/'`      |{word: "user-word"} |


Rather than initializing a Django model and passing the words to a database, I kept the dictionary words in the original text file since that is sort of a database in its self. So for every call to the server, a function is called that loads the dictionary data into memory and checks are made against it.

Originally I wrote the functions to search through a list of words but I also included a hash table later on to assist with the speed of the word retrieval. Being that I do not have to return the word if correct, the hash table checks if the word exists within the dictionary. The list is only searched if the hash table does not contain the specific word or if the function governing the rules of the spellchecker returns False (the function failed at least one rule if False is returned).