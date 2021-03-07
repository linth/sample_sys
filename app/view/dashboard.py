from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

# CRUD
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy, reverse

# search
from django.db.models import Q
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from app.models import Medication

import json


# LoginRequiredMixin, PermissionRequiredMixin,
# class MedicationList(ListView):
#     """ the process profile list page (operation). """
#     login_url = '/login/'
#     model = Medication
#     template_name = 'app/medication/medication_list.html'
#     paginate_by = 10
#     # permission_required = 'oven.view_process_profile'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['medication'] = Medication.objects.all()
#         return context
#
#     def get_queryset(self):
#         return Medication.objects.all()

def Dashboard(request):
    template = 'app/dashboard/dashboard.html'
    context = {}
    return render(request, template, context)
