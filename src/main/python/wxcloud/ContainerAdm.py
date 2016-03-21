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
def startContainer1():
        cli = Client(base_url=DOCKER_HOST)
        print('container=',cli.containers())
        
        container = cli.create_container(image='aadebuger/lightingthrift',ports=[9092],
    host_config=cli.create_host_config(port_bindings={
        9092: 9090
    }))
        cli.start(container)
#         client.start('aadebuger/lightingthrift', expose={9092: 9090})         
    
if __name__ == '__main__':
     startContainer1()