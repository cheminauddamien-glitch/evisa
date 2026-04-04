#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate English text in Russian (ru) expat guide pages.
Processes all expat-guide-*.html files in www/ru/
"""

import os
import re
import glob

# Directory containing RU guide files
RU_DIR = os.path.join(os.path.dirname(__file__), "www", "ru")

# Ordered list of (pattern, replacement) tuples.
# More specific patterns first to avoid partial replacement issues.
REPLACEMENTS = [
    # ── Title / meta ──────────────────────────────────────────────────────────
    ("How to Live in Thailand | eVisa-Card.com",
     "Как жить в Таиланде | eVisa-Card.com"),
    ("How to Live in Portugal | eVisa-Card.com",
     "Как жить в Португалии | eVisa-Card.com"),
    ("How to Live in Spain | eVisa-Card.com",
     "Как жить в Испании | eVisa-Card.com"),
    ("How to Live in Japan | eVisa-Card.com",
     "Как жить в Японии | eVisa-Card.com"),
    ("How to Live in Vietnam | eVisa-Card.com",
     "Как жить во Вьетнаме | eVisa-Card.com"),
    ("How to Live in Cambodia | eVisa-Card.com",
     "Как жить в Камбодже | eVisa-Card.com"),
    ("How to Live in Malaysia | eVisa-Card.com",
     "Как жить в Малайзии | eVisa-Card.com"),
    ("How to Live in Georgia | eVisa-Card.com",
     "Как жить в Грузии | eVisa-Card.com"),
    ("How to Live in Greece | eVisa-Card.com",
     "Как жить в Греции | eVisa-Card.com"),
    ("How to Live in Mexico | eVisa-Card.com",
     "Как жить в Мексике | eVisa-Card.com"),
    ("How to Live in Colombia | eVisa-Card.com",
     "Как жить в Колумбии | eVisa-Card.com"),
    ("How to Live in Panama | eVisa-Card.com",
     "Как жить в Панаме | eVisa-Card.com"),
    ("How to Live in Paraguay | eVisa-Card.com",
     "Как жить в Парагвае | eVisa-Card.com"),
    ("How to Live in Costa Rica | eVisa-Card.com",
     "Как жить в Коста-Рике | eVisa-Card.com"),
    ("How to Live in Laos | eVisa-Card.com",
     "Как жить в Лаосе | eVisa-Card.com"),
    ("How to Live in Dubai & Abu Dhabi | eVisa-Card.com",
     "Как жить в Дубае и Абу-Даби | eVisa-Card.com"),

    # ── Page H1 titles ────────────────────────────────────────────────────────
    ("Expat Guide: Living in Thailand 2026",
     "Руководство для экспатов: Жизнь в Таиланде 2026"),
    ("Expat Guide: Living in Portugal 2026",
     "Руководство для экспатов: Жизнь в Португалии 2026"),
    ("Expat Guide: Living in Spain 2026",
     "Руководство для экспатов: Жизнь в Испании 2026"),
    ("Expat Guide: Living in Japan 2026",
     "Руководство для экспатов: Жизнь в Японии 2026"),
    ("Expat Guide: Living in Vietnam 2026",
     "Руководство для экспатов: Жизнь во Вьетнаме 2026"),
    ("Expat Guide: Living in Cambodia 2026",
     "Руководство для экспатов: Жизнь в Камбодже 2026"),
    ("Expat Guide: Living in Malaysia 2026",
     "Руководство для экспатов: Жизнь в Малайзии 2026"),
    ("Expat Guide: Living in Georgia 2026",
     "Руководство для экспатов: Жизнь в Грузии 2026"),
    ("Expat Guide: Living in Greece 2026",
     "Руководство для экспатов: Жизнь в Греции 2026"),
    ("Expat Guide: Living in Mexico 2026",
     "Руководство для экспатов: Жизнь в Мексике 2026"),
    ("Expat Guide: Living in Colombia 2026",
     "Руководство для экспатов: Жизнь в Колумбии 2026"),
    ("Expat Guide: Living in Panama 2026",
     "Руководство для экспатов: Жизнь в Панаме 2026"),
    ("Expat Guide: Living in Paraguay 2026",
     "Руководство для экспатов: Жизнь в Парагвае 2026"),
    ("Expat Guide: Living in Costa Rica 2026",
     "Руководство для экспатов: Жизнь в Коста-Рике 2026"),
    ("Expat Guide: Living in Laos 2026",
     "Руководство для экспатов: Жизнь в Лаосе 2026"),
    ("Expat Guide: Living in the UAE 2026",
     "Руководство для экспатов: Жизнь в ОАЭ 2026"),

    # ── Breadcrumb "Home" link ─────────────────────────────────────────────────
    ('>Home <i class="fa fa-chevron-right"></i></a>',
     '>Главная <i class="fa fa-chevron-right"></i></a>'),

    # ── Breadcrumb expat guide label ───────────────────────────────────────────
    ('Expat Guide Thailand <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Таиланд <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Portugal <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Португалия <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Spain <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Испания <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Japan <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Япония <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Vietnam <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Вьетнам <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Cambodia <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Камбоджа <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Malaysia <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Малайзия <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Georgia <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Грузия <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Greece <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Греция <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Mexico <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Мексика <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Colombia <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Колумбия <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Panama <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Панама <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Paraguay <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Парагвай <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Costa Rica <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Коста-Рика <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide Laos <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: Лаос <i class="fa fa-chevron-right"></i>'),
    ('Expat Guide UAE <i class="fa fa-chevron-right"></i>',
     'Руководство для экспатов: ОАЭ <i class="fa fa-chevron-right"></i>'),

    # ── "at a Glance" section headings ────────────────────────────────────────
    ("Thailand at a Glance", "Обзор Таиланда"),
    ("Portugal at a Glance", "Обзор Португалии"),
    ("Spain at a Glance", "Обзор Испании"),
    ("Japan at a Glance", "Обзор Японии"),
    ("Vietnam at a Glance", "Обзор Вьетнама"),
    ("Cambodia at a Glance", "Обзор Камбоджи"),
    ("Malaysia at a Glance", "Обзор Малайзии"),
    ("Georgia at a Glance", "Обзор Грузии"),
    ("Greece at a Glance", "Обзор Греции"),
    ("Mexico at a Glance", "Обзор Мексики"),
    ("Colombia at a Glance", "Обзор Колумбии"),
    ("Panama at a Glance", "Обзор Панамы"),
    ("Paraguay at a Glance", "Обзор Парагвая"),
    ("Costa Rica at a Glance", "Обзор Коста-Рики"),
    ("Laos at a Glance", "Обзор Лаоса"),
    ("UAE at a Glance", "Обзор ОАЭ"),

    # ── Key fact labels ───────────────────────────────────────────────────────
    ("<strong>Capital</strong>", "<strong>Столица</strong>"),
    ("<strong>Currency</strong>", "<strong>Валюта</strong>"),
    ("<strong>Language</strong>", "<strong>Язык</strong>"),
    ("<strong>Time Zone</strong>", "<strong>Часовой пояс</strong>"),
    ("<strong>Climate</strong>", "<strong>Климат</strong>"),

    # ── Last updated line ─────────────────────────────────────────────────────
    ("Last updated: March 2026", "Последнее обновление: март 2026"),
    ("Updated March 2026", "Обновлено: март 2026"),

    # ── Section headings ─────────────────────────────────────────────────────
    ("Visa &amp; Residency Options", "Варианты виз и проживания"),
    ("Visa & Residency Options", "Варианты виз и проживания"),

    # Step-by-Step with country names
    ("Step-by-Step: How to Move to Thailand",
     "Пошаговое руководство по переезду в Таиланд"),
    ("Step-by-Step: How to Move to Portugal",
     "Пошаговое руководство по переезду в Португалию"),
    ("Step-by-Step: How to Move to Spain",
     "Пошаговое руководство по переезду в Испанию"),
    ("Step-by-Step: How to Move to Japan",
     "Пошаговое руководство по переезду в Японию"),
    ("Step-by-Step: How to Move to Vietnam",
     "Пошаговое руководство по переезду во Вьетнам"),
    ("Step-by-Step: How to Move to Cambodia",
     "Пошаговое руководство по переезду в Камбоджу"),
    ("Step-by-Step: How to Move to Malaysia",
     "Пошаговое руководство по переезду в Малайзию"),
    ("Step-by-Step: How to Move to Georgia",
     "Пошаговое руководство по переезду в Грузию"),
    ("Step-by-Step: How to Move to Greece",
     "Пошаговое руководство по переезду в Грецию"),
    ("Step-by-Step: How to Move to Mexico",
     "Пошаговое руководство по переезду в Мексику"),
    ("Step-by-Step: How to Move to Colombia",
     "Пошаговое руководство по переезду в Колумбию"),
    ("Step-by-Step: How to Move to Panama",
     "Пошаговое руководство по переезду в Панаму"),
    ("Step-by-Step: How to Move to Paraguay",
     "Пошаговое руководство по переезду в Парагвай"),
    ("Step-by-Step: How to Move to Costa Rica",
     "Пошаговое руководство по переезду в Коста-Рику"),
    ("Step-by-Step: How to Move to Laos",
     "Пошаговое руководство по переезду в Лаос"),
    ("Step-by-Step: How to Move to the UAE",
     "Пошаговое руководство по переезду в ОАЭ"),

    # Practical sections
    ("🏠 Housing", "🏠 Жильё"),
    ("🏦 Banking", "🏦 Банковские услуги"),
    ("🏥 Healthcare", "🏥 Здравоохранение"),

    # "Стоимость of Living" already partially translated – fix remaining variants
    ("Стоимость of Living", "Стоимость жизни"),
    ("💰 Стоимость of Living", "💰 Стоимость жизни"),
    # handle raw English "Cost of Living" that may remain
    ("Cost of Living", "Стоимость жизни"),
    ("💰 Cost of Living", "💰 Стоимость жизни"),

    ("Frequently Asked Questions", "Часто задаваемые вопросы"),

    # ── Tax section ───────────────────────────────────────────────────────────
    ("Tax &amp; Fiscal Exile", "Налоги и фискальная эмиграция"),
    ("Tax & Fiscal Exile", "Налоги и фискальная эмиграция"),
    ("Capital Gains Tax", "Налог на прирост капитала"),
    ("Tax Regime", "Налоговый режим"),
    ("Crypto-Friendliness", "Отношение к крипто"),
    ("Exit Tax", "Налог при выезде"),
    ("Key Tax Points", "Ключевые налоговые аспекты"),
    ("Simulate Your Tax Savings", "Рассчитайте свою налоговую экономию"),
    ("Use our free tax exile simulator to compare your tax savings",
     "Используйте наш бесплатный симулятор для сравнения налоговой экономии"),
    ("Tax information provided for general guidance only. Consult a qualified tax advisor before making relocation decisions.",
     "Налоговая информация предоставлена исключительно в ознакомительных целях. Проконсультируйтесь с квалифицированным налоговым советником перед принятием решений о переезде."),

    # ── Author box ────────────────────────────────────────────────────────────
    ("Editorial Team — eVisa-Card.com", "Редакционная команда — eVisa-Card.com"),
    (">Expat guides written by travel experts, immigration specialists and expats with first-hand experience in",
     ">Руководства для экспатов, написанные экспертами по путешествиям, специалистами по иммиграции и экспатами с личным опытом в"),
    ("&#x2714; Verified information", "&#x2714; Проверенная информация"),
    ("&#x2714; Updated March 2026", "&#x2714; Обновлено в марте 2026"),
    ("&#x2714; Official sources cited", "&#x2714; Официальные источники"),

    # ── Official Sources section ───────────────────────────────────────────────
    ("&#128218; Official Sources &amp; References",
     "&#128218; Официальные источники и ссылки"),

    # ── Pro Tips (if present) ─────────────────────────────────────────────────
    ("Pro Tips", "Советы экспертов"),

    # ── Table headers ─────────────────────────────────────────────────────────
    (">Visa Type<", ">Тип визы<"),
    (">Stay<", ">Срок пребывания<"),
    (">Requirements<", ">Требования<"),
    (">Best For<", ">Лучший для<"),
    (">Fee<", ">Стоимость<"),
    (">Processing<", ">Срок оформления<"),

    # "Mandatory / Recommended / Optional" badge labels
    (">Mandatory<", ">Обязательно<"),
    (">Recommended<", ">Рекомендуется<"),
    (">Optional<", ">По желанию<"),
    ("Mandatory</", "Обязательно</"),
    ("Recommended</", "Рекомендуется</"),
    ("Optional</", "По желанию</"),

    # Per-period labels
    ("/year", " в год"),
    ("/month", " в месяц"),
    ("/night", " за ночь"),
    ("per year", "в год"),
    ("per month", "в месяц"),
    ("per night", "за ночь"),

    # Yes / No
    (">Yes<", ">Да<"),
    (">No<", ">Нет<"),

    # ── Footer ────────────────────────────────────────────────────────────────
    ("Global eVisa &amp; Travel Information Platform",
     "Глобальная платформа информации об электронных визах и путешествиях"),
    ("Global eVisa & Travel Information Platform",
     "Глобальная платформа информации об электронных визах и путешествиях"),
    ("Follow eVisa-Card.com", "Следите за eVisa-Card.com"),

    # ── Fix residual partial translations ─────────────────────────────────────
    # "Стоимостьs" → "Стоимости" (plural artifact from prior partial translate)
    ("Стоимостьs", "Стоимости"),
    # "Стоимостьa" → "Коста" (Spain Costa region artifact)
    ("Стоимостьa del Sol", "Коста-дель-Соль"),
    ("Стоимостьa Blanca", "Коста-Бланка"),
    # "Услуга" → "Служба" (from partial translation of "Service")
    ("National Health Услуга", "Национальная служба здравоохранения"),
    ("Immigration Услугаs Agency", "Агентство иммиграционных услуг"),
]


def translate_file(filepath: str) -> tuple[int, int]:
    """Translate a single HTML file. Returns (replacements_made, patterns_applied)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    total_changes = 0
    patterns_applied = 0

    for pattern, replacement in REPLACEMENTS:
        if pattern in content:
            count = content.count(pattern)
            content = content.replace(pattern, replacement)
            total_changes += count
            patterns_applied += 1

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    return total_changes, patterns_applied


def main():
    files = sorted(glob.glob(os.path.join(RU_DIR, "expat-guide-*.html")))
    if not files:
        print(f"No expat-guide-*.html files found in {RU_DIR}")
        return

    print(f"Found {len(files)} expat guide files in {RU_DIR}\n")

    grand_total = 0
    for filepath in files:
        name = os.path.basename(filepath)
        changes, patterns = translate_file(filepath)
        grand_total += changes
        if changes:
            print(f"  [OK] {name:45s} {changes:4d} replacement(s) across {patterns} pattern(s)")
        else:
            print(f"  [--] {name:45s}  (no changes needed)")

    print(f"\nDone. Total replacements made: {grand_total}")


if __name__ == "__main__":
    main()
