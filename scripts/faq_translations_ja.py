#!/usr/bin/env python3
"""Japanese translations for all 48 FAQ questions and answers."""

CATEGORY_TRANSLATIONS = {
    "General Visa Questions": "ビザに関する一般的な質問",
    "Schengen & European Visas": "シェンゲン・ヨーロッパビザ",
    "Documents & Application Process": "必要書類と申請手続き",
    "Fees & Processing Times": "費用と処理時間",
    "Extensions, Overstay & Refusal": "延長・オーバーステイ・拒否",
    "Special Visa Types": "特殊なビザの種類",
    "Embassy & Application Process": "大使館と申請手続き",
}

FAQ_TRANSLATIONS = [
    # ── Category 1: General Visa Questions (7 questions) ──
    {
        "q_en": "What is an eVisa?",
        "q_ja": "eビザとは何ですか？",
        "a_ja": 'eビザ（電子ビザ）は、デジタルで発行される渡航認証です。オンラインで申請し、手数料を支払い、メールで承認を受け取ります。大使館への訪問は不要です。<a href="/ja/visa-turkey.html">トルコ</a>、<a href="/ja/visa-india.html">インド</a>、<a href="/ja/visa-vietnam.html">ベトナム</a>、<a href="/ja/visa-cambodia.html">カンボジア</a>、<a href="/ja/visa-australia.html">オーストラリア</a>などの国がeビザを提供しています。',
    },
    {
        "q_en": "What is the difference between a visa and an eVisa?",
        "q_ja": "ビザとeビザの違いは何ですか？",
        "a_ja": "従来のビザは、大使館または領事館を訪問し、紙の書類を提出し、場合によっては面接を受ける必要があります。eビザは完全にオンラインで申請でき、処理が速く（通常24〜72時間以内）、電子メールで届きます。",
    },
    {
        "q_en": "What is an ETA (Electronic Travel Authorization)?",
        "q_ja": "ETA（電子渡航認証）とは何ですか？",
        "a_ja": 'ETAは、ビザ免除国の国民を対象とした渡航前審査です。ビザではなく、パスポートに紐づけられた渡航認証です。<a href="/ja/visa-australia.html">オーストラリア</a>、カナダ、ニュージーランド、英国などがETAシステムを採用しています。EUのETIASシステムは2026年に開始予定です。',
    },
    {
        "q_en": "What is visa-free travel?",
        "q_ja": "ビザなし渡航とは何ですか？",
        "a_ja": "ビザなし渡航とは、事前にビザを申請することなく入国できることを意味します。入国審査でパスポートを提示するだけです。滞在可能期間は通常30〜90日間です。日本、シンガポール、EUなどの強力なパスポートでは、190か国以上にビザなしでアクセスできます。",
    },
    {
        "q_en": "What is a visa-on-arrival (VOA)?",
        "q_ja": "到着ビザ（VOA）とは何ですか？",
        "a_ja": '到着ビザは、事前申請なしに入国地点（空港や国境）で発行されるビザです。パスポートを提示し、申請書に記入し、手数料を支払い、ビザスタンプを受け取ります。<a href="/ja/visa-indonesia.html">インドネシア</a>、<a href="/ja/visa-nepal.html">ネパール</a>、<a href="/ja/visa-jordan.html">ヨルダン</a>などの国が多くの国籍に対してVOAを提供しています。',
    },
    {
        "q_en": "How do I check if I need a visa?",
        "q_ja": "ビザが必要かどうかはどのように確認できますか？",
        "a_ja": 'ビザの要件は、国籍と渡航先によって異なります。ホームページの<a href="../index.html">ビザ検索ツール</a>をご利用いただくか、<a href="../destination.html">国別ページ</a>をご確認ください。一般的に、強力なパスポートを持つ国（EU、米国、英国、日本）の国民は150か国以上にビザなしでアクセスできます。',
    },
    {
        "q_en": "What is the strongest passport in the world?",
        "q_ja": "世界で最も強力なパスポートはどれですか？",
        "a_ja": "2026年現在、日本、シンガポール、およびいくつかのEUのパスポートが最も強力で、190か国以上にビザなしまたは到着ビザでアクセスできます。ヘンリー・パスポート・インデックスやアートン・キャピタル・インデックスが、渡航の自由度に基づいてパスポートを四半期ごとにランク付けしています。",
    },

    # ── Category 2: Schengen & European Visas (6 questions) ──
    {
        "q_en": "What is a Schengen visa?",
        "q_ja": "シェンゲンビザとは何ですか？",
        "a_ja": 'シェンゲンビザは、1つのビザでヨーロッパ27か国を旅行できるビザです。180日間のうち最大90日間の短期滞在に有効です。最も長く滞在する国（または最初に入国する国）の大使館で申請します。<a href="/ja/visa-france.html">フランス</a>、<a href="/ja/visa-germany.html">ドイツ</a>、<a href="/ja/visa-spain.html">スペイン</a>、<a href="/ja/visa-italy.html">イタリア</a>のビザページもご参照ください。',
    },
    {
        "q_en": "How many countries are in the Schengen Area?",
        "q_ja": "シェンゲン圏には何か国が含まれていますか？",
        "a_ja": "2026年現在、シェンゲン圏には27か国が含まれています。オーストリア、ベルギー、クロアチア、チェコ共和国、デンマーク、エストニア、フィンランド、フランス、ドイツ、ギリシャ、ハンガリー、アイスランド、イタリア、ラトビア、リヒテンシュタイン、リトアニア、ルクセンブルク、マルタ、オランダ、ノルウェー、ポーランド、ポルトガル、ルーマニア、スロバキア、スロベニア、スペイン、スウェーデン、スイスです。",
    },
    {
        "q_en": "Can I visit multiple Schengen countries with one visa?",
        "q_ja": "1つのビザで複数のシェンゲン圏の国を訪問できますか？",
        "a_ja": "はい。シェンゲンビザがあれば、許可された滞在期間中（180日間のうち最大90日間）、27のシェンゲン圏すべての国を自由に移動できます。主な渡航先または最初の入国国の大使館で申請する必要があります。",
    },
    {
        "q_en": "What is the 90/180 rule for Schengen?",
        "q_ja": "シェンゲン圏の90/180日ルールとは何ですか？",
        "a_ja": "90/180日ルールとは、180日間のうち最大90日間シェンゲン圏に滞在できるという規則です。これはローリング方式で計算されます。90日間を使い切った場合、シェンゲン圏を離れ、十分な日数が「期限切れ」になるまで待ってから再入国する必要があります。",
    },
    {
        "q_en": "What is ETIAS and when does it start?",
        "q_ja": "ETIASとは何ですか？いつ開始されますか？",
        "a_ja": "ETIAS（欧州渡航情報・認証システム）は、シェンゲン圏を訪問するビザ免除の旅行者を対象とした新しい渡航前認証です。2026年に開始予定です。60か国以上の国民（米国、英国、カナダ、オーストラリア、日本）がヨーロッパへの渡航前にETIASの承認（7ユーロ、3年間有効）を取得する必要があります。",
    },
    {
        "q_en": "Can I enter a Schengen country different from my visa country?",
        "q_ja": "ビザ申請国と異なるシェンゲン圏の国から入国できますか？",
        "a_ja": "はい。ただし、シェンゲンビザは主な渡航先（最長滞在国）の国が発行する必要があります。異なる国から入国する場合、入国審査で旅程について質問される可能性があります。すべての滞在期間が同じ場合は、最初の入国国に申請してください。",
    },

    # ── Category 3: Documents & Application Process (9 questions) ──
    {
        "q_en": "What documents do I need for a visa application?",
        "q_ja": "ビザ申請にはどのような書類が必要ですか？",
        "a_ja": '一般的な要件は、有効なパスポート（残存有効期間6か月以上）、パスポート写真、記入済みの申請書、旅行日程表、ホテル予約確認書、財務証明（銀行残高証明書）、旅行保険、招待状（該当する場合）です。詳しくは<a href="/ja/visa-documents-checklist.html">必要書類チェックリスト</a>をご覧ください。',
    },
    {
        "q_en": "What size photo is needed for a visa?",
        "q_ja": "ビザ用の写真のサイズはどれくらいですか？",
        "a_ja": 'ほとんどの国では、白い背景の35x45mmの写真が必要です。米国では51x51mm（2x2インチ）が必要です。写真は最近（6か月以内）のもので、無表情であり、特定の照明要件を満たす必要があります。詳しくは<a href="/ja/visa-photo-requirements.html">ビザ用写真の要件ガイド</a>をご参照ください。',
    },
    {
        "q_en": "Do I need travel insurance for a visa?",
        "q_ja": "ビザに旅行保険は必要ですか？",
        "a_ja": 'はい。シェンゲンビザの場合、最低30,000ユーロの補償がある旅行保険が必要です。他の多くの国でも旅行保険を義務付けるか、強く推奨しています。詳しくは<a href="/ja/travel-insurance-for-visa-applications.html">旅行保険ガイド</a>をご覧ください。',
    },
    {
        "q_en": "How long must my passport be valid for travel?",
        "q_ja": "渡航にはパスポートの有効期限がどれくらい残っている必要がありますか？",
        "a_ja": "ほとんどの国では、予定滞在期間終了後少なくとも6か月間のパスポート有効期限が必要です。シェンゲン圏の国では、出国日から3か月以上の有効期限と2ページ以上の空白ページが必要です。渡航前に各国の具体的な要件を必ず確認してください。",
    },
    {
        "q_en": "Can I apply for a visa if my passport expires soon?",
        "q_ja": "パスポートの有効期限が近い場合でもビザを申請できますか？",
        "a_ja": "一般的にはできません。ほとんどの国ではパスポートの残存有効期間が6か月以上必要です。パスポートの有効期限が6か月以内の場合は、ビザ申請前にパスポートを更新してください。ビザステッカー用の空白ページ（通常2ページ）が必要な国もあります。",
    },
    {
        "q_en": "What bank statement amount do I need for a visa?",
        "q_ja": "ビザ申請に必要な銀行残高証明書の金額はいくらですか？",
        "a_ja": "必要金額は国によって異なります。シェンゲンビザの場合、滞在1日あたり50〜100ユーロを証明する必要があります。米国B1/B2ビザでは十分な資金を証明します（固定金額はありません）。英国では3〜6か月間の安定した収入を示す必要があります。一般的に、旅行費用に加えて30〜50%の余裕をもった残高を示してください。",
    },
    {
        "q_en": "Is a hotel booking required for a visa application?",
        "q_ja": "ビザ申請にホテルの予約は必要ですか？",
        "a_ja": "ほとんどのビザ申請では、滞在期間全体の宿泊先証明が必要です。ホテルの予約確認書（事前支払いは必ずしも必要ではありません）、Airbnbの予約、またはホスト（受入先）からの招待状が利用できます。シェンゲンビザの場合、すべての宿泊日がカバーされている必要があります。",
    },
    {
        "q_en": "Do I need a return ticket to get a visa?",
        "q_ja": "ビザの取得に復路航空券は必要ですか？",
        "a_ja": "ほとんどの国では、ビザ申請時および入国審査時に帰国便または出国便の証明が必要です。確定済みのフライト予約、バスチケット、フェリーチケットなど、ビザの有効期限内に出国する予定を示すものが該当します。",
    },
    {
        "q_en": "What is an invitation letter for a visa?",
        "q_ja": "ビザ用の招待状とは何ですか？",
        "a_ja": "招待状は、渡航先の国にいる個人または団体があなたの訪問を招待する文書です。招待者の詳細、あなたとの関係、訪問の目的と日程、宿泊の手配、経済的責任などが記載されます。多くのシェンゲンビザやビジネスビザの申請で必要とされます。",
    },
    {
        "q_en": "What are biometrics for a visa?",
        "q_ja": "ビザの生体認証とは何ですか？",
        "a_ja": "生体認証には、ビザ申請時に採取される指紋スキャンとデジタル写真が含まれます。シェンゲン圏の国、英国、米国、カナダ、その他多くの国で生体認証が必要です。本人確認のためにデータベースに保存され、通常5年間有効です。",
    },

    # ── Category 4: Fees & Processing Times (6 questions) ──
    {
        "q_en": "How much does a visa cost?",
        "q_ja": "ビザの費用はいくらですか？",
        "a_ja": 'ビザの費用は国によって大きく異なります。例：シェンゲンビザ80ユーロ、米国B1/B2ビザ185ドル、インドeビザ25〜80ドル、トルコeビザ50ドル、オーストラリアETA 20豪ドル、カンボジアeビザ36ドル。子供や一部の国籍には割引が適用される場合があります。詳しくは<a href="/ja/visa-processing-times.html">処理時間</a>ページをご覧ください。',
    },
    {
        "q_en": "How long does visa processing take?",
        "q_ja": "ビザの処理にはどのくらいの時間がかかりますか？",
        "a_ja": "eビザは通常24〜72時間で処理されます。シェンゲンビザは15〜45暦日かかります。米国B1/B2ビザは大使館によって数週間から数か月かかる場合があります。渡航日に余裕をもって申請してください。",
    },
    {
        "q_en": "How far in advance should I apply for a visa?",
        "q_ja": "ビザはどのくらい前に申請すべきですか？",
        "a_ja": "eビザの場合：渡航の1〜2週間前。シェンゲンビザの場合：3〜6か月前（最早で6か月前、最遅で出発15日前）。米国ビザの場合：待ち時間が長いため3〜6か月以上前。繁忙期にはさらに早めの申請が必要になる場合があります。",
    },
    {
        "q_en": "Can I get a visa refund if my application is rejected?",
        "q_ja": "ビザ申請が却下された場合、返金を受けられますか？",
        "a_ja": "ほとんどの場合、ビザ申請料は結果にかかわらず返金されません。申請料は申請処理の費用をカバーするものであり、承認を保証するものではありません。",
    },
    {
        "q_en": "How do I track my visa application status?",
        "q_ja": "ビザ申請の状況はどのように確認できますか？",
        "a_ja": "ほとんどの大使館やVFSグローバルのオフィスではオンライン追跡が可能です。申請書提出時に参照番号が発行されます。大使館またはVFSのウェブサイトでこの番号を入力して状況を確認できます。一部の国では処理段階ごとにメールやSMSで通知が届きます。",
    },
    {
        "q_en": "What is VFS Global?",
        "q_ja": "VFSグローバルとは何ですか？",
        "a_ja": "VFSグローバルは、各国政府に代わってビザ申請を処理する民間企業です。世界中にビザ申請センター（VAC）を運営しています。大使館に直接ではなく、VFSセンターで書類を提出します。VFSはビザ申請料に加えてサービス料を請求します。",
    },

    # ── Category 5: Extensions, Overstay & Refusal (4 questions) ──
    {
        "q_en": "Can I extend my visa?",
        "q_ja": "ビザを延長することはできますか？",
        "a_ja": '国やビザの種類によります。一部の国では延長が可能です（例：インドネシアのVOAは30日間延長可能、タイの観光ビザは30日間延長可能）。シェンゲンビザは例外的な状況でのみ延長できます。関連情報は<a href="/ja/visa-rejection-reasons.html">ビザ却下の理由</a>ページをご参照ください。',
    },
    {
        "q_en": "What happens if my visa is refused?",
        "q_ja": "ビザが拒否された場合はどうなりますか？",
        "a_ja": "理由を記載した書面による通知を受け取ります。よくある理由には、財務証明の不足、書類の不備、移民目的の疑いなどがあります。通常、1〜3か月以内に異議を申し立てるか、改善された書類で再申請することができます。",
    },
    {
        "q_en": "What is overstaying a visa?",
        "q_ja": "ビザのオーバーステイとは何ですか？",
        "a_ja": "オーバーステイとは、許可された滞在期間を超えて滞在することです。結果として、罰金（例：タイでは1日500バーツ）、強制送還、拘留、入国禁止（1〜10年）、将来のビザ取得の困難さなどが生じます。ビザの有効期限を必ず守ってください。",
    },
    {
        "q_en": "What happens if I lose my passport with a valid visa?",
        "q_ja": "有効なビザが入ったパスポートを紛失した場合はどうなりますか？",
        "a_ja": "最寄りの自国大使館に直ちに連絡し、緊急渡航書類を取得してください。紛失したパスポートのビザは無効とみなされるため、新しいビザを申請する必要があります。警察届出書を作成し、新しいビザ申請のためにそのコピーを保管してください。",
    },

    # ── Category 6: Special Visa Types (10 questions) ──
    {
        "q_en": "What is a transit visa?",
        "q_ja": "トランジットビザとは何ですか？",
        "a_ja": "トランジットビザは、最終目的地に向かう途中で国を通過するためのビザです。通常24〜72時間有効です。空港から出ない場合でもトランジットビザが必要な国もあります。",
    },
    {
        "q_en": "Can I work on a tourist visa?",
        "q_ja": "観光ビザで働くことはできますか？",
        "a_ja": "いいえ。観光ビザでは一般的に就労は認められていません。観光ビザでの就労はほとんどの国で違法であり、強制送還、罰金、将来のビザ拒否につながる可能性があります。就労には別途、就労ビザまたは労働許可証が必要です。",
    },
    {
        "q_en": "What is a digital nomad visa?",
        "q_ja": "デジタルノマドビザとは何ですか？",
        "a_ja": 'デジタルノマドビザは、リモートワーカーが海外の雇用主やクライアントのために働きながら、他国に居住することを可能にするビザです。人気のある国には<a href="/ja/visa-portugal.html">ポルトガル</a>、<a href="/ja/visa-spain.html">スペイン</a>、<a href="/ja/visa-thailand.html">タイ</a>、<a href="/ja/visa-colombia.html">コロンビア</a>、<a href="/ja/visa-indonesia.html">インドネシア</a>があります。詳しくは<a href="/ja/digital-nomad-visas-guide.html">デジタルノマドビザガイド</a>をご覧ください。',
    },
    {
        "q_en": "What is a student visa?",
        "q_ja": "学生ビザとは何ですか？",
        "a_ja": "学生ビザは、他国の教育機関で学ぶためのビザです。一般的な要件として、入学許可書、授業料の支払い証明または奨学金証明、生活費の資金証明、健康保険、場合によっては語学力の証明書が必要です。",
    },
    {
        "q_en": "What is a Working Holiday Visa?",
        "q_ja": "ワーキングホリデービザとは何ですか？",
        "a_ja": 'ワーキングホリデービザ（WHV）は、若者（通常18〜30歳または18〜35歳）が他国で1〜2年間旅行しながら働くことを可能にするビザです。人気のあるプログラムには<a href="/ja/visa-australia.html">オーストラリア</a>、<a href="/ja/visa-new-zealand.html">ニュージーランド</a>、<a href="/ja/visa-canada.html">カナダ</a>、<a href="/ja/visa-japan.html">日本</a>があります。',
    },
    {
        "q_en": "What is a Golden Visa?",
        "q_ja": "ゴールデンビザとは何ですか？",
        "a_ja": 'ゴールデンビザは、不動産や事業への多額の投資を行った投資家に付与される居住許可です。<a href="/ja/visa-portugal.html">ポルトガル</a>、<a href="/ja/visa-spain.html">スペイン</a>、<a href="/ja/visa-greece.html">ギリシャ</a>、<a href="/ja/visa-uae.html">UAE</a>に人気のプログラムがあります。投資額は25万ユーロから50万ユーロ以上です。',
    },
    {
        "q_en": "What is a long-stay visa (Type D)?",
        "q_ja": "長期滞在ビザ（タイプD）とは何ですか？",
        "a_ja": "タイプDビザ（国内ビザ）は、特定の国に90日を超える滞在を可能にするビザです。シェンゲン短期滞在ビザ（タイプC）とは異なり、タイプDは留学、就労、家族の呼び寄せ、退職などの目的で各国が個別に発行します。",
    },
    {
        "q_en": "What is a multiple-entry visa?",
        "q_ja": "マルチプルエントリービザ（数次ビザ）とは何ですか？",
        "a_ja": "マルチプルエントリービザは、ビザの有効期間中に何度でも入出国できるビザです。ビジネス旅行者や近隣国を訪問する方に便利です。シングルエントリービザは、一度出国すると無効になります。",
    },
    {
        "q_en": "Do children need their own visa?",
        "q_ja": "子供にも自分のビザが必要ですか？",
        "a_ja": "はい。ほとんどの場合、乳幼児を含む子供にもそれぞれビザが必要です。一部の国では6歳未満または12歳未満の子供に対して割引料金が適用されます。ほとんどの国際渡航では、子供も自分のパスポートを持っている必要があります。",
    },
    {
        "q_en": "What is a visa exemption agreement?",
        "q_ja": "ビザ免除協定とは何ですか？",
        "a_ja": "ビザ免除協定は、二国間の条約で、両国の国民がビザなしで相互に渡航できるようにするものです。通常、観光やビジネス目的で30〜90日間の滞在が認められます。例としては、シェンゲン圏内のEU市民の移動や、米国と韓国のビザなし渡航などがあります。",
    },
    {
        "q_en": "Can dual citizens use either passport for visas?",
        "q_ja": "二重国籍者はどちらのパスポートでもビザを申請できますか？",
        "a_ja": "はい。二重国籍者はどちらのパスポートを使用するか選ぶことができます。より有利なビザ条件が得られるパスポートを使用してください。同じ国への入出国は必ず同じパスポートで行ってください。二重国籍を認めていない国もありますので、両国の法律を確認してください。",
    },

    # ── Category 7: Embassy & Application Process (5 questions) ──
    {
        "q_en": "How do I apply for a visa at an embassy?",
        "q_ja": "大使館でのビザ申請方法を教えてください。",
        "a_ja": '手順：1) 大使館のウェブサイトで要件を確認。2) 必要書類を準備。3) 予約を取る。4) 予約日に出向き書類を提出。5) 手数料を支払う。6) 処理を待つ。7) ビザが貼付されたパスポートを受け取る。詳しくは<a href="/ja/how-to-apply-evisa.html">申請方法ガイド</a>をご覧ください。',
    },
    {
        "q_en": "What is a visa interview?",
        "q_ja": "ビザ面接とは何ですか？",
        "a_ja": "一部の国（特に米国、英国、カナダ）では、ビザ申請の一環として大使館での面接が必要です。領事官が渡航計画、母国との結びつき、経済状況、訪問目的について質問します。正直に答え、裏付け書類を持参してください。",
    },
    {
        "q_en": "Can I apply for a visa from a country I am not a citizen of?",
        "q_ja": "国籍のない国からビザを申請できますか？",
        "a_ja": "はい。多くの場合、合法的に居住している国の大使館でビザを申請できます。在留許可証や長期ビザなどの合法的な居住証明が必要です。一部の国では、大使館がある国の国民または永住者からの申請のみ受け付けています。",
    },
    {
        "q_en": "What is a visa sticker vs stamp vs e-visa?",
        "q_ja": "ビザステッカー、スタンプ、eビザの違いは何ですか？",
        "a_ja": "ビザステッカーは、パスポートのページに貼付される物理的なラベルです（シェンゲン、米国、英国で使用）。ビザスタンプは、入国審査で押される入出国の印です。eビザはパスポート番号に紐づけられたデジタル認証で、物理的なステッカーは不要です。",
    },
    {
        "q_en": "Can I travel with a visa in a cancelled passport?",
        "q_ja": "失効したパスポートのビザで渡航できますか？",
        "a_ja": "ビザがまだ有効であれば、可能な場合があります。米国や英国などでは、旧パスポートの有効なビザと新しいパスポートを併せて持参すれば渡航できます。ただし、ビザの新パスポートへの移転を求める国もあるため、各国のルールを必ず確認してください。",
    },
]

# Mapping of question index ranges to categories (for use by apply script)
CATEGORY_QUESTION_RANGES = {
    "General Visa Questions": (0, 7),
    "Schengen & European Visas": (7, 13),
    "Documents & Application Process": (13, 23),
    "Fees & Processing Times": (23, 29),
    "Extensions, Overstay & Refusal": (29, 33),
    "Special Visa Types": (33, 44),
    "Embassy & Application Process": (44, 49),
}

# Verify count
assert len(FAQ_TRANSLATIONS) == 49, f"Expected 49, got {len(FAQ_TRANSLATIONS)}"

# Total: 49 questions across 7 categories:
#   General (7) + Schengen (6) + Documents (10) + Fees (6) + Extensions (4) + Special (11) + Embassy (5) = 49
# This includes all 47 accordion questions from the HTML plus 2 additional questions
# from the JSON-LD schema ("Can I apply for a visa if my passport expires soon?"
# and "What is a visa exemption agreement?").
