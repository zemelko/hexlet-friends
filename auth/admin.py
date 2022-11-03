from django.contrib.auth.admin import UserAdmin

from auth.forms import UserChangeForm, UserCreationForm
from auth.models import SiteUser
from auth.models import GroupUser
from contributors.admin.custom import site


class SiteUserAdmin(UserAdmin):
    """Site user representation."""

    model = SiteUser
    add_form = UserCreationForm
    form = UserChangeForm


site.register(SiteUser)
site.register(GroupUser)
