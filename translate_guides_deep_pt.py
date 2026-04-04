#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deep translation of ALL remaining English content in PT expat guide pages."""
import os

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www\pt"

REPLACEMENTS = [
    # ── INTRO PARAGRAPHS ──────────────────────────────────────────────────────
    ("Thailand remains one of the world's most popular expat destinations, offering warm weather, affordable living, world-class cuisine and welcoming visa options for retirees, remote workers and families.",
     "A Tailândia continua sendo um dos destinos de expatriados mais populares do mundo, oferecendo clima quente, custo de vida acessível, gastronomia de classe mundial e opções de visto acolhedoras para aposentados, trabalhadores remotos e famílias."),
    ("Japan is a unique expat destination",
     "O Japão é um destino único para expatriados"),
    ("Vietnam has emerged as one of Southeast Asia's most exciting expat destinations",
     "O Vietnã se tornou um dos destinos mais empolgantes para expatriados no Sudeste Asiático"),
    ("Malaysia offers one of Southeast Asia's most accessible expat experiences",
     "A Malásia oferece uma das experiências de expatriado mais acessíveis do Sudeste Asiático"),

    # ── VISA TABLE CONTENT ────────────────────────────────────────────────────
    ("Requires proof of 800,000 THB in a Thai bank account OR 65,000 THB/month income. Valid 1 year, renewable. Allows multiple entries.",
     "Exige comprovação de 800.000 THB em conta bancária tailandesa OU 65.000 THB/mês de renda. Válido por 1 ano, renovável. Permite entradas múltiplas."),
    ("Valid 10 years. Allows working for overseas employers without a Thai work permit. Fast-track immigration.",
     "Válido por 10 anos. Permite trabalhar para empregadores estrangeiros sem permissão de trabalho tailandesa. Imigração acelerada."),
    ("5–20 year stay, VIP airport service. No income requirement. Purely residence-based.",
     "Estadia de 5 a 20 anos, serviço VIP no aeroporto. Sem requisito de renda. Puramente residencial."),
    ("Must be accompanied by a Thai Work Permit. Annual renewal.",
     "Deve ser acompanhado de permissão de trabalho tailandesa. Renovação anual."),
    ("60 days (Tourist) or 30 days (visa-exempt). Can extend once at immigration. Many expats use border runs — now strictly monitored.",
     "60 dias (turístico) ou 30 dias (isenção de visto). Pode ser prorrogado uma vez na imigração. Muitos expatriados fazem saídas de fronteira — agora monitoradas rigorosamente."),

    # ── STEP-BY-STEP ─────────────────────────────────────────────────────────
    ("retirement, LTR, Elite or business", "aposentadoria, LTR, Elite ou negócios"),
    ("passport (6+ months), photos, bank statements, health insurance, medical certificate",
     "passaporte (validade 6+ meses), fotos, extratos bancários, seguro saúde, atestado médico"),
    ("Thai embassy or consulate in your home country", "embaixada ou consulado tailandês no seu país de origem"),
    ("TM.30 address notification within 24 hours", "notificação de endereço TM.30 dentro de 24 horas"),
    ("required for retirement visa deposit", "exigido para depósito do visto de aposentadoria"),
    ("at the Immigration Bureau (online, by post or in person)", "no Departamento de Imigração (online, por correio ou pessoalmente)"),
    ("at your local Immigration office", "no escritório local de Imigração"),

    # ── HEALTHCARE SECTION ────────────────────────────────────────────────────
    ("Thailand's public healthcare system (30-Baht Scheme) is available to Thai nationals and permanent residents only. As a non-resident expat, you cannot access public healthcare at subsidised rates.",
     "O sistema público de saúde tailandês (Programa 30 Bahts) está disponível apenas para cidadãos tailandeses e residentes permanentes. Como expatriado não residente, você não pode acessar a saúde pública a preços subsidiados."),
    ("Private hospitals in Thailand (Bangkok Hospital, Bumrungrad, Samitivej) are world-class and significantly cheaper than Western equivalents. A consultation costs 500–1,500 THB (~$14–42). Major surgery is 60–80% cheaper than in the US or Europe.",
     "Os hospitais privados na Tailândia (Bangkok Hospital, Bumrungrad, Samitivej) são de classe mundial e significativamente mais baratos do que os equivalentes ocidentais. Uma consulta custa 500–1.500 THB (~$14–42). Cirurgias de grande porte são 60–80% mais baratas do que nos EUA ou na Europa."),
    ("Most visa types (including LTR and Retirement OA) require proof of health insurance with minimum 40,000 THB outpatient / 400,000 THB inpatient coverage.",
     "A maioria dos tipos de visto (incluindo LTR e Aposentadoria OA) exige comprovação de seguro saúde com cobertura mínima de 40.000 THB ambulatorial / 400.000 THB hospitalar."),

    # ── INSURANCE SECTION ─────────────────────────────────────────────────────
    ("for retirement and LTR visas. Even on other visas, it is strongly recommended. Thai private hospitals can be expensive for major procedures, and repatriation costs without insurance can exceed $50,000.",
     "para vistos de aposentadoria e LTR. Mesmo com outros vistos, é fortemente recomendado. Hospitais privados tailandeses podem ser caros para procedimentos maiores, e os custos de repatriação sem seguro podem ultrapassar $50.000."),
    ("Local insurer specialising in expats in Southeast Asia. Plans from ~$800/year. Good network of Thai private hospitals.",
     "Seguradora local especializada em expatriados no Sudeste Asiático. Planos a partir de ~$800/ano. Boa rede de hospitais privados tailandeses."),
    ("Strong regional network. Plans from ~$1,000/year. Well-regarded for cancer coverage.",
     "Forte rede regional. Planos a partir de ~$1.000/ano. Reconhecida pela cobertura de câncer."),
    ("International coverage, ideal if you travel frequently or split time between countries. From ~$1,500/year.",
     "Cobertura internacional, ideal se você viaja com frequência ou divide o tempo entre países. A partir de ~$1.500/ano."),
    ("Comprehensive plans with worldwide coverage. Particularly suited for high earners on LTR visas. From ~$1,800/year.",
     "Planos abrangentes com cobertura mundial. Particularmente adequado para altos rendimentos com visto LTR. A partir de ~$1.800/ano."),
    ("Flexible modular plans. Can add dental, optical and maternity. From ~$1,200/year.",
     "Planos modulares flexíveis. Pode adicionar dentário, óptico e maternidade. A partir de ~$1.200/ano."),
    ("For the Retirement OA visa, your policy must be issued by a Thai-licensed insurer and must specifically state 40,000 / 400,000 THB minimum coverage. Pacific Cross and BUPA are the easiest to use for this purpose.",
     "Para o visto de Aposentadoria OA, sua apólice deve ser emitida por uma seguradora licenciada na Tailândia e deve indicar especificamente uma cobertura mínima de 40.000 / 400.000 THB. Pacific Cross e BUPA são as mais fáceis de usar para este fim."),

    # ── BANK ACCOUNT SECTION ──────────────────────────────────────────────────
    ("it's required for the retirement visa deposit (800,000 THB), utility payments, rent transfers and daily transactions.",
     "é exigido para o depósito do visto de aposentadoria (800.000 THB), pagamento de contas, transferências de aluguel e transações diárias."),
    ("Most expat-friendly bank. English-language app and staff in main branches. Fixed deposit accounts accepted for visa purposes.",
     "Banco mais amigável para expatriados. App e funcionários em inglês nas agências principais. Contas de depósito a prazo aceitas para fins de visto."),
    ("Largest bank in Thailand. Strong international wire support. Commonly used for pension/income transfers.",
     "Maior banco da Tailândia. Forte suporte para transferências internacionais. Comumente usado para transferências de pensão/renda."),
    ("Good English-language online banking. Competitive FX rates.",
     "Bom banco online em inglês. Taxas de câmbio competitivas."),
    ("Easier account opening in some provinces. Partners with Mitsubishi UFJ.",
     "Abertura de conta mais fácil em algumas províncias. Parceiro do Mitsubishi UFJ."),
    ("online opening not available for foreigners", "abertura online não disponível para estrangeiros"),
    ("to the bank officer", "ao funcionário do banco"),
    ("same day or within 5 business days", "no mesmo dia ou dentro de 5 dias úteis"),
    ("may require Thai phone number", "pode exigir número de telefone tailandês"),

    # ── REAL ESTATE SECTION ───────────────────────────────────────────────────
    ("Foreigners cannot own land in Thailand, but they can own condominium units freehold (up to 49% of a building's total floor area may be foreign-owned). Houses and land must be held through a Thai company, a 30-year leasehold or a Thai spouse.",
     "Estrangeiros não podem possuir terrenos na Tailândia, mas podem possuir unidades de condomínio em plena propriedade (até 49% da área total do edifício pode ser de propriedade estrangeira). Casas e terrenos devem ser detidos por meio de uma empresa tailandesa, arrendamento de 30 anos ou cônjuge tailandês."),
    ("Full ownership permitted for foreigners. Must be paid from overseas in foreign currency (proof required). Most popular option.",
     "Propriedade plena permitida para estrangeiros. Deve ser pago do exterior em moeda estrangeira (comprovante exigido). Opção mais popular."),
    ("for 30 years, renewable twice (total 90 years in practice). Common for villas and townhouses.",
     "por 30 anos, renovável duas vezes (90 anos no total na prática). Comum para vilas e casas geminadas."),
    ("A Thai limited company (min. 51% Thai shareholders) can hold land. Complex, legal fees $2,000–5,000. Requires ongoing compliance.",
     "Uma empresa limitada tailandesa (mín. 51% de acionistas tailandeses) pode deter terrenos. Complexo, honorários jurídicos $2.000–5.000. Exige conformidade contínua."),
    ("a Thai spouse's name. No legal protection in case of divorce. Not recommended.",
     "nome de cônjuge tailandês. Sem proteção legal em caso de divórcio. Não recomendado."),

    # ── PURCHASE PROCESS ──────────────────────────────────────────────────────
    ("Hire a reputable real estate lawyer (budget 30,000–80,000 THB)",
     "Contrate um advogado imobiliário de renome (orçamento 30.000–80.000 THB)"),
    ("Verify the title deed (Chanote / Nor Sor 4 — the only fully secure title)",
     "Verifique a escritura de propriedade (Chanote / Nor Sor 4 — o único título totalmente seguro)"),
    ("Sign a Reservation Agreement and pay deposit (50,000–100,000 THB)",
     "Assine um Contrato de Reserva e pague o sinal (50.000–100.000 THB)"),
    ("Due diligence: check no liens, correct zoning, building permits",
     "Due diligence: verificar ausência de ônus, zoneamento correto, licenças de construção"),
    ("Transfer funds from overseas bank to Thailand (keep FET form for proof)",
     "Transfira fundos de banco estrangeiro para a Tailândia (guarde o formulário FET como comprovante)"),
    ("Sign Sale & Purchase Agreement (SPA)", "Assine o Contrato de Compra e Venda (SPA)"),
    ("Transfer at the Land Office — both parties must attend",
     "Transferência no Departamento de Terras — ambas as partes devem estar presentes"),
    ("Pay transfer fees (typically 2–3% of assessed value)",
     "Pague as taxas de transferência (geralmente 2–3% do valor avaliado)"),

    # ── COST TABLE ────────────────────────────────────────────────────────────
    ("Transfer fee", "Taxa de transferência"),
    ("Stamp duty or specific business tax", "Imposto de selo ou imposto comercial específico"),
    ("Withholding tax", "Imposto retido na fonte"),
    ("Lawyer fees", "Honorários advocatícios"),
    ("Agent commission", "Comissão do agente"),
    ("2% of the appraised value (split buyer/seller)", "2% do valor avaliado (dividido entre comprador/vendedor)"),
    ("0.5% stamp duty OR 3.3% SBT if sold within 5 years", "0,5% imposto de selo OU 3,3% SBT se vendido em 5 anos"),
    ("1–3% (paid by seller)", "1–3% (pago pelo vendedor)"),
    ("3–5% (paid by seller)", "3–5% (pago pelo vendedor)"),

    # ── PRO TIPS ──────────────────────────────────────────────────────────────
    ("Always use a Chanote (NS4J) title deed. Avoid Nor Sor 3 or Sor Kor 1 titles — they offer less legal protection and cannot be mortgaged.",
     "Use sempre uma escritura Chanote (NS4J). Evite títulos Nor Sor 3 ou Sor Kor 1 — oferecem menos proteção legal e não podem ser hipotecados."),
    ("The LTR Visa is the best option for remote workers — 10 years, no 90-day reports, and it exempts certain income from Thai tax.",
     "O Visto LTR é a melhor opção para trabalhadores remotos — 10 anos, sem relatórios de 90 dias e isenta certos rendimentos do imposto tailandês."),
    ("Kasikorn Bank's Asoke (Bangkok) or Nimman (Chiang Mai) branches are known for being particularly helpful to expats. Arrive early — queues can be long.",
     "As agências Asoke (Bangkok) ou Nimman (Chiang Mai) do Kasikorn Bank são conhecidas por serem particularmente úteis para expatriados. Chegue cedo — as filas podem ser longas."),

    # ── E-E-A-T SECTION ───────────────────────────────────────────────────────
    ("We strive to keep all information current but visa rules, healthcare costs and property regulations change frequently. Always verify current requirements with official government sources and consult a licensed professional before making major decisions.",
     "Nos esforçamos para manter todas as informações atualizadas, mas as regras de visto, custos de saúde e regulamentações imobiliárias mudam frequentemente. Sempre verifique os requisitos atuais com fontes governamentais oficiais e consulte um profissional licenciado antes de tomar decisões importantes."),
    ("This guide is researched and maintained by the editorial team at eVisa-Card.com.",
     "Este guia é pesquisado e mantido pela equipe editorial do eVisa-Card.com."),

    # ── GENERIC PATTERNS ──────────────────────────────────────────────────────
    ("Valid passport", "Passaporte válido"),
    ("Proof of address in Thailand (rental contract or TM.30 confirmation)",
     "Comprovante de endereço na Tailândia (contrato de aluguel ou confirmação TM.30)"),
    ("Thai SIM card or phone number", "Cartão SIM ou número de telefone tailandês"),
    ("Initial deposit (typically 500–2,000 THB)", "Depósito inicial (geralmente 500–2.000 THB)"),
    ("Non-Immigrant visa (tourist visa may be refused at some branches)",
     "Visto Não-Imigrante (visto turístico pode ser recusado em algumas agências)"),
    ("GP consultation (private)", "Consulta de clínico geral (privado)"),
    ("Specialist consultation", "Consulta especialista"),
    ("Emergency room visit", "Visita à emergência"),
    ("Hospitalisation (per night)", "Hospitalização (por noite)"),
    ("Dental cleaning", "Limpeza dentária"),
    ("Eye exam + glasses", "Exame de vista + óculos"),

    # ── FOOTER / MISC ────────────────────────────────────────────────────────
    ("Global eVisa & Travel Information Platform", "Plataforma Global de Informações sobre eVisa e Viagens"),
    ("Follow eVisa-Card.com", "Siga eVisa-Card.com"),
    ("March 2026", "Março de 2026"),
    ("Last updated:", "Última atualização:"),
]

def main():
    total_replacements = 0
    files_updated = 0

    for fname in sorted(os.listdir(BASE)):
        if not fname.startswith("expat-guide-") or not fname.endswith(".html"):
            continue
        fpath = os.path.join(BASE, fname)
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            html = f.read()
        original = html
        file_replacements = 0
        for eng, pt in REPLACEMENTS:
            count = html.count(eng)
            if count > 0:
                html = html.replace(eng, pt)
                file_replacements += count
        if html != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            files_updated += 1
            total_replacements += file_replacements
            print(f"  OK {fname}: {file_replacements} replacements")

    print(f"\nDone: {files_updated} files, {total_replacements} total replacements.")

if __name__ == "__main__":
    main()
