import pytest
from ircholla import Holla


@pytest.fixture
def holla():
    return Holla('irc.example.org:6667', '#test', 'nickname')


def test_holla_noport():
    holla = Holla('irc.example.org', '#test', 'nickname')
    assert holla.port == 6667


def test_handle_new_connection(holla):
    holla._handle(':servername 001 :more stuff')
    assert holla._deque.popleft() == ':source JOIN #test\n'


def test_handle_nick_inuse(holla):
    holla._handle(':servername 433 :nick in use')
    assert holla._deque.popleft().startswith('NICK nickname_')
    assert holla._deque.popleft().startswith('USER nickname_')


def test_handle_join_msg(holla):
    holla.notice = False
    holla.message = 'test'
    holla._handle(':server JOIN #test')
    assert holla._deque.popleft().startswith('PRIVMSG')
    assert holla._deque.popleft().startswith('QUIT')


def test_handle_join_notice(holla):
    holla.notice = True
    holla.message = 'test'
    holla._handle(':server JOIN #test')
    assert holla._deque.popleft().startswith('NOTICE')
    assert holla._deque.popleft().startswith('QUIT')
