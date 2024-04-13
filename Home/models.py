from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.urls import reverse
from datetime import datetime


# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    socialSecurityNum = models.CharField(max_length=9)
    street_num = models.CharField(max_length=30)

    BOOL_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    STATE_OPTIONS = (
        ('Alabama', 'Alabama'),
        ('Alaska', 'Alaska'),
        ('Arizona', 'Arizona'),
        ('Arkansas', 'Arkansas'),
        ('California', 'California'),
        ('Colorado', 'Colorado'),
        ('Conneticut', 'Conneticut'),
        ('Deleware', 'Deleware'),
        ('Florida', 'Florida'),
        ('Georgia', 'Georgia'),
        ('Hawaii', 'Hawaii'),
        ('Idaho', 'Idaho'),
        ('Illinois', 'Illinois'),
        ('Indiana', 'Indiana'),
        ('Iowa', 'Iowa'),
        ('Kansas', 'Kansas'),
        ('Kentucky', 'Kentucky'),
        ('Louisiana', 'Louisiana'),
        ('Maine', 'Maine'),
        ('Maryland', 'Maryland'),
        ('Massachusetts', 'Massachusetts'),
        ('Michigan', 'Michigan'),
        ('Minnesota', 'Minnesota'),
        ('Mississippi', 'Mississippi'),
        ('Missouri', 'Missouri'),
        ('Montana', 'Montana'),
        ('Nebraska', 'Nebraska'),
        ('Nevada', 'Nevada'),
        ('New Hampshire', 'New Hampshire'),
        ('New Jersey', 'New Jersey'),
        ('New Mexico', 'New Mexico'),
        ('New York', 'New York'),
        ('North Carolina', 'North Carolina'),
        ('North Dakota', 'North Dakota'),
        ('Ohio', 'Ohio'),
        ('Oklahoma', 'Oklahoma'),
        ('Oregon', 'Oregon'),
        ('Pennsylvania', 'Pennsylvania'),
        ('Rhode Island', 'Rhode Island'),
        ('South Carolina', 'South Carolina'),
        ('South Dakota', 'South Dakota'),
        ('Tennessee', 'Tennessee'),
        ('Texas', 'Texas'),
        ('Utah', 'Utah'),
        ('Vermont', 'Vermont'),
        ('Virginia', 'Virgina'),
        ('Washington', 'Washington'),
        ('West Virginia', 'West Virginia'),
        ('Wisconsin', 'Wisconsin'),
        ('Wyoming', 'Wyoming'),
    )

    state = models.CharField(
        max_length=25,
        choices=STATE_OPTIONS,
        blank=False

    )
    city = models.CharField(max_length=45)
    zipcode = models.CharField(max_length=5)
    telephone = models.CharField(max_length=12)
    cell_phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=45)
    legally_employeed = models.CharField(max_length=30, choices=BOOL_CHOICES)
    pled_guilty = models.CharField(max_length=30, choices=BOOL_CHOICES)
    date_of_birth = models.DateField()
    date_available_start = models.DateField()

    EMPLOYMENT_OPTIONS = (
        ('Part Time', 'Part Time'),
        ('Full Time', 'Full Time'),
    )

    employment_desired = models.CharField(
        max_length=30,
        choices=EMPLOYMENT_OPTIONS,
        blank=False
    )

    drivers_liscence_number = models.CharField(max_length=30)
    drivers_liscence_state_iss = models.CharField(
        max_length=30,
        choices=STATE_OPTIONS,
        blank=False
    )

    # for employer 1 history
    employer_1 = models.CharField(max_length=25)
    employer_1_tel = models.CharField(max_length=30)
    employer_1_date_started = models.DateField(null=False)
    employer_1_date_terminated = models.DateField(blank=True, null=True)
    employer_1_still_employed = models.CharField(max_length=25, choices=BOOL_CHOICES,
                                                 blank=False)
    employer_1_may_we_contact = models.CharField(max_length=30, choices=BOOL_CHOICES,
                                                 blank=False)
    employer_1_street = models.CharField(max_length=30)
    employer_1_city = models.CharField(max_length=30)
    employer_1_state = models.CharField(
        max_length=30,
        choices=STATE_OPTIONS,
        blank=False,
    )
    employer_1_zipcode = models.CharField(max_length=5)
    employer_1_starting_title = models.CharField(max_length=25)
    employer_1_starting_wage = models.CharField(max_length=25)
    employer_1_final_title = models.CharField(max_length=25)
    employer_1_final_wage = models.CharField(max_length=25, blank=True)
    employer_1_summary = models.TextField(blank=True)
    employer_1_favorite_details = models.CharField(max_length=300)
    employer_1_least_details = models.CharField(max_length=300, blank=True)

    # for employer 2 history
    employer_2 = models.CharField(max_length=30, blank=True)
    employer_2_tel = models.CharField(max_length=30, blank=True)
    employer_2_date_started = models.DateField(blank=True, null=True)
    employer_2_date_terminated = models.DateField(blank=True, null=True)
    employer_2_still_employed = models.CharField(max_length=30, choices=BOOL_CHOICES,
                                                 blank=True)
    employer_2_may_we_contact = models.CharField(max_length=30, choices=BOOL_CHOICES,
                                                 blank=True)
    employer_2_street = models.CharField(max_length=30, blank=True)
    employer_2_city = models.CharField(max_length=30, blank=True)
    employer_2_state = models.CharField(
        max_length=25,
        choices=STATE_OPTIONS,
        blank=True,
    )
    employer_2_zipcode = models.CharField(max_length=30, blank=True)
    employer_2_starting_title = models.CharField(max_length=30, blank=True)
    employer_2_starting_wage = models.CharField(max_length=30, blank=True)
    employer_2_final_title = models.CharField(max_length=30, blank=True)
    employer_2_final_wage = models.CharField(max_length=30, blank=True)
    employer_2_summary = models.TextField(max_length=30, blank=True)
    employer_2_favorite_details = models.CharField(max_length=30, blank=True)
    employer_2_least_details = models.CharField(max_length=30, blank=True)

    # for employer 3 history
    employer_3 = models.CharField(max_length=30, blank=True)
    employer_3_tel = models.CharField(max_length=30, blank=True)
    employer_3_date_started = models.DateField(blank=True, null=True)
    employer_3_date_terminated = models.DateField(blank=True, null=True)
    employer_3_still_employed = models.CharField(max_length=30, choices=BOOL_CHOICES,
                                                 blank=True)
    employer_3_may_we_contact = models.CharField(max_length=30, choices=BOOL_CHOICES,
                                                 blank=True)
    employer_3_street = models.CharField(max_length=30, blank=True)
    employer_3_city = models.CharField(max_length=30, blank=True)
    employer_3_state = models.CharField(
        max_length=30,
        choices=STATE_OPTIONS,
        blank=True,
    )
    employer_3_zipcode = models.CharField(max_length=30, blank=True)
    employer_3_starting_title = models.CharField(max_length=30, blank=True)
    employer_3_starting_wage = models.CharField(max_length=30, blank=True)
    employer_3_final_title = models.CharField(max_length=30, blank=True)
    employer_3_final_wage = models.CharField(max_length=30, blank=True)
    employer_3_summary = models.TextField(blank=True)
    employer_3_favorite_details = models.CharField(max_length=30, blank=True)
    employer_3_least_details = models.CharField(max_length=30, blank=True)

    # for skills q&a section
    skills_and_qual = models.TextField(blank=True)

    # Education and Background
    school_name = models.CharField(max_length=30)
    years_completed = models.IntegerField()
    completed = models.CharField(max_length=30, choices=BOOL_CHOICES, blank=True)
    degree = models.CharField(max_length=30)
    certification = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    minor = models.CharField(max_length=30, blank=True)

    # references informatiion
    reference_1_name = models.CharField(max_length=45)
    reference_1_relationship = models.CharField(max_length=30)
    reference_1_telephone = models.CharField(max_length=12)
    reference_1_years_known = models.CharField(max_length=2)

    reference_2_name = models.CharField(max_length=45)
    reference_2_relationship = models.CharField(max_length=30)
    reference_2_telephone = models.CharField(max_length=12)
    reference_2_years_known = models.CharField(max_length=2)

    reference_3_name = models.CharField(max_length=45)
    reference_3_relationship = models.CharField(max_length=30)
    reference_3_telephone = models.CharField(max_length=12)
    reference_3_years_known = models.CharField(max_length=2)

    applicantSignature = models.CharField(max_length=100, blank=False)
    todaysDate = models.DateField(blank=False)
    hired = models.BooleanField(null=True)


class requestAQuote(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=30)
    streetAddress = models.CharField(max_length=45)
    city = models.CharField(max_length=30)
    # need to set the state field to be an options, where the only option is IA or NE.
    STATE_OPTIONS = [
        ('Iowa', 'Iowa'),
        ('Nebraska', 'Nebraska')
    ]

    state = models.CharField(max_length=25,
                             choices=STATE_OPTIONS,
                             blank=False)
    zipcode = models.CharField(max_length=5)
    details = models.TextField(blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)


class Service(models.Model):
    name = models.CharField(max_length=225)
    details = models.TextField(blank=False)
    slug = models.SlugField(max_length=30, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Home:service_detail",
                       args=[self.id, self.slug])


class ServicePromotion(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='promotion/')

    def __str__(self):
        return str(self.image)


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='our_work/', blank=True)
    is_default = models.BooleanField(null=True)

    def __str__(self):
        return str(self.image)

    def get_thumbnail(self, pk):
        # return a list of all images, belonging to service param that was
        # passed in.
        service = Service.objects.filter(pk=pk).get()
        images = ServiceImage.objects.filter(service_id=pk).all()
        for image in images:
            # is this image set to default or not?
            if image.is_default == True:
                # return url of current image and break out of loop.
                return image
                break
