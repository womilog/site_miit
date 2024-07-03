from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AddPrepodPostForm, EditPrepodPostForm
from .models import Prepod
from .utils import DataMixin


class PrepodyHomeView(ListView):
    model = Prepod
    template_name = 'prepody/prepody_home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Prepod.published.all()
        context['title'] = 'Преподы'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Prepod.published.all().select_related('cat')



class PrepodPostView(DetailView):
    template_name = 'prepody/prepody_post.html'
    context_object_name = 'prepod'
    slug_url_kwarg = 'post_slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Препод' + context['prepod'].nickname
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Prepod.published, slug=self.kwargs[self.slug_url_kwarg])



class PrepodyCategoryView(ListView):
    template_name = 'prepody/prepody_home.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория ' + cat.name
        context['cat_selected'] = cat.id
        return context

    def get_queryset(self):
        return Prepod.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')



class PrepodyAddPageView(LoginRequiredMixin, CreateView):
    template_name = 'prepody/add_prepody_post.html'
    form_class = AddPrepodPostForm
    success_url = reverse_lazy('prepody_add_page')
    # permission_required = 'prepody.prepody_add_page'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи о преподе'
        return context

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class PrepodyEditPageView(LoginRequiredMixin, UpdateView):
    form_class = EditPrepodPostForm
    template_name = 'prepody/edit_prepody_post.html'
    success_url = reverse_lazy('home')
    # permission_required = 'prepody.prepody_edit_page'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование статьи'
        return context

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Prepod.published.all()


class PrepodyDeletePageView(LoginRequiredMixin, DeleteView):
    model = Prepod
    success_url = reverse_lazy('prepody_home')
    template_name = 'prepody/delete_prepody_post.html'
    title_page = 'Удаление статьи про препода'
    # context_object_name = 'prepod'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление статьи'
        print(kwargs)
        return context

    # def post(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)



