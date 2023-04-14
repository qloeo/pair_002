from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review, Comment, ReComment
from .forms import CommentForm, ReviewForm, ReCommentForm
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    firstpk = Review.objects.order_by('pk')[0].pk
    lastpk = Review.objects.order_by('-pk')[0].pk
    comment_form = CommentForm()
    comments = review.comment_set.all()

    recomment_form = ReCommentForm()
    # recomments = review.recomment_set.all()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
        'firstpk': firstpk,
        'lastpk': lastpk,
        # 'recomments': recomments,
        'recomment_form': recomment_form,
    }
    return render(request, 'reviews/detail.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
    }
    return render(request, 'reviews/create.html', context)


@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail', review.pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('reviews:detail', review.pk)
    
    context = {
        'review': review,
        'form': form,
    }
    return render(request, 'reviews/update.html', context)


@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        if request.method == "POST":
            review.delete()
            return redirect('reviews:index')
    return redirect('reviews:index')


@login_required
def create_comment(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return redirect('reviews:detail', review.pk)
    return redirect('reviews:detail', review.pk)


@login_required
def create_recomment(request, review_pk, comment_pk):
    review = Review.objects.get(pk=review_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == "POST":
        recomment_form = ReCommentForm(request.POST)
        if recomment_form.is_valid():
            recomment = recomment_form.save(commit=False)
            recomment.comment = comment
            recomment.review = review
            recomment.user = request.user
            recomment.save()
            return redirect('reviews:detail', review.pk)
    return redirect('reviews:detail', review.pk)


@login_required
def delete_comment(request, review_pk, comment_pk):
    review = Review.objects.get(pk=review_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        if request.method == "POST":
            comment.delete()
            return redirect('reviews:detail', review.pk)
    return redirect('reviews:detail', review.pk)
    


def prev(request, review_pk):
    firstpk = Review.objects.order_by('pk')[0].pk

    if review_pk != firstpk:
        newpk = review_pk - 1
        while True:
            if Review.objects.filter(pk=newpk).exists() == False:
                newpk -= 1
            else:
                return redirect('reviews:detail', newpk)


def next(request, review_pk):
    lastpk = Review.objects.order_by('-pk')[0].pk

    if review_pk != lastpk:
        newpk = review_pk + 1
        while True:
            if Review.objects.filter(pk=newpk).exists() == False:
                newpk += 1
            else:
                return redirect('reviews:detail', newpk)
            

@login_required
def review_like(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('reviews:detail', review.pk)


@login_required
def comment_like(request, review_pk, comment_pk):
    review = Review.objects.get(pk=review_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.user in comment.like_users.all():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect('reviews:detail', review.pk)