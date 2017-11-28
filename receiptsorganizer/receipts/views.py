from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = 'index.html'
    
class CategoriesView(ListView):
    template_name = 'categories.html'
