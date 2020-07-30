from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, CreateView
from .models import Contact
from .forms import ContactForm
from django.forms import BaseForm


class HomeView(TemplateView):
    template_name = "portfolio/index.html"


class AboutView(TemplateView):
    template_name = "portfolio/about.html"


class ContactView(CreateView):
    model = Contact
    template_name = "portfolio/contact.html"
    form_class = ContactForm

    def get(self, request, *args, **kwargs) -> HttpResponse:
        form = ContactForm()
        context = {"form": form, "message": None}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs) -> HttpResponse:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Thank You for submitting you query.<br> \
                       We will get in touch with you soon!!"
            context = {"form": form, "message": message}
            return render(request, self.template_name, context)

