# eCommerce: Teetime

![Am I Responsive](/media/responsive1.png)

**Developer: Basel Hussein**

💻 [Visit live website](https://evlore-pp5-a96d6c1e75b5.herokuapp.com/)  
(Ctrl + click to open in new tab)



## Table of Contents
  - [Executive Summary](#executive-summary)
     - [Market Analysis](#market-analysis)
     - [Marketing and Sales Strategy](#marketing-and-sales-strategy)
     - [Operations and Management](#operations-and-management)
     - [Financial Plan](#financial-plan)
     - [Conclusion](#conclusion)
  - [Marketing](#marketing)
     - [Social Media](#social-media)
     - [Mailing List](#mailing-list)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Design](#design)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [AWS](#aws)
      - [Database](#database)
      - [Models](#models)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

<hr>

## Business Plan  
### Executive Summary:
This project is developed as my 5th and final portfolio project during my course at Code Institute. It is a e-commerce website. Here you can find nice shop and product to buy. You can register an account for save your information and order history, And of course buy your magical stuff secure and safe with stripe pay system!

### Market Analysis:


### Marketing and Sales Strategy:

### Operations and Management:

#### Financial Plan:

### Conclusion:

##### Back to [top](#table-of-contents)<hr>

## Marketing  

### Social Media 

### Mailing List  

## User Goals


## Site Owner Goals



## User Experience

### Target Audience


### User Requirements and Expectations


##### Back to [top](#table-of-contents)<hr>


## User Stories


| User Story ID                  | As A/AN             | I CAN...                                                | SO THAT I CAN...                                          |
|--------------------------------|---------------------|---------------------------------------------------------|-----------------------------------------------------------|
| Registration and User Accounts ||||
| 1 | Shopper / Site User | register for an account | have an account and view my profile |
| 2 | Shopper / Site User | login and logout | have an account with my information stored for fast usage |
| 3 | Shopper / Site User | recover my password | set a new password if I forgot it                         |
| 4 | Shopper / Site User | receive an email confirmation after registration| be notified registration was successful                   |
| 5 | Shopper / Site User | have a profile | store my information for faster checkouts in the future |
| Viewing and navigation ||||
| 6 | Shopper / Site User | navigate across the site | can access all parts of the site                          |
| 7 | Shopper / Site User | use a navbar, footer, and social icons | navigate the site, access menus, and access socials       |
| 8 | Shopper / Site User | be notified of my actions | be aware the action was completed successfully or not     |
| 9 | Shopper / Site User | see my login status | know if I am logged in or not |
| 10 | Shopper / Site User | visit the shop| view all products available |
| 11 | Shopper / Site User | view my basket and total cost at any time | so I am aware of what I am buying and it's cost |
| 12 | Shopper / Site User | view a list of products | select a product to purchase                              |
| 13 | Shopper / Site User | view an individual product details | view a more detailed view of the product |
| 14 | Shopper / Site User | view a list of golf courses | select a golf course I want to play on |
| 15 | Shopper / Site User | view individual golf course details | see more detailed information about it |
| 16 | Shopper / Site User | view a list of tee times available for each golf course | select a date and time to play |
| Sorting and Searching ||||
| 17 | Shopper / Site User | search for a product by name or description | find a certain product                                    |
| 18 | Shopper / Site User | see my search results | only see what I am searching for |
| 19 | Shopper / Site User | sort by category | select products of a certain category |
| 20 | Shopper / Site User | sort by price low to high and high to low | view products according to my budget |
| 21 | Shopper / Site User | select only available dates/times | I can only purchase available tee slots |
| Purchasing and Checkout ||||
| 22 | Shopper / Site User | use a card as the payment method | complete my purchase                                      |
| 23 | Shopper / Site User | select the size and quantity of a product | select a size and quantity to my needs |
| 24 | Shopper / Site User | view items in my basket | be aware of what I am buying and it's cost |
| 25 | Shopper / Site User | adjust item quantity in my basket | increase or reduce item count according to my needs |
| 26 | Shopper / Site User | receive order confirmation | be notified of a successful order |
| 27 | Shopper / Site User | receive email confirmation | have a record of my purchase |
| Admin and Store Management | | | |
| 28 | Store Owner / Admin | add a product | add new products to the shop |
| 29 | Store Owner / Admin | edit a product | edit existing products in the shop |
| 30 | Store Owner / Admin | delete a product | delete existing products from the shop |
| 31 | Store Owner / Admin | add a golf club | add a golf club to the site |
| 32 | Store Owner / Admin | edit a golf club |edit an existing golf club on the site|
| 33 | Store Owner / Admin | delete a golf club | delete existing golf club from the site |
| 34 | Store Owner / Admin | add a tee time | add a tee time to a golf club |
| 35 | Store Owner / Admin | edit a tee time | edit an existing tea time on a golf club |
| 36 | Store Owner / Admin | delete a tee time | delete a tee time from a golf club |
| 37 | Shopper / Site User | book a tee time | book a tee time for a golf club |
| 38 | Shopper / Site User | edit a tee time booking | edit a tee time booking as I alter my schedule to play golf |
| 39 | Shopper / Site User | delete a tee time booking | delete a tee time booking if I need to cancel |
| 40 | Shopper / Site User | view my tee time bookings | view my tee time bookings |


### Kanban, Epics & User Stories



##### Back to [top](#table-of-contents)<hr>


## Wireframes



## Design

### Colors



### Fonts


# Structure

## Website pages




  ##### Back to [top](#table-of-contents)
  <hr>


## AWS 

I am using AWS S3 buckets to store my data. S3 is a highly scalable and durable cloud storage service provided by Amazon Web Services. It allows me to easily store and retrieve large amounts of data, and its built-in security features provide added protection for my files. I chose S3 for its scalability, durability, and security features.



## Database

I built my database using PostgreSQL. It's a powerful and open-source object-relational database system that is known for its reliability, robustness, and performance. I chose it because it provides a flexible tool for efficiently managing and organizing my data.



### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [AWS](https://aws.amazon.com/)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [CI Python Liner(PEP8)](https://pep8ci.herokuapp.com/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

##### Back to [top](#table-of-contents)


## Features  


### Search Engine Optimisation (SEO)
I have used meta tags in the HTML of my web app's pages to optimize them for search engines. The description tag provides a brief summary of the content on the page, while the keywords tag lists relevant keywords to help search engines understand the content of the webpage and its relevance to related search queries.


### Home page
- Home page includes nav bar, main body and a footer.

### Logo
- A custom logo for the business.
- User stories covered: 6, 7


### Navigation
- Fully Responsive.
- On small screens switches to hamburger menu.
- Indicates login/logout in status.
- displayed on all pages.  
- User stories covered: 6, 7

### Footer
- Contains social media links, privacy policy, and copyright.
- displayed across all pages.  
- User stories covered: 6, 7

### Mailing List Sign Up
- Mailchimp signup for email mailing list.  


### Sign up / Register
- Allow users to register an acoount.
- User stories covered: 1  


### Sign In
- User can sign in.  
- User stories covered: 2


### Sign Out
- Allows the user to securely sign out.
- Ask user if they are sure they want to sign out.  
- User stories covered: 2

### Checkout
- Allows the user to purchase items in their basket.  
- User stories covered: 22, 23, 24, 25


### Stripe
- Allows the user to use stripe for card payments.  
- User stories covered: 22


### Email Confirmation
- Allows the user to receive an email confirmation for their order. 


### Profile
- Allows the user to update their information and see their order history.  


### Add Product
- Allows the Admin to add new products.

### Edit Product
- Allows the user to edit the products. 

### Delete Product
- Allows the user to delete products, includes confirmation prompt before deletion.

