#CLI Based Ticket Viewer (Zendesk Coding Challenge 2021)

This project consists of Zendesk 2021 Coding Challenge. I have attempted to create a CLI (Command Line Interface) based system which allows the user to view tickets fetched by Zendesk API.

##Files Included

* **Main.py** :- This is the driver program of the system.
* **pull_json_data.py** :- This program fetches JSON data from the API. GetSingleTicket (for single ticket) and Get_Data (For all tickets). CheckResponse module will check the response when the API is hit.
* **credentials.json** :- This file contains the required credentials for the user to use the Zendesk API
* **tickets.json** :- Provided JSON file
* **UnitTesting.py** :- Contains code to perform unit testing on the system.

## Instructions to Setup the program

Following instructions will help you setup the project on a local machine.

###Python Version
* [python 3.7](https://www.python.org/downloads/release/python-373/)

Execute the following command for cloning the repository and installing the dependencies.

```
git clone https://github.com/adwait1998/Zendesk-Coding-Challenge_Python-3.7
```


Execute the following command in CLI to verify installation and python version


```
python3 version
```
### Installing Dependencies

```
pip install -r requirements.txt
```

###All set to start the program!!

```
python Main.py
```

*Note* : Add your credentials in credentials.json before running the program.
###Unit Testing

Tested on Windows10

```
python UnitTesting.py
```

## Author

* **Adwait Nilesh Patil** - [Zendesk_Coding_Challenge](https://github.com/adwait1998/Zendesk-Coding-Challenge_Python-3.7)
