import copy
import time

# ==========================================
# 1. CLASSE PRODUTO E BASE INICIAL (20 ITENS)
# ==========================================
class Produto:
    def __init__(self, codigo, nome, categoria, preco, estoque, quantidade_vendida):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque
        self.quantidade_vendida = quantidade_vendida

    def __str__(self):
        return (f"[Cód: {self.codigo:03d}] {self.nome:<28} | Categoria: {self.categoria:<15} | "
                f"Preço: R$ {self.preco:>7.2f} | Estoque: {self.estoque:>3d} | Vendas: {self.quantidade_vendida:>3d}")


def get_base_inicial():
    """Retorna a base inicial com 20 produtos conforme requisito do projeto."""
    return [
        Produto(105, "Fone de Ouvido Bluetooth", "Eletrônicos", 199.90, 45, 120),
        Produto(102, "Mouse Sem Fio Ergonomico", "Periféricos", 89.90, 60, 210),
        Produto(118, "Teclado Mecanico RGB", "Periféricos", 250.00, 25, 95),
        Produto(101, "Monitor 24 Polegadas Full HD", "Monitores", 749.00, 15, 40),
        Produto(110, "Cadeira Gamer Ergonomica", "Móveis", 899.90, 10, 15),
        Produto(104, "Webcam 1080p Full HD", "Periféricos", 159.00, 30, 85),
        Produto(115, "Suporte para Notebook", "Acessórios", 45.00, 100, 310),
        Produto(108, "Hub USB-C 7 em 1", "Acessórios", 129.90, 50, 140),
        Produto(103, "Carregador Rapido 65W", "Acessórios", 99.00, 80, 250),
        Produto(112, "Cabo HDMI 2.1 2m", "Acessórios", 35.00, 150, 420),
        Produto(119, "Mesa Digitalizadora", "Periféricos", 320.00, 12, 30),
        Produto(107, "Microfone Condensador USB", "Áudio", 210.00, 20, 65),
        Produto(114, "Caixa de Som Bluetooth 20W", "Áudio", 179.90, 35, 110),
        Produto(106, "HD Externo 1TB", "Armazenamento", 280.00, 40, 90),
        Produto(120, "SSD NVMe 1TB", "Armazenamento", 420.00, 55, 180),
        Produto(111, "Pen Drive 64GB USB 3.0", "Armazenamento", 39.90, 200, 500),
        Produto(116, "Filtro de Linha 6 Tomadas", "Energia", 55.00, 70, 160),
        Produto(109, "Nobreak 600VA", "Energia", 450.00, 8, 12),
        Produto(113, "Roteador Wi-Fi 6", "Redes", 299.00, 22, 75),
        Produto(117, "Switch Gigabit 8 Portas", "Redes", 119.00, 18, 45),
    ]

# ==========================================
# 2. ALGORITMOS DE BUSCA (PARTE A)
# ==========================================
def busca_sequencial(lista, codigo_alvo):
    comparacoes = 0
    for idx, p in enumerate(lista):
        comparacoes += 1
        if p.codigo == codigo_alvo:
            return p, idx, comparacoes
    return None, -1, comparacoes

def busca_binaria(lista_ordenada, codigo_alvo):
    comparacoes = 0
    inicio = 0
    fim = len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista_ordenada[meio].codigo == codigo_alvo:
            return lista_ordenada[meio], meio, comparacoes
        elif lista_ordenada[meio].codigo < codigo_alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None, -1, comparacoes

# ==========================================
# 3. ALGORITMOS DE ORDENAÇÃO (PARTE B)
# ==========================================

# 3.1 Bubble Sort (Critério: Preço)
def bubble_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0
    deslocamentos = 0

    for i in range(n - 1):
        houve_troca = False
        for j in range(0, n - i - 1):
            comparacoes += 1
            if lista[j].preco > lista[j + 1].preco:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
                houve_troca = True
        if not houve_troca:
            break
    return comparacoes, trocas, deslocamentos

# 3.2 Selection Sort (Critério: Estoque)
def selection_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0
    deslocamentos = 0

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[j].estoque < lista[min_idx].estoque:
                min_idx = j
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            trocas += 1
    return comparacoes, trocas, deslocamentos

# 3.3 Insertion Sort (Critério: Nome)
def insertion_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0
    deslocamentos = 0

    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if lista[j].nome.lower() > chave.nome.lower():
                lista[j + 1] = lista[j]
                deslocamentos += 1
                j -= 1
            else:
                break
        lista[j + 1] = chave
    return comparacoes, trocas, deslocamentos

# 3.4 MergeSort (Critério: Quantidade Vendida)
def merge_sort(lista):
    comparacoes = 0
    trocas = 0
    deslocamentos = 0

    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        comp_esq, tr_esq, des_esq = merge_sort(esquerda)
        comp_dir, tr_dir, des_dir = merge_sort(direita)

        comparacoes += comp_esq + comp_dir
        trocas += tr_esq + tr_dir
        deslocamentos += des_esq + des_dir

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            comparacoes += 1
            if esquerda[i].quantidade_vendida <= direita[j].quantidade_vendida:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            deslocamentos += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
            deslocamentos += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
            deslocamentos += 1

    return comparacoes, trocas, deslocamentos

# 3.5 QuickSort (Critério: Código)
def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    comparacoes = 0
    trocas = 0
    deslocamentos = 0

    if inicio < fim:
        pivo_idx, comp_part, tr_part = _particionar(lista, inicio, fim)
        comparacoes += comp_part
        trocas += tr_part

        c1, t1, d1 = quick_sort(lista, inicio, pivo_idx - 1)
        c2, t2, d2 = quick_sort(lista, pivo_idx + 1, fim)

        comparacoes += c1 + c2
        trocas += t1 + t2
        deslocamentos += d1 + d2

    return comparacoes, trocas, deslocamentos

