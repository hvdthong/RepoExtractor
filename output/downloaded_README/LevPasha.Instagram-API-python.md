# Instagram-API-python
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=7BMM6JGE73322&lc=US&item_name=GitHub%20donation&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted" title="Support project"><img src="https://img.shields.io/badge/Support%20project-paypal-brightgreen.svg"></a>
<a href="https://github.com/LevPasha/Instagram-bot-cs" title="Instagram C# bot"><img src="https://img.shields.io/badge/C%23%20InstaBot-v1.0-blue.svg"></a>
<a href="https://github.com/LevPasha/instabot.py" title="python InstaBot"><img src="https://img.shields.io/badge/python%20InstaBot-v1.0.1-blue.svg"></a>
<a href="http://isdb.pw" title="Instagram stories data base"><img src="https://img.shields.io/badge/ISDB.pw-free-purple.svg"></a>

Unofficial Instagram API to give you access to ALL Instagram features (like, follow, upload photo and video, etc)! Written in Python.

This is the Python port of https://github.com/mgp25/Instagram-API which is written in PHP.
It is still a work in progress to copy all of its API endpoints.

NOTE: To successfully parse for a long time you should verify your phone number in your Instagram account. 
The new fake Instagram account with an unverified phone number after ~ 1-24 hours could not do any requests. All requests will be redirected to the page https://instagram.com/challenge

### Installation Instructions

1. Fork/Clone/Download this repo

    `git clone https://github.com/LevPasha/Instagram-API-python.git`


2. Navigate to the directory

    `cd Instagram-API-python`


3. Install the dependencies

    `pip install -r requirements.txt`


4. Modify examples\test.py with your own username and password


5. Run the test.py script (**use text editor to edit the script and type in valid Instagram username/password**)



### Pip Installation Instructions
1. Install via pip

    `pip install InstagramApi`

    or

    `py -m install InstagramApi`

2. Import InstagramAPI from a python command prompt

    `from InstagramAPI import InstagramAPI`
