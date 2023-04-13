from django.shortcuts import render, redirect
from .forms import CommentForm, ReviewForm
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.

def index(request):
    
    context = {
        
    }
    return render(request, 'reviews/index.html', context)