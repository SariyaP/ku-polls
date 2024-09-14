# KU Polls: Online Survey Questions 

An application to conduct online polls and surveys based
on the [Django Tutorial project](https://docs.djangoproject.com/en/4.1/intro/tutorial02/), with
additional features.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at [Kasetsart University](https://www.ku.ac.th).

## Installation

Django >= 5.1

python-decouple >= 3.8

## Running the Application

1. Clone the project
   >git clone https://github.com/SariyaP/ku-polls
2. Change to project directory
   >cd ku-polls
3. Install the requirements.txt
   >pip install -r requirements.txt
4. Migrate
   >python manage.py migrate
5. Load data
   >python manage.py loaddata data/users.json
6. Generate your secret key
   >python manage.py loaddata data/polls-v3.json
7. Run the server
   >python manage.py runserver
   

## Project Documents
All project documents are in the [Project Wiki](https://github.com/SariyaP/ku-polls/wiki).

- [Vision Statement](../../wiki/Vision-and-Scope)
- [Requirements](../../wiki/Requirements)
- [Project Plan](../../wiki/Project-Plan)
  - [Iteration 1](../../wiki/Iteration-1-Plan)
  - [Iteration 2](../../wiki/Iteration-2-Plan)
  - [Iteration 3](../../wiki/Iteration-3-Plan)
  - [Iteration 3](../../wiki/Iteration-4-Plan)
