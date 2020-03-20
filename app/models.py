from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext, gettext_lazy as _

from photologue.models import Photo, Gallery

from rules.contrib.models import RulesModelBase, RulesModelMixin

class Sphere(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    def page_name(self):
        return "%s %s" % (gettext('User'), str(self))

    def __str__(self):
        if self.first_name or self.last_name:
            return '%s %s' % (self.first_name, self.last_name)
        else:
            return self.username

    def get_absolute_url(self):
        return reverse('user', kwargs={'pk': self.pk})

class Timestamped(RulesModelMixin, models.Model, metaclass=RulesModelBase):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super(Timestamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class MandalaUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    spheres = models.ManyToManyField(Sphere)

    phone = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=0)
    location = models.CharField(max_length=100)
    membership = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, blank=True, null=True)
