# Blog

## Author
### *Gloria Givondo* (24/11/2018)
There is no better way to express your ideas and opinions than with a personal blo .

You can view the live link on: 

## User Stories
These are the behaviours that the application implenents for use by a user.

As a user, I would like: 

* To view the blog posts submitted
* To comment on blog posts
* To view the most recent posts
* To alerted when a new post is made by joining a subscription.

As a writer, I would like: 
* To sign in to the blog.
* To create a blog from the application.
* To delete comments that I find insulting or degrading.
* To update or delete blogs I have created.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display all posts | **On page load** | All blog posts are displayed on the landing page |
| Display pitch from a pitch category | **Click on category** | Redirected to a page with a list of pitches from the category |
| Display the pitch | **On page load** | Each pitch displays the title, content, posted by, on |
| Comment the pitch | **Comment** | Redirected to the sign-in page |
|Profile| **On page load**|The logged in user is able to view their profile-pic, bio, pitches posted and edit their profile|
| Edit profile | **Edit profile** | Redirects the user to a page to update their bio and upload a profile-pic|

## Setup / Installation Requirements
* Web browser
* Virtual environment
* Flask
* Python version 3.6


### Cloning the Repo
* In your terminal run:

        $ git clone https://github.com/GeGe-K/blog.git
        $ cd blog

## Running the Application 
* Create the virtual environment

        $ sudo apt-get install python3.6 -venv
        $ python3.6 -m venv virtual

* Activate virtual environment

        $ source virtual/bin/activate

* Install Flask and other Modules

        $ pip install -r requirements.txt

* Set up the environment variables
        
Create a start.sh file and paste the following.
`export SECRET_KEY='<secret_key>'`
`export MAIL_USERNAME='<username>'`
`export MAIL_PASSWORD='<password>'`

* Run the application in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application 
* To run the tests for the class files and check if they function well:

        $ python3.6 manage.py tests

## Technologies Used
* Virtual environment
* Flask
* Python version 3.6
* Flask-Bootstrap4
* Pip
* HTML
* CSS
* Heroku
* Visual Studio Editor

## Known Bugs
There are no known bugs. Contact gloriagivondo@gmail.com in-case of any bugs.

## License
The content of this site is license under the MIT license
Copyright (c) 2018 **Gloria**

