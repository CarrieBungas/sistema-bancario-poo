# sistema-bancario-poo

Sistema Bancário Orientado a Objetos – Sprint 6
Sobre o projeto

Este projeto foi desenvolvido em Python como parte do Desafio Sprint 6.

O objetivo é desenvolver um sistema bancário utilizando os principais conceitos de Programação Orientada a Objetos (POO), incluindo classes, objetos, encapsulamento, herança, polimorfismo e abstração.

Tecnologias utilizadas
Python 3
Programação Orientada a Objetos
Git e GitHub
Estrutura de classes

O sistema possui cinco classes:

Cliente: representa os clientes do banco.
Conta: classe abstrata que define os comportamentos básicos de uma conta.
ContaCorrente: representa uma conta corrente.
ContaPoupanca: representa uma conta poupança.
Banco: gerencia os clientes e as contas.
Diagrama de classes
mermaid
classDiagram
    class Cliente {
        -nome
        -email
        +__init__()
        +__str__()
    }

    class Conta {
        <<abstract>>
        -numero
        -saldo
        -cliente
        +depositar()
        +sacar()
        +calcular_rendimento()*
    }

    class ContaCorrente {
        -taxa
        +calcular_rendimento()
        +sacar()
    }

    class ContaPoupanca {
        -rendimento
        +calcular_rendimento()
    }

    class Banco {
        -nome
        -clientes
        -contas
        +adicionar_cliente()
        +adicionar_conta()
        +listar_contas()
    }

    Conta <|-- ContaCorrente
    Conta <|-- ContaPoupanca
    Cliente "1" <-- "1..*" Conta
    Banco o-- Cliente
    Banco o-- Conta

Conceitos de POO aplicados
1. Abstração

A classe Conta utiliza ABC e @abstractmethod para definir um contrato que deve ser implementado pelas classes filhas.

2. Encapsulamento

Foram utilizadas propriedades com @property e setters para proteger os atributos e validar os dados.

Exemplos:

Impedir saldo negativo.
Validar o número da conta.
Validar o e-mail do cliente.
Impedir taxas e rendimentos negativos.
3. Herança

As classes ContaCorrente e ContaPoupanca herdam da classe Conta.

Foi utilizado super().init() para reaproveitar o construtor da classe mãe.

4. Polimorfismo

O método calcular_rendimento() possui implementações diferentes nas classes ContaCorrente e ContaPoupanca.

Assim, cada tipo de conta responde de maneira diferente à mesma chamada.

5. Composição

A classe Banco gerencia objetos Cliente e Conta.

Essa abordagem permite organizar os elementos do sistema sem criar uma hierarquia de herança desnecessária.

Métodos especiais
Foram implementados:

init: inicialização dos objetos.
str: representação amigável.
repr: representação técnica.
eq: comparação entre contas.
Testes realizados

O arquivo main.py demonstra:

Criação de 10 clientes e 10 contas.
Operações de depósito e saque.
Cálculo de rendimento.
Polimorfismo entre contas correntes e poupanças.
Tratamento de exceções com try/except.
Validação de dados inválidos.
Como executar
Clone o repositório:
bash
git clone URL_DO_SEU_REPOSITORIO

Entre na pasta:
bash
cd sistema-bancario-poo

Execute o projeto:
bash
python main.py
