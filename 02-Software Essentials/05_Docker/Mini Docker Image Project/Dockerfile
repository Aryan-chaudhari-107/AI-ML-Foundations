# base image
FROM python:3.9

# workdir
WORKDIR /app

# copy files
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# port 
EXPOSE 5000

# run app
CMD ["python", "app.py"]