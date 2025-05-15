from django.shortcuts import  get_object_or_404,render, redirect
from .models import ArticlesModel
from .forms import ArticleCreateForm
# Create your views here.

def get_list_view(request):
    articles = ArticlesModel.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'home.html',context)

def get_detail_view(request, pk):
    article = ArticlesModel.objects.get(id=pk)
    context = {
        'article':article
    }
    return render(request, 'detail.html',context)


def post_create_view(request):
    if request.method == "POST":
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form':form
            }
            return redirect('home')
            #return render(request,'home.html', context)
    else:
        form = ArticleCreateForm()
    context = {
        'form':form
    }
    return render(request, 'create.html', context)

def post_edit_view(request, id):
    article = get_object_or_404(ArticlesModel, id=id)
    if request.method == "POST":
        form = ArticleCreateForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =  ArticleCreateForm(instance=article)
    context = {
        'form':form,
        'article': article
    }
    return render(request, 'edit.html', context)

def post_delete_view(request, id):
    article = get_object_or_404(ArticlesModel, id=id)
    if request.method == "POST":
        article.delete()
        return redirect('home')
    return render(request, 'delete.html', {'article':article})




















    


