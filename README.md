# Tutorial de Pytest

Este repositório contém um exemplo prático de como utilizar o Pytest, um framework de testes para Python que torna fácil escrever testes simples e escaláveis.

## O que é o Pytest?

Pytest é um framework de teste que permite escrever testes de forma simples e poderosa. Ele facilita a escrita de testes pequenos, mas escaláveis, e pode ser usado para todos os tipos de testes: unitários, funcionais, de integração, etc.

## Instalação

Para instalar o Pytest, basta executar:

```bash
pip install pytest
```

## Estrutura Básica de um Teste

No Pytest, os testes são funções Python que começam com o prefixo `test_`. Aqui está um exemplo simples:

```python
def test_exemplo():
    assert 1 + 1 == 2
```

## Executando Testes

Para executar todos os testes:

```bash
pytest
```

Para executar um arquivo de teste específico:

```bash
pytest test_arquivo.py
```

Para executar um teste específico:

```bash
pytest test_arquivo.py::test_funcao
```

## Marcadores (Markers)

Os marcadores permitem categorizar testes e executá-los seletivamente. Neste projeto, usamos marcadores para categorizar testes por funcionalidade.

### Definindo Marcadores

Os marcadores são definidos no arquivo `pytest.ini`:

```ini
[pytest]
addopts = --strict-markers
markers =
    faturamento
    lucro
```

### Usando Marcadores

Para marcar um teste:

```python
@pytest.mark.faturamento
def test_calcular_faturamento():
    assert calcular_faturamento() > 0
```

Para executar testes com um marcador específico:

```bash
pytest -m faturamento
```

## Fixtures

Fixtures são funções que fornecem dados ou estado para os testes. Elas são usadas para configurar pré-condições para os testes.

### Definindo uma Fixture

```python
@pytest.fixture()
def cotacao_dolar():
    return 5.99
```

### Usando uma Fixture

```python
def test_calcular_custo(cotacao_dolar):
    assert calcular_custo(cotacao_dolar) > 0
```

## Asserções (Assertions)

As asserções verificam se o resultado do teste é o esperado. O Pytest fornece mensagens de erro detalhadas quando as asserções falham.

```python
assert calcular_faturamento() > 0
assert type(calcular_faturamento()) == int
assert calcular_lucro(faturamento, 500) > 0
```

## Opções de Linha de Comando

O Pytest oferece várias opções de linha de comando úteis:

- `-v` ou `--verbose`: Mostra informações detalhadas sobre os testes
- `-x` ou `--exitfirst`: Para a execução após o primeiro teste falhar
- `--maxfail=n`: Para a execução após n falhas
- `-k "expressão"`: Executa testes que correspondem à expressão
- `-m "marcador"`: Executa testes com o marcador especificado

## Exemplos Práticos deste Projeto

### Teste de Faturamento

```python
@pytest.mark.faturamento
def test_calcular_faturamento():
    assert calcular_faturamento() > 0
```

Este teste verifica se a função `calcular_faturamento()` retorna um valor maior que zero.

### Teste de Lucro

```python
@pytest.mark.lucro
def test_calcular_lucro():
    faturamento = calcular_faturamento()
    assert calcular_lucro(faturamento, 500) > 0
```

Este teste verifica se a função `calcular_lucro()` retorna um valor maior que zero quando chamada com o faturamento calculado e um custo de 500.

### Teste com Fixture

```python
@pytest.fixture()
def cotacao_dolar():
    return 5.99

def test_calcular_custo(cotacao_dolar):
    assert calcular_custo(cotacao_dolar) > 0
```

Este teste usa uma fixture para fornecer a cotação do dólar e verifica se a função `calcular_custo()` retorna um valor maior que zero.

## Conclusão

O Pytest é uma ferramenta poderosa e flexível para testes em Python. Com sua sintaxe simples e recursos avançados, ele torna o processo de teste mais eficiente e agradável.

Para mais informações, consulte a [documentação oficial do Pytest](https://docs.pytest.org/).
