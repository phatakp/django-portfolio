from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from django.forms import BaseModelForm


class HomeView(TemplateView):
    template_name = "portfolio/index.html"


class AboutView(TemplateView):
    template_name = "portfolio/about.html"


class ContactView(CreateView):
    model = Contact
    template_name = "portfolio/contact.html"
    form_class = ContactForm
    success_url = "/contact/"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        messages.success(
            self.request,
            "Thank You for submitting you query.<br>We will get in touch with you soon!!",
        )
        return super().form_valid(form)

