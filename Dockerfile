from python:2.7
run pip install ahab
run pip install docker-map
run pip install blinker
add src/main/python /code
workdir /code
CMD ["python","-m","wxcloud.ContainerMonitor"]
