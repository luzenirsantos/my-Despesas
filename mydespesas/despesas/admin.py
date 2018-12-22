from django.contrib import admin
from .models import Despesa
from django.utils.timezone import now
from django.utils.timezone import timedelta


class DespesaAdmin(admin.ModelAdmin):
	list_display = ('descricao', 'vencimento', 'forma_pagamento', 'pago', 'proximo_vencimento')
	list_filter = ('vencimento','pago')
	date_hierarchy = 'vencimento'
	
	def proximo_vencimento(self, obj):
		return obj.vencimento <= now() + timedelta(days=2)
	proximo_vencimento.short_description = 'Próximo vencimento?'
	proximo_vencimento.boolean = True
		

admin.site.register(Despesa, DespesaAdmin)
admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'Minhas Despesas' 

