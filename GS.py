# =============================================================
#   ORBCITY — Dados Orbitais para Cidades Inteligentes
#   Global Solution 2025 | Felipe · Fabrício · Gustavo · Andrey
# =============================================================

import time
import os

# ─── Dados simulados (estruturas de lista) ───────────────────

regioes = [
    {"nome": "Zona Norte",    "cobertura_verde": 18.5, "risco_enchente": "Alto",   "temp_media": 32.1},
    {"nome": "Zona Sul",      "cobertura_verde": 34.2, "risco_enchente": "Baixo",  "temp_media": 28.4},
    {"nome": "Zona Leste",    "cobertura_verde": 12.0, "risco_enchente": "Crítico","temp_media": 34.7},
    {"nome": "Zona Oeste",    "cobertura_verde": 27.8, "risco_enchente": "Médio",  "temp_media": 30.2},
    {"nome": "Centro",        "cobertura_verde":  8.3, "risco_enchente": "Alto",   "temp_media": 35.9},
]

alertas_ativos = []

historico_monitoramento = []

# ─── Utilitários visuais ─────────────────────────────────────

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def linha(char="─", tam=55):
    print(char * tam)

def cabecalho(titulo):
    limpar()
    linha("═")
    print(f"  🛰️  ORBCITY  |  {titulo}")
    linha("═")
    print()

def pausar():
    print()
    input("  Pressione ENTER para voltar ao menu...")

def cor_risco(risco):
    match risco:
        case "Crítico": return "🔴"
        case "Alto":    return "🟠"
        case "Médio":   return "🟡"
        case "Baixo":   return "🟢"
        case _:         return "⚪"

# ─── OPÇÃO 1 — Descrição da solução ──────────────────────────

def descricao_solucao():
    cabecalho("Sobre o Sistema")
    print("  A OrbCity é uma plataforma de inteligência urbana que utiliza")
    print("  dados de satélites (ESA Copernicus e INPE) para monitorar")
    print("  cidades em tempo real. O sistema analisa risco de enchentes,")
    print("  cobertura vegetal e ilhas de calor urbano, gerando alertas")
    print("  automáticos para apoiar decisões de gestores municipais.")
    print()
    linha()
    print("  Equipe  : Felipe · Fabrício · Gustavo · Andrey")
    print("  Tema    : Indústria Espacial + Cidades Inteligentes")
    print("  Versão  : 1.0 — Global Solution 2025")
    linha()
    pausar()

# ─── OPÇÃO 2 — Monitorar regiões (leitura de dados orbitais) ─

def monitorar_regioes():
    cabecalho("Monitoramento de Regiões")
    print(f"  {'Região':<14} {'Verde%':>7} {'Risco Enchente':<16} {'Temp °C':>7}")
    linha()

    for r in regioes:
        icone = cor_risco(r["risco_enchente"])
        print(f"  {r['nome']:<14} {r['cobertura_verde']:>6.1f}%  "
              f"{icone} {r['risco_enchente']:<13} {r['temp_media']:>6.1f}°C")
        historico_monitoramento.append(r["nome"])

    linha()
    print(f"  Total de regiões monitoradas: {len(regioes)}")
    media_verde = sum(r["cobertura_verde"] for r in regioes) / len(regioes)
    print(f"  Média de cobertura verde    : {media_verde:.1f}%")
    pausar()

# ─── OPÇÃO 3 — Analisar risco de enchente ────────────────────

def analisar_risco():
    cabecalho("Análise de Risco de Enchente")

    print("  Regiões disponíveis:")
    for i, r in enumerate(regioes, 1):
        print(f"    {i}. {r['nome']}")
    print()

    while True:
        entrada = input("  Digite o número da região (ou 0 para voltar): ").strip()
        if entrada == "0":
            return
        if entrada.isdigit() and 1 <= int(entrada) <= len(regioes):
            break
        print("  ⚠️  Opção inválida. Tente novamente.")

    r = regioes[int(entrada) - 1]
    icone = cor_risco(r["risco_enchente"])

    print()
    linha()
    print(f"  Região analisada : {r['nome']}")
    print(f"  Risco de enchente: {icone} {r['risco_enchente']}")
    print(f"  Cobertura verde  : {r['cobertura_verde']}%")
    print(f"  Temperatura média: {r['temp_media']}°C")
    linha()

    # Recomendação baseada no risco
    match r["risco_enchente"]:
        case "Crítico":
            print("  🚨 AÇÃO IMEDIATA: Acionar Defesa Civil e emitir alerta à")
            print("     população. Verificar sistemas de drenagem urgentemente.")
            alertas_ativos.append(f"CRÍTICO — {r['nome']}")
        case "Alto":
            print("  ⚠️  ATENÇÃO: Monitorar precipitações nas próximas 24h.")
            print("     Preparar equipes de resposta rápida.")
            alertas_ativos.append(f"ALTO — {r['nome']}")
        case "Médio":
            print("  ℹ️  OBSERVAÇÃO: Acompanhar dados orbitais diariamente.")
        case "Baixo":
            print("  ✅  SITUAÇÃO NORMAL: Nenhuma ação necessária no momento.")

    pausar()

