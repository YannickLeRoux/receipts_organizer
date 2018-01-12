from django.views.generic import (TemplateView, ListView, CreateView,
                                    DetailView, DeleteView, YearArchiveView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

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


class CategoryDetailView(LoginRequiredMixin, ListView):
    model = Receipt
    context_object_name = "receipts"
    template_name = 'category_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['category'] = self.category
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        queryset = self.category.receipts.all()
        return queryset


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('categories')
    template_name = "category_confirm_delete.html"

class ReceiptsYearsView(LoginRequiredMixin, ListView):
    model = Receipt
    context_object_name = "receipts"
    template_name = 'receipts_years.html'

    # def get_queryset(self):
    #     queryset = Receipt.objects.filter(created_by=self.request.user)
    #     return queryset


    def get_queryset(self):
        queryset = Receipt.objects.dates('date_created','year',order="DESC")
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ReceiptsYearsView, self).get_context_data(**kwargs)
        context['years_available'] = Receipt.objects.dates('date_created',
                'year', order="DESC")
        return context

class ReceiptsMonthsView(LoginRequiredMixin, YearArchiveView):
    queryset = Receipt.objects.all()
    date_field = "date_created"
    make_object_list = True
    template_name ='receipts_months.html'


class ReceiptsOfOneMonthView(LoginRequiredMixin, ListView):
    model = Receipt
    context_object_name = "receipts"
    template_name = 'receipts.html'

    def get_queryset(self):
        queryset = Receipt.objects.all()
        return queryset


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

    def get_context_data(self, **kwargs):
        kwargs['pk'] = self.pk
        return super().get_context_data(**kwargs)

