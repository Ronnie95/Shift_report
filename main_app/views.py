from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Shift
from django.urls import reverse
from .forms import ShiftReport


# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class Sucess(TemplateView):
    template_name = "success.html"


# class ShiftReportCreate(CreateView):
#     model = Shift
#     fields = [
#             'date',
#             'shift_name',
#             'people_amount',
#             'breakdowns',
#             'assistance_needed',
#             'additional_comments'
#         ]
#     template_name = "shift_report.html"
#     success_url = "/success/"

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(ShiftReportCreate, self).form_valid(form)

#     def get_success_url(self):
#         print(self.kwargs)
#         return reverse('success', kwargs={'pk': self.object.pk})

class ShiftReportCreate(CreateView):
    model = Shift
    form_class = ShiftReport
    template_name = "shift_report.html"

    def get_success_url(self):
        return reverse('success', kwargs={'pk': self.object.pk})