from django.conf.urls import url
from django.contrib.admin import *
from django.contrib.auth import *
from app_base.views import *
from app_estoque.views import *
from app_receita.views import *
from app_perfis.views import *
from app_atendimento.views import *
from app_campanha.views import *
from django.conf import settings
from app_contrato.views import *
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', site.urls),
    url(r'^$',inicia),
    url(r'^insere_profissional/',insere_profissional),
    url(r'^insere_funcionario/',insere_funcionario),
    url(r'^insere_cliente/',insere_cliente),
    url(r'^insere_fornecedor/',insere_fornecedor),
    url(r'^insere_produto/',insere_produto),
    url(r'^insere_retirada_produtos/',insere_retira_produtos),
    url(r'^insere_compra_produtos/',insere_compra_produtos),
    url(r'^insere_dentes/',InsereDentes),
    url(r'^insere_orcamento_odonto/',InsereOrcamentoOdonto),
    url(r'^insere_orcamento_psico/',InsereOrcamentoPsico),
    url(r'^insere_orcamento_nutri/',InsereOrcamentoNutri),
    url(r'^insere_recebimento_plano/',InsereRecebimentoPlano),
    url(r'^insere_recebimento_plano_nutri/',InsereRecebimentoPlanoNutri),
    url(r'^insere_recebimento_plano_Psico/',InsereRecebimentoPlanoPsico),
    url(r'^insere_atendiemento_avulso/',InsereAtendimentoAvulso),
    url(r'^insere_contrato_odonto/',InsereContratoOdonto),
    url(r'^insere_contrato_nutri/',InsereContratoNutri),
    url(r'^insere_contrato_psico/',InsereContratoPsico),
    url(r'^insere_relatorio_exame_odonto/',insere_relatorio_exame_odonto),
    url(r'^insere_relatorio_exame_psico/',insere_relatorio_exame_psico),
    url(r'^insere_relatorio_exame_nutri/',insere_relatorio_exame_nutri),
    url(r'^insere_agendamento_plano_odonto/',insere_agendamento_plano_odonto),
    url(r'^insere_agendamento_plano_nutri/',insere_agendamento_plano_nutri),
    url(r'^insere_agendamento_plano_psico/',insere_agendamento_plano_psico),
    url(r'^insere_contato_cliente_indica/',insere_contato_cliente),


    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login.html'}, name='logout'),

    #----------administracao-------------------#
    url(r'^profissionais/', lista_profissionais),
    url(r'^funcionarios/', lista_funcionarios),
    url(r'^fornecedores/', lista_fornecedor),
    url(r'^clientes/', lista_clientes),
    url(r'^dentes/', lista_dentes),
    url(r'^orcamento_odonto/', lista_orcamentoOdonto),
    url(r'^orcamento_nutri/', lista_orcamentonutri),
    url(r'^orcamento_psico/', lista_orcamento_psico),
    url(r'^atendimento_avulso/', lista_atendimento_avulso),
    url(r'^recebimento_plano/', lista_recebimento_plano),
    url(r'^contratos_odonto/', lista_ContratoOdonto),
    url(r'^contratos_nutri/', lista_ContratoNutri),
    url(r'^contratos_psico/', lista_ContratoPsico),
    ######
    url(r'^relatorios_exame_odonto/', lista_relatorios_exame_odonto),
    url(r'^relatorios_exame_psico/', lista_relatorios_exame_psico),
    url(r'^relatorios_exame_nutri/', lista_relatorios_exame_nutri),
    url(r'^agendamentos_plano_odonto/', lista_agendamento_plano_odonto),
    url(r'^agendamentos_plano_nutri/', lista_agendamento_plano_nutri),
    url(r'^agendamentos_plano_psico/', lista_agendamento_plano_psico),
    #----------------item detalhados---------------#
    url(r'^item_dentista/(?P<nr_item>\d+)/$', detalha_profissional),
    url(r'^item_funcionario/(?P<nr_item>\d+)/$', detalha_funcinario),
    url(r'^item_cliente/(?P<nr_item>\d+)/$', detalha_cliente),
    url(r'^item_dentes/(?P<nr_item>\d+)/$', detalha_dentes),
    url(r'^item_orcamento_odonto/(?P<nr_item>\d+)/$', detalha_orcamentoodonto),
    url(r'^item_orcamento_nutri/(?P<nr_item>\d+)/$', detalha_orcamento_nutri),
    url(r'^item_orcamento_psico/(?P<nr_item>\d+)/$', detalha_orcamento_psico),
    url(r'^item_atendimento_avulso/(?P<nr_item>\d+)/$', detalha_atendimento_avulso),
    url(r'^item_recebimento_plano/(?P<nr_item>\d+)/$', detalha_recebimento_plano),
    url(r'^item_recebimento_plano_nutri/(?P<nr_item>\d+)/$', detalha_recebimento_plano_nutri),
    url(r'^item_recebimento_plano_psico/(?P<nr_item>\d+)/$', detalha_recebimento_plano_Psico),
    url(r'^item_contrato_odonto/(?P<nr_item>\d+)/$', detalha_contrato_odonto),
    url(r'^item_contrato_nutri/(?P<nr_item>\d+)/$', detalha_contrato_nutri),
    url(r'^item_contrato_psico/(?P<nr_item>\d+)/$', detalha_contrato_psico),
    url(r'^item_relatorio_exame_odonto/(?P<nr_item>\d+)/$', detalha_relatorio_exame_odonto),
    url(r'^item_relatorio_exame_psico/(?P<nr_item>\d+)/$', detalha_relatorio_exame_psico),
    url(r'^item_relatorio_exame_nutri/(?P<nr_item>\d+)/$', detalha_relatorio_exame_nutri),
    url(r'^item_agendamento_plano_odonto/(?P<nr_item>\d+)/$', detalha_agendamento_plano_odonto),
    url(r'^item_agendamento_plano_nutri/(?P<nr_item>\d+)/$', detalha_agendamento_plano_nutri),
    url(r'^item_agendamento_plano_psico/(?P<nr_item>\d+)/$', detalha_agendamento_plano_psico),

    #---------- edita -------------------------#

    url(r'^edita_profissional/(?P<nr_item>\d+)/$',edita_profissional),
    url(r'^edita_funcionario/(?P<nr_item>\d+)/$',edita_funcionario),
    url(r'^edita_fornecedor/(?P<nr_item>\d+)/$',edita_fornecedor),
    url(r'^edita_cliente/(?P<nr_item>\d+)/$',edita_cliente),
    url(r'^edita_dentes/(?P<nr_item>\d+)/$',edita_dentes),
    url(r'^edita_orcamento_odonto/(?P<nr_item>\d+)/$',edita_orcamentoodonto),
    url(r'^edita_orcamento_nutri/(?P<nr_item>\d+)/$',edita_orcamento_nutri),
    url(r'^edita_orcamento_psico/(?P<nr_item>\d+)/$',edita_orcamento_psico),
    url(r'^edita_atendimento_avulso/(?P<nr_item>\d+)/$',edita_atendiemento_avulso),
    url(r'^edita_recebimento_plano/(?P<nr_item>\d+)/$',edita_recebimento_plano),
    url(r'^edita_recebimento_plano_nutri/(?P<nr_item>\d+)/$',edita_recebimento_plano_nutri),
    url(r'^edita_recebimento_plano_psico/(?P<nr_item>\d+)/$',edita_recebimento_plano_Psico),
    url(r'^edita_contrato_odonto/(?P<nr_item>\d+)/$',edita_contrato_odonto),
    url(r'^edita_contrato_nutri/(?P<nr_item>\d+)/$',edita_contrato_nutri),
    url(r'^edita_contrato_psico/(?P<nr_item>\d+)/$',edita_contrato_psico),
    url(r'^edita_relatorio_exame_odonto/(?P<nr_item>\d+)/$',edita_relatorio_exame_odonto),
    url(r'^edita_relatorio_exame_psico/(?P<nr_item>\d+)/$',edita_relatorio_exame_psico),
    url(r'^edita_relatorio_exame_nutri/(?P<nr_item>\d+)/$',edita_relatorio_exame_nutri),
    url(r'^edita_agendamento_plano_odonto/(?P<nr_item>\d+)/$',edita_agendamento_plano_odonto),
    url(r'^edita_agendamento_plano_nutri/(?P<nr_item>\d+)/$',edita_agendamento_plano_nutri),
    url(r'^edita_agendamento_plano_psico/(?P<nr_item>\d+)/$',edita_agendamento_plano_psico),

    url(r'^mapa_odonto/$', mapa_atendimento_odonto),
    url(r'^registrar/$', registrar),
    url(r'^usuarios/$', lista_usuarios),
    url(r'^edita_usuarios/(?P<nr>\d+)/$', edita_usuario),

    # url(r'^chat/', include('chatrooms.urls')),

    url(r'^campanha_venda/$', camapanha_venda),
    url(r'^cria_campanha/$', campanha),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