def _particionar(lista, inicio, fim):
    pivo = lista[fim].codigo
    i = inicio - 1
    comparacoes = 0
    trocas = 0

    for j in range(inicio, fim):
        comparacoes += 1
        if lista[j].codigo <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
            trocas += 1

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    trocas += 1
    return i + 1, comparacoes, trocas

# ==========================================
# 4. EXPERIMENTOS E TABELA DE RESULTADOS (PARTE C)
# ==========================================
def rodar_experimentos(base_original):
    base_aleatoria = copy.deepcopy(base_original)

    base_quase = copy.deepcopy(base_original)
    quick_sort(base_quase)
    base_quase[2], base_quase[17] = base_quase[17], base_quase[2]

    base_inversa = copy.deepcopy(base_original)
    quick_sort(base_inversa)
    base_inversa.reverse()

    cenarios = {
        "Aleatória": base_aleatoria,
        "Quase ordenada": base_quase,
        "Ordem inversa": base_inversa
    }

    algoritmos = [
        ("Bubble Sort (Preço)", bubble_sort),
        ("Selection Sort (Estoque)", selection_sort),
        ("Insertion Sort (Nome)", insertion_sort),
        ("MergeSort (Qtd. Vendida)", merge_sort),
        ("QuickSort (Código)", quick_sort)
    ]

    print("\n" + "="*85)
    print(f"{'TABELA DE RESULTADOS DOS EXPERIMENTOS':^85}")
    print("="*85)
    print(f"{'Algoritmo':<28} | {'Entrada':<15} | {'Comparações':<12} | {'Trocas':<8} | {'Deslocamentos':<13}")
    print("-" * 85)

    for nome_alg, func_alg in algoritmos:
        for nome_cenario, dados_cenario in cenarios.items():
            copia_dados = copy.deepcopy(dados_cenario)
            comp, trocas, desloc = func_alg(copia_dados)
            print(f"{nome_alg:<28} | {nome_cenario:<15} | {comp:<12} | {trocas:<8} | {desloc:<13}")
        print("-" * 85)

# ==========================================
# 5. MENU PRINCIPAL (INTERFACE)
# ==========================================
def menu():
    produtos = get_base_inicial()

    while True:
        print("\n========== SMARTSTOCK ==========")
        print("1- Cadastrar produto")
        print("2- Listar produtos")
        print("3- Busca sequencial por código")
        print("4- Busca binária por código")
        print("5- Ordenar por preço (Bubble Sort)")
        print("6- Ordenar por estoque (Selection Sort)")
        print("7- Ordenar por nome (Insertion Sort)")
        print("8- Ordenar por quantidade vendida (MergeSort)")
        print("9- Ordenar por código (QuickSort)")
        print("10- Comparar algoritmos (Experimentos)")
        print("0- Encerrar")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                cod = int(input("Código: "))
                nome = input("Nome: ")
                cat = input("Categoria: ")
                preco = float(input("Preço: R$ "))
                est = int(input("Estoque: "))
                vendas = int(input("Qtd Vendida: "))
                produtos.append(Produto(cod, nome, cat, preco, est, vendas))
                print("Produto cadastrado com sucesso!")
            except ValueError:
                print("Erro: Entrada inválida.")

        elif opcao == "2":
            print("\n--- CATÁLOGO DE PRODUTOS ---")
            for p in produtos:
                print(p)

        elif opcao == "3":
            try:
                cod = int(input("Informe o código para busca sequencial: "))
                res, pos, comp = busca_sequencial(produtos, cod)
                print(f"Comparações realizadas: {comp}")
                if res:
                    print(f"Produto encontrado na posição {pos}:\n{res}")
                else:
                    print("Código de produto não encontrado.")
            except ValueError:
                print("Erro: Insira um número inteiro.")

        elif opcao == "4":
            try:
                cod = int(input("Informe o código para busca binária: "))
                quick_sort(produtos)
                res, pos, comp = busca_binaria(produtos, cod)
                print("ℹ️ Lista foi pré-ordenada por código para executar a Busca Binária.")
                print(f"Comparações realizadas: {comp}")
                if res:
                    print(f"Produto encontrado na posição {pos}:\n{res}")
                else:
                    print("Código de produto não encontrado.")
            except ValueError:
                print("Erro: Insira um número inteiro.")

        elif opcao == "5":
            c, t, d = bubble_sort(produtos)
            print(f"Lista ordenada por PREÇO (Bubble Sort). | Comparações: {c}, Trocas: {t}")

        elif opcao == "6":
            c, t, d = selection_sort(produtos)
            print(f"Lista ordenada por ESTOQUE (Selection Sort). | Comparações: {c}, Trocas: {t}")

        elif opcao == "7":
            c, t, d = insertion_sort(produtos)
            print(f"Lista ordenada por NOME (Insertion Sort). | Comparações: {c}, Deslocamentos: {d}")

        elif opcao == "8":
            c, t, d = merge_sort(produtos)
            print(f"Lista ordenada por QUANTIDADE VENDIDA (MergeSort). | Comparações: {c}, Deslocamentos: {d}")

        elif opcao == "9":
            c, t, d = quick_sort(produtos)
            print(f"Lista ordenada por CÓDIGO (QuickSort). | Comparações: {c}, Trocas: {t}")

        elif opcao == "10":
            rodar_experimentos(get_base_inicial())

        elif opcao == "0":
            print("Encerrando o SmartStock... Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
