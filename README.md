# Gerador de Sequência Numérica

Este programa exibe uma sequência numérica específica baseada em um valor de entrada, `N`. A sequência segue uma lógica onde cada número da série é apresentado em linhas organizadas, com potências e somas. O código lê um valor inteiro `N` e gera `N * 2` linhas de saída no formato adequado.

## Exemplo de Saída

Para uma entrada `N = 5`, a saída será:

```
1 1 1
1 2 2
2 4 8
2 5 9
3 9 27
3 10 28
4 16 64
4 17 65
5 25 125
5 26 126
```

## Lógica de Funcionamento

Para cada número `i` de 1 até `N`, são geradas duas linhas:

1. Primeira linha: contém `i`, `i²`, `i³`.
2. Segunda linha: contém `i`, `i² + 1`, `i³ + 1`.

### Entrada

- O programa lê um valor inteiro `N`, onde `1 < N < 1000`.

### Saída

- O programa imprime `N * 2` linhas, seguindo o formato demonstrado acima. Cada número da linha é separado por espaços e aparece na sequência correta.

## Como Executar o Código

1. Certifique-se de ter Python 3 instalado.
2. Execute o programa em um terminal ou ambiente Python.
3. Insira um valor para `N` conforme solicitado.

### Arquivo

O nome do arquivo para o código deve ser **`gerador_sequencia_numerica.py`**.

Execute com:

```bash
python gerador_sequencia_numerica.py
```

O programa exibirá as `N * 2` linhas de saída com os valores calculados.
