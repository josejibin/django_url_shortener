from django.shortcuts import render
from django.http import HttpResponse
from models import UrlTable
from forms import UrlForm
import random
from django.http import HttpResponseRedirect

def home(request):
  form = UrlForm()
  if request.method=="POST": 
    form = UrlForm(request.POST)
    if form.is_valid():
      if form.is_valid():
        url = form.cleaned_data['original_url']
        url_set = UrlTable.objects.filter(original_url = url)
        if not url_set:
        	short_url=str(random_string(5))
        	p = UrlTable(original_url = url,shortened_url = short_url)
        	p.save()
  
  url_set = UrlTable.objects.all()
  return render(request,'url.html',{ 'form': form , 'urlset': url_set } )


def change(request,url=None):
  print url
  shortUrl = url
  url_set = UrlTable.objects.filter(shortened_url = shortUrl)
  if url_set:
  	for i in url_set:
  		orgUrl = i. original_url
    	return HttpResponseRedirect(orgUrl)
  else:
    return render('pageNotFound.html',url=url)
  


def random_string(length=5):
  possibles = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  return ''.join(random.choice(possibles) for i in range(0, length))