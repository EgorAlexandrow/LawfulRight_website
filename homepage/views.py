from django.shortcuts import render

# from homepage.models import MainPageContent


def index(request):
    # content = MainPageContent.objects.all()
    return render(request, 'homepage/index.html') # {'content': content})