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
The global pillow market is experiencing steady growth, driven by increasing consumer awareness of the importance of sleep quality and the demand for ergonomic and specialized pillows. As consumers prioritize health and wellness, the bedding industry, particularly pillows, has seen innovation in materials, design, and functionality.

### Marketing and Sales Strategy:
Evlore Pillow Shop primarily targets adults aged 25-55 who are conscious of their sleep quality and overall well-being.
The focus is on urban and suburban areas in the United States where there is a higher disposable income and a tendency to invest in home and wellness products
### Operations and Management:
Evlore will be operated and managed by a small team of experienced professionals. The team will consist of a CEO, CTO, and marketing and sales staff.

### Conclusion:

The pillow market presents a lucrative opportunity for Evlore Pillow Shop, especially with the growing consumer focus on health and wellness. By carving out a niche in the premium segment with a focus on quality, sustainability, and innovation, Evlore can establish itself as a trusted brand in the competitive pillow market.

##### Back to [top](#table-of-contents)<hr>

## Marketing  

### Social Media 
- Online Store: The primary sales channel is the e-commerce website, offering a seamless shopping experience with detailed product descriptions, customer reviews, and easy checkout.
- Social Media: Platforms like Instagram, Facebook, and Pinterest will be leveraged for brand promotion, product showcases, and direct sales through shoppable posts.
[Facebook](hhttps://www.facebook.com/profile.php?id=61563967860716) 

### Mailing List  
Evlore Shope  uses Mailchimp to manage its mailing list. By joining the mailing list, users will receive updates on new features, upcoming events, and exclusive promotions. The process to join the mailing list is simple, users just need to provide their email address on the website, and they will start receiving email updates. 

## User Goals
To find and purchase a high-quality pillow that enhances sleep comfort and supports overall well-being, tailored to their specific sleep needs.

## Site Owner Goals
- Increase Online Sales
- Build Brand Awareness
- Enhance Customer Satisfaction
- Drive Repeat Business


## User Experience

### Target Audience
- Health-Conscious Consumers : Individuals who prioritize their health and wellness, particularly those who understand the importance of good sleep. They are likely to invest in products that promise better sleep quality and overall well-being.
- Home Decor Enthusiasts : People who take pride in the aesthetics of their home, particularly their bedroom. They are interested in pillows that complement their interior design and add a touch of luxury or style.
- Gift Buyers : Individuals shopping for special occasions like birthdays, weddings, or holidays. They are looking for premium, thoughtful gifts that convey care and quality.

### User Requirements and Expectations
- Product Quality : Users expect pillows made from high-quality materials that are durable, comfortable, and offer the benefits advertised.
- Easy Navigation : he website should be intuitive and easy to navigate, allowing users to find products quickly and efficiently.
- Mobile-Friendly :  Users expect a fully functional mobile version of the website that is easy to use on smartphones and tablets.
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
- GitHub Kanban was used to track all open user stories
- Epics were created using the milestones feature
- Backlog, In Progress, Done headings were used in the kanban


##### Back to [top](#table-of-contents)<hr>


## Wireframes



## Design

### Colors
The color I chose was dark green with a light background.  
<details><summary>See Color Palette</summary>

![Color Palette](/media/color(2).png)
</details>


### Fonts

The font selected was from Google Fonts, Lato.


# Structure

## Website pages

- The site consists of the following pages:
  - Home
  - product
  - all products
  - Product List
  - Product Expanded
  - cart
  - Checkout
  - Checkout Success
  - Contact
  - Register
  - Profile
  - Login
  - Logout
  - Reset Password
  - Register
  - 404


  ##### Back to [top](#table-of-contents)
  <hr>


## AWS 

I am using AWS S3 buckets to store my data. S3 is a highly scalable and durable cloud storage service provided by Amazon Web Services. It allows me to easily store and retrieve large amounts of data, and its built-in security features provide added protection for my files. I chose S3 for its scalability, durability, and security features.

![aws bucket](/media/aws2.png)
![aws media](/media/aws1.png)
![aws static](/media/aws3.png)
</details>
<hr>

## Database

I built my database using PostgreSQL. It's a powerful and open-source object-relational database system that is known for its reliability, robustness, and performance. I chose it because it provides a flexible tool for efficiently managing and organizing my data.

## Models  

### User Model

| Key        | Name         | Type        |
| ---------- | ------------ | ----------- |
| PrimaryKey | user_id      | AutoField   |
|            | password     | VARCHAR(45) |
|            | last_login   | VARCHAR(45) |
|            | is_superuser | BOOLEAN     |
|            | username     | VARCHAR(45) |
|            | first_name   | VARCHAR(45) |
|            | last_name    | VARCHAR(45) |
|            | email        | VARCHAR(45) |
|            | is_staff     | BOOLEAN     |
|            |              |             |
|            | is_active    | BOOLEAN     |
|            | date_joined  | VARCHAR(45) |

### User Profile Model

| Key        | Name                 | Type          |
| ---------- | -------------------- | ------------- |
| PrimaryKey | user_profile_id      | AutoField     |
| ForeignKey | user                 | User model    |
|            | default_phone_number | CharField[20] |
|            | default_address1     | CharField[80] |
|            | default_address2     | CharField[80] |
|            | default_town_city    | CharField[40] |
|            | default_county       | CharField[80] |
|            | default_postcode     | CharField[20] |
|            | default_country      | CharField[40] |

### Products Model
| Title       	| Key in Database 	| Form Validaton 	| Data Type    	|
|-------------	|-----------------	|----------------	|--------------	|
| Id          | _id                    |                     | PrimaryKey      |
| Category    	| category        	| None           	| ForeignKey   	|
| Sku         	| sku             	| max_length=254 	| CharField    	|
| Name        	| name            	| max_length=254 	| CharField    	|
| Description 	| description     	| None           	| TextField    	|
| Price       	| price           	| max_digits=6   	| DecimalField 	|
| Image       	| image           	| None           	| ImageField   	|
| Rating      	| rating          	| max_digits=6   	| DecimalField 	|  



## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django

## Features  


### Search Engine Optimisation (SEO)
I have used meta tags in the HTML of my web app's pages to optimize them for search engines. The description tag provides a brief summary of the content on the page, while the keywords tag lists relevant keywords to help search engines understand the content of the webpage and its relevance to related search queries.


### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v4.6](https://getbootstrap.com/)
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
![seo](/media/seo.png)

### Home page
- Home page includes nav bar, main body and a footer.
![Home](/media/home1.png)

### Navigation
- Fully Responsive.
- On small screens switches to hamburger menu.
- Indicates login/logout in status.
- displayed on all pages.  

![Nav](/media/nav1.png)

### Footer
- Contains social media links, privacy policy, and copyright.

![Footer](/media/footer.png)

### Mailing List Sign Up
- Mailchimp signup for email mailing list.  

![Email](/media/email.png)


### Sign up / Register
- Allow users to register an acoount.

![Signup](/media/signup.png)



### Sign In
- User can sign in.  

![sigin](/media/signin.png)


### Sign Out
- Allows the user to securely sign out.
- Ask user if they are sure they want to sign out.  

![signout](/media/signout2.png)


### Search
- Allows the user to search for products.

![search](/media/search.png)

### Basket
- Allows the user to view the basket with their items.
- Pops up as items are added and removed.  

![cart](/media/cart.png)

### Checkout
- Allows the user to purchase items in their basket.  

![checkout](/media/checkout.png)


### Stripe
- Allows the user to use stripe for card payments.  

![strip](/media/strip.png)


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

##### Back to [top](#table-of-contents)<hr>

# Validation  

## HTML Validation

The W3C Markup Validation Service was used to validate the HTML of the website.  

### Home  
