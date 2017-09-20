**Python test**

**Steps to run the application**

**Virtual Environment :**  Create virtual environment using command *virtualenv python_test_env*

**Activate Environment :** activate the virtual environment *source python_test_env/bin/activate*

**Requirements.** install the requirements in virtual env using *pip install -r docs/requirements.txt*

**Make Migrations** *Python manage.py makemigrations*

**Migrate** *Python manage.py migrate*

**Load Dummy Data** Load dummy data using *python manage.py initdata* .

**Run the Server** *Python manage.py runserver* 

**Demo accounts**

* username - user1, password - password1
* username - user2, password - password2
* username - user3, password - password3
* username - user4, password - password4

* tanant - neosoft  api-key - 23cb00a63d7945eba0ff5b846de1b728
* tenant - webwerks api-key - 3c1a5d88ac914da6a92e860789453779

**apis**

* get access token
     * url - /api-token-auth/ 
     * method - POST
     * params - username, password 

* get questions
    * url - /questions
    * method - GET
    * headers - token, api-key
    * params - q (optional)
