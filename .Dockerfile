FROM python:3.8
RUN mkdir /app
WORKDIR /app/src
COPY . /app/src
RUN pip install -r requirements.txt
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/src/credentials.json

CMD ["scrapy", "crawl", "thuvienphapluat"]

# docker build ./ -f .Dockerfile -t crawl-class:thuvienphapluat
# Docker run -d -p 5004:5003 crawl-class:thuvienphapluat