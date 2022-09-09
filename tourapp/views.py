from django.shortcuts import render, redirect, get_object_or_404
from .models import Search, Post
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator

def home(request):
    return render(request,'index.html')

# 검색
def search(request):
    tours = Post.objects.all().order_by('-id')
    searched = request.POST.get('searched', "")
    if searched:
        tours = tours.filter(title__contains=searched)
        return render(request, 'searched.html', {'searched': searched, 'tours': tours})
    else:  
        return render(request, 'searched.html', {})

# 지역
def region(request):
    return render(request,'region.html')

def jeju(request):
    return render(request, 'jeju.html')

# 축제
def festival(request):
    return render(request,'festival.html')

def festivalnext(request):
    return render(request,'festivalnext.html')

def festivalpre(request):
    return render(request,'festivalpre.html')

def festivaldetail(request): 
    return render(request, 'festivaldetail.html')



# 게시판   
def board(request):
    posts = Post.objects.filter().order_by('-date')
    paginator = Paginator(posts, 5)
    pagenum = request.GET.get('page')
    posts = paginator.get_page(pagenum)
    return render(request, 'board.html', {'posts':posts})


def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post_detail':post_detail, 'comment_form':comment_form})


def postcreate(request):
    # request method가 POST 일 경우
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # 입력값 저장
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('board')
    # request method가 GET 일 경우
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('detail', post_id)