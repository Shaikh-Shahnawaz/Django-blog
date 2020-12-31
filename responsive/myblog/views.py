from django.shortcuts import render
from myblog.models import Contact

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(name=name, phone=phone, email=email, message=message)
        contact.save()

    return render(request, 'myblog/index.html')
