from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    emai = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome - self.telefone - self.EmailField

class Endereço(models.Model):
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name = 'enredecos')
    rua = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)

class FormaPagamento(models.Model):
    tipo = models.CharField(max_length=50)

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)

class Item(models.Model):
    #vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name = 'itens')
    nome  = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    categoria = models.CharField(max_length=50)
    quantidade = models.IntegerField()

class Pedido(models.Model):
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name = 'pedidos')
    #endereco = models.ForeignKey(Endereço on_delete=models.CASCADE, related_name = 'pedidos_entregues')
    #forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, related_name = 'pedidos')
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

class ItemPedido(models.Model):
    #pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name = 'itens')
    #item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'itens_pedido')
    quantidade = models.IntegerField()
