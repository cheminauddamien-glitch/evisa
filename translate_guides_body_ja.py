#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translate remaining English body content in JA expat guide pages."""
import os

BASE = r"C:\Users\chemi\Documents\evisa\pacific-main\www\ja"

REPLACEMENTS = [
    # ── PAGE TITLES (remaining untranslated ones) ──────────────────────────
    ("Complete Expat Guide Cambodia 2026 — Live & Retire in Cambodia", "カンボジア移住ガイド2026 — カンボジアでの生活"),
    ("Expat Guide Colombia 2026 — Live & Work in Colombia | eVisa-Card.com", "コロンビア移住ガイド2026 — コロンビアでの生活 | eVisa-Card.com"),
    ("Complete Expat Guide Georgia 2026 — Live & Work in Georgia (Caucasus)", "ジョージア移住ガイド2026 — ジョージアでの生活"),
    ("Complete Expat Guide Greece 2026 — Live & Retire in Greece", "ギリシャ移住ガイド2026 — ギリシャでの生活"),
    ("Complete Expat Guide Laos 2026 — Live & Work in Laos", "ラオス移住ガイド2026 — ラオスでの生活"),
    ("Complete Expat Guide Panama 2026 — Live & Retire in Panama", "パナマ移住ガイド2026 — パナマでの生活"),
    ("Complete Expat Guide Paraguay 2026 — Live & Retire in Paraguay", "パラグアイ移住ガイド2026 — パラグアイでの生活"),
    ("Expat Guide UAE 2026 — How to Live in Dubai & Abu Dhabi | eVisa-Card.com", "UAE移住ガイド2026 — ドバイ・アブダビでの生活 | eVisa-Card.com"),
    ("Complete Expat Guide Costa Rica 2026 — Live & Retire in Costa Rica", "コスタリカ移住ガイド2026 — コスタリカでの生活"),

    # ── VISA SECTION PARAGRAPHS ──────────────────────────────────────────────
    ("Thailand offers several long-stay options: the Tourist Visa (60 days, extendable), Non-Immigrant O-A Retirement Visa (1 year, renewable, for 50+), Thailand Elite Visa (5–20 years, premium), Long-Term Resident (LTR) Visa for professionals and digital nomads. There is no standard permanent residency path but long-term visa holders can renew indefinitely.",
     "タイには複数の長期滞在オプションがあります：観光ビザ（60日間、延長可）、非移民O-A退職ビザ（1年間、更新可能、50歳以上）、タイエリートビザ（5〜20年間、プレミアム）、専門家やデジタルノマド向け長期居住者（LTR）ビザ。標準的な永住権の道はありませんが、長期ビザ保有者は無期限に更新できます。"),

    # ── STEP-BY-STEP TITLES ──────────────────────────────────────────────────
    ("Choose your visa type", "ビザの種類を選ぶ"),
    ("Gather required documents", "必要書類を揃える"),
    ("Apply at a Thai embassy or consulate", "タイ大使館または領事館で申請する"),
    ("Arrive and register your address", "入国し住所を登録する"),
    ("Open a Thai bank account", "タイの銀行口座を開設する"),
    ("Get health insurance", "健康保険に加入する"),
    ("Annual extension / 90-day report", "年次更新 / 90日報告"),
    ("Choose the right visa", "適切なビザを選ぶ"),
    ("Gather your documents", "書類を揃える"),
    ("Submit your application", "申請書を提出する"),
    ("Wait for processing", "審査を待つ"),
    ("Receive your visa", "ビザを受け取る"),
    ("Travel and entry", "旅行と入国"),
    ("Register and settle in", "登録し定住する"),

    # ── STEP-BY-STEP CONTENT ─────────────────────────────────────────────────
    ("Determine if you qualify for the Retirement O-A (50+, pension/savings proof), LTR Visa (remote worker, $80k income), or Thailand Elite. Most expats start with a Tourist Visa and switch after arrival.",
     "退職O-A（50歳以上、年金/貯蓄証明）、LTRビザ（リモートワーカー、年収8万ドル）、またはタイエリートの資格があるか確認してください。ほとんどの駐在員は観光ビザで始め、入国後に切り替えます。"),
    ("Passport (6+ months validity), passport photos, bank statements (800,000 THB in Thai bank for retirement visa or proof of $80k income for LTR), health insurance, medical certificate.",
     "パスポート（有効期間6ヶ月以上）、証明写真、銀行口座証明（退職ビザ用にタイの銀行に80万バーツ、またはLTR用に年収8万ドルの証明）、健康保険、医療証明書。"),
    ("Submit your visa application at your nearest Thai embassy. Processing takes 3–5 business days. You can also enter on a tourist visa and extend at the Immigration Bureau in Thailand.",
     "最寄りのタイ大使館でビザ申請書を提出してください。処理には3〜5営業日かかります。観光ビザで入国し、タイの移民局で延長することもできます。"),
    ("Within 24 hours of arriving, notify your accommodation. If renting, your landlord must file a TM.30 report. You receive a TM.6 arrival card.",
     "到着後24時間以内に宿泊先に通知してください。賃貸の場合、家主はTM.30報告書を提出する必要があります。TM.6入国カードを受け取ります。"),
    ("Open a Kasikorn Bank (KBank) or Bangkok Bank account. You'll need your passport, Non-Immigrant visa, and proof of address. Required for the 800,000 THB retirement deposit.",
     "カシコン銀行（KBank）またはバンコク銀行の口座を開設してください。パスポート、非移民ビザ、住所証明が必要です。80万バーツの退職金デポジットに必要です。"),
    ("Mandatory for retirement and LTR visas. Compare providers: Pacific Cross, BUPA Thailand, AXA. Budget ฿15,000–฿60,000/year depending on age and coverage.",
     "退職ビザとLTRビザには必須です。プロバイダーを比較してください：Pacific Cross、BUPA Thailand、AXA。年齢と補償内容によって年間15,000〜60,000バーツの予算が必要です。"),
    ("Renew your visa annually at the local Immigration office. File 90-day reports in person, by post, or online via the Immigration Bureau website.",
     "地元の移民局で毎年ビザを更新してください。90日報告書は直接、郵送、またはイミグレーション局のウェブサイトからオンラインで提出できます。"),

    # ── PRACTICAL INFO SECTIONS ───────────────────────────────────────────────
    ("Visa & Residency Options", "ビザ・在留資格オプション"),
    ("Step-by-Step Guide to Moving to Thailand", "タイへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Japan", "日本への移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Vietnam", "ベトナムへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Malaysia", "マレーシアへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Cambodia", "カンボジアへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Laos", "ラオスへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Georgia", "ジョージアへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Greece", "ギリシャへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Spain", "スペインへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Portugal", "ポルトガルへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Mexico", "メキシコへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Colombia", "コロンビアへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Costa Rica", "コスタリカへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Panama", "パナマへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to Paraguay", "パラグアイへの移住ステップバイステップガイド"),
    ("Step-by-Step Guide to Moving to UAE", "UAEへの移住ステップバイステップガイド"),

    # ── COMMON SECTION HEADERS ────────────────────────────────────────────────
    ("Healthcare in Thailand", "タイの医療"),
    ("Healthcare in Japan", "日本の医療"),
    ("Healthcare in Vietnam", "ベトナムの医療"),
    ("Healthcare in Malaysia", "マレーシアの医療"),
    ("Healthcare in Cambodia", "カンボジアの医療"),
    ("Healthcare in Laos", "ラオスの医療"),
    ("Healthcare in Georgia", "ジョージアの医療"),
    ("Healthcare in Greece", "ギリシャの医療"),
    ("Healthcare in Spain", "スペインの医療"),
    ("Healthcare in Portugal", "ポルトガルの医療"),
    ("Healthcare in Mexico", "メキシコの医療"),
    ("Healthcare in Colombia", "コロンビアの医療"),
    ("Healthcare in Costa Rica", "コスタリカの医療"),
    ("Healthcare in Panama", "パナマの医療"),
    ("Healthcare in Paraguay", "パラグアイの医療"),
    ("Healthcare in UAE", "UAEの医療"),
    ("Banking in Thailand", "タイの銀行"),
    ("Banking in Japan", "日本の銀行"),
    ("Banking in Vietnam", "ベトナムの銀行"),
    ("Banking in Malaysia", "マレーシアの銀行"),
    ("Cost of Living in Thailand", "タイの生活費"),
    ("Cost of Living in Japan", "日本の生活費"),
    ("Cost of Living in Vietnam", "ベトナムの生活費"),
    ("Cost of Living in Malaysia", "マレーシアの生活費"),
    ("Real Estate in Thailand", "タイの不動産"),
    ("Real Estate in Japan", "日本の不動産"),
    ("Real Estate in Vietnam", "ベトナムの不動産"),
    ("Real Estate in Malaysia", "マレーシアの不動産"),
    ("Pro Tips", "プロのヒント"),
    ("Frequently Asked Questions", "よくある質問"),
    ("Last updated: March 2026", "最終更新：2026年3月"),
    ("March 2026", "2026年3月"),
    ("Global eVisa & Travel Information Platform", "グローバル電子ビザ・旅行情報プラットフォーム"),
    ("Follow eVisa-Card.com", "eVisa-Card.comをフォロー"),
    ("Home", "ホーム"),

    # ── TABLE HEADERS ─────────────────────────────────────────────────────────
    ("Visa Type", "ビザの種類"),
    ("Duration", "期間"),
    ("Requirements", "要件"),
    ("Best For", "最適な対象"),
    ("Processing Time", "処理時間"),
    ("Fee", "手数料"),
    ("Mandatory", "必須"),
    ("Recommended", "推奨"),
    ("Optional", "任意"),
    ("per year", "年間"),
    ("per month", "月間"),
    ("per night", "1泊"),
    ("Yes", "はい"),
    ("No", "いいえ"),
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
        for eng, ja in REPLACEMENTS:
            html = html.replace(eng, ja)
        if html != original:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            total += 1
            print(f"  OK {fname}")
    print(f"\nDone: {total} files updated.")

if __name__ == "__main__":
    main()
