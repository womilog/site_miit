from django.urls import path

from . import views

urlpatterns = [
    path('', views.PrepodyHomeView.as_view(), name='prepody_home'),
    path('post/<slug:post_slug>/', views.PrepodPostView.as_view(), name='prepody_post'),
    path('category/<slug:cat_slug>/', views.PrepodyCategoryView.as_view(), name='prepody_cat'),
    path('add_prepody_post/', views.PrepodyAddPageView.as_view(), name='prepody_add_page'),
    path('edit_prepody_post/<slug:slug>/', views.PrepodyEditPageView.as_view(), name='prepody_edit_page'),
    path('delete/<slug:slug>', views.PrepodyDeletePageView.as_view(), name='prepody_delete_page'),
]
