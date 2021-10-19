from django.urls import path
from .views import RecipeList,RecipeDetail,RecipeCreate,RecipeUpdate,RecipeDelete,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',CustomLoginView.as_view(),name = 'login'),
    path('logout/',LogoutView.as_view(next_page = 'login'),name = 'logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',RecipeList.as_view(),name='recipes'),
    path('recipe/<int:pk>/',RecipeDetail.as_view(),name='recipe'),
    path('recipe-create/',RecipeCreate.as_view(),name='recipe-create'),
    path('recipe-update/<int:pk>/',RecipeUpdate.as_view(),name='recipe-update'),
    path('recipe-delete/<int:pk>/',RecipeDelete.as_view(),name='recipe-delete'),
]
