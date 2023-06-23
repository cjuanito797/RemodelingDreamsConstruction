from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Home.models import requestAQuote, Service, ServiceImage, Employee, ServicePromotion
from .models import *
from .forms import EditService, EditThumbnail, AddImage, AddService, AddTestimonial, AddPromotion, AddGalleryImage, CreateGallery, EditProject, EditTestimonial
import json
from django.utils.text import slugify

@login_required(login_url = '/login/')
def deleteApplicant(request, pk):
    applicant = get_object_or_404(Employee, pk=pk)
    applicant.delete()

    return redirect("Admin:applicants")


@login_required(login_url = '/login/')
def view_applicant_details(request, pk):
    # get the applicant, of whom we are wanting to view the details for.
    applicant = get_object_or_404(Employee, pk=pk)

    return render(request, "admin/applicant_details.html", {'applicant': applicant})

@login_required(login_url= '/login/')
def applicants(request):
    employee_apps = Employee.objects.all()

    return render(request, "admin/applicants.html", {'applicants': employee_apps})

@login_required (login_url = '/login/')
def testimonials(request):
    testimonials = Testimonial.objects.all()

    if request.method == 'POST':
        form = AddTestimonial(request.POST)

        if form.is_valid():
            new_testimonial = form.save(commit=False)
            new_testimonial.save()
            form = AddTestimonial()
    else:
        form = AddTestimonial()

    return render(request, "admin/testimonials.html", {'testimonials': testimonials, 'form': form})

@login_required (login_url = '/login/')
def delete_testimonial(request, pk):
    # query the testimonial to be deleted.
    test_del = Testimonial.objects.filter(pk=pk)
    test_del.delete()

    return redirect('Admin:testimonials')

@login_required (login_url = '/login/')
def edit_testimonial(request, pk):
    # query the testimonial to be edited.
    test_edit = Testimonial.objects.filter(pk=pk).first()

    # load the form with the instance of this object.
    #
    print("About to edit a testimonial.")
    if request.method == "POST":
        form = EditTestimonial(request.POST, instance=test_edit)
        print("Yes, the method is of type post.")
        # ensure that the form is valid, save and return to main testimonials page.
        if form.is_valid():
            test_edit = form.save()
            test_edit.save()
            print("form is valid!")

            return redirect('Admin:testimonials')

    else:
        form = EditTestimonial(instance=test_edit)

    return render(request, "admin/edit_testimonials.html", {'form': form, 'testimonial': test_edit})



# Create your views here.
@login_required (login_url='/login/')
def admin(request):


    return render(request, 'admin/admin.html')


@login_required (login_url='/login/')
def view_quotes(request):
    quotes = requestAQuote.objects.all()

    return render(request, "admin/view_quotes.html", {'quotes' : quotes})

def delete_quote(request, id):
	quote = requestAQuote.objects.filter(pk=id).get()
	quote.delete()

	return redirect('Admin:view_quotes')

def deleteService(request, pk):
    # query the service that is to be deleted.
    service = Service.objects.filter(pk=pk)
    service.delete()

    return redirect('Admin:view_services')

def view_services(request):

    services = Service.objects.all().order_by('name')
    if request.method == "POST":
        form = AddService(request.POST)

        if form.is_valid():
            new_service = form.save(commit=False)
            new_service.slug = slugify(new_service.name)
            new_service.save()

            return redirect('Admin:view_services')
    else:
        form = AddService()

    return render(request, "admin/view_services.html", {'services': services, 'form': form})

def edit_service(request, pk):
    service = get_object_or_404(Service, pk=pk)

    # load the form.
    # we need to get the thumbnail corresponding to the service.

    # load the promotional images.
    # get all of the promotional images pertaining to this service.
    promotional_images = ServicePromotion.objects.filter(service_id=pk).all()

    # get all of the projects, to display a row of project galleries.
    projects = Project.objects.filter(service_id=pk).all()

    images = ServiceImage.objects.filter(service_id=pk).all()
    id = False
    url = None
    for image in images:
        # is this image set to default or not?
        if image.is_default == True:
            # return id of current image.
            id = image.id
            break

    # load up the thumbnail form, with the instance being the url for our current image.
    if request.method == "POST":

        form = EditService(request.POST, instance=service)
        edit_thumbnail = EditThumbnail(request.POST, request.FILES)

        new_url = request.FILES.get('image', False)
        print("URL OF NEW FILE IS: ", new_url)

        if form.is_valid():
            print("Inside of the first elif statement.")
            service = form.save()
            service.save()

            if ((new_url)) != False:

                # delete the current thumbnail.
                if id > 0:
                    service_image = ServiceImage.objects.filter(pk=id).get()
                    service_image.delete()

                new_service_image = edit_thumbnail.save(commit=False)
                new_service_image.service_id = pk
                new_service_image.is_default = True
                new_service_image.save()

            return redirect('Admin:view_services')

        else:
            return redirect("Admin:view_services")

    else:
        form = EditService(instance=service)
        edit_thumbnail = EditThumbnail()


    return render(request, "admin/editService.html", {'form': form, 'edit_thumbnail': edit_thumbnail, 'service': service,
        'images' : images, 'promotional_images': promotional_images, 'projects': projects})


