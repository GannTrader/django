from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Catagory
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
    # return render(request, 'home.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']

    def get_context_data(self, *args, **kwargs):
        # cat_menu = Catagory.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["cat_menu"] = Catagory.objects.all()
        return context

def CatagoryListView(request):
    cat_menu_list = Catagory.objects.all()
    return render(request, 'catagory_list.html', {'cat_menu_list':cat_menu_list})

def CatagoryView(request, cats):
    catagory_posts = Post.objects.filter(catagory=cats.replace('-', ' '))
    return render(request, 'catagories.html', {'cats':cats.title().replace('-', ' '), 'catagory_posts': catagory_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Catagory.objects.all()
        context = super().get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class AddCatagoryView(CreateView):
    model = Catagory
    # form_class = PostForm
    template_name = 'add_catagory.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
