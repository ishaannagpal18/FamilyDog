from django.contrib import admin
from .models import about,slider,featuredservices, services, clients, portfolio, testimonial, contactlist, contactform

# Register your models here.
admin.site.register(about)
admin.site.register(slider)
admin.site.register(featuredservices)
admin.site.register(services)
admin.site.register(clients)
admin.site.register(portfolio)
admin.site.register(contactlist)
admin.site.register(contactform)
