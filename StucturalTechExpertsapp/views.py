import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth

from StucturalTechExpertsapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from StucturalTechExpertsapp.forms import QuoteForm, ContactForm, ImageUploadForm
from StucturalTechExpertsapp.models import Contact, Quote, Comment, Member, ImageModel, Admin


# Create your views here.
def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def blog_details(request):
    if request.method == 'POST':
        comment = Comment(
            name=request.POST['name'],
            email=request.POST['email'],
            website=request.POST['website'],
            comment = request.POST['comment']
        )

        comment.save()
        return redirect('/comment')
    else:
        return render(request, 'blog-details.html')

def comment(request):
    Comments = Comment.objects.all()
    return render(request, 'comment.html', {'comments': Comments})

def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('/comment')

def contact(request):
    if request.method == 'POST':
        contact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message = request.POST['message']
        )

        contact.save()
        return redirect('/show/contact/')
    else:
        return render(request, 'contact.html')

def show_contact(request):
    Contacts = Contact.objects.all()
    return render(request, 'show-contact.html', {'contacts': Contacts})

def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('/show/contact/')



def quoteform(request):
    if request.method == 'POST':
        quote = Quote(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message = request.POST['message']
        )

        quote.save()
        return redirect('quote')
    else:
        return render(request, 'quoteform.html')

def quote(request):
    Quotes = Quote.objects.all()
    return render(request, 'quote.html', {'quotes': Quotes})

def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']
        ).exists():
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def delete_quote(request, id):
    quote = Quote.objects.get(id=id)
    quote.delete()
    return redirect('/quote')

def edit_quote(request, id):
   editquote = Quote.objects.get(id=id)
   return render(request, 'edit.html', {'quote':editquote})

def update_quote(request, id):
    updateinfo = Quote.objects.get(id=id)
    form = QuoteForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/quote')
    else:
        return render(request, 'edit.html')

def edit(request, id):
   editcontact = Contact.objects.get(id=id)
   return render(request, 'edit-contact.html', {'contact':editcontact})

def update(request, id):
    updatecontact = Contact.objects.get(id=id)
    form = ContactForm(request.POST, instance=updatecontact)
    if form.is_valid():
        form.save()
        return redirect('/show/contact')
    else:
        return render(request, 'edit-contact.html')



def project_details(request):
    return render(request,'project-details.html')

def project(request):
    return render(request,'projects.html')

def service_details(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request,'services.html')

def register(request):
    if request.method == 'POST':
        members = Member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')

    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')



def portfolio(request):
    return render(request,'portfolio.html')
def starter_page(request):
    return render(request, 'starter-page.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')


def adminsection(request):
    if request.method == 'POST':
        admin = Admin(
            username=request.POST['username'],
            password=request.POST['password']
        )
        admin.save()
        return redirect('/uploadimage')

    else:
        return render(request, 'adminform.html')

def login(request):
    return render(request, 'login.html')

def adminform(request):
    return render(request, 'adminform.html')

def token(request):
    consumer_key = 'urqR4BB1EBfDed2Yaj4lvER8Z9VY08eRhm0DdvXGgAxbGUez'
    consumer_secret = 'ShwEXq6DcTIMF4vdA1bAL9zi3RJIhwlV8dehQmet5qbKP7CNoZQHAyxtrRIGc6fP'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "StructuralTech",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")










