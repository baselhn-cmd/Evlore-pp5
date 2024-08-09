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
| 1 | Customer / Site User | register for an account | have an account and view my profile |
| 2 | Customer / Site User | login and logout | have an account with my information stored for fast usage |
| 3 | Customer / Site User | reset my password | set a new password if I forgot it                         |
| 4 | Customer / Site User | receive an email confirmation after registration| be notified registration was successful                   |
| 5 | SCustomer / Site User | have a profile | store my information for faster checkouts in the future |
| Viewing and navigation ||||
| 6 | Customer / Site User | navigate across the site | can access all parts of the site                          |
| 7 | Customer / Site User | use a navbar, footer, and social icons | navigate the site, access menus, and access socials       |
| 8 | Customer / Site User | be notified of my actions | be aware the action was completed successfully or not     |
| 9 | Customer / Site User | see my login status | know if I am logged in or not |
| 10 | Customer/ Site User | visit the shop| view all products available |
| 11 | Customer / Site User | view my basket and total cost at any time | so I am aware of what I am buying and it's cost |
| 12 | Customer / Site User | view a list of products | select a product to purchase                              |
| 13 | Customer / Site User | view an individual product details | view a more detailed view of the product |
| 14 | Customer / Site User | view a list of golf courses | select a golf course I want to play on |
| 15 | Customer / Site User | view individual golf course details | see more detailed information about it |
| 16 | Customer / Site User | view a list of tee times available for each golf course | select a date and time to play |
| Sorting and Searching ||||
| 17 | Customer / Site User | search for a product by name or description | find a certain product                                    |
| 18 | Customer / Site User | see my search results | only see what I am searching for |
| 19 | Customer / Site User | sort by category | select products of a certain category |
| 20 | Customer / Site User | sort by price low to high and high to low | view products according to my budget |
| 21 | Customer / Site User | select only available dates/times | I can only purchase available tee slots |
| Purchasing and Checkout ||||
| 22 | Customer / Site User | use a card as the payment method | complete my purchase                                      |
| 23 | Customer / Site User | view items in my cart | be aware of what I am buying and it's cost |
| 24 | Customer / Site User | adjust item quantity in my basket | increase or reduce item count according to my needs |
| 25 | Customer / Site User | receive order confirmation | be notified of a successful order |
| 26 | Customer / Site User | receive email confirmation | have a record of my purchase |
| Admin and Store Management | | | |
| 27 | Store Owner / Owner| add a product | add new products to the shop |
| 28 | Store Owner / Owner | edit a product | edit existing products in the shop |
| 29 | Developer / Owner | delete a product | delete existing products from the shop |
| 30 | Developer / Owner | set up a development environment | the team has a standardized and functional workspace. |
| 31 | Developer / Owner | I want to initialize a new project repository | we have a centralized location for code storage and version |
| 32 | Developer/ Owner | make the initial commit to populate  | the repository with a basic project skeleton.* |



### Kanban, Epics & User Stories
- GitHub Kanban was used to track all open user stories
- Epics were created using the milestones feature
- Backlog, In Progress, Done headings were used in the kanban


##### Back to [top](#table-of-contents)<hr>


