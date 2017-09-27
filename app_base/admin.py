from django.contrib import admin
from app_base.models import *
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Profissionais,SimpleHistoryAdmin)
admin.site.register(Cliente,SimpleHistoryAdmin)
admin.site.register(Funcionario,SimpleHistoryAdmin)
