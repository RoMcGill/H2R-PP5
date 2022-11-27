"""
imports:
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscribersForm, SendNewsForm
from .models import Subscribers
from django.core.mail import send_mail
from django_pandas.io import read_frame


def Newsletter(request):
    """
    view for newsletter page
    """
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for Subscribing to our email List\
                we will never Contact you Unless We have something\
                to say that we know you want to hear!')
            return redirect('home')
        else:
            messages.error(
                request,
                'There was an Issue Subscribing you to Our mailing List,\
                please contact us through our Contact Us page')
    else:
        form = SubscribersForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter.html', context)


def send_newsletter(request):
    """
    view for send newsletter page
    """
    emails = Subscribers.objects.all()
    data_frame = read_frame(emails, fieldnames=['email'])
    email_list = data_frame['email'].values.tolist()
    print(email_list)
    if request.method == 'POST':
        form = SendNewsForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                email_list,
                fail_silently=False,
            )
            messages.success(request, 'Your newsletter Has been sent To all')
            return redirect('home')
        else:
            print('not working')
    else:
        form = SendNewsForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/send-newsletter.html', context)
