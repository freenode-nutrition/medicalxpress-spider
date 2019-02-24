#!/usr/bin/env bash
rm -v ../data/articles.csv
scrapy runspider ./spider.py -o ../data/articles.csv
