from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CommentDataForm
from django.views import View
from django.views.generic import ListView
from .models import CommentData
# Create your views here.

class PostsView(ListView):
    template_name = "app1/posts.html"
    model = CommentData
    context_object_name = "data"
    ordering = ['-timestamp']

class functionview1(View):
    def get(self, request):
        form = CommentDataForm()
        return render(request, "app1/forms1.html", {
            "formkey": form
        })
    def post(self, request):
        form = CommentDataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/formpage/submitted")
        return render(request, "app1/forms1.html", {
            "formkey": form
        })

def functionsubmitted(request):
    return render(request,"app1/submitted.html")

def homepage(request):
    return render(request,"app1/home.html")
