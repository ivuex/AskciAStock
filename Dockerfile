FROM ivuex/3.7-alpine3.8-sshd7.7-scrapy1.5.1:latest

ADD . /AskciAStock
WORKDIR /AskciAStock
RUN pip install -r /AskciAStock/requirements.txt

ENTRYPOINT ["/bin/sh", "-c", "scrapy crawl askciAStock"]
