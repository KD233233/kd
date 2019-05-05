from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Sentence, Post, Tags, ReadNum, About
from django.core.paginator import Paginator
from django.db.models import Q
from comment.forms import CommentForm
from comment.models import Comment
from message.forms import MessageForm
from message.models import Message
from friendly.models import Friendly
from friendly.forms import FriendlyForm
from django.views.decorators.csrf import csrf_exempt
import time


# Create your views here.
def contrl(request, posts):
    sen = Sentence.objects.order_by('-time')
    sentences = sen[0] if sen else []
    page_num = request.GET.get('page', 1)
    tags = Tags.objects.all()

    form = CommentForm()
    # 最新评论
    comment_list2 = Comment.objects.all().order_by('-time')
    num3 = comment_list2[5].time
    comment_list3 = Comment.objects.filter(time__gt=num3)

    # 获取分类
    classify = request.GET.get('classify', 0)
    title = '凯多首页'

    # 如果用于选择网站前端，还是后端技术
    if classify == '1':
        posts = Post.objects.all().filter(classify='网站前端')
        title = '网站前端'

    elif classify == '2':
        posts = Post.objects.all().filter(classify='后端技术')
        title = '后端技术'




    post = Post.objects.filter(tags=tags)
    # post = Post.objects.filter(tags=tags)
    p = Paginator(posts, 3)
    page = p.get_page(page_num)
    page_nums = p.num_pages
    current_page_num = page.number
    page_range = list(range(max(1, current_page_num - 2), min(current_page_num + 2, page_nums) + 1))

    # posts = Post.objects.all()
    post_list = Post.objects.all().order_by('-readnum__look')  # 按文章观看次数降序排列
    num = post_list[5].read_num()
    num1 = post_list[1].read_num()
    context = {}
    context['page_range'] = page_range
    context['page_nums'] = page_nums
    context['tags'] = tags
    context['post_list'] = post_list
    context['num'] = num
    context['num1'] = num1
    context['post'] = post
    context['posts'] = posts
    context['page'] = page
    context['form'] = form
    context['comment_list3'] = comment_list3
    context['comment_list2'] = comment_list2

    context['sentences'] = sentences
    context['posts'] = posts
    context['title'] = title
    context['classify'] = classify

    return context


def content(request, id):
    sen = Sentence.objects.order_by('-time')
    sentences = sen[0] if sen else []
    post = get_object_or_404(Post, pk=id)
    tags = Tags.objects.all()

    # 阅读次数
    readnum = ReadNum.objects.filter(post=post)
    if not request.COOKIES.get(f'post_id{post.pk}'):
        readnum = readnum[0] if readnum else ReadNum(post=post)
        readnum.look += 1
        readnum.save()

    post_list = Post.objects.all().order_by('-readnum__look')
    num = post_list[5].read_num()
    num1 = post_list[1].read_num()

    # 上一篇 下一篇
    previous_post = Post.objects.filter(pub_time__gt=post.pub_time).last()
    next_post = Post.objects.filter(pub_time__lt=post.pub_time).first()

    # 评论
    form = CommentForm()
    comment_list = post.comment_set.all()

    # 最新评论
    comment_list2 = Comment.objects.all().order_by('-time')
    num3 = comment_list2[5].time
    comment_list3 = Comment.objects.filter(time__gt=num3)



    context = {}
    context['form'] = form
    context['comment_list'] = comment_list

    context['sentences'] = sentences
    context['post'] = post
    context['previous_post'] = previous_post
    context['next_post'] = next_post
    context['post_list'] = post_list
    context['num'] = num
    context['num1'] = num1
    context['tags'] = tags

    context['comment_list3'] = comment_list3
    response = render(request, 'content.html', context=context)
    response.set_cookie(f'post_id{post.pk}', 'true', httponly=True)  # 向浏览器发送第一个cookie
    return response

@csrf_exempt
def zan(request):
    # 获取用户访问的文章id
    id_ = request.POST.get('id')
    post = Post.objects.get(pk=id_)

    # 获取session 保存的id时间戳，如果没有说明没有为这篇文章点赞过可以点，如果获取到值
    zan_time = request.session.get(id_,False)
    # 判断距离上上一次点赞是否有一天的时间，如果有可以点
    if not zan_time and zan_time < time.time():
        post.zan += 1
        post.save()
        # 点赞成功后将键为id的session值更新 时间是一天后的当前时间
        request.session[id_] = time.time() + 60 * 60 * 24
        response = HttpResponse(post.zan)
    else:
        response = HttpResponse(post.zan)
    return response


