# Capstone Readme


### Intro

Title: Storia

Storia is a web app for children to learn to read with interactive storybooks. It turns plain stories into interactive stories with an analyses of the child's progress. 

It is divided into two main parts: 
    1. user interactivity with the storybook page (click and hear words, unscramble words and sentences, play video, record audio)
    2. collects user interface data, stores the data, visualizes and analyzes the data and shares the data.

link to project:
<a href="docs/my_proposal.md">Rebecca's Proposal</a>

### Setup

1. Media folders are built and filed by multiple upload functions built within the apps.models.  Visual, audio and video media is managed through the admin, built in Django.
2. There are three types of users: 
    a. superuser (me) --  creates and manages the storybook pages and the entire website through the admin.  
    b. child/parent or teacher/student -- access their own bookshelf and storybooks, a merit dashboard to observe progress.  (Audio, word/sentence scrambles, and message interaction to be added at a later date.)
    c. author (future feature)-- access his or her dashboard that monitors user interactivity with the interactive online storybook books that he or she has authored.  This publishing feature can be done multiple ways such as embedding into the author's website or maintained in the Storia library.  Both will require deployments to be further explored and decided upon.
3. REST Framework and other useful APIs 
4. Initial development with db_sqlite3.  As project develops move to  PostgreSQL.
5. Deploy to AWS, AWS Elastic Beanstalk.

### Usage

TBD
