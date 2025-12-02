def avaliar_peca(peso, cor, comprimento):
    """
    Regra de qualidade:
    - Peso entre 95g e 105g
    - Cor azul ou verde
    - Comprimento entre 10cm e 20cm
    """
    motivos = []

    if not (95 <= peso <= 105):
        motivos.append("peso fora da faixa (95g a 105g)")
    if cor.lower() not in ("azul", "verde"):
        motivos.append("cor inválida (apenas azul ou verde)")
    if not (10 <= comprimento <= 20):
        motivos.append("comprimento fora da faixa (10cm a 20cm)")

    if motivos:
        return False, "; ".join(motivos)
    return True, ""


# "Banco de dados" em memória
pecas = []  # lista de dicionários
caixas_fechadas = []  # lista de caixas já cheias
caixa_atual = {"numero": 1, "pecas": []}  # caixa em uso (ainda não fechada)


def alocar_em_caixa(id_peca):
    """
    Coloca a peça aprovada na caixa atual.
    Quando a caixa atinge 10 peças, ela é fechada
    e uma nova caixa é iniciada.
    """
    global caixa_atual, caixas_fechadas

    caixa_atual["pecas"].append(id_peca)

    if len(caixa_atual["pecas"]) >= 10:
        # Fecha a caixa
        caixas_fechadas.append({
            "numero": caixa_atual["numero"],
            "pecas": list(caixa_atual["pecas"])
        })
        # Cria uma nova caixa
        caixa_atual = {"numero": caixa_atual["numero"] + 1, "pecas": []}


def cadastrar_peca():
    print("\n=== Cadastro de nova peça ===")
    id_peca = input("ID da peça: ").strip()

    # Evita IDs duplicados
    for p in pecas:
        if p["id"] == id_peca:
            print("Já existe uma peça cadastrada com esse ID.")
            return

    try:
        peso = float(input("Peso da peça (em gramas): "))
        comprimento = float(input("Comprimento da peça (em cm): "))
    except ValueError:
        print("Valor numérico inválido para peso ou comprimento.")
        return

    cor = input("Cor da peça (azul/verde): ").strip()

    aprovada, motivo = avaliar_peca(peso, cor, comprimento)

    registro = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": "APROVADA" if aprovada else "REPROVADA",
        "motivo_reprovacao": motivo,
        "caixa_numero": None
    }

    if aprovada:
        registro["caixa_numero"] = caixa_atual["numero"]
        alocar_em_caixa(id_peca)
        print(f"Peça {id_peca} APROVADA e alocada na caixa {registro['caixa_numero']}.")
    else:
        print(f"Peça {id_peca} REPROVADA. Motivo(s): {motivo}")

    pecas.append(registro)


def listar_pecas():
    print("\n=== Peças APROVADAS ===")
    aprovadas = [p for p in pecas if p["status"] == "APROVADA"]

    if not aprovadas:
        print("Nenhuma peça aprovada cadastrada.")
    else:
        for p in aprovadas:
            print(
                f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | "
                f"Comp: {p['comprimento']}cm | Caixa: {p['caixa_numero']}"
            )

    print("\n=== Peças REPROVADAS ===")
    reprovadas = [p for p in pecas if p["status"] == "REPROVADA"]

    if not reprovadas:
        print("Nenhuma peça reprovada cadastrada.")
    else:
        for p in reprovadas:
            print(
                f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | "
                f"Comp: {p['comprimento']}cm | Motivo: {p['motivo_reprovacao']}"
            )


def remover_peca():
    global pecas, caixas_fechadas, caixa_atual

    print("\n=== Remover peça ===")
    id_peca = input("Informe o ID da peça que deseja remover: ").strip()

    existe = any(p["id"] == id_peca for p in pecas)
    if not existe:
        print("Nenhuma peça encontrada com esse ID.")
        return

    # Remove da lista de peças
    pecas = [p for p in pecas if p["id"] != id_peca]

    # Remove de caixas fechadas
    for caixa in caixas_fechadas:
        if id_peca in caixa["pecas"]:
            caixa["pecas"].remove(id_peca)

    # Remove da caixa atual (se estiver lá)
    if id_peca in caixa_atual["pecas"]:
        caixa_atual["pecas"].remove(id_peca)

    print(f"Peça {id_peca} removida com sucesso.")


def listar_caixas_fechadas():
    print("\n=== Caixas FECHADAS ===")
    if not caixas_fechadas:
        print("Nenhuma caixa fechada até o momento.")
        return

    for caixa in caixas_fechadas:
        print(f"Caixa {caixa['numero']} - Quantidade de peças: {len(caixa['pecas'])}")
        print(f"IDs: {', '.join(caixa['pecas'])}")
        print("-" * 40)


def gerar_relatorio():
    print("\n=== RELATÓRIO FINAL ===")
    total_aprovadas = sum(1 for p in pecas if p["status"] == "APROVADA")
    total_reprovadas = sum(1 for p in pecas if p["status"] == "REPROVADA")

    print(f"Total de peças cadastradas: {len(pecas)}")
    print(f"Total de peças aprovadas: {total_aprovadas}")
    print(f"Total de peças reprovadas: {total_reprovadas}")
    print(f"Quantidade de caixas fechadas: {len(caixas_fechadas)}")

    print("\nDetalhes das peças reprovadas:")
    if total_reprovadas == 0:
        print("Nenhuma peça reprovada.")
    else:
        for p in pecas:
            if p["status"] == "REPROVADA":
                print(f"ID: {p['id']} | Motivo(s): {p['motivo_reprovacao']}")


def exibir_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas_fechadas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
