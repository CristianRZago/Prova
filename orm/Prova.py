from sqlalchemy import create_engine, Column, Integer, String, inspect, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

URL = "mysql+mysqlconnector://root:123456@localhost:3306/ORM"

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)


class Marca(Base):
    __tablename__ = "Marca"
    id = Column(Integer, primary_key=True)
    Nome = Column(String(150), nullable=False)
    Endereco = Column(String(150), nullable=False)


class Loja(Base):
    __tablename__ = "Loja"
    id = Column(Integer, primary_key=True)
    Nome = Column(String(150), nullable=False)
    Endereco = Column(String(150), nullable=False)


class Estoque_Produto(Base):
    __tablename__ = "Estoque_Produto"
    id = Column(Integer, primary_key=True)
    Marca_id = Column(Integer, nullable=False)
    Preco = Column(Float, nullable=False)
    Nome = Column(String(150), nullable=False)
    Quantidade = Column(Integer, nullable=False)


class Prod_Loja_Desconto(Base):
    __tablename__ = "Prod_Loja_Desconto"
    id = Column(Integer, primary_key=True)
    Loja_id = Column(Integer, nullable=False)
    Estoque_Produto_id = Column(Integer, nullable=False)
    NovoPreco = Column(Float, nullable=False)
    Desconto = Column(Float, nullable=False)


class Calculadora(Base):
    __tablename__ = "Calculadora"
    id = Column(Integer, primary_key=True)
    Pessoa_id = Column(Integer, nullable=False)
    Prod_Loja_Desconto_id = Column(Integer, nullable=False)
    Nome = Column(String(150), nullable=False)
    DiaCompra = Column(Integer, nullable=False)


class Historico(Base):
    __tablename__ = "Historico"
    id_Historico = Column(Integer, primary_key=True)
    Calculadora_id = Column(Integer, nullable=False)
    Numero1 = Column(Float, nullable=False)
    Numero2 = Column(Float, nullable=False)
    Funcao = Column(String(150), nullable=False)
    Resultado = Column(Float, nullable=False)


def main():
    print('criação da marca')
    marca1 = input("Digite o nome da marca: ")
    MarcaEndereco = input("Digite o endereco da marca (somente rua): ")

    print('\n\nAqui temos a criação do produto da marca criada anteriormente')
    nome1 = input("De um nome a um produto: ")
    preco1 = float(input("Preco: "))
    quantidade1 = int(input("Quantidade: "))

    print('\n\nCriação da loja')
    Loja1 = input("Digite o nome da loja: ")
    LojaEndereco = input("Digite o endereco da loja (somente a rua): ")

    print('\n\nAtrelando o produto criado anteriormente com a loja criada agora')
    novoPreco1 = float(input("De o novo preco que a loja cobrara: "))
    desconto = input("Desconto? (sim ou nao)")
    if desconto == "sim":
        global desconto1
        desconto1 = float(input("Desconto: "))
        resultadoDesc = novoPreco1 - desconto1
        print(f"O preco final do produto eh: {resultadoDesc}")
    else:
        desconto1 = 0
        resultadoDesc = novoPreco1
        print(f"O produto nao teve desconto")

    QuantidadeLoja1 = int(input("Digite a quantidade que a loja possui: "))

    print('\n\nAqui criamos a pessoa e atrelamos ela a uma calculadora (e damos nome a ela :D) ')
    Pessoa1 = input("De um nome a pessoa: ")

    DiaCompra1 = int(input("Dia da compra da calculadora(apenas dia): "))
    NomeCalc = input("De um nome a sua calculadora: ")

    print(f'a(o) {NomeCalc} pertence ao(a) {Pessoa1}')

    print('\n\nAqui nós iremos ultilizar a calculadora')
    Funcao = input("Digite a funcao que voce quer (com 2 numeros, podendo ser: soma, subtracao ou multiplicacao): ")
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    if Funcao == "soma":
        global resultado
        resultado = num1 + num2
    elif Funcao == "subtracao":
        resultado = num1 - num2
    elif Funcao == "multiplicacao":
        resultado = num1 * num2
    else:
        print("Comando invalido, realizando soma")
        resultado = num1 + num2

    print(resultado)

    engine = create_engine(url=URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        pessoa = Pessoa(nome=Pessoa1)
        session.add(pessoa)

        marcaf = Marca(Nome=marca1, Endereco=MarcaEndereco)
        session.add(marcaf)

        lojaf = Loja(Nome=Loja1, Endereco=LojaEndereco)
        session.add(lojaf)

        estoque_produtof = Estoque_Produto(Marca_id='1', Preco=preco1, Nome=nome1, Quantidade=quantidade1)
        session.add(estoque_produtof)

        prod_Loja_descontof = Prod_Loja_Desconto(Loja_id='1', Estoque_Produto_id='1', NovoPreco=novoPreco1,
                                                 Desconto=desconto1)
        session.add(prod_Loja_descontof)

        calculadoraf = Calculadora(Pessoa_id='1', Prod_Loja_Desconto_id=1, Nome=NomeCalc, DiaCompra=DiaCompra1)
        session.add(calculadoraf)

        historicof = Historico(Calculadora_id='1', Numero1=num1, Numero2=num2, Funcao=Funcao, Resultado=resultado)
        session.add(historicof)


if __name__ == "__main__":
    main()
