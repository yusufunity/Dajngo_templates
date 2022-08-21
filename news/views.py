from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# def home(request):
# 	news=News.objects.all()
# 	ozger='<h1>Yangiliklar Royxati</h1>'

# 	for item in news:
# 		ozger+=f"<div>\n<p>{item.title}</p>\n<p>{item.content}</p></div><hr>"
# 	return HttpResponse(ozger)




# def test(request):
# 	return HttpResponse('<h1>Test Rejim </h1>')


# derektiva ,tegiy ,filter

def home(request):
	# news=News.objects.all()
	news=News.objects.order_by('-create_at')
	context={
		'news':news,
		'title':'News yangiliklar'
	}
	## 1-variant
	# return render(request,'news/index.html',{'news':news,'title':'News yangiliklar'} )
	## 2-variant
	return render(request,template_name='news/index.html', context=context)