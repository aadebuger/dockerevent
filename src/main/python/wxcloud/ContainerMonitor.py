'''
Created on Mar 21, 2016

@author: aadebuger
'''

from ahab import Ahab
import containersignal
import ContainerAdm

def subConfig():
    
    containersignal.containerdestroy.connect(ContainerAdm.subscriber)
def f(event, data):
#    print 'event=',event
    print("status",event['status'],'from',event['from'])
    print 'data=',data
#    pass        # Handle the Docker event (and extended info, as available)
    if event['status']=='kill':
        print 'State',data['State']
        print 'Config',data['Config']
        print 'Name',data['Name']
        containersignal.containerdestroy.send(event)

def startAhab():
    pass

if __name__ == '__main__':
    subConfig()
    ahab = Ahab(handlers=[f])
    print 'listen'
    ahab.listen()