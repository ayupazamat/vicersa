from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'greeting':'Hello!'})
def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    print(reversed_text)
    print(user_text)
#    test_get_text = request.GET['usertext']
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext': reversed_text})
