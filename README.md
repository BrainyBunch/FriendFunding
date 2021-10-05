# FriendFunding

## Applications : 
- FireBase and Dynamic Links (Shared Links) 
- Passport or Auth0 (User Authen)
- FIRST GOING TO BE A SINGLE PERSON APP BEFORE WE CAN BE MATCHED WITH OTHERS 

## Data Structure

- User Authentication:
    - User:
	- Name:
    - Goal:
	
- Goal:
	- Name:
	- Cost:
	- AmountSaved:
 
## Description: 
	Our app is set to be a fun and competitive way of saving money with friends or family.  The user can save money for whatever they desire, whether it be a new console, a house, or even a trip.  It becomes a game between a group you choose, whoever can pick the lowest number to save that given time!  How much do you think you’d have to put away?  Will you put away the biggest number?? 

## Technology Used: 
- Django 
- HTML
- CSS 
- Heroku

## How To Install The App: 
- Fork and Clone and run npm i
	
## MVP User stories detailing app functionality
- As a user I would like to be able to see specific details of a goal
- As a user I would like to be able to edit a goal
- As a user I would like to be able to update a goal
- As a user I would like to delete a goal once I’ve reached it
 
## Stretch Goals
- Firebase
- PassportJS/Auth0
- Connect with friends/family/other users
 
MAJOR WINS:
 
## Wireframes with page layouts:
 
 
## Models including field names and their data types:
-	User:
		Name:
    - Goal:
	
- Goal:
	- Name:
	- Cost:
	- AmountSaved:
	- User = models.ForeignKey(User,on_delete=models.CASCADE,          related_name='goals')

## A list of routes:
- /home/ListGoals
- /SpecificGoal
- /create
- /edit/update
- /delete
## User Stories
- As a user I want to be able to click a user and see all of the goals
- As a user I would like to be able to see specific details of a goal
- As a user I would like to be able to edit a goal
- As a user I would like to be able to update a goal
- As a user I would like to delete a goal once I’ve reached it
- As a user I would like to see how much i have saved for my goal (percentage bar)
- As a user I would like to share a goal with friends/family to save together
- As a user I would like to be able to login to see my information 
- As a user I would like to be able to save for more than 1 goal 
- As a user I would like to i would like to be able to pick a random number to add to my savings 
 
