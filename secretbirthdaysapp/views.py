from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
  def get(self, request):
    num_users = User.objects.count()
    login_url = ""
    return render(
      request,
      "secretbirthdaysapp/home.html",
      {"login_url": login_url, "num_users": num_users},
    )
