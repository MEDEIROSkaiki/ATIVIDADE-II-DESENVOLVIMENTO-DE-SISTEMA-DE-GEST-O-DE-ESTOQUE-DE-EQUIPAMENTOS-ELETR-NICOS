from django.db import models

# Modelo para a tabela Produto_Cadastro
class Produto_Cadastro(models.Model):
    # PK: ID_Produto (Geralmente, o Django cria um 'id' auto-incremento como PK por padrão)
    # Se você quiser que ID_Produto seja a PK primária, descomente a linha abaixo e comente a próxima linha.
    # id = models.AutoField(primary_key=True) # Descomente se quiser ID_Produto como PK
    
    # Mantendo a convenção do Django para PKs
    id_produto = models.AutoField(primary_key=True) # Renomeei para seguir a convenção Python/Django (snake_case)
    
    nome_produto = models.CharField(max_length=255)
    limite_produto = models.IntegerField()
    qtd_atual = models.IntegerField()

    class Meta:
        # Nome da tabela no banco de dados (opcional, mas bom para corresponder ao DER)
        db_table = 'Produto_Cadastro'

    def __str__(self):
        return self.nome_produto

# Modelo para a tabela Usuario
class Usuario(models.Model):
    # PK: ID_Usuario
    id_usuario = models.AutoField(primary_key=True)
    
    nome_usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128) # Armazenar senhas de forma segura (usar hash)

    class Meta:
        db_table = 'Usuario'

    def __str__(self):
        return self.nome_usuario

# Modelo para a tabela Movimentacao
class Movimentacao(models.Model):
    # PK: ID_Movimentacao
    id_movimentacao = models.AutoField(primary_key=True)
    
    # FK: ID_Produto FK -> Relacionamento com Produto_Cadastro
    # O Django usa ForeignKey para chaves estrangeiras
    id_produto_fk = models.ForeignKey(
        Produto_Cadastro, 
        on_delete=models.CASCADE,  # Define a ação quando o produto é deletado (CASCADE é comum)
        db_column='ID_Produto_FK'  # Nome da coluna no banco de dados
    )
    
    # FK: ID_Usuario FK -> Relacionamento com Usuario
    id_usuario_fk = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        db_column='ID_Usuario_FK'
    )
    
    data_movimentacao = models.DateTimeField() # Geralmente, data e hora
    entrada_saida = models.CharField(max_length=10, choices=[('ENTRADA', 'Entrada'), ('SAIDA', 'Saída')]) # Para controlar o tipo de movimento
    qtd_movimentacao = models.IntegerField()

    class Meta:
        db_table = 'Movimentacao'

    def __str__(self):
        return f"Movimento {self.id_movimentacao} - Produto: {self.id_produto_fk.nome_produto}"