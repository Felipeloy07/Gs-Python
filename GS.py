# RM 570720 Gustavo Maciel
# RM 569922 Andrey Durante
# RM 573450 Fabricio
# RM 573404 Felipe Eloy
 
# =============================================================
#   ORBCITY — Dados Orbitais para Cidades Inteligentes
#   Global Solution 2025 | Felipe · Fabrício · Gustavo · Andrey
# =============================================================
 
import time
 
# ─── Dados das regiões ───────────────────────────────────────
# Cada região é um dicionário com nome, cobertura verde, risco e temperatura
 
regioes = [
    {"nome": "Zona Norte",  "cobertura_verde": 18.5, "risco_enchente": "Alto",    "temp_media": 32.1},
    {"nome": "Zona Sul",    "cobertura_verde": 34.2, "risco_enchente": "Baixo",   "temp_media": 28.4},
    {"nome": "Zona Leste",  "cobertura_verde": 12.0, "risco_enchente": "Critico", "temp_media": 34.7},
    {"nome": "Zona Oeste",  "cobertura_verde": 27.8, "risco_enchente": "Medio",   "temp_media": 30.2},
    {"nome": "Centro",      "cobertura_verde":  8.3, "risco_enchente": "Alto",    "temp_media": 35.9},
]
 
# Lista de alertas — começa vazia e vai sendo preenchida pelo usuário
alertas_ativos = []
 
 
# ─── Funções auxiliares ──────────────────────────────────────
 
def linha():
    print("=" * 50)
 
def pausar():
    input("\nPressione ENTER para voltar ao menu...")
 
def icone_risco(risco):
    if risco == "Critico":
        return "[CRITICO]"
    elif risco == "Alto":
        return "[ALTO]"
    elif risco == "Medio":
        return "[MEDIO]"
    elif risco == "Baixo":
        return "[BAIXO]"
    else:
        return "[?]"
 
 
# ─── Tela de boas-vindas ─────────────────────────────────────
 
def boas_vindas():
    print()
    linha()
    print("   Bem-vindo ao ORBCITY")
    linha()
    print()
    print("  Ola! Fico feliz em ter voce aqui.")
    print()
    print("  O OrbCity usa imagens de satelite para monitorar")
    print("  cidades em tempo real: enchentes, calor urbano")
    print("  e muito mais.")
    print()
    print("  Carregando o sistema", end="")
    for i in range(4):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print(" Pronto!")
    time.sleep(0.5)
 
 
# ─── OPÇÃO 1 — Sobre o sistema ───────────────────────────────
 
def descricao_solucao():
    print()
    linha()
    print("   SOBRE O SISTEMA")
    linha()
    print()
    print("  A OrbCity e uma plataforma de inteligencia urbana")
    print("  que usa dados de satelites para monitorar cidades.")
    print()
    print("  O sistema analisa:")
    print("   - Risco de enchentes")
    print("   - Cobertura vegetal")
    print("   - Ilhas de calor urbano")
    print()
    linha()
    print("  Equipe  : Felipe, Fabricio, Gustavo, Andrey")
    print("  Tema    : Industria Espacial + Cidades Inteligentes")
    print("  Versao  : 1.0 — Global Solution 2025")
    linha()
    pausar()
 
 
# ─── OPÇÃO 2 — Monitorar regiões ─────────────────────────────
 
def monitorar_regioes():
    print()
    linha()
    print("   MONITORAMENTO DE REGIOES")
    linha()
    print()
    print("  Buscando dados orbitais mais recentes...")
    time.sleep(1)
    print()
    print(f"  {'Regiao':<14} {'Verde':>7}  {'Risco':<10}  {'Temp'}")
    print("  " + "-" * 44)
 
    total_verde = 0
 
    for regiao in regioes:
        nome = regiao["nome"]
        verde = regiao["cobertura_verde"]
        risco = regiao["risco_enchente"]
        temp = regiao["temp_media"]
        icone = icone_risco(risco)
 
        print(f"  {nome:<14} {verde:>6.1f}%  {icone:<10}  {temp:.1f}C")
 
        total_verde = total_verde + verde
 
    media_verde = total_verde / len(regioes)
 
    print()
    linha()
    print(f"  Total de regioes monitoradas : {len(regioes)}")
    print(f"  Media de cobertura verde     : {media_verde:.1f}%")
    pausar()
 
 
