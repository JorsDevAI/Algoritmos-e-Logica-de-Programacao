# Controle de Produção e Qualidade de Peças - Sistema em Python

## Sobre o Projeto

Este sistema foi desenvolvido como protótipo para automação do controle de **produção** e **qualidade** de peças em uma linha de montagem industrial. Inspirado em uma demanda real do setor, seu objetivo é diminuir atrasos, evitar erros de conferência e reduzir custos causados por inspeções manuais.

A automação é feita integralmente em **Python** e simula toda a lógica de cadastro, avaliação, alocação e relatório das peças fabricadas.

---

## Funcionalidades

O sistema apresenta um menu interativo, permitindo as seguintes operações:

- **Cadastro de Peça:** Recebe os dados das peças produzidas — ID, peso, cor e comprimento.
- **Avaliação da Qualidade:** Aprova ou reprova automaticamente cada peça segundo critérios rígidos:
  - Peso entre **95g e 105g**
  - Cor **azul** ou **verde**
  - Comprimento entre **10cm e 20cm**
- **Armazenamento Inteligente:** Peças aprovadas são alocadas automaticamente em caixas de capacidade limitada (**10 peças cada**). Ao atingir o limite, a caixa é **fechada** e uma nova é iniciada.
- **Listagens e Remoção:** Permite consultar peças aprovadas/reprovadas, remover peças cadastradas, e exibir as caixas fechadas.
- **Relatórios Consolidados:** Gera relatório final com total de peças aprovadas, total reprovadas (com motivos) e quantidade de caixas utilizadas.

---

## Estrutura do Código

- **Função `avaliar_peca(peso, cor, comprimento)`**
  Analisa os critérios de qualidade. Retorna status e motivos em caso de reprovação.

- **Banco de Dados em Memória**
  As peças e caixas são armazenadas em listas e dicionários locais (não utiliza banco externo).

- **Função `alocar_em_caixa(id_peca)`**
  Aloca a peça aprovada na caixa corrente; se atingir 10 peças, fecha e inicia uma nova caixa.

- **Função `cadastrar_peca()`**
  Controla o fluxo de cadastro, valida dados e chama a avaliação.

- **Listagem e Remoção**
  - `listar_pecas()`: lista todas peças aprovadas e reprovadas.
  - `remover_peca()`: remove peça pelo ID, atualizando caixas correspondentes.

- **Funções de Relatório**
  - `listar_caixas_fechadas()`
  - `gerar_relatorio()`: mostra estatísticas gerais do período (produção, qualidade e logística).

- **Interface via Menu**
  A função `main()` exibe o menu e direciona as operações conforme escolha do usuário.

---

## Como Executar

1. Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado.
2. Salve o código principal como, por exemplo, `controle_pecas.py`.
3. No terminal, execute:

   ```
   python controle_pecas.py
   ```

4. Siga o menu interativo para cadastrar peças, listar, consultar caixas e gerar relatórios.

---

## Exemplo de Fluxo

- Ao cadastrar uma nova peça, informe ID, peso, cor e comprimento.
- O sistema avalia automaticamente e informa se está **Aprovada** (alocando-a em uma caixa) ou **Reprovada** (mostrando motivo).
- Peças aprovadas vão para caixas numeradas. Ao atingir 10 peças a caixa é fechada.
- Relatórios mostram a produção consolidada, qualidade, causas de reprovação e uso das caixas.

---

## Observações e Possíveis Extensões

- **Prototípico (didático):** O armazenamento é feito em memória para fins de demonstração. Para produção, sugere-se uso de banco de dados.
- **Extensões:** Pode ser adaptado para integração com sistemas industriais, interface gráfica ou API.
- **Critérios de Qualidade:** Os parâmetros podem ser facilmente ajustados conforme política da fábrica.

---

## Autor

Desenvolvido por [JorsDevAI] para fins de automação e otimização industrial.

---