# ─── OPÇÃO 4 — Emitir alerta orbital ─────────────────────────

def emitir_alerta():
    cabecalho("Emissão de Alerta Orbital")

    print("  Preencha os dados para emitir um novo alerta:\n")

    while True:
        regiao = input("  Nome da região afetada : ").strip()
        if regiao:
            break
        print("  ⚠️  Campo obrigatório.")

    print()
    print("  Tipos de alerta disponíveis:")
    print("    1 — Enchente")
    print("    2 — Calor extremo")
    print("    3 — Desmatamento detectado")
    print("    4 — Outro")
    print()

    while True:
        tipo_num = input("  Escolha o tipo (1-4): ").strip()
        if tipo_num in ["1", "2", "3", "4"]:
            break
        print("  ⚠️  Digite um número entre 1 e 4.")

    tipos = {"1": "Enchente", "2": "Calor extremo",
             "3": "Desmatamento detectado", "4": "Outro"}
    tipo = tipos[tipo_num]

    while True:
        nivel = input("  Nível de severidade (Baixo/Médio/Alto/Crítico): ").strip().capitalize()
        if nivel in ["Baixo", "Médio", "Alto", "Crítico"]:
            break
        print("  ⚠️  Digite: Baixo, Médio, Alto ou Crítico.")

    alerta = f"{cor_risco(nivel)} [{nivel}] {tipo} — {regiao}"
    alertas_ativos.append(alerta)

    print()
    linha()
    print("  ✅  Alerta registrado com sucesso!")
    print(f"  {alerta}")
    linha()
    pausar()

# ─── OPÇÃO 5 — Ver alertas ativos ────────────────────────────

def ver_alertas():
    cabecalho("Alertas Ativos")

    if not alertas_ativos:
        print("  ✅  Nenhum alerta ativo no momento.")
    else:
        print(f"  Total de alertas: {len(alertas_ativos)}\n")
        for i, alerta in enumerate(alertas_ativos, 1):
            print(f"  {i:>2}. {alerta}")
        print()
        linha()

        # Contagem por nível usando for + if
        criticos = sum(1 for a in alertas_ativos if "CRÍTICO" in a.upper() or "Crítico" in a)
        altos    = sum(1 for a in alertas_ativos if "ALTO" in a.upper() and "CRÍTICO" not in a.upper())
        print(f"  🔴 Críticos : {criticos}")
        print(f"  🟠 Altos    : {altos}")
        print(f"  📊 Total    : {len(alertas_ativos)}")

    pausar()

# ─── OPÇÃO 6 — Comparar regiões ──────────────────────────────

def comparar_regioes():
    cabecalho("Comparação entre Regiões")

    # Ordenar por cobertura verde (maior → menor)
    ordenadas = sorted(regioes, key=lambda r: r["cobertura_verde"], reverse=True)

    print("  Ranking de cobertura verde (satélite Sentinel-2):\n")
    for i, r in enumerate(ordenadas, 1):
        barra = "█" * int(r["cobertura_verde"] / 2)
        print(f"  {i}. {r['nome']:<14} {barra:<20} {r['cobertura_verde']:.1f}%")

    print()
    linha()

    # Região mais quente
    mais_quente = max(regioes, key=lambda r: r["temp_media"])
    mais_verde  = max(regioes, key=lambda r: r["cobertura_verde"])
    mais_risco  = [r for r in regioes if r["risco_enchente"] == "Crítico"]

    print(f"  🌡️  Região mais quente : {mais_quente['nome']} ({mais_quente['temp_media']}°C)")
    print(f"  🌿 Mais área verde   : {mais_verde['nome']} ({mais_verde['cobertura_verde']}%)")
    if mais_risco:
        nomes = ", ".join(r["nome"] for r in mais_risco)
        print(f"  🔴 Risco crítico     : {nomes}")
    else:
        print("  ✅  Nenhuma região em risco crítico.")

    pausar()

# ─── MENU PRINCIPAL ──────────────────────────────────────────

def menu():
    while True:
        cabecalho("Menu Principal")
        print("  1  —  Sobre o sistema OrbCity")
        print("  2  —  Monitorar regiões (dados orbitais)")
        print("  3  —  Analisar risco de enchente")
        print("  4  —  Emitir alerta orbital")
        print("  5  —  Ver alertas ativos")
        print("  6  —  Comparar regiões")
        print("  0  —  Sair")
        print()
        linha()
        opcao = input("  Escolha uma opção: ").strip()
        linha()

        match opcao:
            case "1": descricao_solucao()
            case "2": monitorar_regioes()
            case "3": analisar_risco()
            case "4": emitir_alerta()
            case "5": ver_alertas()
            case "6": comparar_regioes()
            case "0":
                limpar()
                print()
                linha("═")
                print("  🛰️  OrbCity encerrado. Até logo!")
                linha("═")
                print()
                break
            case _:
                print("  ⚠️  Opção inválida. Digite um número entre 0 e 6.")
                time.sleep(1.5)

# ─── Entrada do programa ─────────────────────────────────────

if __name__ == "__main__":
    menu()