# ─── OPÇÃO 3 — Analisar risco de enchente ────────────────────
 
def analisar_risco():
    print()
    linha()
    print("   ANALISE DE RISCO DE ENCHENTE")
    linha()
    print()
    print("  Escolha uma regiao para analisar:\n")
 
    for i in range(len(regioes)):
        regiao = regioes[i]
        icone = icone_risco(regiao["risco_enchente"])
        print(f"  {i + 1}. {regiao['nome']}  {icone}")
 
    print()
    entrada = input("  Digite o numero da regiao (ou 0 para voltar): ")
 
    if entrada == "0":
        print("\n  Voltando ao menu...")
        time.sleep(1)
        return
 
    # Verifica se a entrada e valida
    if not entrada.isdigit():
        print("\n  Entrada invalida! Digite um numero.")
        time.sleep(1)
        return
 
    numero = int(entrada)
 
    if numero < 1 or numero > len(regioes):
        print("\n  Numero fora do intervalo valido.")
        time.sleep(1)
        return
 
    # Pega a regiao escolhida (indice começa em 0, por isso subtraimos 1)
    regiao = regioes[numero - 1]
    risco = regiao["risco_enchente"]
 
    print()
    print(f"  Analisando {regiao['nome']}...")
    time.sleep(1)
    print()
    linha()
    print(f"  Regiao         : {regiao['nome']}")
    print(f"  Risco enchente : {icone_risco(risco)} {risco}")
    print(f"  Cobertura verde: {regiao['cobertura_verde']}%")
    print(f"  Temperatura    : {regiao['temp_media']}C")
    linha()
    print()
 
    # Recomendacoes de acordo com o nivel de risco
    if risco == "Critico":
        print("  ACAO IMEDIATA NECESSARIA!")
        print("  Recomendamos acionar a Defesa Civil agora.")
        print("  Verifique os sistemas de drenagem!")
        alertas_ativos.append("CRITICO — " + regiao["nome"])
 
    elif risco == "Alto":
        print("  ATENCAO — situacao preocupante!")
        print("  Monitore as precipitacoes nas proximas 24h.")
        alertas_ativos.append("ALTO — " + regiao["nome"])
 
    elif risco == "Medio":
        print("  SITUACAO MODERADA — fique de olho!")
        print("  Acompanhe os dados diariamente.")
 
    elif risco == "Baixo":
        print("  TUDO CERTO POR AQUI!")
        print("  Nenhuma acao necessaria no momento.")
 
    pausar()
 
 
# ─── OPÇÃO 4 — Emitir alerta ─────────────────────────────────
 
def emitir_alerta():
    print()
    linha()
    print("   EMISSAO DE ALERTA ORBITAL")
    linha()
    print()
    print("  Preencha as informacoes abaixo:\n")
 
    regiao = input("  Nome da regiao afetada: ").strip()
 
    if regiao == "":
        print("\n  Campo obrigatorio! Tente novamente.")
        time.sleep(1)
        return
 
    print()
    print("  Tipo de situacao:")
    print("  1 - Enchente")
    print("  2 - Calor extremo")
    print("  3 - Desmatamento detectado")
    print("  4 - Outro")
    print()
 
    tipo_num = input("  Escolha o tipo (1-4): ").strip()
 
    if tipo_num == "1":
        tipo = "Enchente"
    elif tipo_num == "2":
        tipo = "Calor extremo"
    elif tipo_num == "3":
        tipo = "Desmatamento detectado"
    elif tipo_num == "4":
        tipo = "Outro"
    else:
        print("\n  Opcao invalida!")
        time.sleep(1)
        return
 
    print()
    print("  Nivel de gravidade: Baixo / Medio / Alto / Critico")
    nivel = input("  Nivel: ").strip().capitalize()
 
    if nivel not in ["Baixo", "Medio", "Alto", "Critico"]:
        print("\n  Nivel invalido! Use: Baixo, Medio, Alto ou Critico.")
        time.sleep(1)
        return
 
    alerta = icone_risco(nivel) + " [" + nivel + "] " + tipo + " — " + regiao
    alertas_ativos.append(alerta)
 
    print()
    print("  Registrando alerta", end="")
    for i in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()
    print()
    linha()
    print("  Alerta registrado com sucesso!")
    print("  " + alerta)
    linha()
    pausar()
 
 
