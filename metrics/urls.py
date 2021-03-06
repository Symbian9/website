# coding: utf-8

from django.conf.urls import url

from metrics import views

urlpatterns = [
    url(
        r'cpu_data',
        views.cpu_data,
        name='cpu_data'),
    url(
        r'cpu_hour_data',
        views.cpu_hour_data,
        name='cpu_hour_data'),
    url(
        r'mem_data',
        views.mem_data,
        name='mem_data'),
    url(
        r'mem_hour_data',
        views.mem_hour_data,
        name='mem_hour_data'),
    url(
        r'system',
        views.System.as_view(),
        name='system'),

    url(
        r'data_week',
        views.data_week,
        name='data_week'),

    url(
        r'data_month',
        views.data_month,
        name='data_month'),
    url(
        r'docs_data_all',
        views.docs_data_all,
        name='docs_data_all'),

    url(
        r'visiters',
        views.Visiters.as_view(),
        name='visiters'),

    url(
        r'urls_from',
        views.URLSFrom.as_view(),
        name='urls_from'),

    url(
        r'urls',
        views.URLS.as_view(),
        name='urls'),

    url(
        r'user_agents',
        views.UserAgents.as_view(),
        name='user_agents'),

    url(
        r'',
        views.HomePage.as_view(),
        name='home_page'),
]
