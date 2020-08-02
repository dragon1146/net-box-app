FROM ubuntu

RUN apt update && \
    apt install python3 -y && \
    apt install python3-pip -y
VOLUME [ "/app/src" ]

WORKDIR /app/src/

RUN pip3 --no-cache-dir install -r requirements.txt

ENV FLASK_APP=app.py 
ENV FLASK_RUN_PORT=11
ENV FLASK_RUN_HOST=0.0.0.0

# this line of code will expose port "11" on the container
EXPOSE 11