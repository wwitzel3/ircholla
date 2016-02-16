# ircholla

A very simple library that connects to an IRC server and sends a
notice or message to a channel. It supports very few features and
does not handle failure cases well.

Currently you can cannot to a single server, join a single channel,
and send a single message.

## Features

 - Will attempt to find a random name if there is a NICK conflict.
 - Can join channels with keys.
 - Can send either a NOTICE or PRIVMSG to a channel.
 - No dependencies on large libraries.

## Usage
```python
    holla = IRCHolla('chat.freenode.net:6667', '#botwar', 'mybot123')

    # note, this will connect a bot for notice and msg
    holla.notice('I need you')
    holla.msg('I need you')
```

