# Generated by Django 3.1.5 on 2023-05-15 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('socialSecurityNum', models.CharField(max_length=9)),
                ('street_num', models.CharField(max_length=30)),
                ('state', models.CharField(choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Conneticut', 'Conneticut'), ('Deleware', 'Deleware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virgina'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')], max_length=25)),
                ('city', models.CharField(max_length=45)),
                ('zipcode', models.CharField(max_length=5)),
                ('telephone', models.CharField(max_length=12)),
                ('cell_phone', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=45)),
                ('legally_employeed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30)),
                ('pled_guilty', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30)),
                ('date_of_birth', models.DateField()),
                ('date_available_start', models.DateField()),
                ('employment_desired', models.CharField(choices=[('Casual', 'Casual'), ('Part Time', 'Part Time'), ('Full Time', 'Full Time')], max_length=30)),
                ('drivers_liscence_number', models.CharField(max_length=30)),
                ('drivers_liscence_state_iss', models.CharField(choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Conneticut', 'Conneticut'), ('Deleware', 'Deleware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virgina'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')], max_length=30)),
                ('employer_1', models.CharField(max_length=25)),
                ('employer_1_tel', models.CharField(max_length=30)),
                ('employer_1_date_started', models.DateField()),
                ('employer_1_date_terminated', models.DateField(blank=True, null=True)),
                ('employer_1_still_employed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25)),
                ('employer_1_may_we_contact', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30)),
                ('employer_1_street', models.CharField(max_length=30)),
                ('employer_1_city', models.CharField(max_length=30)),
                ('employer_1_state', models.CharField(choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Conneticut', 'Conneticut'), ('Deleware', 'Deleware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virgina'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')], max_length=30)),
                ('employer_1_zipcode', models.CharField(max_length=5)),
                ('employer_1_starting_title', models.CharField(max_length=25)),
                ('employer_1_starting_wage', models.CharField(max_length=25)),
                ('employer_1_final_title', models.CharField(max_length=25)),
                ('employer_1_final_wage', models.CharField(blank=True, max_length=25)),
                ('employer_1_summary', models.TextField(blank=True)),
                ('employer_1_favorite_details', models.CharField(max_length=300)),
                ('employer_1_least_details', models.CharField(blank=True, max_length=300)),
                ('employer_2', models.CharField(blank=True, max_length=30)),
                ('employer_2_tel', models.CharField(blank=True, max_length=30)),
                ('employer_2_date_started', models.DateField(blank=True, null=True)),
                ('employer_2_date_terminated', models.DateField(blank=True, null=True)),
                ('employer_2_still_employed', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30)),
                ('employer_2_may_we_contact', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30)),
                ('employer_2_street', models.CharField(blank=True, max_length=30)),
                ('employer_2_city', models.CharField(blank=True, max_length=30)),
                ('employer_2_state', models.CharField(blank=True, choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Conneticut', 'Conneticut'), ('Deleware', 'Deleware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virgina'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')], max_length=25)),
                ('employer_2_zipcode', models.CharField(blank=True, max_length=30)),
                ('employer_2_starting_title', models.CharField(blank=True, max_length=30)),
                ('employer_2_starting_wage', models.CharField(blank=True, max_length=30)),
                ('employer_2_final_title', models.CharField(blank=True, max_length=30)),
                ('employer_2_final_wage', models.CharField(blank=True, max_length=30)),
                ('employer_2_summary', models.TextField(blank=True, max_length=30)),
                ('employer_2_favorite_details', models.CharField(blank=True, max_length=30)),
                ('employer_2_least_details', models.CharField(blank=True, max_length=30)),
                ('employer_3', models.CharField(blank=True, max_length=30)),
                ('employer_3_tel', models.CharField(blank=True, max_length=30)),
                ('employer_3_date_started', models.DateField(blank=True, null=True)),
                ('employer_3_date_terminated', models.DateField(blank=True, null=True)),
                ('employer_3_still_employed', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30)),
                ('employer_3_may_we_contact', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30)),
                ('employer_3_street', models.CharField(blank=True, max_length=30)),
                ('employer_3_city', models.CharField(blank=True, max_length=30)),
                ('employer_3_state', models.CharField(blank=True, choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Conneticut', 'Conneticut'), ('Deleware', 'Deleware'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virgina'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')], max_length=30)),
                ('employer_3_zipcode', models.CharField(blank=True, max_length=30)),
                ('employer_3_starting_title', models.CharField(blank=True, max_length=30)),
                ('employer_3_starting_wage', models.CharField(blank=True, max_length=30)),
                ('employer_3_final_title', models.CharField(blank=True, max_length=30)),
                ('employer_3_final_wage', models.CharField(blank=True, max_length=30)),
                ('employer_3_summary', models.TextField(blank=True)),
                ('employer_3_favorite_details', models.CharField(blank=True, max_length=30)),
                ('employer_3_least_details', models.CharField(blank=True, max_length=30)),
                ('skills_and_qual', models.TextField(blank=True)),
                ('school_name', models.CharField(max_length=30)),
                ('years_completed', models.IntegerField()),
                ('completed', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30)),
                ('degree', models.CharField(max_length=30)),
                ('certification', models.CharField(max_length=30)),
                ('major', models.CharField(max_length=30)),
                ('minor', models.CharField(blank=True, max_length=30)),
                ('reference_1_name', models.CharField(max_length=45)),
                ('reference_1_relationship', models.CharField(max_length=30)),
                ('reference_1_telephone', models.CharField(max_length=12)),
                ('reference_1_years_known', models.CharField(max_length=2)),
                ('reference_2_name', models.CharField(max_length=45)),
                ('reference_2_relationship', models.CharField(max_length=30)),
                ('reference_2_telephone', models.CharField(max_length=12)),
                ('reference_2_years_known', models.CharField(max_length=2)),
                ('reference_3_name', models.CharField(max_length=45)),
                ('reference_3_relationship', models.CharField(max_length=30)),
                ('reference_3_telephone', models.CharField(max_length=12)),
                ('reference_3_years_known', models.CharField(max_length=2)),
                ('applicantSignature', models.CharField(max_length=100)),
                ('todaysDate', models.DateField()),
                ('hired', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='requestAQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=30)),
                ('streetAddress', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('zipcode', models.CharField(max_length=5)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('details', models.TextField()),
                ('slug', models.SlugField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='our_work/')),
                ('is_default', models.BooleanField(null=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.service')),
            ],
        ),
    ]