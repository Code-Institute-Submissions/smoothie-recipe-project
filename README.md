# Seasonal Smoothie Recipe Database

## Overview

This data centric development project is the third project for the Code Institute. The fictional web application is a multipage site which has been 
designed for users looking for smoothie recipes. The web app categorises smoothies in to the four different seasons and enables
users to add, edit and delete recipes. 
The site is aimed at people with an interest and/or curiousity about the many types of smoothie recipes possible ! 

## UX

The project has been designed in a way to entice users to view smoothie recipes and add/edit their own recipes. The colour scheme has therefor been 
carefully thought about and I think this has a 'fresh fruit undertone' to the whole site! 

As a user I want to be informed of the purpose of the site. The landing page of this project provides a clear description of what lies inside the site. 
There is a user login form (although for the purpose of this project, this does not need to be securely authenticated), 

As a user I want a clear layout of the website providing easy navigation throughout the site. This was achieved with a fixed navbar containing 
all necessary links to the site. The navbar has been created with an attractive sidebar for smaller screens, in line with mobile first design.

As a user I also would like to filter results, and so a 'search by' section has been created separating the categories to suit the users desires. 
Dietary requirements, difficulty and highest star rating have been chosen as key search features, alongside the more prominant Season filter.

I would like to see some visual data, therefore I have implemndted a pie chart to show users how many recipes include the various dietary requirements. I chose to 
create a chart showing the dietary requirement breakdown, as this is often high up on people's interest/concern.

One of the benefits to this site is that users can add their own recipes. As a user I would want this form to be clear, concise and easy to use. 
I would want a clear submit button, but also the option to navigate away from (ie cancel) the form in case I changed my mind. I would also like the 
ability to edit a recipe, and to completely remove a recipe. 

I would of course like to see the usual social media icons to accompany the website, to reassure me of the company's presence on different social media platforms.
These should be easy to find, stand out, but be in keeping with the design and feel of the website. 

Wireframes can be found in the wireframes folder.

## Features

Landing page - As the initial page the user views, it should have an impact and be clear what the purpose of the site is. This was achieved by the
use of a striking background image (used throughout whole site for continuity), the title of the site and a brief description of what the
website has been created for. There is also a username form, giving the site a more 'secure feel' and helps make the site feel more personal.

On entering the site, the user is directed to the Seasons Page. This is the main filter feature of the site, and gives the smoothie recipe site some
individuality by categorising the recipes so that they compliment the time of year. The four seasons can be selected, and all recipes with the 
corresponding field value will be returned on the Search Results page. 

The Navigation of this site has been thought about carefully. There are links to each part of the site in the navbar and the footer. There is a 
sidenav bar tailored for smaller screens which contains the same information as the navbar. The navbar contains dropdown options which include a hover feature 
for the submenus. 
The option to view all recipes is present on the navbars (and footer), these results are displayed in date added order, with the most recent recipe 
displayed at the top. This creates a better UX as it means after a new recipe is added, the user can see their recipe straight away preventing the otherwise
random default order that would occur. 


The site has been designed to allow the user to filter through the recipes. Although season is the primary focus, users are able to search 
recipes based on their diet requirements, difficulty of the recipe and by star rating (popularity). 

Part of the project brief was to ensure CRUD functions are demonstrated. The user is therefor able to create, read, update and delete a recipe 
successfully.

The site also contains a Stats page demonstrating some visual data. This pie chart breaks down the number of recipes containing each dietary requirement. 
It has been created using Chart JS and fits in with the UI / UX of the overall site.

# Features Left to Implement

I would like to enable users to upload an image for their submitted smoothie recipe. This would give the site a more 'realisitc' feel 
and provide a more attractive UI. Due to time constraints I have not implemented this as yet.

I would also implement a more detailed Statistics page, using multiple charts to display results more thoroughly. 

The site enables users to search for the most popular recipes, this has been created by choosing a star rating on the addition of new recipes.
I would like to implement a more effective way of determining popularity in the future, by creating an upvote function. 

In the future, I will create a secure authenticatation feature for this site, this is particularly important 
given anyone can edit/delete any of the recipes!

