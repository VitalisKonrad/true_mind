from django.shortcuts import render
from .models import MindPost

def home(request):
    return render(request, 'true_mind_app/minds.html')
# Create your views here.
def minds(request):
    minds_list = MindPost.objects.all().order_by('-timestamp')
    print (minds_list)

    return render_to_response('true_mind_app/minds.html', {'minds_list':minds_list,})

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    return render(request, 'true_mind_app/minds.html', {'key_usertext':user_text,
                                            'reversedtext':reversed_text})
