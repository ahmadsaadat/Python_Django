# Title: Remarcable Assessment
### Author: Ahmad Saadat

##### Table of Contents
1. [Project Summary](#project-summary-▶️-click-me-🔗)
2. [Requirements](#requirements)
3. [Solution](#solution)<br>
    a. [Deconstructing the requirement](#deconstruction)
2. [Setting Up Locally](#setting-up-locally)

# Project Summary ▶️ [Click Me :link: ](http://54.166.78.71:8000/)

Ecomm is a web platform that allows users to browse through all products offered. 
It provides a search and filtering functionality to aid with browsing. <br>
**[please see figure 1]**

For the ecomm administrators, this application provides a portal to manage products.<br> 
**[please see figure 2]**

**[figure 1]**
![Figure 1](https://ecommerce-app-bucket.s3.amazonaws.com/ecommerce-main.png)

**[figure 2]**
![Figure 2](https://ecommerce-app-bucket.s3.amazonaws.com/ecommerce-admin.png)


# Requirements:
## Original set of requirements were:


We would like you to build a simple Django project with the following models: product, category, and tag. You should be able to assign a single category to any given product, and you could assign multiple tags to multiple products. For example, if your product is iPhone 13, you could assign a single category of phone and you could assign tags like smart phone,  128GB, camera, 6.1”. You should also be able to assign the same tags like smart phone to other products like Samsung Galaxy 21.

Please populate your database with some random data using Django admin. And design a very simple HTML page to allow a user to search the product by description and filter by category and tag. You can use Django template to do this or any front end of your choosing. The goal is to see if you can write a query function with Django. Styling is not really important.
Please let me know if you have any questions about this project.

# Solution

First we will start off by deconstructing the requirement above as much as possible
#### Deconstructing the requirement:
1. Domain: Product, Category, Tag
2. User-Admin: Populate Database with random data using Django Admin
3. User: Design simple HTML page to allow user to search product by description
4. User: Design simple HTML page to allow user to filter by category and tag
5. Write query functions with Django

#### Designing our Data Model:

1. I chose to create 3 tables. <br>
a. The Product table which contains the product information.<br>
b. The Category domain table. <br>
c. The Tag domain table.
2. Their attributes and relationships are detailed in figure 3 below

**[figure 3]**
![Figure 3](https://ecommerce-app-bucket.s3.amazonaws.com/ERD.png)


# Performance & Optimizations
Solution 1: Place onus on Client Side
- return all data rows 
- write javascript to perform client side search and filtering
Issues: 
- Database performance issues

Solution 2: Reducing burden on database
- Introduce pagination to take load off of database
Issues: 
- searching and filtering cannot be done on client side

Solution 3: Finding a balance
- Make use of django libraries to search and filter
Issues:
- Increases server utilization

references:
UI:
https://www.devgap.uk/blog/wp-content/uploads/2018/09/E-Commerce-Sites-With-UX-Design-Farmdrop-devgap.uk_-1200x706.jpg
tutorial:
https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc
pagination:
https://www.youtube.com/watch?v=N-PB-HMFmdo

# Setting up locally

### Technical Requirements:
- python3 (version 3.11.4)
- pip3
- virtualenv
- django

### Steps to running locally:

1. make sure you've installed python3, you can do so by running this command
```
python3 --version
```
2. Create a new virtual environment
```
python3 -m venv .venv
```
3. Activate the virtual environment
```
source .venv/bin/activate
```
4. Install dependencies:
```
pip3 install -r requirements.txt
```
5. Spin up server
```
cd ecommerce_project
python3 manage.py runserver
```
6. ✅ navigate to  localhost:8000