def editPromotionalBanner(request, pk):
    # get all of the promotional images, pertaining to the service, which is the pk that was passed in as a parameter.
    promotional_images = ServicePromotion.objects.filter(service_id=pk).all()

    # render the form, if everything is valid, create a new ServicePromotion that pertains to this service, reload the same-page.
    # this time displaying new promotional image.

    if request.method == 'POST':
        form = AddPromotion(request.POST, request.FILES)

        # check to make sure that the form is valid.
        if form.is_valid():
            new_url = request.FILES.get('image', False)
            if new_url != False:
                new_promotion = form.save(commit=False)
                new_promotion.service_id = pk
                new_promotion.save()

            return redirect('Admin:editPromotionalBanner', pk)
    else:
        form = AddPromotion()


    return render(request, "admin/edit_promotional_banner.html", {'promotional_images': promotional_images, 'form': form, 'id': pk})

def deletePromotion(request, pk):
    # query the promotion image based off of the pk that was passed in.
    promotion = ServicePromotion.objects.filter(pk=pk).get()
    # set the pk equal to the pertaining service.
    pk = promotion.service_id
    promotion.delete()

    return redirect('Admin:editPromotionalBanner', pk)

def edit_service_images(request, pk):
    # get all of the images of the belonging to the service.
    images = ServiceImage.objects.filter(service_id=pk).all()
    service = Service.objects.filter(pk=pk).get()

    # include here the form to allow user to submit new image.

    if request.method == 'POST':
        form = AddImage(request.POST, request.FILES)

        # check to make sure that the form is valid.
        if form.is_valid():
            new_url = request.FILES.get('image', False)
            if new_url != False:
                new_service_image = form.save(commit=False)
                new_service_image.service_id = pk
                new_service_image.is_default = False
                new_service_image.save()

                return redirect('Admin:edit_service_images', service.id)
    else:
        form = AddImage()
    # get the id of the service as well, so that we can loop back to image gallery after deleting an image.

    return render(request, "admin/editImages.html", {'images': images, 'form': form, 'service': service})

def deleteServiceImage(request, pk):
    # get the object of the service image that was passed in.
    image = ServiceImage.objects.filter(pk=pk).get()
    # get the id of the service, based off of the image.
    pk = image.service_id
    image.delete()

    return redirect('Admin:edit_service_images', pk)

def edit_gallery(request, pk):
    # get all of the images pertaining to the project, we will pass in the proj.

    images = ProjectGallery.objects.filter(project_id=pk).all()
    # get the id of the service.
    project = Project.objects.filter(pk=pk).get()
    # get the id of the service, pertaining to this project.

    id = project.service_id

    if request.method == "POST":

        form = AddGalleryImage(request.POST, request.FILES)

        if form.is_valid():
            new_url = request.FILES.get('image', False)
            if new_url != False:
                new_gallery_image = form.save(commit=False)
                new_gallery_image.project_id = pk
                new_gallery_image.save()

                return redirect("Admin:edit_gallery", pk)
    else:
        form = AddGalleryImage()

    return render(request, "admin/edit_gallery.html", {'images': images, 'form': form, 'id': id})

def edit_project(request, pk):
    # filter the project that we need to edit.
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = EditProject(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()

            project.save()

            # get the id of the service.
            pk = project.service_id

            return redirect("Admin:edit_service", pk)


    else:
        form = EditProject(instance=project)

    return render(request, "Admin/edit_project.html", {'form': form, 'project': project})



def createGallery(request, pk):
    if request.method == "POST":
        form = CreateGallery(request.POST, request.FILES)

        if form.is_valid():
            # create the new project.
            gallery = form.save(commit=False)

            # get the service and assign it to this gallery object.
            gallery.service_id = pk
            gallery.save()
            # return the user to the page where they can add images for this new gallery.
            return redirect('Admin:edit_gallery', gallery.id)
    else:
        form = CreateGallery()

    return render(request, "admin/create_gallery.html", {'form': form})

def deleteGalleryImage(request, pk):
    # get the image to be deleted.
    image = ProjectGallery.objects.filter(pk=pk).get()
    # get the id of the project, so that we can return to the same page.
    pk = image.project_id
    image.delete()

    return redirect("Admin:edit_gallery", pk)

def deleteProject(request, pk):
    # get the project that is to be deleted.
    project = Project.objects.filter(pk=pk).get()

    # get the id of the service that we are referencing.
    pk = project.service_id

    project.delete()
    return redirect('Admin:edit_service', pk)
