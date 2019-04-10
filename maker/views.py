from django.shortcuts import render

import wikipedia
import urllib.request
import urllib.parse
import re

# Create your views here.

def maker(request):
    title = wikipedia.search(request.GET.get('title'))[0]
    page = wikipedia.page(title)
    (card_title, *cards) = wikipedia.summary(title).split(". ")
    sessaoi = page.content.find("==")+2
    sessaof = page.content[sessaoi:].find("==")+sessaoi
    sessao = page.content[sessaoi:sessaof].strip()
    textao = page.section(sessao)
    # tabela = page.html()[page.html().find("<table"):page.html().find("</table>")].replace("\n", "")
    html_content = urllib.request.urlopen("http://www.youtube.com/results?search_query=" + title)
    search_results = re.findall("href=\"\/watch\?v=(.{11})", html_content.read().decode())
    video = "http://www.youtube.com/embed/" + search_results[0]
    return render(request, 'maker/base.html', { 
        'titulo': title, 
        'card_title': card_title,
        'card1i' : cards[0],
        'card2i' : cards[1], 
        'card3i' : cards[2],
        'video': video,
        'textao': textao,
        'sessao': sessao,
    })