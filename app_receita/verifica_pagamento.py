from .models import *
from app_contrato.models import *
from app_receita.models import *
from datetime import date


def getNomeOdonto(nr_id):
    '''o parametro identifica o contrato do cliente'''
    obj_contrato_odonto = Contrato_odonto.objects.get(pk=nr_id)

    hoje = date.today()

    if obj_contrato_odonto.date_payment_per_month == hoje.day:
        return 0

    if obj_contrato_odonto.date_payment_per_month > hoje.day:
        return obj_contrato_odonto.date_payment_per_month - hoje.day
