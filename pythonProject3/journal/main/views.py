from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def main(request):
    return render(request, 'main/home.html')


class NewsView(ListView):
    model = News
    template_name = "main/posts.html"
    context_object_name = 'news_list'
    ordering = '-date'

    def get_context_data(self, **kwards):
        ctx = super(NewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Статьи'
        return ctx

class NewsDetail(DetailView):
    model = News
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super(NewsDetail, self).get_context_data(**kwargs)
        ctx['title'] = self.object.name
        return ctx


class NewsAdd(LoginRequiredMixin, CreateView):
    model = News
    template_name = "main/create_news.html"
    context_object_name = "addnews"

    def get_context_data(self, **kwargs):
        ctx = super(NewsAdd, self).get_context_data(**kwargs)
        ctx['title'] = 'Добавить новость'
        ctx['button'] = 'Опубликовать'
        return ctx

    fields = ['name', 'post']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


class NewsUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'main/create_news.html'
    fields = ['name', 'post']

    def get_context_data(self, **kwargs):
        ctx = super(NewsUpdate, self).get_context_data(**kwargs)
        ctx['title'] = 'Редактирование статьи'
        ctx['button'] = 'Сохранить изменения'
        return ctx

    def test_func(self):
        post = self.get_object()
        if post.avtor == self.request.user:
            return True
        return False

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


class NewsDel(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'main/delete.html'

    def test_func(self):
        post = self.get_object()
        if post.avtor == self.request.user:
            return True
        return False
