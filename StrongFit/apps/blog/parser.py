import requests
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
from django.http import HttpResponse
from PIL import Image
import os
import glob




def parsing(request):
 
    req = requests.get('http://blogozdorovie.ru/category/pravilnoe-pitanie') # получаем всю страницу
    html = BS(req.content, 'html.parser')
    
    result = {}     # Будем хранить все URL

    for el in html.select('.post'): # Разбиваем на посты
        result.update({el.find('a', rel="bookmark").text : el.find('a', rel="bookmark").attrs['href']}) # заголовок / url


    for val, key in result.items():     # Будем ходить по каждому URL и получать "детальную страницу" поста


        html = BS(requests.get(key).content, 'html.parser')     # Получаем содержимое страницы
        link = html.find('img').get('src')
        name_img = link.split('/')[-1]     # Получаем имя картинки поста "name.jpg"


        path = fr'media\posts\image\temp\{name_img}'         # Задаём путь для картинки
        Image.open(urlopen(link)).save(path)       # Сохраняем картинку в папку TEMP


        content = html.find_all(style="text-align: justify;")       # Собираем текст статьи
        txt = ''
        for block in content:
            txt = txt + block.text + '\n'

        payload =   {'title': val,        # Структура, которую нужно вернуть для модели Post
                    'text': txt
                    }
        
        files = [       # Передаваемые файлы
                    ('image_pub', open(path,'rb'))
                ]
                    
        url = 'http://127.0.0.1:8000/blog/create/'
        response = requests.request("POST", url,  data = payload, files = files)

       # os.remove(path)
    #os.remove(r'media\posts\image\temp')
    
    files = glob.glob('media/posts/image/temp/*')
    for f in files:
        os.remove(f)
    
    
    
    
    return HttpResponse('Спарсили отлично')