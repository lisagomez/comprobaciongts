from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from .models import ComprobacionGastos


def home(request):
    context = {
        'posts': ComprobacionGastos.objects.all()
    }
    return render(request, 'inv/home.html', context)

class ComprobacionGastosListView(ListView):
    model = ComprobacionGastos
    template_name = "inv/home.html"
    context_object_name = 'ComprobacionGastos'
    ordering = ['-date_posted']

class UserComprobacionGastosListView(ListView):
    model = ComprobacionGastos
    template_name = 'inv/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'ComprobacionGastos'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ComprobacionGastos.objects.filter(author=user).order_by('-date_posted')

class ComprobacionGastosDetailView(DetailView):
    model = ComprobacionGastos

class ComprobacionGastosCreateView(CreateView):
    model = ComprobacionGastos
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ComprobacionGastosUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = ComprobacionGastos
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ComprobacionGastos = self.get_object()
        if self.request.user == ComprobacionGastos.author:
            return True
        return False    
    
class ComprobacionGastosDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = ComprobacionGastos
    success_url = '/'

    def test_func(self):
        ComprobacionGastos = self.get_object()
        if self.request.user == ComprobacionGastos.author:
            return True
        return False

def about(request):
     return render(request, 'inv/about.html')