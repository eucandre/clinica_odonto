from .models import *
from app_contrato.models import *
from app_receita.models import *
from datetime import date


def VerificaPagamento(nr_id):
    '''o parametro identifica o contrato do cliente.
    Este metodo vai buscar os dias em que o cliente esta em dias.'''

    obj_contrato_odonto = Contrato_odonto.objects.get(pk=nr_id)
    obj_recebimento_odonto = RecebimentoPlanoOdonto.objects.get(pk=nr_id)
    hoje = date.today()
    mes = date.month
    atual = False

    if obj_recebimento_odonto.getMes() == mes:
        return atual==True
    elif obj_recebimento_odonto.getMes() < mes:
        return hoje - int(obj_contrato_odonto.date_payment_per_month)+30

# def condition_to_tratment_cancel(value_contract):
#     if value_contract
#         return
