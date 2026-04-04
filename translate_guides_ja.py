#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
translate_guides_ja.py
Translates remaining English text in JA (Japanese) expat guide HTML files.
"""

import os
import re

JA_DIR = os.path.join(os.path.dirname(__file__), "www", "ja")

# ---------------------------------------------------------------------------
# Ordered replacement table  (longest / most specific first where needed)
# Each entry: (exact_string_to_find, replacement)
# We use plain str.replace so the order matters for overlapping patterns.
# ---------------------------------------------------------------------------

REPLACEMENTS = [
    # -----------------------------------------------------------------------
    # Title tag translations
    # -----------------------------------------------------------------------
    ("Expat Guide Thailand 2026 — How to Live in Thailand | eVisa-Card.com",
     "タイ移住ガイド2026 — タイでの生活 | eVisa-Card.com"),
    ("Expat Guide Vietnam 2026 — How to Live in Vietnam | eVisa-Card.com",
     "ベトナム移住ガイド2026 — ベトナムでの生活 | eVisa-Card.com"),
    ("Expat Guide Portugal 2026 — How to Live in Portugal | eVisa-Card.com",
     "ポルトガル移住ガイド2026 — ポルトガルでの生活 | eVisa-Card.com"),
    ("Expat Guide Spain 2026 — How to Live in Spain | eVisa-Card.com",
     "スペイン移住ガイド2026 — スペインでの生活 | eVisa-Card.com"),
    ("Expat Guide Japan 2026 — How to Live in Japan | eVisa-Card.com",
     "日本移住ガイド2026 — 日本での生活 | eVisa-Card.com"),
    ("Expat Guide Malaysia 2026 — How to Live in Malaysia | eVisa-Card.com",
     "マレーシア移住ガイド2026 — マレーシアでの生活 | eVisa-Card.com"),
    ("Expat Guide UAE 2026 — How to Live in Dubai & Abu Dhabi | eVisa-Card.com",
     "UAE移住ガイド2026 — ドバイ・アブダビでの生活 | eVisa-Card.com"),
    ("Expat Guide Mexico 2026 — How to Live in Mexico | eVisa-Card.com",
     "メキシコ移住ガイド2026 — メキシコでの生活 | eVisa-Card.com"),
    ("Expat Guide Colombia 2026 — How to Live in Colombia | eVisa-Card.com",
     "コロンビア移住ガイド2026 — コロンビアでの生活 | eVisa-Card.com"),
    ("Expat Guide Costa Rica 2026 — How to Live in Costa Rica | eVisa-Card.com",
     "コスタリカ移住ガイド2026 — コスタリカでの生活 | eVisa-Card.com"),
    ("Expat Guide Panama 2026 — How to Live in Panama | eVisa-Card.com",
     "パナマ移住ガイド2026 — パナマでの生活 | eVisa-Card.com"),
    ("Expat Guide Paraguay 2026 — How to Live in Paraguay | eVisa-Card.com",
     "パラグアイ移住ガイド2026 — パラグアイでの生活 | eVisa-Card.com"),
    ("Expat Guide Greece 2026 — How to Live in Greece | eVisa-Card.com",
     "ギリシャ移住ガイド2026 — ギリシャでの生活 | eVisa-Card.com"),
    ("Expat Guide Georgia 2026 — How to Live in Georgia | eVisa-Card.com",
     "ジョージア移住ガイド2026 — ジョージアでの生活 | eVisa-Card.com"),
    ("Expat Guide Cambodia 2026 — How to Live in Cambodia | eVisa-Card.com",
     "カンボジア移住ガイド2026 — カンボジアでの生活 | eVisa-Card.com"),
    ("Expat Guide Laos 2026 — How to Live in Laos | eVisa-Card.com",
     "ラオス移住ガイド2026 — ラオスでの生活 | eVisa-Card.com"),

    # -----------------------------------------------------------------------
    # Hero breadcrumbs (keep country names in English as proper nouns)
    # -----------------------------------------------------------------------
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Thailand <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>タイ移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Vietnam <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>ベトナム移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Portugal <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>ポルトガル移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Spain <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>スペイン移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Japan <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>日本移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Malaysia <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>マレーシア移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide UAE <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>UAE移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Mexico <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>メキシコ移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Colombia <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>コロンビア移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Costa Rica <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>コスタリカ移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Panama <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>パナマ移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Paraguay <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>パラグアイ移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Greece <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>ギリシャ移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Georgia <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>ジョージア移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Cambodia <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>カンボジア移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),
    (">Home <i class=\"fa fa-chevron-right\"></i></a></span> <span>Expat Guide Laos <i class=\"fa fa-chevron-right\"></i></span>",
     ">ホーム <i class=\"fa fa-chevron-right\"></i></a></span> <span>ラオス移住ガイド <i class=\"fa fa-chevron-right\"></i></span>"),

    # -----------------------------------------------------------------------
    # H1 page headings  (without year — Colombia has a different format)
    # -----------------------------------------------------------------------
    ("Expat Guide: Living in Colombia",
     "海外移住ガイド：コロンビア生活"),

    # Step-by-Step with "Moving" variant
    ("Step-by-Step: Moving to Colombia",
     "コロンビアへの移住ステップバイステップガイド"),
    ("Step-by-Step: Moving to Cambodia",
     "カンボジアへの移住ステップバイステップガイド"),
    ("Step-by-Step: Moving to Laos",
     "ラオスへの移住ステップバイステップガイド"),
    ("Step-by-Step: Moving to Georgia",
     "ジョージアへの移住ステップバイステップガイド"),
    ("Step-by-Step: Moving to Greece",
     "ギリシャへの移住ステップバイステップガイド"),
    ("Step-by-Step: Moving to Panama",
     "パナマへの移住ステップバイステップガイド"),
    ("Step-by-Step: Moving to Paraguay",
     "パラグアイへの移住ステップバイステップガイド"),
    ("Step-by-Step: Moving to Costa Rica",
     "コスタリカへの移住ステップバイステップガイド"),
    ("Step-by-Step: Moving to Malaysia",
     "マレーシアへの移住ステップバイステップガイド"),
    ("Step-by-Step: Moving to Mexico",
     "メキシコへの移住ステップバイステップガイド"),

    # -----------------------------------------------------------------------
    # H1 page headings  "Expat Guide: Living in X 2026"
    # -----------------------------------------------------------------------
    ("Expat Guide: Living in Thailand 2026",
     "海外移住ガイド：2026年のタイ生活"),
    ("Expat Guide: Living in Vietnam 2026",
     "海外移住ガイド：2026年のベトナム生活"),
    ("Expat Guide: Living in Portugal 2026",
     "海外移住ガイド：2026年のポルトガル生活"),
    ("Expat Guide: Living in Spain 2026",
     "海外移住ガイド：2026年のスペイン生活"),
    ("Expat Guide: Living in Japan 2026",
     "海外移住ガイド：2026年の日本生活"),
    ("Expat Guide: Living in Malaysia 2026",
     "海外移住ガイド：2026年のマレーシア生活"),
    ("Expat Guide: Living in the UAE 2026",
     "海外移住ガイド：2026年のUAE生活"),
    ("Expat Guide: Living in Mexico 2026",
     "海外移住ガイド：2026年のメキシコ生活"),
    ("Expat Guide: Living in Colombia 2026",
     "海外移住ガイド：2026年のコロンビア生活"),
    ("Expat Guide: Living in Costa Rica 2026",
     "海外移住ガイド：2026年のコスタリカ生活"),
    ("Expat Guide: Living in Panama 2026",
     "海外移住ガイド：2026年のパナマ生活"),
    ("Expat Guide: Living in Paraguay 2026",
     "海外移住ガイド：2026年のパラグアイ生活"),
    ("Expat Guide: Living in Greece 2026",
     "海外移住ガイド：2026年のギリシャ生活"),
    ("Expat Guide: Living in Georgia 2026",
     "海外移住ガイド：2026年のジョージア生活"),
    ("Expat Guide: Living in Cambodia 2026",
     "海外移住ガイド：2026年のカンボジア生活"),
    ("Expat Guide: Living in Laos 2026",
     "海外移住ガイド：2026年のラオス生活"),

    # -----------------------------------------------------------------------
    # "at a Glance" country boxes
    # -----------------------------------------------------------------------
    ("Thailand at a Glance", "タイ概要"),
    ("Vietnam at a Glance", "ベトナム概要"),
    ("Portugal at a Glance", "ポルトガル概要"),
    ("Spain at a Glance", "スペイン概要"),
    ("Japan at a Glance", "日本概要"),
    ("Malaysia at a Glance", "マレーシア概要"),
    ("UAE at a Glance", "UAE概要"),
    ("Mexico at a Glance", "メキシコ概要"),
    ("Colombia at a Glance", "コロンビア概要"),
    ("Costa Rica at a Glance", "コスタリカ概要"),
    ("Panama at a Glance", "パナマ概要"),
    ("Paraguay at a Glance", "パラグアイ概要"),
    ("Greece at a Glance", "ギリシャ概要"),
    ("Georgia at a Glance", "ジョージア概要"),
    ("Cambodia at a Glance", "カンボジア概要"),
    ("Laos at a Glance", "ラオス概要"),

    # -----------------------------------------------------------------------
    # Key Facts labels (strong tags inside at-a-glance boxes)
    # -----------------------------------------------------------------------
    ("<strong>Capital</strong>", "<strong>首都</strong>"),
    ("<strong>Currency</strong>", "<strong>通貨</strong>"),
    ("<strong>Language</strong>", "<strong>言語</strong>"),
    ("<strong>Time Zone</strong>", "<strong>タイムゾーン</strong>"),
    ("<strong>Climate</strong>", "<strong>気候</strong>"),
    ("<strong>Schengen Area</strong>", "<strong>シェンゲン圏</strong>"),
    ("<strong>Schengen</strong>", "<strong>シェンゲン</strong>"),
    ("<strong>Income Tax</strong>", "<strong>所得税</strong>"),

    # "費用 of Living" is already partially translated but inconsistently:
    # Some files use 費用 of Living; standardise to 生活費
    ("<strong>費用 of Living</strong>", "<strong>生活費</strong>"),
    ("<strong>Cost of Living</strong>", "<strong>生活費</strong>"),

    # -----------------------------------------------------------------------
    # Section headings
    # -----------------------------------------------------------------------
    # Visa section
    (">Visa &amp; Residency Options<", ">ビザ・在留資格オプション<"),
    (">Visa & Residency Options<", ">ビザ・在留資格オプション<"),

    # Step-by-step section headings (country specific)
    ("Step-by-Step: How to Move to Thailand",
     "タイへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Vietnam",
     "ベトナムへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Portugal",
     "ポルトガルへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Spain",
     "スペインへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Japan",
     "日本への移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Malaysia",
     "マレーシアへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to the UAE",
     "UAEへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Mexico",
     "メキシコへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Colombia",
     "コロンビアへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Costa Rica",
     "コスタリカへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Panama",
     "パナマへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Paraguay",
     "パラグアイへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Greece",
     "ギリシャへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Georgia",
     "ジョージアへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Cambodia",
     "カンボジアへの移住ステップバイステップガイド"),
    ("Step-by-Step: How to Move to Laos",
     "ラオスへの移住ステップバイステップガイド"),

    # FAQ heading
    (">Frequently Asked Questions<",
     ">よくある質問<"),

    # Tax section heading (appears with whitespace in h2)
    ("&#128176; Tax &amp; Fiscal Exile",
     "&#128176; 税制・財政亡命"),
    ("&#128176; Tax & Fiscal Exile",
     "&#128176; 税制・財政亡命"),

    # -----------------------------------------------------------------------
    # Practical info card headings (emoji + English)
    # -----------------------------------------------------------------------
    (">🏠 Housing<", ">🏠 住居<"),
    (">🏦 Banking<", ">🏦 銀行サービス<"),
    (">🏥 Healthcare<", ">🏥 医療<"),
    # "費用 of Living" already partially translated; cover all variants
    (">💰 費用 of Living<", ">💰 生活費<"),
    (">💰 Cost of Living<", ">💰 生活費<"),

    # -----------------------------------------------------------------------
    # Tax card labels (uppercase small text inside cards)
    # -----------------------------------------------------------------------
    (">Capital Gains Tax<", ">キャピタルゲイン税<"),
    (">Tax Regime<", ">税制<"),
    (">Crypto-Friendliness<", ">暗号資産フレンドリー度<"),
    (">Exit Tax<", ">出国税<"),

    # -----------------------------------------------------------------------
    # Tax section body text labels
    # -----------------------------------------------------------------------
    ("<strong>Capital Gains Tax:</strong>", "<strong>キャピタルゲイン税：</strong>"),
    (">Key Tax Points<", ">税制の重要ポイント<"),
    (">Simulate Your Tax Savings<", ">税金節約シミュレーション<"),
    ("&#128640; Simulate Your Tax Savings &rarr;",
     "&#128640; 税金節約シミュレーション &rarr;"),

    # Tax CTA body text (country-specific)
    ("Use our free tax exile simulator to compare your tax savings in Thailand.",
     "無料の財政亡命シミュレーターでタイでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Vietnam.",
     "無料の財政亡命シミュレーターでベトナムでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Portugal.",
     "無料の財政亡命シミュレーターでポルトガルでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Spain.",
     "無料の財政亡命シミュレーターでスペインでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Japan.",
     "無料の財政亡命シミュレーターで日本での節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Malaysia.",
     "無料の財政亡命シミュレーターでマレーシアでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in UAE.",
     "無料の財政亡命シミュレーターでUAEでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Mexico.",
     "無料の財政亡命シミュレーターでメキシコでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Colombia.",
     "無料の財政亡命シミュレーターでコロンビアでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Costa Rica.",
     "無料の財政亡命シミュレーターでコスタリカでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Panama.",
     "無料の財政亡命シミュレーターでパナマでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Paraguay.",
     "無料の財政亡命シミュレーターでパラグアイでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Greece.",
     "無料の財政亡命シミュレーターでギリシャでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Georgia.",
     "無料の財政亡命シミュレーターでジョージアでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Cambodia.",
     "無料の財政亡命シミュレーターでカンボジアでの節税額を比較しましょう。"),
    ("Use our free tax exile simulator to compare your tax savings in Laos.",
     "無料の財政亡命シミュレーターでラオスでの節税額を比較しましょう。"),
    ("Compare tax rates across 27+ countries with our interactive simulator",
     "インタラクティブシミュレーターで27カ国以上の税率を比較"),

    # Tax disclaimer
    ("<em>Tax information provided for general guidance only. Consult a qualified tax advisor before making relocation decisions.</em>",
     "<em>税務情報は一般的な参考情報として提供されています。移住の決定前に資格のある税務アドバイザーにご相談ください。</em>"),

    # -----------------------------------------------------------------------
    # Official Sources section
    # -----------------------------------------------------------------------
    (">&#128218; Official Sources &amp; References<",
     ">&#128218; 公式情報源・参考資料<"),
    (">&#128218; Official Sources & References<",
     ">&#128218; 公式情報源・参考資料<"),

    # -----------------------------------------------------------------------
    # Author box
    # -----------------------------------------------------------------------
    (">Editorial Team — eVisa-Card.com<",
     ">編集チーム — eVisa-Card.com<"),
    # Country-specific author box descriptions
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Thailand.",
     "タイでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Vietnam.",
     "ベトナムでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Portugal.",
     "ポルトガルでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Spain.",
     "スペインでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Japan.",
     "日本での実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Malaysia.",
     "マレーシアでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in the UAE.",
     "UAEでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Mexico.",
     "メキシコでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Colombia.",
     "コロンビアでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Costa Rica.",
     "コスタリカでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Panama.",
     "パナマでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Paraguay.",
     "パラグアイでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Greece.",
     "ギリシャでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Georgia.",
     "ジョージアでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Cambodia.",
     "カンボジアでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),
    ("Expat guides written by travel experts, immigration specialists and expats with first-hand experience in Laos.",
     "ラオスでの実体験を持つ旅行専門家、入国管理専門家、駐在員によって執筆された移住ガイドです。"),

    # Verified info footer in author box
    ("&#x2714; Verified information", "&#x2714; 検証済み情報"),
    ("&#x2714; Updated March 2026", "&#x2714; 2026年3月更新"),
    ("&#x2714; Official sources cited", "&#x2714; 公式情報源引用"),

    # -----------------------------------------------------------------------
    # "Last updated" line
    # -----------------------------------------------------------------------
    ("Last updated: March 2026 — <em>編集チーム, eVisa-Card.com</em>",
     "最終更新：2026年3月 — <em>編集チーム, eVisa-Card.com</em>"),
    # Some files use 12px font-size variant
    ("Last updated: March 2026 — 編集チーム, eVisa-Card.com",
     "最終更新：2026年3月 — 編集チーム, eVisa-Card.com"),

    # -----------------------------------------------------------------------
    # "Yes" / "No" standalone values inside tax cards
    # (wrapped in style tags — match the full inline context)
    # -----------------------------------------------------------------------
    (">Yes (> 100M JPY in assets)<", ">はい（1億円超の資産）<"),
    (">Yes (> 4 years residency, > 4M assets)<", ">はい（居住4年超・資産400万ユーロ超）<"),
    # Generic Yes/No at end of div content for tax cards only
    (";color:#28a745;\">No<", ";color:#28a745;\">いいえ<"),
    (";color:#dc3545;\">Yes<", ";color:#dc3545;\">はい<"),

    # -----------------------------------------------------------------------
    # Country intro paragraphs
    # -----------------------------------------------------------------------
    ("Thailand is one of the world's top expat destinations, attracting retirees, digital nomads and families with its warm climate, affordable cost of living, world-class cuisine and welcoming culture. This guide walks you through everything you need to know to relocate to Thailand in 2026.",
     "タイは世界有数の海外移住先であり、温暖な気候、手頃な生活費、世界水準の料理、そして温かい文化で退職者、デジタルノマド、家族連れを惹きつけています。このガイドでは、2026年にタイへ移住するために必要なすべての情報をお伝えします。"),

    ("Vietnam has emerged as one of Southeast Asia's top expat and digital nomad destinations, with ultra-low cost of living, vibrant cities, and stunning landscapes. Hanoi, Ho Chi Minh City, Da Nang and Hoi An offer exceptional quality of life at a fraction of Western costs.",
     "ベトナムは東南アジアを代表する移住・デジタルノマドの目的地として台頭しており、超低コストの生活費、活気ある都市、絶景の自然が魅力です。ハノイ、ホーチミン市、ダナン、ホイアンは欧米の一部のコストで卓越した生活水準を提供しています。"),

    ("Portugal has become one of Europe's most sought-after expat destinations, offering a D7 Passive Income Visa, Golden Visa, affordable cost of living compared to Western Europe, mild climate, safety, and the NHR tax regime for significant tax savings. This guide covers everything you need to relocate to Portugal.",
     "ポルトガルはヨーロッパで最も人気の移住先の一つとなっており、D7パッシブインカムビザ、ゴールデンビザ、西欧と比べて手頃な生活費、温暖な気候、安全性、そして大幅な節税が可能なNHR税制を提供しています。このガイドではポルトガルへの移住に必要なすべてをカバーしています。"),

    ("Spain remains one of the world's top expat destinations thanks to its Mediterranean climate, vibrant culture, excellent healthcare, high quality of life and relatively affordable cost of living outside major cities. Whether you're retiring, working remotely or starting a business, Spain has a path for you.",
     "スペインは地中海性気候、活気ある文化、優れた医療制度、高い生活水準、そして主要都市以外では比較的手頃な生活費により、世界有数の海外移住先であり続けています。退職、リモートワーク、起業など、あなたのニーズに合ったビザがあります。"),

    ("Japan offers a unique expat experience: ultra-safe, technologically advanced, culturally rich and with excellent public services. Tokyo, Osaka, Kyoto and Fukuoka attract expats with high quality of life, world-class healthcare and efficient public transport. Japan introduced a digital nomad visa in 2024.",
     "日本は超安全、技術先進、文化豊かで優れた公共サービスを誇るユニークな移住体験を提供します。東京、大阪、京都、福岡は高い生活水準、世界水準の医療、効率的な公共交通で移住者を引き付けています。日本は2024年にデジタルノマドビザを導入しました。"),

    ("The United Arab Emirates offers one of the world's most attractive expat packages: zero income tax, world-class infrastructure, multicultural society and a strategic location between East and West. Dubai and Abu Dhabi attract professionals, entrepreneurs and retirees with multiple residency pathways introduced in recent years.",
     "アラブ首長国連邦は世界で最も魅力的な移住先の一つであり、所得税ゼロ、世界水準のインフラ、多文化社会、そして東西を結ぶ戦略的な立地を誇ります。ドバイとアブダビは近年導入された複数の在留資格ルートで専門職、起業家、退職者を惹きつけています。"),

    # -----------------------------------------------------------------------
    # Full Visa Requirements links
    # -----------------------------------------------------------------------
    ("→ Full Thailand Visa Requirements &amp; Application Guide",
     "→ タイのビザ要件・申請ガイド（完全版）"),
    ("→ Full Thailand Visa Requirements & Application Guide",
     "→ タイのビザ要件・申請ガイド（完全版）"),
    ("→ Full Vietnam Visa Requirements Guide",
     "→ ベトナムのビザ要件ガイド（完全版）"),
    ("→ Full Portugal Visa Requirements &amp; Application Guide",
     "→ ポルトガルのビザ要件・申請ガイド（完全版）"),
    ("→ Full Portugal Visa Requirements & Application Guide",
     "→ ポルトガルのビザ要件・申請ガイド（完全版）"),
    ("→ Full Spain Visa Requirements Guide",
     "→ スペインのビザ要件ガイド（完全版）"),
    ("→ Full Japan Visa Requirements Guide",
     "→ 日本のビザ要件ガイド（完全版）"),
    ("→ Full Malaysia Visa Requirements Guide",
     "→ マレーシアのビザ要件ガイド（完全版）"),
    ("→ Full UAE Visa Requirements Guide",
     "→ UAEのビザ要件ガイド（完全版）"),
    ("→ Full Mexico Visa Requirements Guide",
     "→ メキシコのビザ要件ガイド（完全版）"),
    ("→ Full Colombia Visa Requirements Guide",
     "→ コロンビアのビザ要件ガイド（完全版）"),
    ("→ Full Costa Rica Visa Requirements Guide",
     "→ コスタリカのビザ要件ガイド（完全版）"),
    ("→ Full Panama Visa Requirements Guide",
     "→ パナマのビザ要件ガイド（完全版）"),
    ("→ Full Paraguay Visa Requirements Guide",
     "→ パラグアイのビザ要件ガイド（完全版）"),
    ("→ Full Greece Visa Requirements Guide",
     "→ ギリシャのビザ要件ガイド（完全版）"),
    ("→ Full Georgia Visa Requirements Guide",
     "→ ジョージアのビザ要件ガイド（完全版）"),
    ("→ Full Cambodia Visa Requirements Guide",
     "→ カンボジアのビザ要件ガイド（完全版）"),
    ("→ Full Laos Visa Requirements Guide",
     "→ ラオスのビザ要件ガイド（完全版）"),

    # -----------------------------------------------------------------------
    # Powered by line
    # -----------------------------------------------------------------------
    ("Powered by", "提供："),

    # -----------------------------------------------------------------------
    # Meta description (generic English pattern)
    # -----------------------------------------------------------------------
    # These are already English in the meta but let's leave them as-is
    # (Google indexes the Japanese page; meta description is not user-facing UI)

    # -----------------------------------------------------------------------
    # Table of Contents link text (detailed-format pages)
    # -----------------------------------------------------------------------
    (">Visa &amp; Residency<", ">ビザ・在留資格<"),
    (">Visa & Residency<", ">ビザ・在留資格<"),
    (">Healthcare<", ">医療<"),
    (">Health Insurance<", ">健康保険<"),
    (">Bank Account<", ">銀行口座<"),
    (">Buying Property<", ">不動産購入<"),
    (">Tax &amp; Fiscal Exile<", ">税制・財政亡命<"),
    (">Tax & Fiscal Exile<", ">税制・財政亡命<"),
    (">Cost of Living<", ">生活費<"),

    # -----------------------------------------------------------------------
    # Section headings with emoji prefix (detailed-format pages)
    # -----------------------------------------------------------------------
    ("🛂 Visa & Residency Options", "🛂 ビザ・在留資格オプション"),
    ("🛂 Visa &amp; Residency Options", "🛂 ビザ・在留資格オプション"),
    ("🏥 Healthcare in Cambodia", "🏥 カンボジアの医療"),
    ("🏥 Healthcare in Laos", "🏥 ラオスの医療"),
    ("🏥 Healthcare in Georgia", "🏥 ジョージアの医療"),
    ("🏥 Healthcare in Greece", "🏥 ギリシャの医療"),
    ("🏥 Healthcare in Panama", "🏥 パナマの医療"),
    ("🏥 Healthcare in Paraguay", "🏥 パラグアイの医療"),
    ("🏥 Healthcare in Colombia", "🏥 コロンビアの医療"),
    ("🏥 Healthcare in Costa Rica", "🏥 コスタリカの医療"),
    ("🏥 Healthcare in Mexico", "🏥 メキシコの医療"),
    ("🏥 Healthcare in Malaysia", "🏥 マレーシアの医療"),
    ("🏥 Healthcare in UAE", "🏥 UAEの医療"),
    ("🛡️ Health Insurance in Cambodia", "🛡️ カンボジアの健康保険"),
    ("🛡️ Health Insurance in Laos", "🛡️ ラオスの健康保険"),
    ("🛡️ Health Insurance in Georgia", "🛡️ ジョージアの健康保険"),
    ("🛡️ Health Insurance in Greece", "🛡️ ギリシャの健康保険"),
    ("🛡️ Health Insurance in Panama", "🛡️ パナマの健康保険"),
    ("🛡️ Health Insurance in Paraguay", "🛡️ パラグアイの健康保険"),
    ("🛡️ Health Insurance in Colombia", "🛡️ コロンビアの健康保険"),
    ("🛡️ Health Insurance in Costa Rica", "🛡️ コスタリカの健康保険"),
    ("🏦 Opening a Bank Account in Cambodia", "🏦 カンボジアでの銀行口座開設"),
    ("🏦 Opening a Bank Account in Laos", "🏦 ラオスでの銀行口座開設"),
    ("🏦 Opening a Bank Account in Georgia", "🏦 ジョージアでの銀行口座開設"),
    ("🏦 Opening a Bank Account in Greece", "🏦 ギリシャでの銀行口座開設"),
    ("🏦 Opening a Bank Account in Panama", "🏦 パナマでの銀行口座開設"),
    ("🏦 Opening a Bank Account in Paraguay", "🏦 パラグアイでの銀行口座開設"),
    ("🏦 Opening a Bank Account in Colombia", "🏦 コロンビアでの銀行口座開設"),
    ("🏦 Opening a Bank Account in Costa Rica", "🏦 コスタリカでの銀行口座開設"),
    ("🏠 Buying Property in Cambodia", "🏠 カンボジアでの不動産購入"),
    ("🏠 Buying Property in Laos", "🏠 ラオスでの不動産購入"),
    ("🏠 Buying Property in Georgia", "🏠 ジョージアでの不動産購入"),
    ("🏠 Buying Property in Greece", "🏠 ギリシャでの不動産購入"),
    ("🏠 Buying Property in Panama", "🏠 パナマでの不動産購入"),
    ("🏠 Buying Property in Paraguay", "🏠 パラグアイでの不動産購入"),
    ("🏠 Buying Property in Colombia", "🏠 コロンビアでの不動産購入"),
    ("🏠 Buying Property in Costa Rica", "🏠 コスタリカでの不動産購入"),
    ("📋 Table of Contents", "📋 目次"),

    # Step-by-Step Process as h3 (detailed pages)
    (">Step-by-Step Process<", ">ステップバイステップ手順<"),

    # at-a-glance table labels (td format, not strong tag)
    ("\">Capital<", "\">首都<"),
    ("\">Currency<", "\">通貨<"),
    ("\">Language<", "\">言語<"),
    ("\">Time Zone<", "\">タイムゾーン<"),
    ("\">Climate<", "\">気候<"),
    ("\">Monthly cost<", "\">月額費用<"),

    # Breadcrumb for detailed pages
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Cambodia<",
     ">移住ガイド <i class=\"fa fa-chevron-right\"></i></a></span> <span>カンボジア<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Laos<",
     ">移住ガイド <i class=\"fa fa-chevron-right\"></i></a></span> <span>ラオス<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Georgia<",
     ">移住ガイド <i class=\"fa fa-chevron-right\"></i></a></span> <span>ジョージア<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Greece<",
     ">移住ガイド <i class=\"fa fa-chevron-right\"></i></a></span> <span>ギリシャ<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Panama<",
     ">移住ガイド <i class=\"fa fa-chevron-right\"></i></a></span> <span>パナマ<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Paraguay<",
     ">移住ガイド <i class=\"fa fa-chevron-right\"></i></a></span> <span>パラグアイ<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Colombia<",
     ">移住ガイド <i class=\"fa fa-chevron-right\"></i></a></span> <span>コロンビア<"),
    (">Expat Guides <i class=\"fa fa-chevron-right\"></i></a></span> <span>Costa Rica<",
     ">移住ガイド <i class=\"fa fa-chevron-right\"></i></a></span> <span>コスタリカ<"),

    # Colombia heading format "Expat Guide: Living in Colombia 2026" in h1 (already covered above)
    # Colombia/Costa Rica last updated line (different format)
    ("Last updated: March 2026",
     "最終更新：2026年3月"),

    # -----------------------------------------------------------------------
    # Remaining inline English fragments in body text
    # -----------------------------------------------------------------------
    # "サービス" appears in some files already (partial translation artifact)
    # "費用" appears as partial translation artifact — normalise
    ("費用 of Living", "生活費"),
    ("費用s significantly lower", "費用は大幅に低く"),
    ("費用s high but insurance", "費用は高いが保険で"),
    ("費用a del Sol", "コスタ・デル・ソル"),
    ("費用a Blanca", "コスタ・ブランカ"),
    ("費用s 70-80% lower than USA", "費用は米国より70〜80%低い"),
    ("サービスs Agency", "サービス庁"),
    ("National Health サービス", "国民保健サービス"),

    # -----------------------------------------------------------------------
    # Footer copyright line  (some files still have English variant)
    # -----------------------------------------------------------------------
    ("Global eVisa &amp; Travel Information Platform",
     "グローバル電子ビザ・旅行情報プラットフォーム"),
    ("Global eVisa & Travel Information Platform",
     "グローバル電子ビザ・旅行情報プラットフォーム"),

    # eVisa-Card.com follow text (if present)
    ("Follow eVisa-Card.com", "eVisa-Card.comをフォロー"),
]


def translate_file(filepath: str) -> tuple[int, str]:
    """Apply all replacements to a single file. Returns (count, filepath)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    for eng, jpn in REPLACEMENTS:
        content = content.replace(eng, jpn)

    changes = sum(1 for a, b in zip(original, content) if a != b)
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return (1, filepath)
    return (0, filepath)


def main():
    files = [
        os.path.join(JA_DIR, f)
        for f in os.listdir(JA_DIR)
        if f.endswith(".html") and "expat-guide" in f
    ]
    files.sort()

    print(f"Processing {len(files)} file(s) in: {JA_DIR}\n")
    changed = 0
    for fp in files:
        status, path = translate_file(fp)
        label = "UPDATED" if status else "no change"
        print(f"  [{label}] {os.path.basename(path)}")
        changed += status

    print(f"\nDone. {changed}/{len(files)} file(s) updated.")


if __name__ == "__main__":
    main()
