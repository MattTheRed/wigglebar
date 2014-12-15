from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.conf import settings
from register_user.forms import RegistrationForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from bar.models import Bar


User = get_user_model()

def account_profile(request):
    try:
        bar = Bar.objects.filter(user=request.user)[0]
        return HttpResponseRedirect(reverse("edit_bar", kwargs={'pk': bar.id}))
    except:
        return HttpResponseRedirect(reverse("create_bar"))

class _RequestPassingFormView(FormView):
    """
    A version of FormView which passes extra arguments to certain
    methods, notably passing the HTTP request nearly everywhere, to
    enable finer-grained processing.

    """
    def get(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control.
        #self.next = request.GET.get("next")
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control.
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        if form.is_valid():
            # Pass request to form_valid.
            return self.form_valid(request, form)
        else:
            return self.form_invalid(form)

    def get_form_class(self, request=None):
        return super(_RequestPassingFormView, self).get_form_class()

    def get_form_kwargs(self, request=None, form_class=None):
        return super(_RequestPassingFormView, self).get_form_kwargs()

    def get_initial(self, request=None):
        # initial = super(_RequestPassingFormView, self).get_initial()
        # # if request.GET.get("next"):
        # #     initial["next"] = request.GET.get("next")
        # print initial
        return super(_RequestPassingFormView, self).get_initial()

    def get_success_url(self, request=None, user=None):
        # We need to be able to use the request and the new user when
        # constructing success_url.
        return super(_RequestPassingFormView, self).get_success_url()

    def form_valid(self, form, request=None):
        return super(_RequestPassingFormView, self).form_valid(form)

    def form_invalid(self, form, request=None):
        return super(_RequestPassingFormView, self).form_invalid(form)

class RegistrationView(_RequestPassingFormView):
    """
    Base class for user registration views.

    """
    disallowed_url = 'registration_disallowed'
    form_class = RegistrationForm
    http_method_names = ['get', 'post', 'head', 'options', 'trace']
    success_url = None
    template_name = 'registration/registration_form.html'

    def get(self, request, *args, **kwargs):
        return super(RegistrationView, self).get(request, *args, **kwargs)

    def get_initial(self, request=None):
        return super(RegistrationView, self).get_initial(request)

    def dispatch(self, request, *args, **kwargs):
        """
        Check that user signup is allowed before even bothering to
        dispatch or do other processing.

        """
        if not self.registration_allowed(request):
            return redirect(self.disallowed_url)
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, request, form):
        new_user = self.register(request, **form.cleaned_data)
        success_url = reverse("create_bar")

        # success_url may be a simple string, or a tuple providing the
        # full argument set for redirect(). Attempting to unpack it
        # tells us which one it is.
        try:
            to, args, kwargs = success_url
            if self.next_page:
                to = self.next_page
            return redirect(to, *args, **kwargs)
        except ValueError:
            return redirect(success_url)

    def register(self, request, **cleaned_data):
        self.next_page = cleaned_data['next']

        email, password = cleaned_data['email'], cleaned_data['password1']
        user = User.objects.create_user(email, password)
        user.website_url = cleaned_data['website_url']
        user.save()

        new_user = authenticate(email=email, password=password)
        print "New User:", new_user
        login(request, new_user)
        return new_user


    def registration_allowed(self, request):
        """
        Indicate whether account registration is currently permitted,
        based on the value of the setting ``REGISTRATION_OPEN``. This
        is determined as follows:

        * If ``REGISTRATION_OPEN`` is not specified in settings, or is
          set to ``True``, registration is permitted.

        * If ``REGISTRATION_OPEN`` is both specified and set to
          ``False``, registration is not permitted.

        """
        return getattr(settings, 'REGISTRATION_OPEN', True)

    def get_success_url(self, request, user):
        return (user.get_absolute_url(), (), {})


# class RegisterBarUserView(RegistrationView):
# 	pass
