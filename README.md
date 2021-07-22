# Onward and Upward

Onward and Upward is a web app for trekking, hiking and sightseeing enthusiasts who want to discover new and exciting treks all over Ireland while also being able to add their own.

[View Live Website Here](https://onward-and-upward.herokuapp.com/)

![The Veg Table](static/docs/multi-screen-mockup.jpg "The Veg Table")

# UX
## User Stories
---
### First Time user

As a user:

1. I want the design of the site to make a good impression on me.
2. I want to understand the purpose of the site.
3. I want to know how/why this site stands out from others in it's field.
4. I want to be able to easily navigate through the site.
5. I want to find treks that i have never seen before.

### Returning & Frequent User

1. I want to see what new content has been added to the site i.e new treks and hikes.
2. I want to follow the company on social media
3. I want to see which new features have been added to the site.
4. I want to be able to sign up for an email newsletter so i can recieve new recipes directly by email.
5. I want to be able to engage with the site owners to give feedback or request certain content.
6. I want to be able to add and edit my own treks on the site.

### Site Owner

As the site owner:

1. I want to be able to update the site regularly with new and exciting treks that users may not have seen before.
2. I want to be able to control all user conent, i.e editing and deleting users treks if necessary.
3. I want to be able to grow the Onward & Upward community, encouraging our users to update the site with their own treks.
4. I want to be able to engage with users through our social media platforms so we can keep track of feedback to make an improvements necessary.

___

# Design Choices

### Colour Scheme

My aim with the colour scheme of the site was for the aesthetic to reflect nature. I want to keep it simple, so as not to distract the user from the content. The green tones are associated with health, tranquility, power and nature. Greens are used to relax customers and promote environmental issues. 

The colour green stimulates harmony in your brain and encourages a balance leading to decisiveness.

I also added a dark-grey-blue colour for the text and headings to provide balance and reduce the harshness of the black text.

![Colour Scheme](static/docs/color-swatch.png "Colour Scheme")

### Typography

The fonts i have used were chosen to both eye catching and funtional. I think the Josefin Sans font adds a stylish yet solid look to the site with Lato providing a much more functional look.

[Google Fonts](https://fonts.google.com/): PT Sans Narrow & Open Sans

![Google Fonts](static/docs/Google-Fonts.png "Google Fonts")


## Wireframes 

Here are my original wireframe mockups.

![Balsamiq Wireframes](static/docs/Home-Page.png "Balsamiq Wireframes")

![Balsamiq Wireframes](static/docs/Individual-Trek-Page.png "Balsamiq Wireframes")


I like to think i havent diverted too musch from my original idea for the site.

* Rather than a static hero image i opted for Materialize's Slider feature to add more dynamism to the Home page.

* I think i have stayed true to my orginal idea with the look being similar across all screen resolutions.

## Mobile First Design

* While building this site as the focus with Materialize is a mobile first approach i was conscious of my page looking responsive across a variety of media devices. This was something i was extremely vigilent with. 

* I found Materializes grid system to be very handy overrall with only some slight adjustments to be made with the below media query.

---
@media screen and (max-width: 480px) {
    .view-trek h2 {
        font-size: 30px;
        left: 20px;
    }

    .view-trek h4 {
        font-size: 25px;
        left: 20px;
    }

    nav .brand-logo {
        font-size: 25px;
        font-weight: 600;
    }

    .view-trek-headings {
        display: inline-block;
    }


--------

# Features

* Eye catching design with organised categories for admin to manage

![Onward & Upward](static/docs/categories.png "Onward & Upward")

* Sidenav for mobile

![Onward & Upward](static/docs/sidenav.png "Onward & Upward")

* Features Section

![Onward & Upward](static/docs/features.png "Onward & Upward")

* CRUD Functionality for users and admin

![Onward & Upward](static/docs/add-trek-form.png "Onward & Upward")

![Onward & Upward](static/docs/join.png "Onward & Upward")

![Onward & Upward](static/docs/trek-card.png "Onward & Upward")

## Future Scope

* Introduction of more user controls e.g allow user to edit their profile.

* Ratings and Comments feature for each trek.

* Integration of Google Maps API for trek locations.

* Create a tagging system for each trek which would link to treks with similar tags.
----------


# MongoDB

Collections added to MongoDB

![MongoDB](static/docs/MongoDBcontents.png "MongoDB")


# Technologies Used

## Languages Used

* [HTML](https://en.wikipedia.org/wiki/HTML5)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

# Frameworks, Libraries, Programs and Sites.

* [Flask](https://materializecss.com/) - used as a framework in conjunction with Python

* [MongoDB](https://materializecss.com/) - used for the Database

* [Materialize](https://materializecss.com/) - used for Navbar, grid system and styling throughout the site.

* [Photoshop](https://www.adobe.com/ie/products/photoshop.html) - for image editing.

* [Balsamiq](https://balsamiq.com/) - for wireframes.

* [tinypng](https://tinypng.com/) - to reduce the size of the images used.

* [FontAwesome](https://fontawesome.com/) - for the icons used on the site.

* [Google Fonts](https://fonts.google.com/) - for the fonts used. 

* [GitHub](https://github.com/) - to host and publish the site.

* [Gitpod](https://gitpod.io/) - Used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

* [Heroku](https://www.heroku.com/) - Used for deployment of web app.

# Testing

## Manual Testing

Manual testing was carried out on devices of all sizes including desktop, tablet and mobiles.

## Code Validation

I used W3 Schools code validators for the HTML and CSS, there are no errors in the HTML. 

There are errors in the CSS which can be attributed to the Materialize classes used on the site. There was one error in the CSS i had written.

![Onward & Upward](static/docs/html-valid.png "Onward & Upward")

![Onward & Upward](static/docs/css-no-error.png "Onward & Upward")

---

## Lighthouse and WAVE Web Accessibility Reports

* I am happy with the results of my lighthouse accessibilty reports for both Desktop and Mobile respectively below, originally i had a lower score on performance as the filesize of the images on the homepage slider were too large i reduced the size of them in tinypic and updated my image files.


![Lighthouse Desktop Report](static/docs/desktop-lighthouse.png "Lighthouse Desktop Report")

![Lighthouse Mobile Report](static/docs/mobile-lighthouse.png "Lighthouse Mobile Report")


# Deployment

## Deploying Project

This project was deployed to [Heroku](https://www.heroku.com/) as follows:

1. Create a requirements.txt file by typing the following command into the terminal: pip3 freeze --local > requirements.txt

2. Create a Procfile by typing the following command into the terminal:
echo web: python run.py > Procfile

3. Save, add, commit and push the new files to your repository.

4. Sign Up/Login into [Heroku](https://www.heroku.com/) and create a new app. Give the app a unique name.

5. Select 'GitHub' from Deployment method options and search for the repository name. Once found, click on connect.

6. Head over to the settings menu and update the Config Vars to the following key, value pairs:

![alt text](static/images/heroku_configvars.png "Deployment screenshot")

7. Go to the deploy tab and click on Deploy Branch.


## Cloning Project 

1. Log-in to GitHub and open the repo for [Onward & Upward](https://github.com/jeffgallagher86/Onward-and-Upward)
2. Locate and click on the code section at the top of the page.
3. Click the code button as shown below to show copy of URL
4. Open Git bash terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. Type in "git clone" followed by the copied URL and press enter key to create a local clone.


# Credits

## Media

* Images in Home Page slider courtesty of Stephen Coyle and Steven Hylands on Flickr

## Code

* Fonts used courtesy of [Google Fonts](https://fonts.google.com/).

* CSS used for Navbar, grid system and styling throughout the site taken from [Materialize](https://materializecss.com/).

* Icons used in site taken from [Font Awesome](https://fontawesome.com/).

* Some small snippets of code used from users on [Stack Overflow](https://stackoverflow.com/) and YouTube.

* Credit also goes to [w3Schools](http://w3schools.com/) for help along the way.

## Acknowledgements
* I would like to thank my mentor Akshat Garg for all his help with this project.

* I'd also like to thank all at Code Institute and the CI slack community for all their help along the way.

* Special mention for Anna Greaves for her README webinar also.

**Thank you very much for taking the time to review my work!**


