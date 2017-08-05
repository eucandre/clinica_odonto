from app_receita.models import *
tamano = len(Orcamento_Plano_Odonto.objects.all())
for i in range(tamano):
    ob = Orcamento_Plano_Odonto.objects.get(pk = i)
    print ob.value_tratment