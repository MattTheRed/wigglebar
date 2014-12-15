from django.forms import widgets
from django.utils.safestring import mark_safe

class AttrCharField(widgets.Input):
	def __init__(self, attrs):
		self.model = model
		attrs["ng-model"] = "[[ %s ]]" % model
		super(AngularCharField, self).__init__(attrs)

class IconPickerWidget(widgets.Input):
	def __init__(self, choices, choice, colors, attrs):
		self.choices = choices
		self.choice = choice
		self.colors = colors
		super(IconPickerWidget, self).__init__(attrs)

	def render(self, name, value, attrs=None):
		return mark_safe(u"""<icon-picker choices="%s" choice="%s" colors="%s" class="palette-picker"></icon-picker>%s""" % (self.choices, self.choice, self.colors, super(IconPickerWidget, self).render(name, value, attrs)))


class ColorPickerWidget(widgets.Input):
	# Refactor out css/js into related asset files included by widgets
	# https://docs.djangoproject.com/en/dev/topics/forms/media/#topics-forms-media
	def __init__(self, model, attrs):
		self.model = model
		attrs["value"] = "[[ %s ]]" % model
		super(ColorPickerWidget, self).__init__(attrs)

	def render(self, name, value, attrs=None):
		return mark_safe(u'''<ui-colorpicker ng-model="%s"></ui-colorpicker>%s''' % (self.model, super(ColorPickerWidget, self).render(name, value, attrs)))


class OnOffSwitchWidget(widgets.RadioSelect):
	pass
	# def render(self, name, value, attrs=None):
	# 	return mark_safe(u'''%s''' % (super(OnOffSwitchWidget, self).render(name, value, attrs)))


#<palette-picker choices="colorChoices" choice="colors" class="palette-picker"></palette-picker>


#colors.text

# http://tothinkornottothink.com/post/10815277049/django-forms-i-custom-fields-and-widgets-in-detail

# class ExampleForm(forms.Form):
#     user_email = forms.EmailField(
#         widget=HTML5Input(type='email', attrs={'class': "emailFields"})
#     )
