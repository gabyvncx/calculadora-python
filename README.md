# 🧮 Calculadora em Python

Projeto 01 da minha trilha de aprendizado — uma calculadora de linha de comando com menu de operações, validação de erros e loop de uso contínuo.

## 📋 Sobre o projeto

Este foi meu primeiro projeto prático em Python, construído em etapas: comecei com uma versão simples e fui evoluindo o código conforme aprendia novos conceitos, até chegar a uma versão mais completa.

A calculadora apresenta um menu com 7 operações, pede os números ao usuário, calcula o resultado e pergunta se a pessoa quer fazer outro cálculo, repetindo o processo até decidir parar.

## 🎯 Funcionalidades

* Soma, subtração, multiplicação e divisão
* Divisão inteira (`//`)
* Módulo / resto da divisão (`%`)
* Potenciação (`**`)
* Validação de entrada: se o usuário digitar algo que não é um número, o programa avisa e pede novamente
* Tratamento de divisão por zero nas operações de divisão
* Loop contínuo: o usuário pode fazer quantos cálculos quiser antes de encerrar

## 🚀 Como executar

1. Certifique-se de ter o Python 3 instalado
2. Baixe ou clone este repositório
3. No terminal, execute:

```bash
python calculadora.py
```

4. Escolha uma operação pelo número do menu e siga as instruções na tela.

## 🖥️ Exemplo de uso

```text
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Divisão inteira
6 - Módulo / Resto
7 - Potenciação
Escolha uma opção: 1
Digite um número: 5
Digite o segundo número: 3
8.0
Desejá fazer outro calculo? [S/N]: N
```

Se o usuário digitar algo que não é um número, o programa avisa e pede novamente:

```text
Digite um número: abc
Isso não é um número válido! Tente de novo.
Digite um número: 5
```

## 📚 Conceitos aplicados

* Estruturas condicionais (`if` / `elif` / `else`)
* Loops (`while True`) e loops aninhados
* Controle de fluxo com `break`
* Tratamento de exceções (`try` / `except`)
* `ValueError` para entradas inválidas
* `ZeroDivisionError` para divisão por zero
* Conversão de tipos com `float()`
* Operadores matemáticos

## 💡 O que aprendi

* A diferença entre um loop simples e um `while True` controlado por `break`
* Como usar loops aninhados para validar informações antes de continuar o programa
* Como tratar diferentes tipos de erro separadamente
* Como usar `try` e `except` para evitar que o programa seja encerrado por uma entrada inválida
* Como construir uma calculadora aos poucos, adicionando novas funcionalidades conforme aprendo novos conceitos

## 🔜 Próximo projeto

Meu próximo projeto da trilha será um **Gerador de Senhas**, avançando para conceitos de segurança e aleatoriedade.

---

Projeto parte da minha trilha de estudos em **Backend e Cybersecurity**.

[← Voltar para meu perfil no GitHub](https://github.com/gabyvncx)
