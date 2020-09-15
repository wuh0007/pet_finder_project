from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

def inquiry(request):
    if request.method == 'POST':
        pet_id = request.POST['pet_id']
        pet_title = request.POST['pet_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(pet_id=pet_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this pet. Please wait until we get back to you.')
                return redirect('/pets/'+pet_id)

        contact = Contact(pet_id=pet_id, pet_title=pet_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need, city=city,
        state=state, email=email, phone=phone, message=message)

        # send email
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                'New Pet Inquiry',
                'You have a new inquiry for the pet ' + pet_title + '. Please login to your admin panel for more info.',
                'hongyuwu.flyer@gmail.com',
                [admin_email],
                fail_silently=False,
            )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/pets/'+pet_id)
