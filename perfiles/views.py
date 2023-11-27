from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from perfiles.forms import RegisterForm


# Create your views here.

class PerfilRegistration(FormView):
    template_name = 'perfiles/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('perfiles:success')

    def form_valid(self, form):
        form.save()
        return super(PerfilRegistration, self).form_valid(form)





