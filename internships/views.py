from django.shortcuts import render, Http404
from django.core.paginator import Paginator
from .models import Company, City, Internship

# Create your views here.
def home(request):
        context = {}

        interns = Internship.objects.order_by('-posted_at').filter(is_approved=True)
        cities = City.objects.order_by('name')

        paginator = Paginator(interns, 5)
        page = request.GET.get('page')
        i = paginator.get_page(page)

        context['cities'] = cities
        context["internships"] = i
        context['pages'] = paginator.num_pages
        print(paginator.num_pages)
        return render(request, 'templates/home.html', context)

def internship_by_company(request, slug):
        context = {}
        try:
                c = Company.objects.get(slug=slug)
                cities = City.objects.all()
                interns = Internship.objects.filter(company=c)

                paginator = Paginator(interns, 5)
                page = request.GET.get('page')
                i = paginator.get_page(page)

                context["company_name"] = c.name
                context["cities"] = cities
                context["internships"] = i
                context['company'] = c
                context['pages'] = paginator.num_pages
        except Company.DoesNotExist:
                raise Http404("Company does not exist")
        return render(request, 'templates/company.html', context)

def internship_by_city(request, name):
        context = {}
        try:
                city = City.objects.get(name=name)
                cities = City.objects.all()
                interns = Internship.objects.filter(location=city).filter(
                    is_approved=True).order_by('-posted_at')

                paginator = Paginator(interns, 5)
                page = request.GET.get('page')
                i = paginator.get_page(page)

                context["city_name"] = city.name
                context["internships"] = i
                context["cities"] = cities
                context['pages'] = paginator.num_pages
        except Company.DoesNotExist:
                raise Http404("City does not exist")
        return render(request, 'templates/city.html', context)
