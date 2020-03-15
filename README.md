# direct-instagram-bot

This robot is sending direct to a following's ID

### Description

This robot login in with any account and goes with the ID you give and send directs to a following's ID

### Advantages

- selenium
- python
- use mobileEmulation
- headless

### Todo list

- [x] separate the IDs and directories function
- [x] clicke following button instead followers button
- [x] scrolling on following list
- [x] print a message when the user cannot be found
- [x] get id list and  send them a direct
- [x] choosing to get data from follower or following
- [X] message for personal pages
- [ ] Optimize `getFollowingData‍‍` function

## How to use it?

1.Install python2, pip, virtualenv

2.Clone the project `git clone https://github.com/sajadadineh/direct-instagram-bot.git`

3.Create a virtualenv `virtualenv -p python3 venv`

4.Connect to virtualenv `source venv/bin/activate`

5.install packages using `pip install -r requirements.txt`

6.Download a Web Driver from [Selenium](https://www.selenium.dev/downloads/) and set in

`driver = webdriver.Chrome(executable_path='YOUR WEB DRIVER',chrome_options= option)`

7.Now program is ready. Run by `python app.py`
