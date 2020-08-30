from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Article
from .forms import ArticleModelForm
# Create your views here.

class ArticleListView(ListView):
    template_name = 'blog/article-list.html'
    queryset = Article.objects.all() # <blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    queryset = Article.objects.all() # <blog>/<modelname>_list.html

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    queryset = Article.objects.all()


"""
def blog_main_view(request):
    return render(request, 'blog/blog_main.html', context={})

def article_detail_view(request):
    form = ArticleModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleModelForm()
    context = {
        'form': form}
    return render(request, 'blog/article_detail.html', context)
"""