FROM python:3
#-onbuild
# onbuild python docker images are for testing python apps
#copy current folder to /src inside of container
RUN mkdir /code
COPY . /code
VOLUME ["/testData"]


WORKDIR /code
ADD requirements.txt /code/
# installing dependencies
RUN pip install -r requirements.txt

# running app.py code
#WORKDIR /code
CMD ["./wait-for-it.sh", "db:5432", "--", "python", "app.py"]
