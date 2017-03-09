Jenkins Area Meetup @ UC Irvine
===============================

## Synopsis

This repo has a pipeline script and utility python program used for checking out, testing, and submitting homework assignments via eee.uci.edu

## Motivation

I often find myself submitting an assignment, notice something is wrong afterwards, and resubmit with the fix. When I wait until the last minute (intentionally), I forget to submit altogether. Jenkins allows me to continuously submit my assignment whenever and how many times I want.

## Installation

Assuming a Jenkins server is already configured, the following should get you off the ground:
```
git clone https://github.com/jamesalbert/jam-uci
cd jam-uci
ln -s $HERE/src/submit.py /usr/local/bin/submit.py
```

You also need to specify EEE credentials either in $HOME/.eee or the EEE_USERNAME and EEE_PASSWORD environment variables.

$HOME/.eee:
```
{
  "username": "jalbert1",
  "password": "XXXXXXXX"
}
```

There should also be a .eee file in the root directory of the project we're submitting to specify what and where to submit.

$PROJECT_DIR/.eee:
```
{
  "course": "143B",
  "assignment": "src/main.py",
  "name": "CS143B Project 3"
}
```

## API Reference

We'll be triggering the Jenkins build process via an api call. I'm currently using src/build.sh to trigger the builds. Here's a quick reference:
```
curl "http://localhost:8080/job/homework/buildWithParameters?token=buildWithParameters&course=$1&project=$2&assignment=$3&name=$4"
```
