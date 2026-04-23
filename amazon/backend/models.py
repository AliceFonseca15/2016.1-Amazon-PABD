from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.telefone} - {self.EmailField}'

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True,default='sem-email@gmail.com')
    cpf_cnpj = models.CharField(max_length=18,unique = True,default='XXX.XXX.XXX -XX')
    telefone = models.CharField(max_length=15)
    avaliacao = models.DecimalField(max_digits=3,decimal_places=2,default=5.00)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'vendedores'
        ordering = ['nome']
    def __str__(self):
        return f'{self.nome} ({self.cpf_cnpj})'


class Produto(models.Model):
    CATEGORIA_CHOICES = [
        ('eletronicos', 'Eletrônicos'),
        ('roupas', 'Roupas e Acessórios'),
        ('livros', 'Livros'),
        ('alimentos', 'Alimentos'),
        ('outros', 'Outros'),
    ]

    #vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name = 'itens')
    nome  = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    categoria = models.CharField(max_length=50)

    class Meta:
        db_table = 'produtos'
        ordering = ['nome']

    def __str__(self):
        return f'[{self.nome} — R$ {self.preco}'


#class Endereço(models.Model):
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name = 'enredecos')
    #rua = models.CharField(max_length=255)
    #cidade = models.CharField(max_length=100)
    #estado = models.CharField(max_length=50)
    #cep = models.CharField(max_length=10)

#class FormaPagamento(models.Model):
    #tipo = models.CharField(max_length=50)

    
#class Pedido(models.Model):
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name = 'pedidos')
    #endereco = models.ForeignKey(Endereço on_delete=models.CASCADE, related_name = 'pedidos_entregues')
    #forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, related_name = 'pedidos')
    #data = models.DateField()
    #valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    #status = models.CharField(max_length=50)

#class ItemPedido(models.Model):
    #pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name = 'itens')
    #item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'itens_pedido')
    #quantidade = models.IntegerField()
