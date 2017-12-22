from django.views.generic import (TemplateView, ListView, CreateView,
                                    DetailView, DeleteView, YearArchiveView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Category, Receipt

from .forms import NewReceiptForm


class HomePageView(TemplateView):
    template_name = 'index.html'
    

class CategoriesView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'categories.html'

    def get_queryset(self):
        queryset = Category.objects.filter(created_by=self.request.user)
        return queryset


class NewCategory(LoginRequiredMixin, CreateView):
    model = Category
    fields = ('name',)
    # form_class = CategoryForm
    success_url = reverse_lazy('categories')
    template_name = 'new_category.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'category_detail.html'

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('categories')
    template_name = "category_confirm_delete.html"


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name = 'receipts.html'

    def get_queryset(self):
        queryset = Receipt.objects.dates('date_created','year',order="DESC")
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ReceiptListView, self).get_context_data(**kwargs)
        context['years_available'] = Receipt.objects.dates('date_created',
                'year', order="DESC")
        return context

class ReceiptYearArchiveView(LoginRequiredMixin, YearArchiveView):
    queryset = Receipt.objects.all()
    date_field = "date_created"
    make_object_list = True
    template_name ='receipts_year.html'

class ReceiptMonthArchiveView(LoginRequiredMixin, ListView):
    model = Receipt
    template_name ='receipts_month.html'





class NewReceiptView(LoginRequiredMixin, CreateView):
    model = Receipt
    form_class = NewReceiptForm
    success_url = reverse_lazy('receipts')
    template_name = 'new_receipt.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.recorded_by = self.request.user
        self.object.save()
        return super().form_valid(form)


class ReceiptDetailView(LoginRequiredMixin, DetailView):
    model = Receipt
    template_name = 'receipt_detail.html'
