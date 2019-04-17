from django.shortcuts import render, get_object_or_404
from .models import Video


# Create your views here.
def index(request):
    '''
    主页
    :param request:
    :return:
    '''
    last_video = []
    for video in Video.objects.all():
        if video.was_published_recently():
            last_video.append(video)
    context = {
        'last_video': last_video
    }
    return render(request, 'video/index.html', context)


def detail(request, video_id):
    '''
    详情页
    :param request:
    :return:
    '''
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'video/detail.html', {'video': video})


