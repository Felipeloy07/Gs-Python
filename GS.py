# =============================================================
#   ORBCITY — Dados Orbitais para Cidades Inteligentes
#   Global Solution 2025 | Felipe · Fabrício · Gustavo · Andrey
# =============================================================

import time
import os

# ─── Dados simulados ─────────────────────────────────────────

regioes = [
    {"nome": "Zona Norte",  "cobertura_verde": 18.5, "risco_enchente": "Alto",    "temp_media": 32.1},
    {"nome": "Zona Sul",    "cobertura_verde": 34.2, "risco_enchente": "Baixo",   "temp_media": 28.4},
    {"nome": "Zona Leste",  "cobertura_verde": 12.0, "risco_enchente": "Crítico", "temp_media": 34.7},
    {"nome": "Zona Oeste",  "cobertura_verde": 27.8, "risco_enchente": "Médio",   "temp_media": 30.2},
    {"nome": "Centro",      "cobertura_verde":  8.3, "risco_enchente": "Alto",    "temp_media": 35.9},
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

def carregando(mensagem="  Carregando", repeticoes=3):
    print(mensagem, end="", flush=True)
    for _ in range(repeticoes):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()
    time.sleep(0.3)

def cor_risco(risco):
    match risco:
        case "Crítico": return "🔴"
        case "Alto":    return "🟠"
        case "Médio":   return "🟡"
        case "Baixo":   return "🟢"
        case _:         return "⚪"

# ─── Tela de boas-vindas ─────────────────────────────────────

def boas_vindas():
    limpar()
    linha("═")
    print("  🛰️  Bem-vindo ao ORBCITY")
    linha("═")
    print()
    print("  Olá! Fico feliz em ter você aqui. 😊")
    print()
    print("  O OrbCity usa imagens de satélite para monitorar")
    print("  cidades em tempo real — enchentes, calor urbano")
    print("  e muito mais, tudo na palma da sua mão.")
    print()
    carregando("  Inicializando o sistema")
    carregando("  Conectando aos satélites")
    carregando("  Pronto! Carregando o menu")
    time.sleep(0.3)

# ─── OPÇÃO 1 — Descrição da solução ──────────────────────────

def descricao_solucao():
    cabecalho("Sobre o Sistema")
    print("  Oi! Vou te contar um pouco sobre o que é o OrbCity. 🌍")
    print()
    print("  A OrbCity é uma plataforma de inteligência urbana que utiliza")
    print("  dados de satélites (ESA Copernicus e INPE) para monitorar")
    print("  cidades em tempo real. O sistema analisa risco de enchentes,")
    print("  cobertura vegetal e ilhas de calor urbano, gerando alertas")
    print("  automáticos para apoiar decisões de gestores municipais.")
    print()
    linha()
    print("  👥  Equipe  : Felipe · Fabrício · Gustavo · Andrey")
    print("  🌐  Tema    : Indústria Espacial + Cidades Inteligentes")
    print("  🔖  Versão  : 1.0 — Global Solution 2025")
    linha()
    print()
    print("  Qualquer dúvida, fique à vontade para explorar as outras")
    print("  opções do menu. Estamos aqui para ajudar! 🚀")
    pausar()

# ─── OPÇÃO 2 — Monitorar regiões ─────────────────────────────

def monitorar_regioes():
    cabecalho("Monitoramento de Regiões")
    print("  Vou buscar os dados orbitais mais recentes para você...")
    print()
    carregando("  Conectando ao satélite Sentinel-2")
    carregando("  Processando imagens")
    print()
    print(f"  {'Região':<14} {'Verde%':>7} {'Risco Enchente':<16} {'Temp °C':>7}")
    linha()

    for r in regioes:
        icone = cor_risco(r["risco_enchente"])
        print(f"  {r['nome']:<14} {r['cobertura_verde']:>6.1f}%  "
              f"{icone} {r['risco_enchente']:<13} {r['temp_media']:>6.1f}°C")
        historico_monitoramento.append(r["nome"])

    linha()
    media_verde = sum(r["cobertura_verde"] for r in regioes) / len(regioes)
    print(f"  📡 Total de regiões monitoradas : {len(regioes)}")
    print(f"  🌿 Média de cobertura verde     : {media_verde:.1f}%")
    print()
    print("  Dados atualizados com sucesso! ✅")
    pausar()

# ─── OPÇÃO 3 — Analisar risco de enchente ────────────────────

def analisar_risco():
    cabecalho("Análise de Risco de Enchente")
    print("  Vamos analisar o risco de enchente da região que você escolher.")
    print("  Selecione uma das opções abaixo:\n")

    for i, r in enumerate(regioes, 1):
        icone = cor_risco(r["risco_enchente"])
        print(f"    {i}. {r['nome']}  {icone}")
    print()

    while True:
        entrada = input("  Digite o número da região (ou 0 para voltar): ").strip()
        if entrada == "0":
            print("\n  Tudo bem! Voltando ao menu principal... 👋")
            time.sleep(1)
            return
        if entrada.isdigit() and 1 <= int(entrada) <= len(regioes):
            break
        print("  ⚠️  Hmm, esse número não é válido. Tente novamente!")

    r = regioes[int(entrada) - 1]
    icone = cor_risco(r["risco_enchente"])

    print()
    carregando(f"  Analisando dados da {r['nome']}")
    print()
    linha()
    print(f"  📍 Região analisada  : {r['nome']}")
    print(f"  💧 Risco de enchente : {icone} {r['risco_enchente']}")
    print(f"  🌿 Cobertura verde   : {r['cobertura_verde']}%")
    print(f"  🌡️  Temperatura média : {r['temp_media']}°C")
    linha()
    print()

    match r["risco_enchente"]:
        case "Crítico":
            print("  🚨 AÇÃO IMEDIATA NECESSÁRIA!")
            print("     Recomendamos acionar a Defesa Civil agora e emitir")
            print("     alertas à população. Verifique os sistemas de drenagem!")
            alertas_ativos.append(f"CRÍTICO — {r['nome']}")
        case "Alto":
            print("  ⚠️  ATENÇÃO — situação preocupante!")
            print("     Monitore as precipitações nas próximas 24h e deixe")
            print("     as equipes de resposta rápida em prontidão.")
            alertas_ativos.append(f"ALTO — {r['nome']}")
        case "Médio":
            print("  ℹ️  SITUAÇÃO MODERADA — fique de olho!")
            print("     Acompanhe os dados orbitais diariamente.")
        case "Baixo":
            print("  ✅  TUDO CERTO POR AQUI!")
            print("     Nenhuma ação necessária no momento. 😊")

    pausar()

# ─── OPÇÃO 4 — Emitir alerta orbital ─────────────────────────

def emitir_alerta():
    cabecalho("Emissão de Alerta Orbital")
    print("  Vamos registrar um novo alerta. Pode me passar as informações:\n")

    while True:
        regiao = input("  📍 Nome da região afetada : ").strip()
        if regiao:
            break
        print("  ⚠️  Ops! Esse campo é obrigatório. Tente novamente.")

    print()
    print("  Que tipo de situação está acontecendo?")
    print("    1 — 💧 Enchente")
    print("    2 — 🌡️  Calor extremo")
    print("    3 — 🌳 Desmatamento detectado")
    print("    4 — ❓ Outro")
    print()

    while True:
        tipo_num = input("  Escolha o tipo (1-4): ").strip()
        if tipo_num in ["1", "2", "3", "4"]:
            break
        print("  ⚠️  Por favor, digite um número entre 1 e 4.")

    tipos = {"1": "Enchente", "2": "Calor extremo",
             "3": "Desmatamento detectado", "4": "Outro"}
    tipo = tipos[tipo_num]

    print()
    print("  Qual é a gravidade da situação?")
    while True:
        nivel = input("  Nível (Baixo / Médio / Alto / Crítico): ").strip().capitalize()
        if nivel in ["Baixo", "Médio", "Alto", "Crítico"]:
            break
        print("  ⚠️  Digite exatamente: Baixo, Médio, Alto ou Crítico.")

    alerta = f"{cor_risco(nivel)} [{nivel}] {tipo} — {regiao}"
    alertas_ativos.append(alerta)

    print()
    carregando("  Registrando alerta no sistema")
    linha()
    print("  ✅  Alerta registrado com sucesso!")
    print(f"  {alerta}")
    print()
    print("  Os gestores responsáveis serão notificados. 📢")
    linha()
    pausar()

# ─── OPÇÃO 5 — Ver alertas ativos ────────────────────────────

def ver_alertas():
    cabecalho("Alertas Ativos")

    if not alertas_ativos:
        print("  Que ótima notícia! 🎉")
        print("  Não há nenhum alerta ativo no momento.")
        print("  Todas as regiões estão sob controle. ✅")
    else:
        print(f"  Encontrei {len(alertas_ativos)} alerta(s) registrado(s):\n")
        for i, alerta in enumerate(alertas_ativos, 1):
            print(f"  {i:>2}. {alerta}")
        print()
        linha()

        criticos = sum(1 for a in alertas_ativos if "CRÍTICO" in a.upper() or "Crítico" in a)
        altos    = sum(1 for a in alertas_ativos if "ALTO" in a.upper() and "CRÍTICO" not in a.upper())
        print(f"  🔴 Críticos : {criticos}")
        print(f"  🟠 Altos    : {altos}")
        print(f"  📊 Total    : {len(alertas_ativos)}")
        print()
        if criticos > 0:
            print("  ⚠️  Há alertas críticos! Tome as devidas providências.")

    pausar()

# ─── OPÇÃO 6 — Comparar regiões ──────────────────────────────

def comparar_regioes():
    cabecalho("Comparação entre Regiões")
    print("  Aqui você pode ver como cada região se compara às outras.")
    print("  Dados coletados pelo satélite Sentinel-2 🛰️\n")

    carregando("  Processando comparativo")
    print()

    ordenadas = sorted(regioes, key=lambda r: r["cobertura_verde"], reverse=True)

    print("  🌿 Ranking de cobertura verde:\n")
    for i, r in enumerate(ordenadas, 1):
        barra = "█" * int(r["cobertura_verde"] / 2)
        print(f"  {i}. {r['nome']:<14} {barra:<20} {r['cobertura_verde']:.1f}%")

    print()
    linha()

    mais_quente = max(regioes, key=lambda r: r["temp_media"])
    mais_verde  = max(regioes, key=lambda r: r["cobertura_verde"])
    mais_risco  = [r for r in regioes if r["risco_enchente"] == "Crítico"]

    print(f"  🌡️  Região mais quente  : {mais_quente['nome']} ({mais_quente['temp_media']}°C)")
    print(f"  🌿 Mais área verde    : {mais_verde['nome']} ({mais_verde['cobertura_verde']}%)")

    if mais_risco:
        nomes = ", ".join(r["nome"] for r in mais_risco)
        print(f"  🔴 Risco crítico      : {nomes}")
        print()
        print("  💡 Dica: Considere priorizar ações nessas regiões!")
    else:
        print("  ✅  Nenhuma região em risco crítico no momento.")

    pausar()

# ─── MENU PRINCIPAL ──────────────────────────────────────────

def menu():
    boas_vindas()
    while True:
        cabecalho("Menu Principal")
        print("  O que você gostaria de fazer hoje? 😊")
        print()
        print("  1  —  📖  Sobre o sistema OrbCity")
        print("  2  —  📡  Monitorar regiões (dados orbitais)")
        print("  3  —  💧  Analisar risco de enchente")
        print("  4  —  🚨  Emitir alerta orbital")
        print("  5  —  🔔  Ver alertas ativos")
        print("  6  —  📊  Comparar regiões")
        print("  0  —  👋  Sair")
        print()
        linha()
        opcao = input("  Digite sua escolha: ").strip()
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
                print("  👋  Obrigado por usar o OrbCity!")
                print("  🛰️  Até a próxima. Cuide-se!")
                linha("═")
                print()
                break
            case _:
                print("  🤔  Hmm, não reconheci essa opção.")
                print("      Digite um número entre 0 e 6, tá bom?")
                time.sleep(2)

# ─── Entrada do programa ─────────────────────────────────────

if __name__ == "__main__":
    menu()