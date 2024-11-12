from django.shortcuts import render, redirect
from board.forms import CommentForm, PostForm
from board.models import Post

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('/account/login')
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'board/home.html',context)

def post_write(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, "board/post_write.html", context)