from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    wordStorage = {}

    for word in words:
        if word in wordStorage:
            wordStorage[word]+=1
        else:
            wordStorage[word] = 1

    return render(request, 'result.html', {'fulltext': text, 'total': len(words), 'dictionary': wordStorage.items()})