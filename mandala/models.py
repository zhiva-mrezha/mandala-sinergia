from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext, gettext_lazy as _

class User(AbstractUser):
    def page_name(self):
        return "%s %s" % (gettext('User'), str(self))

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('user', kwargs={'pk': self.pk})
