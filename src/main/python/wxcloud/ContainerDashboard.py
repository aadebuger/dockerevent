'''
Created on Mar 22, 2016

@author: aadebuger
'''
from twisted.internet import reactor


def f(s):
    print "this will run 3.5 seconds after it was scheduled: %s" % s


if __name__ == '__main__':
    reactor.callLater(3.5, f, "hello, world")

# f() will only be called if the event loop is started.
    reactor.run()
