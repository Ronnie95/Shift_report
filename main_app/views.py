from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Shift
from django.urls import reverse
from .forms import ShiftReport
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ShiftReport



# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class Sucess(TemplateView):
    template_name = "success.html"



class ShiftReportCreate(CreateView):
    model = Shift
    form_class = ShiftReport
    template_name = "shift_report.html"
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        response = super().form_valid(form)

        shift = self.object

        send_mail(
            subject=f"Shift Report - {shift.shift_name}",
            message=f"""
New Shift Report Submitted

Date:
{shift.date}

Shift:
{shift.shift_name}

Number of People:
{shift.people_amount}

Breakdowns:
{shift.breakdowns}

Assistance Needed:
{shift.assistance_needed}

Additional Comments:
{shift.additiional_comments}
""",
            from_email="your_email@gmail.com",
            recipient_list=[
                "manager_email@gmail.com"
            ],
            fail_silently=False,
        )

        return response