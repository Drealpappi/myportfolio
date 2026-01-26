from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Project
from django.contrib import messages
from .models import ContactMessage

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')
        subject = request.PPOST.get('subject', 'New Contact Message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message_content
        )

        # Send email notification
        try:
            send_mail(
                subject,
                f"Message from {name} ({email}):\n\n{message_content}",
                settings.EMAIL_HOST_USER,
                ['adelekanf7@gmail.com'], 
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f"Email sending failed, but saved in the database. {e}")
        return redirect('home')
    
#load projects for GET request

def home(request):
    projects = Project.objects.all()
    
    if request.method == 'POST':
        # ... your email logic from before ...
        pass

    return render(request, 'home.html', {'projects': projects})