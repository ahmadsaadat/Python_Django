Django project

We would like you to build a simple Django project with the following models: product, category, and tag. You should be able to assign a single category to any given product, and you could assign multiple tags to multiple products. For example, if your product is iPhone 13, you could assign a single category of phone and you could assign tags like smart phone,  128GB, camera, 6.1”. You should also be able to assign the same tags like smart phone to other products like Samsung Galaxy 21.

Please populate your database with some random data using Django admin. And design a very simple HTML page to allow a user to search the product by description and filter by category and tag. You can use Django template to do this or any front end of your choosing. The goal is to see if you can write a query function with Django. Styling is not really important.
Please let me know if you have any questions about this project.

Deconstruction:
1. Domain Model: Product, Category, Tag
2. Admin: Populate Database with random data using Django Admin
3. End User: Design simple HTML page to allow user to search product by description
4. End User: filter by category and tag
5. Write a query function with Django


references:

UI:
https://www.devgap.uk/blog/wp-content/uploads/2018/09/E-Commerce-Sites-With-UX-Design-Farmdrop-devgap.uk_-1200x706.jpg

tutorial:
https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc

pagination:
https://www.youtube.com/watch?v=N-PB-HMFmdo


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