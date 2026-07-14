from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_page, name="home"),
    path("chat/", views.chat_api, name="chat_api"),
    path("viewrepo/", views.get_customer_repo, name="getcust"),
]