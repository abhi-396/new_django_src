import requests 
from bs4 import BeautifulSoup

def scrap_contents(input_string):
    url = "https://www.google.com/search?&q=real+estate"
    url = (url+'+'+input_string) if input_string else url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    service_tags = soup.find_all('a', {'class': 'tHmfQe'})
    if len(service_tags) > 1:
        service_output = []
        for tag in service_tags:
            temp_name = tag.find('div', {'class': 'BNeawe'}).text
            temp_href = tag.get('href')
            obj = {
                'name': temp_name,
                'href': temp_href
            }
            service_output.append(obj)
    
    content_tags = soup.find_all('div', {'class': 'kCrYT'})
    if len(content_tags):
        content_output = []
        for tag in content_tags:
            if tag.find('a'):
                temp_name = tag.find('div', {'class': 'BNeawe'}).text
                temp_href = tag.find('a').get('href')
                obj = {
                    'name': temp_name,
                    'href': temp_href
                }
                content_output.append(obj)
    
    news_output = scrap_news(url)
    
    res = {}
    res['services'] = service_output if (service_output and len(service_output)>0) else ''
    res['contents'] = content_output if (content_output and len(content_output)>0) else ''
    res['news'] = news_output if (news_output and len(news_output)) else ''
    return res

def scrap_news(url):
    url = url+'+news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    tags = soup.find_all('div', {'class': 'kCrYT'})
    if len(tags):
        news_output = []
        for tag in tags:
            if tag.find('a'):
                temp_name = tag.find('div', {'class': 'BNeawe'}).text
                temp_href = tag.find('a').get('href')
                obj = {
                    'name': temp_name,
                    'href': temp_href
                }
                news_output.append(obj)

    return (news_output if (news_output and len(news_output)>0) else None)
