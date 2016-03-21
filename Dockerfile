from python:2.7
run pip install ahab
add src/main/python /code
workdir /code
CMD ["python","-m","wxcloud.ContainerMonitor"]
