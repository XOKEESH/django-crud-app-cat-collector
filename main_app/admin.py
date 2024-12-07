from django.contrib import admin
from .models import Cat, Feeding, Toy, Milestone

# Register your models here.
admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Milestone)
