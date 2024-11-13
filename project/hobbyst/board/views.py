from django.shortcuts import render, redirect
from board.forms import CommentForm, PostForm
from board.models import Post, Comment, PostImage
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect , HttpResponseForbidden


def home(request):
    # if not request.user.is_authenticated:
        # return redirect('/account/login')
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'board': posts,                                       # board로 template에 전달해야함
        'comment_form': comment_form,
    }
    return render(request, 'board/home.html',context)

def post_write(request):
    form = PostForm()
    if request.method == "POST":
        # request.POST로 온 데이터 ("content")는 PostForm 으로 처리
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        # Post 생성 후 request.FILES.getlists("images")로 전송된 이미지들을 순회하며 PostImage 객체를 생성한다.
            for image_file in request.FILES.getlist("images"):
                #request.FILES 로 가져온 파일은 Model의 ImageField 부분에 곧바로 할당한다.
                PostImage.objects.create(
                    post=post,
                    photo=image_file,
                )
            url = f"/board/#post-{post.id}"
            return HttpResponseRedirect(url)
        
        # else :
        #     form = PostForm()
    
    context = {'form': form}
    return render(request, "board/post_write.html", context)


@require_POST  
def comment_add(request):
    # print(request.POST)
    form = CommentForm(data=request.POST)
    if form.is_valid():
#        'post' 필드를 hidden input에서 가져옴
        # post_id = request.POST.get('post')
        # post = Post.objects.get(id=post_id)
#         # Comment 객체를 생성하지만 아직 저장하지 않음 (commit=False)
        comment = form.save(commit=False)
        # comment.post = post
        comment.user = request.user  # 현재 로그인한 사용자를 댓글 작성자로 설정
        comment.save()
        print(comment.id)
        print(comment.content)
        print(comment.user)
        # return redirect('board/')
        url = reverse("board:home") + f"#post-{comment.post.id}"
        return HttpResponseRedirect(url_next)
    # (f"/board/#post-{comment.post.id}")              # 교재에는 posts/feed/#post-{comment.post.id} 로 되있음 (헷갈림;posts/feeds > board? or board/home/ ?)
    
@require_POST
def comment_delete(request, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        if comment.user == request.user:
            comment.delete()
            return HttpResponseRedirect(f"/board/#post-{comment.post.id}")
        else :
            return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다.")
        

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm()
    context = {"board":post,
               "comment_form": comment_form,}
    return render(request, "board/post_detail.html", context)
