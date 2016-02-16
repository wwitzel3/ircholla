import select
import random
import socket
import collections


class Holla(object):
    '''Holla

    Simple class that will connect to an IRC server. Join the
    channel and send a notice or message to the channel.
    '''
    def __init__(self, server, channel, botname, **kwargs):
        server, sep, port = server.partition(':')

        self.server = server
        self.port = int(port) if port else 6667
        self.channel = channel
        self.botname = botname
        self.kwargs = kwargs
        self.sock = None

        self._deque = collections.deque()
        self.working = True
        self.debug = self.kwargs.get('debug', False)

    def notice(self, message):
        '''Sends a notice to the channel provided during instansiation'''
        self.notice = True
        self.message = message
        self._events()

    def msg(self, message):
        '''Sends a regular message to the channel provided during instansiation'''
        self.notice = False
        self.message = message
        self._events()

    def _events(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.server, self.port))
        sock.setblocking(0)

        self._deque.append('NICK %s\n' % self.botname)
        self._deque.append('USER %s 8 * :%s\n' % (self.botname, self.botname))
        channel = ':source JOIN %s' % (self.channel)
        if self.kwargs.get('key'):
            channel += ' %s' % (self.kwargs['key'])
        self._deque.append(channel+'\n')

        read_buffer = ''
        while self.working:
            read, write, _ = select.select([sock], [sock], [], 30)

            if read:
                read_buffer += sock.recv(4096)
                tmp = read_buffer.split('\r\n')
                read_buffer = tmp.pop()

                if tmp:
                    line = tmp[0].strip()
                    if self.debug:
                        print(line)
                    self._handle(line)

            if write and len(self._deque):
                if self.working:
                    data = self._deque.popleft()
                    sock.sendall(data)
        sock.close()

    def _handle(self, line):
        if '001' in line:
            channel = ':source JOIN %s' % (self.channel)
            if self.kwargs.get('key'):
                channel += ' %s' % (self.kwargs['key'])
            self._deque.append(channel+'\n')
        if '433' in line:
            self.botname = '%s_%d' % (self.botname, random.randint(100, 999))
            self._deque.append('NICK %s\n' % self.botname)
            self._deque.append('USER %s 8 * :%s\n' % (self.botname, self.botname))
        if 'JOIN' in line:
            if self.notice:
                self._deque.append('NOTICE %s :%s\n' % (self.channel, self.message))
            else:
                self._deque.append('PRIVMSG %s :%s\n' % (self.channel, self.message))
            self._deque.append('QUIT :My job is done.\n')
        if 'QUIT' in line:
            self.working = False
