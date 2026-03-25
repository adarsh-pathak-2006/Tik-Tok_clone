from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Video


def index(request):
   
    videos = Video.objects.all().order_by('-id')  # newest first
    return render(request, "core/index.html", {"videos": videos})


@csrf_exempt
def like_video(request, video_id):

    if request.method == "POST":
        video = get_object_or_404(Video, id=video_id)
        video.likes += 1
        video.save()
        return JsonResponse({"likes": video.likes})
    return JsonResponse({"error": "Invalid request method"}, status=400)