# 🧮 Calculadora em Python

Projeto 01 da minha trilha de aprendizado — uma calculadora de linha de comando com menu de operações, validação de erros e loop de uso contínuo.

## 📋 Sobre o projeto

Este foi meu primeiro projeto prático em Python, construído em camadas: comecei com uma versão simples (soma, subtração, multiplicação e divisão) e fui evoluindo o código conforme aprendia novos conceitos, até chegar numa versão mais completa e robusta.

A calculadora apresenta um menu com 7 operações, pede os números ao usuário, calcula o resultado e pergunta se a pessoa quer fazer outro cálculo — repetindo até ela decidir parar.

## 🎯 Funcionalidades

- Soma, subtração, multiplicação e divisão
- Divisão inteira (`//`)
- Módulo / resto da divisão (`%`)
- Potenciação (`**`)
- Validação de entrada: se o usuário digitar algo que não é um número, o programa avisa e pede novamente, sem travar
- Tratamento de divisão por zero em todas as operações que envolvem divisão
- Loop contínuo: o usuário pode fazer quantos cálculos quiser antes de encerrar

## 🚀 Como executar

1. Certifique-se de ter o Python 3 instalado
2. Baixe ou clone este repositório
3. No terminal, execute:

```bash
python calculadora.py
```

4. Escolha uma operação pelo número do menu e siga as instruções na tela

## 🖥️ Exemplo de uso

```
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Divisão inteira
6 - Módulo / Resto
7 - Potenciação
Escola uma opção: 1
Digite um número: 5
Digite o segundo número: 3
8.0
Deseja fazer outro calculo? [S/N]: n
```

Se o usuário digitar algo que não é um número, o programa avisa e pede de novo, sem travar:

```
Digite um número: abc
Isso não é um número válido! Tente de novo.
Digite um número: 5
```

## 🎯 Conceitos aplicados

- Estruturas condicionais (`if` / `elif` / `else`)
- Loops (`while True`) e loops aninhados (um `while` dentro de outro)
- Controle de fluxo com `break`
- Tratamento de exceções (`try` / `except`) para dois tipos de erro: `ValueError` (entrada inválida) e `ZeroDivisionError` (divisão por zero)
- Conversão de tipos (`float()`)

## 💡 O que aprendi

- A diferença entre um loop simples (`while` com condição) e um loop `while True` controlado por `break`
- Como usar loops aninhados para resolver problemas onde uma parte do código precisa "repetir sozinha" antes de o resto continuar (nesse caso, validar os números antes de seguir para o cálculo)
- Como identificar e corrigir lógica invertida em uma condição (`==` vs `!=`)
- A importância de tratar diferentes tipos de erro separadamente (`ValueError` para entrada inválida, `ZeroDivisionError` para divisão por zero)

## 🔜 Próximos passos

Meu próximo projeto da trilha será um **Gerador de Senhas**, avançando para conceitos de segurança e aleatoriedade.

---

Projeto parte da minha trilha de estudos em Backend e Cybersecurity. Veja mais em [gabyvncx/gabyvncx](https://github.com/gabyvncx/gabyvncx).