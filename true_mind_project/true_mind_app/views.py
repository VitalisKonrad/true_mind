from django.shortcuts import render
from .models import MindPost
from allauth.socialaccount.models import SocialAccount

def home(request):
    _get_username_from_social()
    return render(request, 'true_mind_app/minds.html', {'user':user,})
# Create your views here.
def minds(request):
    minds_list = MindPost.objects.all().order_by('author')
    print (minds_list)

    return render(request, 'true_mind_app/minds.html', {'minds_list':minds_list,})

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    return render(request, 'true_mind_app/minds.html', {'key_usertext':user_text,
                                            'reversedtext':reversed_text})

def _get_username_from_social(request):
    if request.user.is_authenticated:
        try:
            social_account = SocialAccount.objects.get(user=request.user).extra_data
            return HttpResponse(social_account['login'])
        except SocialAccount.DoesNotExist:  # user created with email and password
            return HttpResponse(request.user.username)
    return HttpResponse("<a href='/accounts/facebook/login/'>Sign Up</a>")