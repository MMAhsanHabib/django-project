from django.http import HttpResponse



def home(request):
    var = """
    <h1>This is homepage</h1>
    <p>This is a paragraph</p>
    """
    return HttpResponse(var)

def contact(request):
    return HttpResponse("Contact page")

def about(request):
    return HttpResponse("About page")