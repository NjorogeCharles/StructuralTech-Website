
from django.contrib import admin
from django.urls import path
from StucturalTechExpertsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/details/', views.blog_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('show/contact/', views.show_contact, name='show_contact'),
    path('quote/', views.quote, name='quote'),
    path('quoteform/', views.quoteform, name='quoteform'),
    path('comment/', views.comment, name='comment'),
    path('delete/<int:id>', views.delete),
    path('delete_quote/<int:id>/', views.delete_quote, name='delete_quote'),
    path('delete_comment/<int:id>/', views.delete_comment, name='delete_comment'),
    path('edit_quote/<int:id>', views.edit_quote, name='edit_quote'),
    path('update_quote/<int:id>', views.update_quote, name='update_quote'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('projects/', views.project, name='project'),
    path('projects/details/', views.project_details, name='project_details'),
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('services/', views.services, name='services'),
    path('services/details/', views.service_details, name='service_details'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('starter-page/', views.starter_page, name='starter_page'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('adminsection/', views.adminsection, name='adminsection'),
    path('adminform/', views.adminform, name='adminform'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),


]
