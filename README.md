# SiteMaker
## About

This is a web application developed using python and django framework.
The idea of this project was to create a simple html page in which the texts and images would be changed according to the title you choose.


## How to use
The first thing you'll need to do is install the stuffs I used, which is:

- Pip3.6: package management;
- Django-admin: python framework for web;
- Wikipedia: api

After that, you will simply run `python3 manage.py runserver` on the main directory, then you'll open the browser on `localhost:8000/?title=` and the theme of the website you want right after the equal sign. If you get some kind of error on loading the themed page, try to use other titles.

## Example
With the aplication running, I opened my browser on `localhost:8000/?title=Cat` and this is the result I got:
![N|Solid](https://i.imgur.com/dGGLOwZ.jpg)

## How it works

First of all, this application wont generate the whole html page. It will simply use an base html and change some texts and images.
The application uses only a main route and only one view.
The texts are taken from wikipedia using their api for python.
The images used in the html are taken from source.unsplash.com.
![N|Solid](https://i.imgur.com/GlxU930.png)
On the navbar, only the main title will be changed to the title you chose
![N|Solid](https://i.imgur.com/s2JuCCx.png)
The carousel will be generated with three random pictures from source.unsplash.com
![N|Solid](https://i.imgur.com/TC5DtP1.png)
The main text is the first sentence of the wikipedia page of your title;
All of the card's images are randomly generated by source.unsplash.com and the texts are the following sentences after the main text.
![N|Solid](https://i.imgur.com/56waXvH.png)
The texts are the second section of the wikipedia page of your title and the video is the first video on youtube when you search by your title

## Another example
![N|Solid](https://i.imgur.com/rQBl99I.jpg)