### Capstone Proposal, by Rebecca York Hanlon

### Product Name,
Storia

### Product Overview
Storia is an interactive storybook.  It allows a child to read the story, listen to the story and song, click each word to hear it, record him or herself reading the page.

To help encourage the child's reading progress and to allow the parent to over-see and encourage the child, progress reports, a reading chart and badges/points with are generated from the data collected while the child interacts with the page.

For this stage I will not focus on the perfect presentation of the website, but on the framework, automation and design of components.

The first stage will focus on the following:
1. Develop the process to design and show the storybook on line with interactivity.
2. Develop the following pages (templates):  library/bookshelf, title page with navigation of the story, the storypage
1. Collect user interface data and store in the database
2. Develop the Reading Chart that shows the users progress based on data collected from user interactions.  User interactions are collected, analyzed and sorted, visualized and then shared

### Specific Functionality
This project will begin with five pages for the website.

****Page 1-3, Home Page:****
Log-in opens to Student's Bookshelf/Dashboard.

Student's Bookshelf/Dashboard:
- Show bookshelf (books read, books to read, recommendations)
- Badges/points
- Message/note from parent (can include emoji)
- Current storybook
- reading chart, shows pages read, amount of time read
- secured option/model window for parent to manage emails, calendar for progress reports

****_or_****

Parent's Dashboard:
Log-in opens to Parents Dashboard.
- same as above with following features
- calendar to choose when to get progress report
- email to receive reports and audio (audio is automatically sent, not saved on server/database)

****_Title Page/Book Contents_****

Opening page to story:
- Shows cover with title
- slider on bottom of page to go to chapter

****Page 4, Story Page:****
Listen and read the story.  
- Audio player with 'play','pause'
- Print of the story, read the word, and click each word to hear it pronounced.
- Avatar and Reading chart to show picture of user and points/badges.  After certain amounts of points are reached, an encouraging message "Great job!", "You rock!"...also use emoji/icon.

****Page 5, Unscramble Page:****
Unscramble the word and sentences.
- Use drag and drop letters to unscramble words used in the story.  
- Use drag and drop words to unscramble sentences used in the story.


### Data Model

Auto generation of the following pages:

- bookshelf  
- title page
- storybook page 

The contents (text, audio, video) are stored in the Django data base.  Django templates are used/designed so each page is build/compiled by accessing the data from the database by using template tags, template variables.

Actions that will be collected, stored in the database, sorted/analyzed and finally visualized are the following:

- time on the page (with activity, stops at no activity at 5 min)
- clicks on each word of the story
- clicks on the audio player
- recording of story, emailed to assigned email

The Reading Chart will visually display these actions with 'merits'.  Stars and badges are used to show the students progress.

Here is an overview of the basic data outline:
![Data Outline](img/CapStone_outline.png)

### Technical Components
++ this will become more specific and clear as the project evolves (next draft of this document)

- jQuery/HTML: capturing the clicks, time on screen user data on the server and then sending to Django framework  +still researching options, is there an API that facilitates this
- Bootstrap: Log-in and dashboard design
- jQuery UI: accordion, droppable, sortable, date picker, select menu
- Flexbox, JavaScript, etc: further functionality for web pages +used with HTML, CSS
- d3j.org: block 6007521 (ball shaped, daily graph for data)
- 3rd party(podsnack)/HTML & CSS/JQuery for audio player and or recorder
- Python/Django: building database on server (storing data, sending back and forth to server)




### Schedule

Time will be split between the front-end and the back-end.  At this time this is a rough estimate due to lack of knowledge about Django

****week one:****
- front-end: finish the mockup of the _story page_, _unscramble page_, wireframe the dashboards

- back-end: start learning Jdango and wireframe how to connect, store and send data to the client. Continue to plan how to visualize the data from the user interactions and send back to server/email.  

****week two:****
- front-end: implement basic functionality on the web page for _story page_ and _unscramble page_, mockup of the _dashboards_
- back-end: complete back-end wireframes/outline, start building the framework to collect the data from the _story page_ and _unscramble page_

****week three:****
- front-end: continue to build and fine tune the functionality on the web page for _story page_, _unscramble page_, the _dashboards_
- back-end: continue to build the framework to collect the data from the _story page_, _unscramble page_ and the _dashboard_

****week four:****
- front-end: finish up details, prepare presentation
- back-end: finish up details, prepare presentation


### Further Work

Options:
- audio player to record and send clip to email address
- messages from child to parent and parent to childv
- choose only one dashboard for MVP(student or parent) then start the other after one is working
- teacher dashboard, with environment to contact her entire class
- package this project as an online story book library, then offer publishing service to independent authors
- finish one story book and play pages (unscramble, color, match)
