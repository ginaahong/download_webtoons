# 📥 Download Webtoons 🎨
Using selenium and BS4 to automatically download Daum and Naver webtoons for offline reading!

## Table of Content

| Section Name  | Section Description |
| ------------- | ------------- |
| [0 - About this project](https://github.com/ginaahong/download_webtoons/blob/master/README.md#0-about-this-project)  | Explaining what this project is and why it was made  |
| [1 - Tech description](https://github.com/ginaahong/download_webtoons/blob/master/README.md#1-tech-description)  | Write up on some of the tech involved in the project  |
| [2 - Future plans](https://github.com/ginaahong/download_webtoons/blob/master/README.md#2-future-plans) | Additional features I want to add later down the road! |
| [3 - Legal disclaimer](https://github.com/ginaahong/download_webtoons/blob/master/README.md#3-legal-disclaimer) | Just a legal disclaimer |

## 0. About this project
### What are webtoons?
  Webtoons are a sort of cultural phenomena in a lot of Asian countries! As far as I know, Korea's main 'source' of webtoons are from
  two portal giants: Daum.net and Naver.com
  They're basically scrollable, digital comics that updated every week.

### Why build this project?
  A few years ago a friend actually asked if it'd be possible to create a program that could download freely available webtoons to read them offline.
  At the time I didn't really know much about webscraping or coding, so I thought the only way was to painstakingly screenshot or save each of the comic's image files.
  Thankfully, I know a little bit more about webpages and coding, and thought I'd try my hands on automatically downloading webcomics!

### What does this project do?

  | [Input] link | [Input] Directory | [Output] Dir of .jpeg |
  |----|----|------|
  | https://webtoon.daum.net/webtoon/... | ~/path/to/output/dir | ~/comic_title/...jpeg |

  As of June 23rd 2019, given a link to **1 DAUM or NAVER comic episode**, and a path for the output files, it will download the webcomic as jpeg/jpg on to the output directory. Make sure the link is surrounded by single quotes ('). This just ensures that the command line arguments are passed correctly to the program, since some links may include ambpersands (&) in them.

  Now with the setup.py, and organized directories you should be able to install this as a package and run it in command line!

    pip install dlwebtoon
    dlwebtoon 'link_to_webtoon' /path/to/output_directory


## 1. Tech description
### Virtual Environment
  I wanted to use Python 3 for this project, but this conflicted with Python2 already installed. Hence, I opted to use virtualenv.

  Creating virtualenv:

    pip install --upgrade virtualenv
    virtualenv -p python3 envname //webtoon_dl in our case

  To activate the script:

    source /path/to/ENV/bin/activate
    python -v //should show 3.7

  To run the program:

    python webtoondl.py link_to_comic /path/to/output

  OR

    pip install dlwebtoon
    dlwebtoon 'link_to_webtoon' /path/to/output_directory

  ~~*You may need to install some packages to run the program. Such as:*~~
  With setup.py, all the necessary packages should be installed when you 'pip install dlwebtoon'

  | Package | Version |
  |----|----|
  | beautifulsoup4 | 4.7.1 |
  | selenium | 3.141.0 |
  | chromedriver | 2.24.1 |
  | imageio | 2.5.0 |

    pip install package_name

### HTML parsing
  There were a lot of options in which tool to use for webscraping. There's Scrapy (webscraping framework), Urllib, and Requests. But I ultimately opted for Selenium!
  I originally tried using urllib, simply because it's included in Python's standard library (meaning no extra installs!), but the images I wanted seem to be loaded clientside via JavaScript.
  (see get_imgurl.py)

### Parsers
  I knew of two options: LXML and BeautifulSoup. I chose BeautifulSoup since there seemed to be a lot of online tutorials and documentation on it!

  ![Here's how I worked on it!](https://github.com/ginaahong/download_webtoons/blob/master/images/workinprogress.png)

### Downloading the image
  Used imageio to first read the images to a bufferimage, then saving the bufferimage to a specific filepath.

  ![Here's how an output folder would look like](https://github.com/ginaahong/download_webtoons/blob/master/images/output.png)


## 2. Future plans
### Daum / Naver distinguishing - DONE (June 24 2019)
  ~~Currently this program only works for Daum webcomics. Later on I plan to make it work for both Daum and Naver webcomics.~~
  I have now implemented support for Naver webtoons too. This was a bit harder since there were some 403 forbidden errors and such. But I found an adequate work around in providing user agents.

### Setup.py and running in command line
    I have now implemented this!

        pip install dlwebtoon
        dlwebtoon 'link_to_comic' /path/to/output

### Combine multiple .jpeg
  One 'episode' of a webcomic is around ~10 .jpeg files. I hope to later on implement an optional function that just stiches together these images automatically.

### One link to download entire webtoon
  It's quite a hassle to download an entire webtoon with the current system. You have to input a new link for every episode of the comic in order to download everything. I want to implement a feature where it'll automatically go through the entire episode list and download all the episodes available. I expect this to be a bit difficult since there's no easy way to identify how many episodes there are for one comic, and whether or not the comic is 'completed' or not.

## 3. Legal disclaimer
  The main purpose of building this program was for me to 1) learn how to build a command line tool and 2) get a small taste of how procedures can be automated.

  With these learning objectives in mind, this program was built for people to enjoy free webtoons offline.
  Please note that using this program to distribute the comics could go against copyright laws.

  More details on why "personal use" is legal.
        In the Korean copyright law it states:
        제30조(사적이용을 위한 복제) 공표된 저작물을 영리를 목적으로 하지 아니하고 개인적으로 이용하거나 가정 및 이에 준하는 한정된 범위 안에서 이용하는 경우에는 그 이용자는 이를 복제할 수 있다. 다만, 공중의 사용에 제공하기 위하여 설치된 복사기기에 의한 복제는 그러하지 아니하다.
