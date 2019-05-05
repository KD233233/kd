from django.shortcuts import render,get_object_or_404
from .models import Friendly
from .forms import FriendlyForm
from blog.models import Sentence,Post
from comment.models import Comment


# Create your views here.

def friendly_link(request):
    link = Friendly.objects.all()
    context = {}
    context['link'] = link
    form = FriendlyForm()
    context['form'] = form
    if request.method == 'POST':
        sen = Sentence.objects.order_by('-time')
        sentences = sen[0] if sen else []
        post_list = Post.objects.all().order_by('-readnum__look')  # 按文章观看次数降序排列
        num = post_list[5].read_num()
        num1 = post_list[1].read_num()
        # 最新评论
        comment_list2 = Comment.objects.all().order_by('-time')
        num3 = comment_list2[5].time
        comment_list3 = Comment.objects.filter(time__gt=num3)
        form = FriendlyForm(request.POST)
        if form.is_valid():
            form.save()
        # context['form'] = form
        context['sentences'] = sentences
        context['post_list'] = post_list
        context['num'] = num
        context['num1'] = num1
        context['comment_list3'] = comment_list3
        context['comment_list2'] = comment_list2
        return render(request,'friendly.html',context=context)
    else:
        return render(request, 'friendly.html', context=context)
