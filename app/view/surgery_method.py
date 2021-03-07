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

from app.models import SurgeryMethod

import json


# LoginRequiredMixin, PermissionRequiredMixin,
class SurgeryMethodList(ListView):
    """ the process profile list page (operation). """
    login_url = '/login/'
    model = SurgeryMethod
    template_name = 'app/surgery_method/surgery_method_list.html'
    paginate_by = 10
    # permission_required = 'oven.view_process_profile'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['surgery_method'] = SurgeryMethod.objects.all()
        surgery_method = self.request.GET.get('surgery_method', None)
        context['search_condition'] = f'&surgery_method={surgery_method}'
        return context

    def get_queryset(self):
        surgery_method = self.request.GET.get('surgery_method', None)
        if surgery_method == '' or surgery_method is None:
            return SurgeryMethod.objects.all()
        sm = SurgeryMethod.objects\
            .filter(name__icontains=surgery_method)
        return sm


# @permission_required('oven.add_product_profile', login_url='/login/')
@csrf_exempt
@login_required(login_url='/login/')
def create(request):
    try:
        res = dict()
        data = json.loads(request.body.decode('utf-8'))['params']

        if data['surgery_method'] == '':
            raise Exception('資料不能為空')

        SurgeryMethod.objects\
            .create(name=data['surgery_method'],
                    user=request.user)
        res['result'] = 'successful'
        res['message'] = '成功建立資料'
    except IntegrityError:
        res['result'] = 'failure'
        res['message'] = '資料重複'
        return JsonResponse(res, safe=False)
    except Exception as e:
        res['result'] = 'failure'
        res['message'] = str(e)
    return JsonResponse(res, safe=False)


# @permission_required('oven.change_product_profile', login_url='/login/')
@csrf_exempt
@login_required(login_url='/login/')
def update(request):
    """
    provide an API to update object.
    :param request:
    :return:
    """
    try:
        res = dict()
        data = json.loads(request.body.decode('utf-8'))['params']

        if data['surgery_method'] == '':
            raise Exception('資料不能為空')

        sm = SurgeryMethod.objects\
            .get(id=data['id'])
        sm.name = data['surgery_method']
        sm.user = request.user
        sm.save()
        res['result'] = 'successful'
        res['message'] = '成功更新資料'
    except IntegrityError:
        res['result'] = 'failure'
        res['message'] = '資料重複'
    except ObjectDoesNotExist:
        res['result'] = 'failure'
        res['message'] = '資料不存在'
    except Exception as e:
        res['result'] = 'failure'
        res['message'] = str(e)
    return JsonResponse(res, safe=False)


# @permission_required('oven.delete_product_profile', login_url='/login/')
@csrf_exempt
@login_required(login_url='/login/')
def delete(request):
    """
    provide an API to update object.
    :param request:
    :return:
    """
    try:
        res = dict()
        data = json.loads(request.body.decode('utf-8'))['params']

        sm = SurgeryMethod.objects\
            .get(id=data['id'])
        sm.delete()
        res['result'] = 'successful'
        res['message'] = '成功刪除資料'
    except ObjectDoesNotExist:
        res['result'] = 'failure'
        res['message'] = '資料不存在'
    except Exception as e:
        res['result'] = 'failure'
        res['message'] = str(e)
    return JsonResponse(res, safe=False)
