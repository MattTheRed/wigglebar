from django import forms
from django.utils.encoding import smart_unicode
import re
from bar import widgets
from bar.models import Bar


class HexColorField(forms.fields.Field):
    default_error_messages = {
        'hex_error': u'This is an invalid color code. It must be a html hex color code e.g. #000000'
    }

    def clean(self, value):

        super(HexColorField, self).clean(value)

        if value in forms.fields.EMPTY_VALUES:
            return u''

        value = smart_unicode(value)
        value_length = len(value)

        if value_length != 7 or not re.match('^\#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$', value):
            raise ValidationError(self.error_messages['hex_error'])

        return value

    def widget_attrs(self, widget):
        if isinstance(widget, (forms.fields.TextInput)):
            return {'maxlength': str(7)}


class BarToggle(forms.ModelForm):
	class Meta:
		model = Bar
		fields = ["is_enabled"]
		widgets = {
            'is_enabled': forms.RadioSelect
        }

class BarForm(forms.ModelForm):
	background_color = HexColorField(
			widget=widgets.ColorPickerWidget(model="colors.background", attrs={"ng-model":"colors.background", "class": "hidden-field"})
		)
	message_color = HexColorField(
			widget=widgets.ColorPickerWidget(model="colors.text", attrs={"ng-model":"colors.text", "class": "hidden-field"})
		)
	button_background_color = HexColorField(
			widget = widgets.ColorPickerWidget(model="colors.buttonBackground", attrs={"ng-model":"colors.buttonBackground", "class": "hidden-field"})
		)
	button_text_color = HexColorField(
			widget = widgets.ColorPickerWidget(model="colors.buttonText", attrs={"ng-model":"colors.buttonText", "class": "hidden-field"})
		)
	message = forms.CharField(widget = forms.TextInput(attrs={"ng-model":"content.messageText"}))
	button_text = forms.CharField(widget = forms.TextInput(attrs={"ng-model":"content.buttonText"}))
	button_link = forms.CharField(widget = forms.TextInput(attrs={"ng-model":"content.buttonLink"}))
	icon = forms.ImageField(required=False, widget=forms.FileInput(attrs={"ng-show":"uploadVisible", "id": "hidden_input"}))
	icon_url = forms.CharField(
			widget = widgets.IconPickerWidget(choices="iconChoices", choice="content.iconUrl", colors="colors", attrs={"ng-model": "content.iconUrl", "class": "hidden-field"})
		)

	class Meta:
		model = Bar
		exclude = ["user", "is_enabled"]

	def clean_icon_url(self):
		print self.cleaned_data["icon_url"]
		return self.cleaned_data["icon_url"]


