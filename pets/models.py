from django.db import models
from datetime import datetime
# from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Pet(models.Model):
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    type_choices = (
            ('Dog', 'Dog'),
            ('Cat', 'Cat'),
        )

    breed_choices = (
        ('Labrador Retriever(dog)', 'Labrador Retriever(dog)'),
        ('German Shepherd(dog)', 'German Shepherd Dog(dog)'),
        ('Golden Retriever(dog)', 'Golden Retriever(dog)'),
        ('Bulldog(dog)', 'Bulldog(dog)'),
        ('Beagle(dog)', 'Beagle(dog)'),
        ('British Shorthair(cat)', 'British Shorthair(cat)'),
        ('Persian Cats(cat)', 'Persian Cats(cat)'),
        ('Maine Coon(cat)', 'Maine Coon(cat)'),
        ('American Shorthair(cat)', 'American Shorthair(cat)'),
        ('Scottish Fold(cat)', 'Scottish Fold(cat)'),
    )

    age_choices = (
        ('Puppy/Kitten', 'Puppy/Kitten'),
        ('Young', 'Young'),
        ('Adult', 'Adult'),
        ('Senior', 'Senior'),
    )

    pet_title = models.CharField(max_length=255)
    pet_type = MultiSelectField(choices=type_choices)
    pet_breed = MultiSelectField(choices=breed_choices)
    color = models.CharField(max_length=100)
    age = MultiSelectField(choices=age_choices)
    gender = models.CharField(max_length=100)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    pet_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    pet_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    pet_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    pet_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    pet_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.pet_title
