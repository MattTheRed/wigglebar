from django import forms
from django.forms import widgets
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class RegistrationForm(forms.Form):
	"""
	Form for registering a new user account.

	Validates that the requested username is not already in use, and
	requires the password to be entered twice to catch typos.

	Subclasses should feel free to add any additional validation they
	need, but should avoid defining a ``save()`` method -- the actual
	saving of collected user data is delegated to the active
	registration backend.

	"""
	required_css_class = 'required'
	website_url = forms.URLField(label=_("Your website url"))
	email = forms.EmailField(label=_("Email address"))
	password1 = forms.CharField(widget=forms.PasswordInput,
	                            label=_("Choose a password"))
	next = forms.CharField(required=False, widget=widgets.HiddenInput)

	# password2 = forms.CharField(widget=forms.PasswordInput,
	#                             label=_("Password (again)"))

	def clean_email(self):
	    """
	    Validate that the username is alphanumeric and is not already
	    in use.

	    """
	    existing = User.objects.filter(email__iexact=self.cleaned_data['email'])
	    if existing.exists():
	        raise forms.ValidationError(_("A user with that username already exists."))
	    else:
	        return self.cleaned_data['email']

	def clean(self):
	    """
	    Verifiy that the values entered into the two password fields
	    match. Note that an error here will end up in
	    ``non_field_errors()`` because it doesn't apply to a single
	    field.

	    """
	    pass
	    # if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
	    #     if self.cleaned_data['password1'] != self.cleaned_data['password2']:
	    #         raise forms.ValidationError(_("The two password fields didn't match."))
	    return self.cleaned_data
