from app_receita.models import *
tamano = len(OrcamentoPlanoOdontologico.objects.all())
for i in range(tamano):
    ob = OrcamentoPlanoOdontologico.objects.get(pk = i)
    print ob.value_tratment