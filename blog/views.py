from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html', {
        'message': 'Hello Djangoblog'
    })
def about(request):
    return render(request, 'blog/about.html', {
        'content': 'This is the Djangoblog team.'
    })
def contact(request):
    return render(request, 'blog/contact.html', {
        'ABC': 'This is the Djangoblog Contact.'
    })
