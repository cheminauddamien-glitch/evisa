#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate remaining English body content in RU expat guide pages."""
import os

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www\ru"

REPLACEMENTS = [
    # ── PAGE TITLES ──────────────────────────────────────────────────────────
    ("Complete Expat Guide Cambodia 2026 — Live & Retire in Cambodia", "Полный гид для экспатов Камбоджа 2026 — Жизнь в Камбодже"),
    ("Expat Guide Colombia 2026 — Live & Work in Colombia | eVisa-Card.com", "Гид для экспатов Колумбия 2026 — Жизнь в Колумбии | eVisa-Card.com"),
    ("Complete Expat Guide Georgia 2026 — Live & Work in Georgia (Caucasus)", "Полный гид для экспатов Грузия 2026 — Жизнь в Грузии"),
    ("Complete Expat Guide Greece 2026 — Live & Retire in Greece", "Полный гид для экспатов Греция 2026 — Жизнь в Греции"),
    ("Complete Expat Guide Laos 2026 — Live & Work in Laos", "Полный гид для экспатов Лаос 2026 — Жизнь в Лаосе"),
    ("Complete Expat Guide Panama 2026 — Live & Retire in Panama", "Полный гид для экспатов Панама 2026 — Жизнь в Панаме"),
    ("Complete Expat Guide Paraguay 2026 — Live & Retire in Paraguay", "Полный гид для экспатов Парагвай 2026 — Жизнь в Парагвае"),
    ("Expat Guide UAE 2026 — How to Live in Dubai & Abu Dhabi | eVisa-Card.com", "Гид для экспатов ОАЭ 2026 — Жизнь в Дубае и Абу-Даби | eVisa-Card.com"),
    ("Complete Expat Guide Costa Rica 2026 — Live & Retire in Costa Rica", "Полный гид для экспатов Коста-Рика 2026 — Жизнь в Коста-Рике"),

    # ── VISA SECTION ─────────────────────────────────────────────────────────
    ("Thailand offers several long-stay options: the Tourist Visa (60 days, extendable), Non-Immigrant O-A Retirement Visa (1 year, renewable, for 50+), Thailand Elite Visa (5–20 years, premium), Long-Term Resident (LTR) Visa for professionals and digital nomads. There is no standard permanent residency path but long-term visa holders can renew indefinitely.",
     "Таиланд предлагает несколько вариантов длительного пребывания: туристическая виза (60 дней, продлевается), неиммиграционная виза O-A для пенсионеров (1 год, возобновляется, для 50+), Thailand Elite Visa (5–20 лет, премиум), долгосрочная резидентская (LTR) виза для профессионалов и цифровых кочевников. Стандартного пути к ПМЖ нет, но держатели долгосрочных виз могут продлевать их бессрочно."),

    # ── STEP-BY-STEP ─────────────────────────────────────────────────────────
    ("Choose your visa type", "Выберите тип визы"),
    ("Gather required documents", "Соберите необходимые документы"),
    ("Apply at a Thai embassy or consulate", "Подайте заявление в посольстве или консульстве Таиланда"),
    ("Arrive and register your address", "Прибудьте и зарегистрируйте адрес"),
    ("Open a Thai bank account", "Откройте счёт в тайском банке"),
    ("Get health insurance", "Оформите медицинскую страховку"),
    ("Annual extension / 90-day report", "Ежегодное продление / 90-дневный отчёт"),

    ("Determine if you qualify for the Retirement O-A (50+, pension/savings proof), LTR Visa (remote worker, $80k income), or Thailand Elite. Most expats start with a Tourist Visa and switch after arrival.",
     "Определите, имеете ли вы право на пенсионную O-A (50+, подтверждение пенсии/сбережений), LTR Visa (удалённый работник, доход $80k), или Thailand Elite. Большинство экспатов начинают с туристической визы и переходят после прибытия."),
    ("Passport (6+ months validity), passport photos, bank statements (800,000 THB in Thai bank for retirement visa or proof of $80k income for LTR), health insurance, medical certificate.",
     "Паспорт (срок действия 6+ месяцев), фотографии, банковские выписки (800 000 бат на тайском счёте для пенсионной визы или подтверждение дохода $80k для LTR), медицинская страховка, медицинское заключение."),
    ("Submit your visa application at your nearest Thai embassy. Processing takes 3–5 business days. You can also enter on a tourist visa and extend at the Immigration Bureau in Thailand.",
     "Подайте заявление на визу в ближайшем посольстве Таиланда. Обработка занимает 3–5 рабочих дней. Можно также въехать по туристической визе и продлить её в Иммиграционном бюро Таиланда."),
    ("Within 24 hours of arriving, notify your accommodation. If renting, your landlord must file a TM.30 report. You receive a TM.6 arrival card.",
     "В течение 24 часов после прибытия уведомите своё жильё. При аренде арендодатель должен подать отчёт TM.30. Вы получаете карточку прибытия TM.6."),
    ("Open a Kasikorn Bank (KBank) or Bangkok Bank account. You'll need your passport, Non-Immigrant visa, and proof of address. Required for the 800,000 THB retirement deposit.",
     "Откройте счёт в Kasikorn Bank (KBank) или Bangkok Bank. Нужны паспорт, неиммиграционная виза и подтверждение адреса. Обязательно для депозита 800 000 бат для пенсионной визы."),
    ("Mandatory for retirement and LTR visas. Compare providers: Pacific Cross, BUPA Thailand, AXA. Budget ฿15,000–฿60,000/year depending on age and coverage.",
     "Обязательно для пенсионных и LTR виз. Сравните провайдеров: Pacific Cross, BUPA Thailand, AXA. Бюджет 15 000–60 000 бат/год в зависимости от возраста и покрытия."),
    ("Renew your visa annually at the local Immigration office. File 90-day reports in person, by post, or online via the Immigration Bureau website.",
     "Ежегодно продлевайте визу в местном иммиграционном офисе. Подавайте 90-дневные отчёты лично, по почте или онлайн через сайт Иммиграционного бюро."),

    # ── COMMON ────────────────────────────────────────────────────────────────
    ("Visa & Residency Options", "Варианты виз и проживания"),
    ("Pro Tips", "Советы экспертов"),
    ("Frequently Asked Questions", "Часто задаваемые вопросы"),
    ("Last updated: March 2026", "Последнее обновление: март 2026"),
    ("March 2026", "март 2026"),
    ("Global eVisa & Travel Information Platform", "Глобальная платформа информации об электронных визах и путешествиях"),
    ("Follow eVisa-Card.com", "Следите за eVisa-Card.com"),
    ("Visa Type", "Тип визы"),
    ("Duration", "Срок"),
    ("Requirements", "Требования"),
    ("Best For", "Лучший для"),
    ("Processing Time", "Срок оформления"),
    ("Fee", "Стоимость"),
    ("Mandatory", "Обязательно"),
    ("Recommended", "Рекомендуется"),
    ("Optional", "По желанию"),
    ("per year", "в год"),
    ("per month", "в месяц"),
    ("per night", "за ночь"),
]

def main():
    total = 0
    for fname in sorted(os.listdir(BASE)):
        if not fname.startswith("expat-guide-") or not fname.endswith(".html"):
            continue
        fpath = os.path.join(BASE, fname)
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            html = f.read()
        original = html
        for eng, ru in REPLACEMENTS:
            html = html.replace(eng, ru)
        if html != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            total += 1
            print(f"  OK {fname}")
    print(f"\nDone: {total} files updated.")

if __name__ == "__main__":
    main()
