# Food Vendor Basic CRM

## The week-6 is dedicated for project implementation as features would be as below
- As an user, I would like to have login/registration screen
- As an user, I would like to have dashboard
- As an user, I would like to have customer module
- As an user, I would like to send promotional messages to each customer
- As an user, I would like to have the order module
- As an user, I would like have menu module

### User Module
- Use will have (username, password, mobile, role)
- Login will be done on the basis of username and password
- Only activated user can access dashboard
- There would be only one admin who activates and deactivates the users

### Customer Module
- Customer registration will be done with unique customer id, name, mobile, email, dob, location
- Customer details (excluding customer id)  can be updated anytime by any user 
- Cutomer can not be deleted but can be blocked
- Order history for perticular customer need to displayed
- Total money paid by customer need to be displayed


### Promotions Module
- location wise promotions can be generated,deleted, updated
- age wise promotions can be generated,deleted, updated
- promotions can be sent to all of few customers
- promotions can be sent to top ten customers who have ordered more frequently

### Order Module
- Order can be placed by user for perticular customer
- Order can be cancelled
- Order can be updated for perticular customer
- There is limit for minimum order amount Inr. 100
- Order will be given to cloud kitchen with some id
- Need to get details like how many orders are executed by perticular kitchen

### Menu
- Only admin can add, update, delete menu


