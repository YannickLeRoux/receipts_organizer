"""receiptsorganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from receipts import views
from accounts import views as accounts_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'signup/$', accounts_views.SignUpView.as_view(), name='signup'),
    url(r'login/$', accounts_views.LogInView.as_view(), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'categories/$', views.CategoriesView.as_view(), name='categories'),
    url(r'categories/new/$', views.NewCategory.as_view(), name='new_category'),
    url(r'categories/(?P<pk>\d+)/$', views.CategoryDetailView.as_view(),
        name='category_detail'),
    url(r'categories/(?P<pk>\d+)/delete/$', views.CategoryDeleteView.as_view(),
        name='category_delete'),
    url(r'receipts/$', views.ReceiptsYearsView.as_view(), name='receipts_years'),
    url(r'receipts/new/$', views.NewReceiptView.as_view(), name='new_receipt'),
    url(r'receipts/(?P<pk>REC[a-zA-Z0-9_]+)/$', views.ReceiptDetailView.as_view(),
        name='receipt_detail'),
    url(r'receipts/(?P<year>[0-9]{4})/$',views.ReceiptsMonthsView.as_view(),
    name='receipts_months'),
     url(r'receipts/(?P<year>[0-9]{4})/(?P<month>\d{2})/$',views.ReceiptsOfOneMonthView.as_view(),
    name='receipts_one_month'),


]
