# ircholla [![Build Status](https://travis-ci.org/wwitzel3/ircholla.svg?branch=master)](https://travis-ci.org/wwitzel3/ircholla)

A very simple library that connects to an IRC server and sends a
notice or message to a channel. It supports very few features and
does not handle failure cases well.

Currently you can only connect to a single server, join a single channel,
and send a single message. Each new message requires a completely new
connection.

## Why

Needed an IRC notify library that didn't require any extra dependencies.

## Features

 - Will attempt to find a random name if there is a NICK conflict.
 - Can join channels with keys.
 - Can send either a NOTICE or PRIVMSG to a channel.
 - No dependencies on large libraries.

## Usage
```python
    from ircholla import Holla
    myholla = Holla('chat.freenode.net:6667', '#botwar', 'mybot123')

    # note, this will connect a bot for notice and msg
    myholla.notice('I need you')
    myholla.msg('I need you')
```

