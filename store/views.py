from typing import Any
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from django.db.models.query import QuerySet
from django.views.generic import ListView, TemplateView, DetailView

from .forms import ContactForm
from .models import Furniture, Category, Project, ProjectItem

from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK")


class HomePageView(TemplateView):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['projects'] = Project.objects.all()
        return context


class ForUsView(TemplateView):
    template_name = 'forus.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['projects'] = Project.objects.all()
        return context


class ServicesView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['projects'] = Project.objects.all()
        return context


# Categories and Furniture

class CategoryListView(ListView):
    model = Category
    context_object_name = 'category'


class FurnitureListView(ListView):
    model = Furniture
    template_name = 'furniture.html'
    context_object_name = 'furniture'

    # This view will display all products filtered by a selected category.
    # We use the get_queryset() method to filter products based on the category ID passed in the URL.
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Furniture.objects.filter(category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['current_category'] = Category.objects.get(id=category_id)
        context['categories'] = Category.objects.all()
        context['projects'] = Project.objects.all()
        return context


class DetailFurnitureView(DetailView):
    model = Furniture
    template_name = 'furniture_details.html'
    context_object_name = 'furniture_details'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['projects'] = Project.objects.all()
        return context


# Project and their items

class ProjectListView(ListView):
    model = Project


class ItemProjectListView(ListView):
    model = ProjectItem
    template_name = 'project_items.html'
    context_object_name = 'projectsitems'

    def get_queryset(self) -> QuerySet[Any]:
        # The project_id is used to filter the ProjectItem objects.
        # Only the ProjectItem objects that are linked to the specific project_id will be returned.
        project_id = self.kwargs['project_id']  # Get the project_id from the URL
        return ProjectItem.objects.filter(project_id=project_id)

    # project_id=project_id is the correct way to filter ProjectItem objects based on the project_id field, which is
    # typically a foreign key linking ProjectItem to Project

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs['project_id']
        context['current_project'] = Project.objects.get(
            id=project_id)  # Get the Project object based on the project_id

        context['projects'] = Project.objects.all()
        context['categories'] = Category.objects.all()
        return context


class DetailProjectItemView(DetailView):
    model = ProjectItem
    context_object_name = 'item_details'
    template_name = 'project_item_details.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = Category.objects.all()
        return context


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data.get('number', 'Не е посочен')
            message = form.cleaned_data['message']

            full_message = (
                f"Име: {name}\n"
                f"Имейл: {email}\n"
                f"Телефон: {number}\n\n"
                f"Съобщение:\n{message}"
            )

            send_mail(
                subject=f"Ново съобщение от {name}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            messages.success(request, 'Съобщението е изпратено успешно!')
            return redirect('contacts')

    context = {
        'form': form,
        'furnitures': Furniture.objects.all(),
        'projects': Project.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'contact.html', context)
