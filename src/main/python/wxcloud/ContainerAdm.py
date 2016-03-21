'''
Created on Mar 21, 2016

@author: aadebuger
'''

from docker import Client
from datetime import datetime
import os
import socket
from dockermap.api import ContainerMap
from dockermap.api import DockerClientWrapper, DockerFile

DOCKER_HOST = os.getenv('DOCKER_HOST', 'unix:///var/run/docker.sock')

def startContainer():
         client = DockerClientWrapper('unix://var/run/docker.sock')
         client.start('aadebuger/lightingthrift', expose={9092: 9090})
         
    
if __name__ == '__main__':
     startContainer()