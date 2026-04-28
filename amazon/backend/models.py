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

   
    def __str__(self):
        return f'{self.nome} ({self.cpf_cnpj})'

class PerfilVendedor(models.Model):
    vendedor = models.OneToOneField(
        Vendedor,
        on_delete=models.CASCADE,
        related_name = 'perfil',
        primary_key = True
    )
    razao_social = models.CharField(max_length=150,blank=True)
    inscricao_estadual = models.CharField(max_length=20,blank=True)
    banco = models.CharField(max_length=50,blank=True) 
    agencia = models.CharField(max_length=10,blank=True) 
    conta = models.CharField(max_length=20,blank=True) 
    chave_pix =  models.CharField(max_length=100,blank=True) 

    

    def __str__(self):
        return f'Perfil de {self.vendedor.nome}'
 
class Produto(models.Model):
    CATEGORIA_CHOICES = [
        ('eletronicos', 'Eletrônicos'),
        ('roupas', 'Roupas e Acessórios'),
        ('livros', 'Livros'),
        ('alimentos', 'Alimentos'),
        ('outros', 'Outros'),
    ]

    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    categoria = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True,blank = True)
    atualizado_em = models.DateTimeField(auto_now=True) 
  
    def __str__(self):
        return f'[{self.nome} — R$ {self.preco}'
  
class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name = 'pedidos')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente'
    )
    data_pedido = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True)



    def __str__(self):
        return f'Pedido #{self.id} — {self.cliente.nome}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido, 
        on_delete=models.CASCADE, 
        related_name = 'itens'
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT,
        related_name = 'itens_vendidos'
    )
    quantidade = models.PositiveIntegerField(default=1) 
    preco_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Preço congelado no momento da compra'
    )

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome}'

    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario

