import json
from .models import Comment
from django.http import HttpResponse, JsonResponse
from django.views import View

class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            Comment(
                    user_id = data['user_id'],
                    comment = data['comment']
                    ).save()
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)

    def get(self, request):
        comment_data = Comment.objects.values()
        return JsonResponse({'comments' : list(comment_data)}, status=200)      
