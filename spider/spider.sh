#!/usr/bin/env bash
rm ../data/articles.csv
scrapy runspider ./spider.py -o ../data/articles.csv