## Technologies Used

HTML - used to build the foundation of the website
CSS - used extensively to provide style and layout to the website. 
Materialize - used to provide a responsive grid system layout.
Javascript - used to create the pie chart and enable multiple ingredients and method steps in the add/edit form pages. Javascript is also used as part of the navbar
in Materialize.
Mongodb - the noSQL database was made by mongodb and hosted using mlab.
Charts JS - used to create pie chart on dietary requirements
Git version control
Heroku for deployment

## Testing

Testing of this website was carried out continuously, with extensive use in google chrome dev tools to ensure the site remained
responsive and functioned as intended. The site has been checked all all screen sizes / devices available in chrome devs. 
One of the main issues I experienced was the sizing and layout of the card. I chose to use a card-reveal for each recipe. These are
set sizes on Materialize and i came across issues fitting in all the information I wanted on each card, particularly as the 
screen was resized to smaller screen sizes. It may be an idea in the future to create a link to a 'detailed recipe' page where there is more
room to provide text. I chose not to implement this feature, mainly due to time but also because overall, Smoothie recipes do not
contain longwinded Methods and so this was not priorortised in the project.
Another issue on smaller screens is the pie chart. Although the chart renders fine on most sizes, it is very small for mobile and this will need further 
research in to making this larger, in the future. 
The site has also been been viewed in firefox and explorer browsers, with no obvious differences. 
I sent the link to this project from heroku across to friends and family so they could check UI/UX using their devices and provide any feedback.

CSS was tested using the W3C CSS Validation service with no resulting errors.
Javascript was tested using JShint. There were several warnings in the code rendering the pie chart. This was regarding the use of '{' due to Jinja Templating. 
This does result in an error in console and so it had been noticed already. This error can be eliminated by wrapping the jinja template
containing 'data labels' and 'data values' in quotations, however the chart does not then render in the browser and so I have left these errors
present for the time being. Further research will be required to figure out another way.
The rest of the javascript in this project did not throw up any errors.

Forms were tested multiple times and after some advice from my mentor, the initial Username form on the landing page was set to 'required'.
The form uses JS to create a new field with the click of the plus sign, enabling the user to add ingredients gradually rather than bulk text. 
This created a few layout problems, but with careful re-orginasation of my divs, I was able to tidy this up. There is an on-going issue with 
the alignment of the cross (cancel/remove) method step which will need looking in to further. 

Functions in app.py were tested using print statements initially, in the console. I was also able to check functions for inserting in to the 
database were working correctly by live viewing mlab (see below).


### mlab

Once mlab had been successfully set up and connected to my project (more detail on this), I added some recipes in manually as a starting
point. The function to display all recipes on the page was then tested frequently to ensure all recipes were displayed correctly.
There were a few issues I came across at this point. including how to go about displaying ingredients in a listed format. My original
code produced only individual letters of the ingredients, followed by a long continuous list. 
This was solved by the help of Slack and a refresh in extracting data in json format from the database, and the use of .getlist was 
implemented with unordered list tags to produce the desired output.


## Deployment

### Deployment to Heroku 

Open up <a herf="">heroku</a> and create a new app. Select Deploy.
In the command line login to Heroku using Heorku login command.


Set config vars:
IP 0.0.0.0
PORT 5000

Set Secret Key to 'some_secret'

Select More tab and click re-start all dynos


## Credits

I spent a while trying to enable the following functions:
1. Creating a card that successfully displayed ingredients and method from each recipe after submission to the database.
2. 
3. 
Stack Overflow was extremely useful in helping with these problems and provided me with the help I needed for the functions to work successfully.

I also thank my tutor Maranatha for his useful tips, particularly giving me advice on how to create my graph, aswell as his review of the project. 


## Media

The photos used in this site were obtained from <a href="https://unsplash.com/">Unsplash</a> and <a href="https://www.pexels.com/">Pexels</a> websites which provide free to use images. 


## Acknowledgements

I spent a while researching cooking and recipe websites, some inspiraiton for this project came from Jamie Oliver and Nigella Lawson websites.