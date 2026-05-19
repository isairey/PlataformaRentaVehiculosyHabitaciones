# FAER : A Rental System -> TODO

- [x] Setup app with restframework

  - Install necessary dependencies
  - Created django-project named core
  - Created a app named api
  - Added urls for index in core
  - Setup for restframework along with urls done
  - Included api urls
  - Tested home index url with some messgae and status-code
  - Added github action workflow along with flake and coverage support
  - Added few settings for simplejwt

- [x] Setting up Accounts

  - Added Manager and model for the custom user along with forms
  - Added functionality for the user in admin view
  - Added tests for testing create_user and creste_superuser
  - Added register user view
  - Added retrieve user view
  - Added user serializer
  - Registered URL for user creation and retrieval
  - Tested all routes for accounts with the postman
  - Added all tests for accounts and verified

- [x] Setting up Models(Room and Media) and kafka

  - Added Room and Media model along with its serializer and views
  - Created compose file for Kafka
  - Created producer and consumer for the app
  - Refactored models and logic for the rooms
  - Removed some unused models
  - Added event-based task under rooms
  - Consumed create_room task and added logic for room creation along with the transaction
  - Added logic for the image file to be stored into temp and it's deletion
  - Changed the response status for creation of the room i.e 201
  - Added validators for a unique title
  - Added tests for room creation ,retrieval and validation

- [x] Add feature for the vehicle

  - Added model for Vehicle
  - Added serializer for vehicle
  - Added viewset for the vehicle
  - Updated serializer fields and viewsets
  - Added consumer for the Vehicle
  - Added task/function for vehicle creation
  - Added Tests for the vehicle creation ,retrieval and validation
  - Refactored some of the components
  - Added Models fields description to todo.md

- [x] Add reservations feature for the rooms and vehicle

  - Added Model for the Reservation
  - Added Serializer,Url and Viewset for Reservation
  - Added create method for the Reservation
  - Added custom validators for Reservation
  - Added methods for listing Reservations
  - Added methods for creating Reservations
  - Added tests for the Reservations

- [x] Deployed the App

  - Added docker compose file for the kafka
  - Added Cloudkarafka servers setup in the producer and consumer
  - Added procfile with heroku setup
  - Added postgres setup
  - Deployed to heroku
  - Refactored serializers for the images
  - Refactored user serializer
  - Added each model id as ready only field in serializer
  - Added single model route for vehicle and room

- [x] Added factory models

  - Installed factory boy and faker
  - Created factory for user, room, vehicle and media
  - Created command to seed the factory
  - Scaped the internet and populated db with some data
  - Added functionality to load data to db

- [x] Added Firebase Storage Feature

  - Added is_renter field visibility in user serializer
  - Removed unique key from room title.
  - Installed firebase storage and other dependencies
  - Added functionality to encode image
  - Added functionality to upload to storage and reflect change in the database

- [x] Minor Updates

  - Removed debug option for the Firebase Storage upload
  - Updated Access token time to 4hrs
  - Added viewset for the services route
  - Added permission for renter to the services route
  - Added permission for renter to the rooms route
  - Added permission for renter to the vehicles route
  - Updated test cases for renter
  - Added Content type and object to reservation serializer

- [x] Mail Support
  - Added mailtrap as default mail
  - Added send email function to utils
  - Added send email option in tasks
  - Added a template to send reservation mail