def index(request):
    posts = Post.objects.all()
    #
    # comment_list2 = Comment.objects.all().order_by('-time')
    # num3 = comment_list2[5].time
    # comment_list = Comment.objects.filter(time__gt=num3)

    # 首页轮播图广告
    adv = Post.objects.filter(adv=True)


    context = contrl(request, posts)
    context['posts'] = posts
    # context['comment_list'] = comment_list
    context['adv'] = adv
    return render(request, 'index.html', context=context)


def c_tag(request, id):
    blog_tags = get_object_or_404(Post, pk=id)
    post_tag = Post.objects.filter(tags=blog_tags)
    context = {}
    context['post_tag'] = post_tag
    return render(request, 'index.html', context=context)


def tags(request):
    # blog_tag = get_object_or_404(Tags, pk=id)
    # context = contrl(request, blog_tag)
    tags = Tags.objects.all()

    # post_list = Post.objects.all().order_by('-look')
    # num = post_list[5].readnum
    # num1 = post_list[1].readnum

    context = contrl(request, tags)
    # context['tag'] = blog_tag
    # context['tags'] = tags
    # context['post_list'] = post_list
    # context['num'] = num
    # context['num1'] = num1
    return render(request, 'tags.html', context=context)


def ts(request, id):
    sen = Sentence.objects.order_by('-time')
    sentences = sen[0] if sen else []
    blog_tags = get_object_or_404(Post, pk=id)
    posts = Post.objects.filter(tags=blog_tags)
    tags = Tags.objects.all()

    post_list = Post.objects.all().order_by('-readnum__look')
    num = post_list[5].read_num()
    num1 = post_list[1].read_num()

    context = {}
    context['post_list'] = post_list
    context['num'] = num
    context['num1'] = num1

    context['tags'] = tags

    context['sentences'] = sentences
    context['posts'] = posts
    context['blog_tags'] = blog_tags
    return render(request, 'tags.html', context=context)


def blog_tag(request, id):
    sen = Sentence.objects.order_by('-time')
    sentences = sen[0] if sen else []
    blog_tags = Tags.objects.filter(Post, pk=id)
    posts = Post.objects.filter(tags=blog_tags)
    tags = Tags.objects.all()

    post_list = Post.objects.all().order_by('-readnum__look')
    num = post_list[5].read_num()
    num1 = post_list[1].read_num()

    context = {}
    context['post_list'] = post_list
    context['num'] = num
    context['num1'] = num1

    context['tags'] = tags

    context['sentences'] = sentences
    context['posts'] = posts
    context['blog_tags'] = blog_tags
    return render(request, 'blog_tag.html', context=context)


# def search(request):
#     info = request.GET.get('q')
#     posts = Post.objects.filter(
#         Q(title__icontains=info) | Q(content__icontains=info) | Q(author__username__icontains=info))
#     context = contrl(request, posts)
#     context['info'] = info
#     return render(request, 'search.html', context=context)


def about(request):
    about_list = About.objects.all()

    form = MessageForm()
    message_list = Message.objects.all()
    posts = Post.objects.all()
    context = contrl(request, posts)
    context['form'] = form
    context['message_list'] = message_list
    context['about_list'] = about_list
    return render(request, 'about.html', context=context)


def friendly(request):
    form = FriendlyForm()
    link = Friendly.objects.all()
    posts = Post.objects.all()
    context = contrl(request, posts)
    context['link'] = link
    context['form'] = form
    return render(request, 'friendly.html', context=context)


def da(request):
    # post = get_object_or_404(Post, pk=id)

    posts = Post.objects.all()
    # 评论
    # form = CommentForm()
    # comment_list2 = Comment.objects.all().order_by('-time')
    # num3 = comment_list2[5]
    # comment_list3 = Comment.objects.filter(time__gt=num3)
    # context = {}
    # context['form'] = form
    # context['comment_list3'] = comment_list3
    # context['post'] = post
    # context['num3'] = num3
    context = contrl(request, posts)

    return render(request, 'base.html', context=context)


def readerWall(request):
    about_list = About.objects.all()

    form = MessageForm()
    message_list = Message.objects.all()
    posts = Post.objects.all()
    context = contrl(request, posts)
    context['form'] = form
    context['message_list'] = message_list
    context['about_list'] = about_list
    return render(request,'readerWall.html',context=context)


from haystack.generic_views import SearchView


class MySearchView(SearchView):
    template = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MySearchView, self).get_context_data(**kwargs)
        context['page'] = context

        post_list = Post.objects.all().order_by('-readnum__look')  # 按文章观看次数降序排列
        num = post_list[5].read_num()
        num1 = post_list[1].read_num()

        comment_list2 = Comment.objects.all().order_by('-time')
        num3 = comment_list2[5]
        comment_list3 = comment_list2[:5]

        context['comment_list3'] = comment_list3
        # context['post'] = post
        context['num3'] = num3
        context['post_list'] = post_list
        context['num'] = num
        context['num1'] = num1
        return context