# ─── OPÇÃO 5 — Ver alertas ativos ────────────────────────────
 
def ver_alertas():
    print()
    linha()
    print("   ALERTAS ATIVOS")
    linha()
    print()
 
    if len(alertas_ativos) == 0:
        print("  Nenhum alerta ativo no momento.")
        print("  Todas as regioes estao sob controle!")
    else:
        print(f"  Total de alertas: {len(alertas_ativos)}\n")
 
        for i in range(len(alertas_ativos)):
            print(f"  {i + 1}. {alertas_ativos[i]}")
 
        # Conta alertas criticos
        criticos = 0
        for alerta in alertas_ativos:
            if "CRITICO" in alerta:
                criticos = criticos + 1
 
        print()
        linha()
        print(f"  Alertas criticos : {criticos}")
        print(f"  Total geral      : {len(alertas_ativos)}")
 
        if criticos > 0:
            print()
            print("  Ha alertas criticos! Tome as devidas providencias.")
 
    pausar()
 
 
# ─── OPÇÃO 6 — Comparar regiões ──────────────────────────────
 
def comparar_regioes():
    print()
    linha()
    print("   COMPARACAO ENTRE REGIOES")
    linha()
    print()
 
    print("  Ranking de cobertura verde:\n")
 
    # Ordenacao simples por cobertura verde (bubble sort)
    lista = regioes.copy()
    n = len(lista)
 
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["cobertura_verde"] < lista[j + 1]["cobertura_verde"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
 
    for i in range(len(lista)):
        regiao = lista[i]
        barra = "#" * int(regiao["cobertura_verde"] / 2)
        print(f"  {i + 1}. {regiao['nome']:<14} {barra:<20} {regiao['cobertura_verde']:.1f}%")
 
    print()
    linha()
 
    # Encontra a mais quente
    mais_quente = regioes[0]
    for regiao in regioes:
        if regiao["temp_media"] > mais_quente["temp_media"]:
            mais_quente = regiao
 
    # Encontra a mais verde
    mais_verde = regioes[0]
    for regiao in regioes:
        if regiao["cobertura_verde"] > mais_verde["cobertura_verde"]:
            mais_verde = regiao
 
    print(f"  Regiao mais quente : {mais_quente['nome']} ({mais_quente['temp_media']}C)")
    print(f"  Mais area verde    : {mais_verde['nome']} ({mais_verde['cobertura_verde']}%)")
 
    # Verifica se existe alguma regiao em risco critico
    tem_critico = False
    for regiao in regioes:
        if regiao["risco_enchente"] == "Critico":
            print(f"  Risco critico      : {regiao['nome']}")
            tem_critico = True
 
    if not tem_critico:
        print("  Nenhuma regiao em risco critico no momento.")
 
    pausar()
 
 
# ─── Menu principal ──────────────────────────────────────────
 
def menu():
    boas_vindas()
 
    while True:
        print()
        linha()
        print("   ORBCITY — Menu Principal")
        linha()
        print()
        print("  1 - Sobre o sistema OrbCity")
        print("  2 - Monitorar regioes (dados orbitais)")
        print("  3 - Analisar risco de enchente")
        print("  4 - Emitir alerta orbital")
        print("  5 - Ver alertas ativos")
        print("  6 - Comparar regioes")
        print("  0 - Sair")
        print()
        linha()
 
        opcao = input("  Digite sua escolha: ").strip()
 
        if opcao == "1":
            descricao_solucao()
        elif opcao == "2":
            monitorar_regioes()
        elif opcao == "3":
            analisar_risco()
        elif opcao == "4":
            emitir_alerta()
        elif opcao == "5":
            ver_alertas()
        elif opcao == "6":
            comparar_regioes()
        elif opcao == "0":
            print()
            linha()
            print("  Obrigado por usar o OrbCity!")
            print("  Ate a proxima!")
            linha()
            print()
            break
        else:
            print()
            print("  Opcao invalida! Digite um numero entre 0 e 6.")
            time.sleep(1.5)
 
 
# ─── Inicio do programa ──────────────────────────────────────
 
menu()