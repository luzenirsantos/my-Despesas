from django.db import models
from django.forms import ModelForm


TIPO_DESPESA = (
    ('Alimentação','Alimentação'),
    ('Educação','Educação'),
    ('Lazer','Lazer'),
    ('Remédio','Remédio'),
    ('Roupa','Roupa'),
    ('Transporte','Transporte'),
    ('Outro','Outro'),
)
TIPO_PAGAMENTO = (
	('Dinheiro','Dinheiro'),
    ('Cartão de crédito','Cartão de crédito'),
    ('Cartão de débito','Cartão de débito'),
    ('Cartão de crediário','Cartão de crediário'),
    ('Cheque','Cheque'),
)

class Despesa(models.Model):
    data_criacao = models.DateField('Data da criação')
    tipo = models.CharField('Tipo de Despesa', max_length=15, choices=TIPO_DESPESA)
    descricao = models.TextField('Descrição')
    vencimento = models.DateTimeField('Vencimento')
    forma_pagamento = models.CharField('Forma de pagamento', max_length=20, choices=TIPO_PAGAMENTO)
    pago = models.BooleanField()
    class Meta:
        ordering = ('vencimento', 'forma_pagamento')

    def __str__(self):
        return self.descricao 

