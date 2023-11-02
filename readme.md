# Python Django
### Author: Ahmad Saadat

##### Table of Contents
1. [Project Summary](#project-summary-▶️-click-me-🔗)
2. [Requirements](#requirements)
3. [Solution](#solution)<br>
    a. [Deconstructing the requirement](#deconstructing-the-requirement) <br>
    b. [Designing our data model](#designing-our-data-model) <br>
    c. [Designing our web app](#designing-our-web-app)
4. [Going forward](#going-forward)
5. [Setting Up Locally](#setting-up-locally)
6. [References](#references)

# Project Summary ▶️ [Click Me :link: ](http://ec2-54-197-71-251.compute-1.amazonaws.com/)

Ecomm is a web platform that allows users to browse through all products offered. 
It provides a search and filtering functionality to aid with browsing.
**[please see figure 1 below]**

For the ecomm administrators, this application provides a portal to manage products.
**[please see figure 2 below]**

**[Figure 1: showing user's view]**
![Figure 1](https://ecommerce-app-bucket.s3.amazonaws.com/ecommerce-main.png)

**[Figure 2: showing administrator's view]**
![Figure 2](https://ecommerce-app-bucket.s3.amazonaws.com/ecommerce-admin.png)


# Requirements:
## Original set of requirements were:


We would like you to build a simple Django project with the following models: product, category, and tag. You should be able to assign a single category to any given product, and you could assign multiple tags to multiple products. For example, if your product is iPhone 13, you could assign a single category of phone and you could assign tags like smart phone,  128GB, camera, 6.1”. You should also be able to assign the same tags like smart phone to other products like Samsung Galaxy 21.

Please populate your database with some random data using Django admin. And design a very simple HTML page to allow a user to search the product by description and filter by category and tag. You can use Django template to do this or any front end of your choosing. The goal is to see if you can write a query function with Django. Styling is not really important.
Please let me know if you have any questions about this project.

# Solution

First we started off by deconstructing the requirement as much as possible
#### Deconstructing the requirement:
- Domain: Product, Category, Tag
- User-Admin: Populate Database with mock data using Django Admin
- User: Design simple HTML page to allow user to search product by description
- User: Design simple HTML page to allow user to filter by category and tag
- Write query functions with Django

#### Designing our Data Model:

- We chose to create 3 tables. <br>
    1. The Product table, which contains the appropriate product information.<br>
    2. The Category domain table, which hold the Category names. <br>
    3. The Tag domain table, which holds the tag names. <br>
- The tables attributes, relationships and cardinalities are detailed in figure 3 below

**[Figure 3: showing tables, attributes, data types, relationships and cardinalities]**
![Figure 3](https://ecommerce-app-bucket.s3.amazonaws.com/ERD.png)


#### Designing our Web App:

#### Solution 1: Making the client do the heavy lifting
- return all data rows to client using following query:
```
    Product.objects.all()
```
- ✅ allows client-side JavaScript to undertake data search and filtration tasks, thereby distributing the computational demand to the client's device.
- ❌ However, this approach carries a risk: if the volume of data records becomes excessively large, it could result in Input/Output (IO) bottlenecking for both the server and the database

#### Solution 2: Reducing burden using Pagination:
- ✅ Introduce client side pagination to take load off of server and database
- ❌ requires javascript libraries to paginate which can be more difficult to achieve using django

#### Solution 3: Finding a balance
- ✅ Make django server do the Pagination, Searching and Filtering

Having tried all three solutions, we found solution 3 the most feasible to stick to for this project

# Going forward

Going forward we believe that two changes need to take place to make this web app more robust

- Data model: Remove the many to many relationship between product and tag and replace it with a join table to create a many to one, one to many relationship between product, tag, and join table.
- Application: Make use of React or other front end technologies to offshore filtering and searching responsibilities to the client

# Setting up locally

### Technical Requirements:
- python3 (version 3.11.4)
- pip3
- virtualenv
- django

### Steps to running locally:

1. make sure you've installed python3, you can check so by running this command
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
6. 💻 navigate to localhost:8000
