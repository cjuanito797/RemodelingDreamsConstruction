from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, EmployeeApplication, quoteForm
from django.contrib.auth.decorators import login_required
from Admin.views import admin
from Admin.models import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


def view_gallery(request, pk):
    # get the associated project.
    project = get_object_or_404(Project, pk=pk)

    # ok so we have the project, now we need to get all of the images that pertain to this project.
    images = ProjectGallery.objects.filter(project_id=pk).all()

    # return both project and images to our view.
    return render(request, "view_gallery.html", {'project': project, 'images': images})

# Create your views here.
def home(request):

    services = Service.objects.filter(name__in=['Additions', 'Doors', 'Decks', 'Design/planning', 'Interior Remodelings', 'Siding', ]).order_by('name')
    testimonials = Testimonial.objects.all()
    testimonial_count = Testimonial.objects.all().count()

    if request.method == "POST":
        form = quoteForm(request.POST)

        if form.is_valid():
            # render the success page.
            print("Customer Succesfully submitted form.")
            # create a new quote object.
            new_quote = form.save(commit=False)
            new_quote.save()

            # send e-mail to customer.
            send_mail(
                 "Thank You For Choosing Remodeling Dreams Construction",
                 "Hello, We Appreciate you for reaching out to us. A representative will contact you in order to set up a date and time for your appointment",
                 "Don't Reply <do_not_reply@domain.example>",
                 [form.cleaned_data['email']],
                 fail_silently=False,
             )

            # send e-mail to admin.
            plaintext = get_template("Send/quote_confirmation.txt")
            content = ({
                'user': new_quote.name
            })

            text_content = plaintext.render(content)


            msg = EmailMultiAlternatives("A New Quote Has Been Created", text_content, 'cfanito797@gmail.com', ['rdcquoterequest@aol.com'])
            msg.send()

            return redirect('Home:success')

    else:
        form = quoteForm()

    return render(request, "home.html", {'services': services, 'testimonials' : testimonials, 'count' : testimonial_count, 'form': form})

def about_us(request):
    return render(request, "about_us.html")

def requestAQuote(request):

    # check to see if the request is of type post.
    if request.method == "POST":
        form = quoteForm(request.POST)

        # ensure that there are no errors with the form.
        if form.is_valid():
            cd = form.cleaned_data

            # create a new instances of the data model.
            lead = form.save(commit=False)

            # create a new requestAQuote instance
            lead.save()

            # send e-mail to customer.
            send_mail(
                "Remodeling Dreams Construction Quote",
                "We Appreciate you for reaching out to us. A representative will contact you in order to set up a date and time for your appointment",
                "Don't Reply <do_not_reply@domain.example>",
                [form.cleaned_data['email']],
                fail_silently=False,
            )

            # send e-mail to admin.
            # send e-mail to admin.
            plaintext = get_template("Send/quote_confirmation.txt")
            content = ({
                'user': lead.name
            })

            text_content = plaintext.render(content)


            msg = EmailMultiAlternatives("A New Quote Has Been Created", text_content, 'cfanito797@gmail.com', ['rdcquoterequest@aol.com'])
            msg.send()

            return redirect('Home:success')

    else:
        form = quoteForm()

    return render(request, "requestAQuote.html", {'form': form})


def logout(request):
    if request.user.is_authenticated:
        request.session['is_signedIn'] = False
        logout (request)
        del request.session['is_signedIn']
        request.session.flush ( )
        return redirect("Home:home")

def form_success(request):
    return render (request, "consultation_form_success.html")


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Admin:admin')
                else:
                    return redirect('Home:home')
            else:
                return redirect ("Home:user_login")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def employeeApplication(request):
    if request.method == 'POST':
        form = EmployeeApplication(request.POST)

        if form.is_valid():
            # generate all fields from the form, and save the data object.
            new_applicant = form.save(commit=False)

            new_applicant.save()

            send_mail(
                "Remodeling Dreams Construction Quote",
                "We Appreciate your interest for working for Remodeling Dreams Construction. We will review your application and reach out to you.",
                "Don't Reply <do_not_reply@domain.example>",
                [form.cleaned_data['email']],
                fail_silently=False,)

            # send e-mail to admin.

            plaintext = get_template("Send/application_confirmation.txt")
            content = ({
                'user': new_applicant.first_name
            })

            text_content = plaintext.render(content)


            msg = EmailMultiAlternatives("A New Application Has Been Submitted", text_content, 'cfanito797@gmail.com', ['rdcjobapplicant@aol.com'])
            msg.send()


        else:
            print(form.errors)

        return redirect('Home:success')
    else:
        form = EmployeeApplication()

    return render (request, "registration/employeeApp.html", {'form': form})

def services(request):
    # function that will be used to display oll of our services.
    services = Service.objects.all ( ).order_by('name')

    return render (request,
                   'services.html',
                   {
                       'services': services,

                   })

def service_detail(request, id, slug):
    service = get_object_or_404 (Service,
                                 id=id,
                                 slug=slug,
                                 )
    service_images = ServiceImage.objects.filter(service_id=id).all()

    # get all of the promotional images pertaining to this service.
    promotional_images = ServicePromotion.objects.filter(service_id=id).all()

    # get all of the projects, to display a row of project galleries.
    projects = Project.objects.filter(service_id=id).all()

    return render(request, "service_details.html", {'service': service, 'service_images': service_images, 'promotional_images': promotional_images,
                                                    'projects' : projects})
