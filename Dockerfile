from python:2.7
run pip install ahab
run pip install docker-map
add src/main/python /code
workdir /code
CMD ["python","-m","wxcloud.ContainerMonitor"]
