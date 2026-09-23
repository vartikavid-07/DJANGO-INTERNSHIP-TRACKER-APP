from django.shortcuts import render, redirect
from .models import Internship


def home(request):

    if request.method == 'POST':
        company = request.POST.get('company')
        position = request.POST.get('position')
        location = request.POST.get('location')
        application_date = request.POST.get('application_date')
        status = request.POST.get('status')
        stipend = request.POST.get('stipend')
        notes = request.POST.get('notes')

        Internship.objects.create(
            company=company,
            position=position,
            location=location,
            application_date=application_date,
            status=status,
            stipend=stipend,
            notes=notes
        )

        return redirect('home')

    applications = Internship.objects.all().order_by('-application_date')

    return render(request, 'tracker/home.html', {
        'applications': applications
    })


def delete_application(request, id):

    application = Internship.objects.get(id=id)
    application.delete()

    return redirect('home')