'''
Created on Mar 21, 2016

@author: aadebuger
'''

from ahab import Ahab
import containersignal

def f(event, data):
#    print 'event=',event
    print("status",event['status'],'from',event['from'])
    print 'data=',data
#    pass        # Handle the Docker event (and extended info, as available)
    containersignal.containerdestroy.send(event)

def startAhab():


if __name__ == '__main__':
    ahab = Ahab(handlers=[f])
    print 'listen'
    ahab.listen()