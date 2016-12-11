# PSErrbot

Using `pywinrm` with Errbot.

<!-- TOC depthFrom:2 -->

- [Linux / Mac](#linux--mac)
    - [Env Var](#env-var)
    - [Create Virtualenv and install](#create-virtualenv-and-install)
    - [Run the bot in text mode for development](#run-the-bot-in-text-mode-for-development)
- [Vagrant](#vagrant)
    - [Env Var](#env-var)
    - [Do the vagrant thing](#do-the-vagrant-thing)
- [Docker](#docker)
    - [Build](#build)
    - [Run](#run)

<!-- /TOC -->

## Linux / Mac
### Env Var
Set environment variable:

`export SLACK_API_TOKEN='xoxb-XXXXXX-XXXXX'`

### Create Virtualenv and install
```
virtualenv -p `which python3` errbot
source errbot/bin/activate
pip install -r requirements.txt
```

### Run the bot in text mode for development
```
errbot -T # text mode for testing
```

## Vagrant
### Env Var
Set environment variable:

`export SLACK_API_TOKEN='xoxb-XXXXXX-XXXXX'`

### Do the vagrant thing
```
vagrant up
```

## Docker
### Build
```
docker build -t matthodge/errbot:latest .
```
### Run
```
 docker run matthodge/errbot
```