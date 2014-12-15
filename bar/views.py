from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.conf import settings
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from payments import settings as payment_settings
from payments.forms import PlanForm


from bar.forms import BarForm, BarToggle
from bar.models import Bar

#http://www.roguelynn.com/words/django-custom-user-models/
# from django.contrib.auth import get_user_model
# User = get_user_model()

class BuilderView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(BuilderView, self).get_context_data(**kwargs)
		context["site_url"] = settings.SITE_URL
		context["static_url"] = settings.STATIC_URL_FULL_PATH
		return context

def dashboard(request, username):
	print request.user
	return render(request, "loggedin/dashboard.html")
	#print username


class ViewBar(DetailView):
	model = Bar
	context_object_name = "bar"
	queryset = Bar.objects.all()
	template_name = "public/viewbar.html"

class UpdateBar(UpdateView):
	model = Bar
	template_name = "loggedin/editbar.html"
	form_class = BarForm
	success_url = "."

	def get(self, request, *args, **kwargs):
		obj = super(UpdateBar, self).get_object()
		if not obj.user == self.request.user:
			raise PermissionDenied
		self.toggle_bar_form = BarToggle(instance=obj)
		return super(UpdateBar, self).get(request, *args, **kwargs)


	def post(self, request, *args, **kwargs):
		obj = super(UpdateBar, self).get_object()
		if not obj.user == self.request.user:
			raise PermissionDenied
		if request.POST.get("is_enabled"):
			self.toggle_bar_form = BarToggle(request.POST, instance=obj)
			if self.toggle_bar_form.is_valid():
				self.toggle_bar_form.save()
				return HttpResponseRedirect(reverse("edit_bar", kwargs={'pk': self.toggle_bar_form.instance.id}) + "?expandembed=true")
		return super(UpdateBar, self).post(request, *args, **kwargs)

	def get_object(self, queryset=None):
		obj = super(UpdateBar, self).get_object()
		if not obj.user == self.request.user:
			raise PermissionDenied
		return obj

	def get_context_data(self, **kwargs):
		context = super(UpdateBar, self).get_context_data(**kwargs)
		context["site_url"] = settings.SITE_URL
		context["static_url"] = settings.STATIC_URL_FULL_PATH
		context["bar_id"] = self.object.id
		context["form_title"] = ""
		context["form_save"] = "Save"

		context["STRIPE_PUBLIC_KEY"] = payment_settings.STRIPE_PUBLIC_KEY
		context["PLAN_CHOICES"] = payment_settings.PLAN_CHOICES
		context["PAYMENT_PLANS"] = payment_settings.PAYMENTS_PLANS
		context["subscribe_form"] = PlanForm
		context["toggle_bar_form"] = self.toggle_bar_form
		#context["toggle_bar_form"] = BarToggle(user=self.request.user)
		return context

	def form_valid(self, form):
		messages.success(self.request, "Your WiggleBar has been saved!")
		return super(UpdateBar, self).form_valid(form)

class CreateBar(CreateView):
	template_name = "loggedin/createbar.html"
	form_class = BarForm

	def get(self, request, *args, **kwargs):
		self.object = None

		form_class = self.get_form_class()
		try:
			initial = self.request.session['saved_form']
			form = form_class(initial)
			form.instance.user = request.user
			form.save()
			del self.request.session['saved_form']
			messages.success(self.request, "Your WiggleBar has been created! You can add it to your site by copying and pasting the code below on to your website.")
			return HttpResponseRedirect(reverse("edit_bar", kwargs={'pk': form.instance.id}) + "?expandembed=true")
		except:
			form = self.get_form(form_class)
		return self.render_to_response(self.get_context_data(form=form))

	def get_context_data(self, **kwargs):
		context = super(CreateBar, self).get_context_data(**kwargs)
		context["site_url"] = settings.SITE_URL
		context["static_url"] = settings.STATIC_URL_FULL_PATH
		context["form_title"] = "Create your Wiggle Bar"
		context["form_save"] = "Save this Bar"
		context["show_preview"] = True

		context["STRIPE_PUBLIC_KEY"] = payment_settings.STRIPE_PUBLIC_KEY
		context["PLAN_CHOICES"] = payment_settings.PLAN_CHOICES
		context["PAYMENT_PLANS"] = payment_settings.PAYMENTS_PLANS
		context["subscribe_form"] = PlanForm
		return context

	def form_valid(self, form):
		if self.request.POST:
			if self.request.user.is_authenticated():
				users_bars = Bar.objects.filter(user=self.request.user)
				if users_bars.count() > 1:
					messages.success(self.request, "It looks like you've already created a WiggleBar. You can edit it below.")
					return HttpResponseRedirect(reverse("edit_bar", kwargs={'pk': users_bars[0].id}))
				form.instance.user = self.request.user
				form.instance.is_enabled = True
				try:
					if self.request.user.customer.current_subscription.status == "active":
						form.instance.is_enabled = True
				except:
					pass
				self.object = form.save()
				messages.success(self.request, "Your WiggleBar has been created! You can add it to your site by copying and pasting below on to your website")
				return HttpResponseRedirect(reverse("edit_bar", kwargs={'pk': form.instance.id}) + "?expandembed=true")
				#return HttpResponseRedirect(self.get_success_url())

    #     return super(ModelFormMixin, self).form_valid(form)
				# return super(CreateBar, self).form_valid(form)
				# return HttpResponseRedirect(self.get_success_url())
			else:
				self.request.session['saved_form'] = form.cleaned_data
				return HttpResponseRedirect(reverse("registration_register") + "?next=/bar/create")


	def get_success_url(self):
		return reverse("create_bar")

class HomePage(CreateBar):
	template_name = "index.html"


