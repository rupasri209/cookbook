from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView , UpdateView , FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from cook.models import Recipe

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'cook/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('recipes')

class RegisterPage(FormView):
    template_name = 'cook/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('recipes')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request , user)
        return super(RegisterPage,self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('recipes')
        return super(RegisterPage,self).get(*args,**kwargs)
class RecipeList(LoginRequiredMixin,ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'cook/recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = context['recipes'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['recipes'] = context['recipes'].filter(title__icontains = search_input)
        context['search_input'] = search_input
        return context

class RecipeDetail(LoginRequiredMixin,DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'cook/recipe.html'

class RecipeCreate(LoginRequiredMixin,CreateView):
    model = Recipe
    fields = ['title','ingredients','procedure','link']
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        return super(RecipeCreate,self).form_valid(form)

class RecipeUpdate(LoginRequiredMixin,UpdateView):
    model = Recipe
    fields = ['title','ingredients','procedure','link']
    success_url = reverse_lazy('recipes')

class RecipeDelete(DeleteView):
    model = Recipe
    context_object_name = 'recipe'
    success_url = reverse_lazy('recipes')