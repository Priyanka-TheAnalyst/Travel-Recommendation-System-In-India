import scrapy
import re

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.holidify.com']

    start_urls = ['https://www.holidify.com/country/india/places-to-visit.html' ]

    def parse(self, response):


        if response.css('h2::text').re(r'\d+\.\s*\w+'):
            print(response.css('h2::text').re(r'\d+\.\s*\w+'))

        elif response.css('b::text').re(r'\d+\.\s*\w+'):
            print(response.css('b::text').re(r'\d+\.\s*\w+'))