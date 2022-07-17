# Hack-A-Thors 
  Present A Website to solve all your brainstorming doudts with 'Ideas'
  
## Problem Statement:-

Part 1 - Many students who are willing to participate in hackathons despite having the tech stack skills and knowledge of theme/ domain, are unable to bring up innovative project idea topics to solve some problems.

Part 2 - Any student who wants to explore a particular CS domain/ techstack would love to see what latest problems solved/ projects build in this domain by students around the country.

## Inspiration

As avid hackathon attendees, we've noticed that there's always a lot of pressure to come up with clever ideas with the potential to win.Many a times it takes 
a lot of time just to come up with an idea and just as you notice,poof! time is out of your hand.

## Solution:- 

A website which lists out hackathon winning/ starred projects from hackathons happening around the country, month wise. The listing of projects will be done in the following manner:-

-> Top 10 projects - overall In this section, top 10 hackathon winning/starred projects of each month will be listed.

-> Top 10 projects - domain wise In this section, every domain like WD, AD, ML, Blockchain, Web3, etc. will have corresponding top 10 list of hackathon winning/ starred projects, month wise.

-> Top 10 projects - theme wise In this section, every theme like Healthcare, Education, Environment, Finance, etc. will have corresponding top 10 list of hackathon winning/ starred projects, month wise

Every project will have corresponding information:-

->Problem statement of the project

->Solution presented

->Techstacks used in the project

->The card will have url which will direct the interested candidate to the github repo of the hackthon project 

## Challenges I ran into

One interesting result of training the GPT-2 system on our scraped dataset was that some of the generated results were exact copies of taglines from the training set.
We're still trying to figure out how to prevent this kind of overtraining from occuring while maintaining high quality hackathon predictions.

On the web development side of things, we found it difficult to balance getting functional code out quickly with delivering high quality code. Obviously it would be ideal
for our code to be beautiful, but we chose to code quickly instead as ugly functional code is better than useless beautiful code. This was largely due to the fact that web
development requires a lot of boilerplate code which is both time consuming and difficult to debug.

Finally, in the process of generating logos and project names, the unofficial API we were hitting had inconsistent functionality, and many queries would cause errors
(somehow within 200 OK responses instead of a 4XX response). 

## What we learned

This was our first time using Uipath for webscraping, and we found it to be an essential and natural part of our workflow in order to retrieve winning hackathon ideas from Devpost.
We used this data to train a machine learning model for idea generation. We've never done text generation using machine learning before, and discovered a program that allows us to 
train OpenAI's GPT-2 model on our own dataset in a process called "fine-tuning", which takes the original GPT-2 model and alters its weights to optimize for our given input data. This forces
the output to be in a similar format to our training data, while maintaining all of the NLP features of the original GPT-2 model.

Additionally, to get banner images for our generated ideas, we used the Google images API, which allows us to programmatically search through google images and find relevent content based off
of keywords in our idea descriptions.

A few of us also didn't have a lot of web development experience, and found this project to be a tremendous learning experience for building full stack web applications.

## Built with

  HTML, CSS, flask , python, bootstrap, javascript

## Deployed with 
  Heroku