## Wireframes
I used Balsamiq to create [wireframes](https://moqups.com/) for my project. It's a user-friendly wireframing tool that enables me to quickly and easily create mockups for my website or application. It offers a wide range of pre-built UI elements, and allows for easy collaboration with my team. I linked a pdf of my wireframes, which you can access it and check it out the design, layout and the flow of the project before implementing it in the real product.  

<details><summary>Wireframe Home</summary> 

![Wireframe Home](/media/wire1.png)
</details>

<details><summary>Wireframe Products</summary>

![Wireframe Home](/media/wire2.png)
</details>

<details><summary>Wireframe profile</summary>

![Wireframe profile](/media/wire3.png)
</details>

<details><summary>Wireframe Product Detail</summary>  

![Product Detail](/media/wire4.png)
</details> 


## Design

### Colors
The color I choose is white and violet.  
<details><summary>See Color Palette</summary>

![Color Palette](/media/color99.png)
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
  -Pillow Shams
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

<details><summary>See feature image</summary>

![seo](/media/seo.png)
</details>  

### Home page
- Home page includes nav bar, main body and a footer.

<details><summary>See feature images</summary>

![Home](/media/home1.png)
</details> 

### Navigation
- Fully Responsive.
- On small screens switches to hamburger menu.
- Indicates login/logout in status.
- displayed on all pages.  

<details><summary>See feature images</summary>

![Nav](/media/nav1.png)
</details>  


### Footer
- Contains social media links, privacy policy, and copyright.

<details><summary>See feature images</summary>

![Footer](/media/footer.png)
</details>  

### Mailing List Sign Up
- Mailchimp signup for email mailing list.  

<details><summary>See feature images</summary>

![Email](/media/email.png)
</details>

### Sign up / Register
- Allow users to register an acoount.

<details><summary>See feature images</summary>

![Signup](/media/signup.png)
</details>


### Sign In
- User can sign in.  

<details><summary>See feature images</summary>

![sigin](/media/signin.png)
</details>


### Sign Out
- Allows the user to securely sign out.
- Ask user if they are sure they want to sign out.  

<details><summary>See feature images</summary>

![signout](/media/signout2.png)
</details>

### Search
- Allows the user to search for products.

<details><summary>See feature images</summary>

![search](/media/search.png)
</details>

### Basket
- Allows the user to view the basket with their items.
- Pops up as items are added and removed.  

<details><summary>See feature images</summary>

![cart](/media/cart.png)
</details>

### Checkout
- Allows the user to purchase items in their basket.  

<details><summary>See feature images</summary>

![checkout](/media/checkout.png)
</details>


### Stripe
- Allows the user to use stripe for card payments.  

<details><summary>See feature images</summary>

![strip](/media/strip.png)
</details>


### Email Confirmation
- Allows the user to receive an email confirmation for their order. 


### Profile
- Allows the user to update their information and see their order history.  

<details><summary>See feature images</summary>

![strip](/media/profil99.png)
</details>


### Add Product
- Allows the Admin to add new products.

<details><summary>See feature images</summary>

![strip](/media/add.png)
</details>

### Edit Product
- Allows the user to edit the products. 

### Delete Product
- Allows the user to delete products, includes confirmation prompt before deletion.

##### Back to [top](#table-of-contents)<hr>

# Validation  

## HTML Validation

The HTML code for the project was validated using the [W3C HTML Validator.](https://validator.w3.org/nu/) All pages passed without errors except for the shopping cart page. The issue arose with the remove product link, which resulted in a duplicated ID error. This occurred because the ID changes dynamically based on the product ID, making it challenging to fix before the deadline.
 

##### Back to [top](#table-of-contents)<hr>  

### CSS Validation

<details><summary>See feature images</summary>

![css](/media/css.png)
</details>

### JavaScript Validation
JSHint javaScript Validation Service was used to validate all javaScript files.

<details><summary>stripe_elements.js</summary>

![jshint](/media/jshint1%20(2).png)
</details>  

<details><summary>country_field.js</summary>

![jshint2](/media/jshint2%20(2).png)
</details>


##### Back to [top](#table-of-contents)<hr>  

## PEP8 Validation

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the code for PEP8 requirements.

<summary>PEP8</summary>

<details><summary>Python</summary>

![pep8](/media/pep8.png)
</details>


##### Back to [top](#table-of-contents)<hr>  

## Testing

- Manual testing User Stories


### Manual testing

1.	As A/AN Customer / Site User	I CAN register for an account	SO THAT I CAN have an account and view my profile  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sign Up | Click pofile button and select register, user is brought to the sign up page| User is brought to the sign up page | Works as expected  

2.	As A/AN Customer / Site User	I CAN login and logout SO THAT I CAN have an account with my information stored for fast usage  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sign In | Click pofile button and select login, user is brought to the sign in page | User is brought to the sign in page | Works as expected  


3.	As A/AN Customer / Site User	I CAN recover my password	SO THAT I CAN set a new password if I forgot it  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Reset Password | Click pofile button and select login, user is brought to the sign in page, click forgot password to go to password reset page | User is brought to password reset page | Works as expected

4.	As A/AN Customer / Site User	I CAN receive an email confirmation after registration	SO THAT I CAN be notified registration was successful  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Registration | Upon registration an email is sent to verify the email address submitted | Registration email arrives into inbox of the email address used to sign up | Works as expected

5.	As A/AN Customer / Site User	I CAN have a profile SO THAT I CAN store my information for faster checkouts in the future  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Profile | From the Nav click the profile icon, select profile from dropdown and be broought to the profile page where user information is stored | Be brought to profile page | Works as expected

6.	As A/AN Customer / Site User	I CAN navigate across the site 	SO THAT I CAN can access all parts of the site  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Navbar | Click on any link in the navbar to be brought to a relevant page, shop for example | Be brought to shop to view all products after clicking all products in the navbar | Works as expected

7.	As A/AN Customer/ Site User	I CAN use a navbar, footer, and social icons  SO THAT I CAN navigate the site, access menus, and access socials  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Navbar/Footer | Scoll to footer, click on the Facebook logo | A new tab will open and bring user to the facebook page | Works as expected

8.	As A/AN Customer / Site User	I CAN be notified of my actions	SO THAT I CAN be aware the action was completed successfully or not  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Alert Box | Add an item from the shop to the basket | A message will appear in the alert box on screen to notify the user of this action | Works as expected 

9.	As A/AN Customer / Site User	I CAN see my login status	SO THAT I CAN know if I am logged in or not  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Navigation | While logged out the profile icon in the navbar will be gray, log in it will change to a green color | Once logged in the profile icon will be green | Works as expected  

10.	As A/AN Customer/ Site User	I CAN visit the shop SO THAT I CAN view all products available  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Shop | Click shop in the navbar, select all products | User is then brought to the all products page of the shop | Works as expected

11.	As A/AN Customer / Site User	I CAN view my cart and total cost at any time	so I am aware of what I am buying and it's cost  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Cart| Click the cart icon in the navbar | User is brought to the cart page where all products in cart are displayed along with their price and total cost | Works as expected

12.	As A/AN Customer / Site User	I CAN view a list of products	SO THAT I CAN select a product to purchase  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Categories | Select a category on the side panel   |     User is brought to the selected category of product and all products are listed | Works as expected

13.	As A/AN Customer / Site User	I CAN view an individual product details SO THAT I CAN view a more detailed view of the product  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Product Detail | Click on any item image in the shop, or the view button     |  User is borught to the product detail page where product details are displayed | Works as expected  

14.	As A/AN Customer / Site User	I CAN see my search results	SO THAT I CAN only see what I am searching for  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Search | Input a keyword into the search box in the navbar and click search | All items matching the search critearia are only displayed | Works as expected

15.	As A/AN Customer / Site User	I CAN sort by category SO THAT I CAN select products of a certain category  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sort | From the shop page, click a category on the side panel such as headwear | User is brought to the headwear page where only products classed as headwear are displayed | Works as expected  

16.	As A/AN Customer / Site User	I CAN sort by price low to high and high to low	SO THAT I CAN view products according to my budget 
 
| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sort | From the shop page, click the sort box and select price from high to low | All items will be sorted from the highest price to the lowest price | Works as expected  

17. As A/AN Customer / Site User	I CAN use a card as the payment method SO THAT I CAN complete my purchase  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Checkout | From the cart select secure checkout | Input user information, input card number 4242 4242 4242 4242 04/24 424 24242, payment is successful | Works as expected 

18. As A/AN Customer / Site User	I CAN view items in my cart	SO THAT I CAN be aware of what I am buying and it's cost  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Cart | Click the cart icon in the navbar | The Cart page will appear and display all items in the cart and their cost alongside total price for all items | Works as expected  

19. As A/AN Customer / Site User	I CAN receive order confirmation SO THAT I CAN be notified of a successful order  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Alert Box | Upon a successful checkout an alert box will be visible to the user | Alert box pops up with the order details | Works as expected 

20. As A/AN Customer / Site User	I CAN receive email confirmation SO THAT I CAN have a record of my purchased28	Store Owner / Admin	add a product	add new products to the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Email Confirmation | Upon a successful checkout a confirmation email will be sent to the provided email address which contains the details of the order |     Email confirmation arrives into inbox | Works as expected

21. As A/AN Store Owner / Admin	I CAN add a product SO THAT I CAN add new products to the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Add Product | From the navbar select the profile button as an admin logged in, click add product from the dropdown | The add product page will appear allowing the addition of a new product via the add product form | Works as expected  


22. As A/AN Store Owner / Admin	I CAN edit a product SO THAT I CAN edit existing products in the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Edit Product | From product detail as an admin account, find a edit button on the page, click edit | Admin is brought to the edit product page where they can adjust any part of the product | Works as expected

23. As A/AN Store Owner / Admin	I CAN delete a product SO THAT I CAN delete existing products from the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Delete Product  | From product detail as an admin account, find a delete button on the page, click delete | A modal pops up and asks the admin to confirm they wish to delete the product | Works as expected |

## Bugs
**Bug:** You can change the html file in product detail and change the maximun number of product to add in cart. It will cause an 500 server error in checkout because it's only allowed to add a maximun of 99 of a product.  
**Fix:** I need to fix this but for now there is left like this because I don't have the time to solve it, but I know it's there.

**Bug:** I had some problem with main nav and mobile-nav includes. There where a duplication of an ID in the search dropdown.  
**Fix:** Solve this by removed the ID from the base and gave it an uniqe ID so there was no duplication that gave problem.

**Bug:** When user had add a review there was an delete option on every review, even if the user had not write it by themself.  
**Fix:** Add a if statement with the request user and it solved it.

**Bug:** When a user had add a product to wishlist, there was shown a filled star at the product page on that product. Adn empty stars at the other product. But if a user added more products to wishlist, there added a star, so if the user had ad three product threr where shown three stars in product page beside the product name.  
**Fix:** I had an else statement that ruined it. When i removed the else statement there was only one filled star that showed on the products that the user had added. And on the rest of the product there is no star at all.   

## Deployment
To deploy my project, I had to use the Code Institute Python Essentials Template with all the neccesserely code for this project to work woth Django. With that template I create a repository in Github where i start my project.
And then open it and work with it at Gitpod workspaces.
It is important to open the same workspace everytime you have to work with it and to do that and secure it's being saved, you have to pin it in your workspace dashboard at gitpod.
When you want to save your work you need to write the commands in the terminal of your workspace: ***git add .*** , ***git commit -m "commit message"*** and then push it to github with ***git push***. To publish it and store it in your Github repositry.

* Then i want to deploy it at heroku, I am using my account on Heroku, if you doesnt have an account you will register first before deploying and then create a project in heroku. 
* Create a Procfile in your project, this required that specifies the commands that are executed by the app on startup.

  * Click the New dropdown and select Create New App.
  * Create a name to your project and it has to be uniqe.
  * Select the region you are working in, in my case Europe
  * Heroku Settings You will need to set your Environment Variables and this is importat to ensure your application is deployed properly.
  * In settings click "Reveal Config Vars" and set the variables that you need. Like the secret keys for stripe and aws in my case and a development key for deploy when i am working with the project.
  * connect your github repository with your heroku project in settings and connect with github.
  * Deploy your branch automatic or manually. At first the automatic deployment creats every time you push your code to github. But in the middle of the project heroku change the way and you had to save it via the heroku CLI and i was using the terminal to push it to heroku. with this steps:
  1. Write heroku login -i in terminal on your workspace.
  2. add your email and then password to heroku 
  3. Write heroku apps, to get all of your heroku apps
  4. Write heroku git:remote -a < appname >
  5. the gut add . , git commit -m "message", git push origin main.
  5. and the last step is "git push heroku main"

After this you have create a workspace and deployed your project to github and heroku!

##### Back to [top](#table-of-contents)<hr>


## Credits

### Code  
- Code Institute for the bag and checkout app as a basis for my checkout and basket apps
- Code Institute Slack community for guidance on many of my bug fixes.

### Media

- Insparation Websites :

[them](https://themewagon.github.io/pillowmart/single-product.html)

- The Boutique Ado project 

[Boutique Ado](https://github.com/mkthewlis/boutique-ado)


##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
- My Mentor Mo Shami  
- Code Institute Slack Community
- Code Institute Tutor Support