# Rezkeeper Frontend
SEI 5/9 Project 4 Capstone: Rezkeeper  </br>
Rezkeeper is a personal keeper app, in which users can schedule restaurant visits, as in enter in the name, image, address, food type (ex: desserts), the day the want to go, and the time. It's a way to keep track of all the great (or not so great) restaurants one has visited. As someone who lives in NYC, such a big place with so many great options for food, it's nice to remember all the places I've been to and all the food I liked at certain places.

</br>

Link to site: https://frontend-rezkeeper.vercel.app/

Link to Trelloboard: https://trello.com/b/lbHHjSfe/capstone-project

Link to Original Big Repo: https://github.com/mkhan42/rezkeep (ps: lost 43 commits so all my commits are not here: Will estamiate a total of over 90/100 commits)

Link to Frontend Repo: https://github.com/mkhan42/frontend-rezkeeper

# User Story
- As a user, we want to be able to create an account for the application and be able to log in and logout.
- Once the user is logged in, the user should be able to schedule restaurant visits, as in enter in the name, image, address, food type (ex: desserts), the day the want to go, and the time. They can also schedule the day as a passed date because maybe they want a place to hold a great restaurant they went to.
- Once a restaurant date is passed the current date, the restaurant gets placed in the history page.
- Users should be able to create, read, update, and delete their restaurants, both scheduled and passed.
- Once as restaurant gets placed in to the history page, the user can see options to add their orders, give it a rating, and write a review. (They can also delete orders, rating, and review).
- The User should only be able to write one rating and review per restaurant, meaning that ince there is a rating or review present, those forms will disappear.

# Technologies Used
- Django
- Django Rest Framework
- Python
- React
- JavaScript
- Heroku
- Vercel
- HTML
- CSS
- Bootstrap

# References
- For auth: https://github.com/sushil-kamble/django-react-auth?fbclid=IwAR2AYzXKi5TdUbihtZ7vMrWbAGkCvBGEFUslp4Hw3ZFUwrLokzXK6IlP49o
- For auth article: https://sushil-kamble.medium.com/django-rest-framework-react-authentication-workflow-2022-part-1-a21f22b3f358
- Styling inspo for cards: https://mdbootstrap.com/snippets/jquery/alexq/1798251#html-tab-view
- Understanding how Django and React work together: https://www.youtube.com/watch?v=VBqJ0-imSMU

# Wireframes
![wireframe](./images/Wirefram4.jpg)

# ERD
![erd](./images/ERD4.jpg)

# Project Pages

## Login Page 
![login](./images/login.png)

## Register Page
![register](./images/register.png)

## Home Page
![landing](./images/landing.png)

## Add Form Page
![addrest](./images/addrest.png)

## Scheduled Visits Page
![scheduled](./images/scheduled.png)

## Passed Visits Page
![passed](./images/passed.png)

## Update Visit Form Page
![update](./images/updatevisit.png)

## Scheduled Visit Detail Page
![detail](./images/scheduleddetail.png)

## Passed Visit Detail Page
![detail](./images/passed1.png)
![detail](./images/passed2.png)
![detail](./images/passed3.png)
![detail](./images/passed4.png)

# Icebox
![detail](./images/trelloboard.png)
- Recreate this app in MERN-STACK
- Fix styling some more
- Make code more readable
- Implement search bar to be able to search by food type, address, name, and rating
- Fix time on card
- Figure out auth on backend (filter user visits)
- Use yelps API and get reviews and info about restaurants
- Use google map API and place it in detail card
- Make it even more mobile friendly and use some media queries