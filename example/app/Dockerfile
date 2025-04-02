# flask python image
FROM python:3.11-slim
# set working directory
WORKDIR /app
# copy requirements.txt
COPY requirements.txt . 
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy all files
COPY . .
# expose port 5000
EXPOSE 5000
# set environment variable
ENV FLASK_APP=app.py
# run flask app
CMD ["flask"]
