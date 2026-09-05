# Agenda 6 — Desenvolvimento de Sistemas I

Este projeto foi desenvolvido como parte da **Agenda 6 da disciplina de Desenvolvimento de Sistemas I**, do **Curso Técnico em Desenvolvimento de Sistemas da ETEC**.

## Objetivo

O objetivo deste programa é praticar o uso de **estruturas condicionais em Python**, utilizando os comandos `if`, `elif` e `else` para tomar decisões de acordo com o valor informado pelo usuário.

O programa simula um sistema simples de descontos em uma compra. O usuário informa o valor total da compra e, a partir desse valor, o programa calcula automaticamente o percentual de desconto correspondente.

## Funcionamento

O programa solicita que o usuário digite o valor total de uma compra:

Depois disso, o programa verifica em qual faixa de preço a compra se encontra.

* Para compras com valor **menor que R$ 200,00**, é aplicado um desconto de **5%**.
* Para compras com valor **maior ou igual a R$ 200,00 e menor que R$ 300,00**, é aplicado um desconto de **10%**.
* Para compras com valor **maior ou igual a R$ 300,00**, é aplicado um desconto de **15%**.

O valor final é calculado subtraindo o percentual de desconto do valor original da compra.
