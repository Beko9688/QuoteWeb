from django.shortcuts import render
from django.http import HttpResponse
from .models import Quotes
import wikipedia
from wikipedia.exceptions import PageError


def index(request):
    quote = Quotes.objects.order_by('?')[0]
    quote_text = quote.quote_text
    author_name = quote.author
    return render(request, 'quoteapp/index.html', {'quote_text': quote_text, 'author_name': author_name})

def get_about_author(request, name):
    try:
        wikipedia.set_lang("ru")
        page = wikipedia.page(name)
        info = page.summary
        wiki_url = page.url

        return render(request, 'quoteapp/about_author.html', {'info': info, 'wiki_url': wiki_url})

    except PageError as page_error:
        return HttpResponse(f'<h2 align="center">{page_error}</h2>')
    except:
        return HttpResponse('<h2 align="center">Википедия не отвечает попробуйте заного</h2>')
