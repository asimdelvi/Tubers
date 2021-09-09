from crispy_forms.layout import Layout, Submit
from django.forms import ModelForm
from .models import ContactAdmin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import PrependedText

class ContactAdminForm(ModelForm):
  global admin_fields
  admin_fields = ['full_name',
                  'phone',
                  'email',
                  'company_name',
                  'subject',
                  'message']

  class Meta:
    model = ContactAdmin
    fields = admin_fields


  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    self.helper = FormHelper()
    self.helper.form_show_labels = False

    for field in admin_fields:
      self.fields[field].widget.attrs.update(
        {'placeholder': field.replace('_', ' ').capitalize()})


