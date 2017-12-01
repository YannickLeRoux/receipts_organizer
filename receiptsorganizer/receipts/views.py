from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = 'index.html'
    
class CategoriesView(TemplateView):
    template_name = 'categories.html'
