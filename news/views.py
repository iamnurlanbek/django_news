from django.shortcuts import render, get_object_or_404
from .models import New, Category

def news_list_view(request):
    news = New.objects.all()
    categories = Category.objects.all()

    context = {
        'news':news,
        'categories':categories
    }
    
    return render(request, 'index.html', context=context)

def news_detail_view(request, pk):
    news = get_object_or_404(New, id=pk)
    
    context = {
        'news':news
    }
    
    return render(request, 'news_detail.html', context)