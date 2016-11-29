# facestats

This is a script to calculate some numbers and statistics on your use of Facebook. Currently does some basic analysis on chat history, including length of your messages, and proportion of conversations started by you v.s. your friends.

# Installation

This is a lightweight Python script. First, make sure you have Python 2 and `pip` installed on your system. Then, install the dependencies of this project (currently, the only dependency is `beautifulsoup`).

```
pip install beautifulsoup4
```

If your system complains about lxml missing, some combination of the following packages may work: `python-dev libxml2 libxml2-dev libxslt-dev python-lxml`

# Usage

[Download a copy of your Facebook data.](https://www.facebook.com/settings). Unzip, then run

```
python fbstats.py <directory of your fb data>/html/messages.htm
```

This may take a few minutes -- I personally have 30mb of message history over 4+ years. Currently the script runs locally so you don't have to worry about your private messages going into my inbox.

Facebook's data is very inconsistent, it may be missing user names, etc. If you run into any issues with the script, feel free to create a Github issue.

# Ideas

See https://dynalist.io/d/wuhWHlISJ3kV1bEF_YWatgQa
