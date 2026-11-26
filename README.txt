==================================================
              SISTEMA SMARTSTOCK - A2
==================================================
Disciplina: Estruturas de Dados (Unidade IV)
Curso: Análise e Desenvolvimento de Sistemas (ADS)
Instituição: Faculdade Municipal de Palhoça (FMP)
Data de Entrega: 19/11/2026

INTEGRANTES DA EQUIPE:
- Daniel Lindoso, Vitor Vieira, Igor Sebastião

LINGUAGEM E TECNOLOGIAS UTILIZADAS:
- Python 3.10+
- Módulo 'copy' (para duplicar estruturas nos experimentos)
- Módulo 'time' (para instrumentação complementar)

INSTRUÇÕES DE EXECUÇÃO:
1. Certifique-se de ter o Python 3 instalado no sistema.
2. Abra o terminal de comando na pasta 'codigo/'.
3. Execute o comando:
   python main.py
4. Utilize o menu interativo via terminal digitando as opções de 0 a 10.

DIVISÃO DE RESPONSABILIDADES:
- Equipe: Implementação da estrutura Produto e carga inicial (20 produtos),
  desenvolvimento dos algoritmos de busca (Sequencial e Binária),
  desenvolvimento dos algoritmos de ordenação (Bubble, Selection, Insertion, Merge, Quick),
  instrumentação de contadores (comparações, trocas, deslocamentos),
  módulo de experimentos e geração do relatório técnico e traces manuais.

FUNCIONALIDADES IMPLEMENTADAS:
- Cadastro e Listagem de Produtos
- Busca Sequencial (composição de posição, contador de comparações e tratamento de ausência)
- Busca Binária (com garantia de pré-ordenação por código)
- Bubble Sort (Ordenação por Preço)
- Selection Sort (Ordenação por Estoque)
- Insertion Sort (Ordenação por Nome)
- MergeSort (Ordenação por Quantidade Vendida)
- QuickSort (Ordenação por Código)
- Módulo de Comparação Automatizada (Opção 10 do menu): executa os 5 algoritmos contra
  3 arranjos de dados (Aleatória, Quase Ordenada e Inversa) e imprime a tabela de resultados.

LIMITAÇÕES CONHECIDAS:
- O QuickSort utiliza o último elemento como pivô simples. Para entradas perfeitamente
  inversas, atinge a complexidade de pior caso O(n²).
- A persistência dos dados é mantida apenas em memória durante a execução.
