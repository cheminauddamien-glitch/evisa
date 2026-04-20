#!/usr/bin/env python3
"""Simplified Chinese (zh) translations for FAQ page — all 48 questions and 7 categories."""

CATEGORY_TRANSLATIONS = {
    "General Visa Questions": "签证常见问题",
    "Schengen &amp; European Visas": "申根及欧洲签证",
    "Documents &amp; Application Process": "所需文件与申请流程",
    "Fees &amp; Processing Times": "费用与处理时间",
    "Extensions, Overstay &amp; Refusal": "延期、逾期居留与拒签",
    "Special Visa Types": "特殊签证类型",
    "Embassy &amp; Application Process": "使馆与申请流程",
}

FAQ_TRANSLATIONS = [
    # ── Category 1: General Visa Questions (7) ──
    {
        "q_en": "What is an eVisa?",
        "q_zh": "什么是电子签证（eVisa）？",
        "a_zh": '电子签证（eVisa）是以数字形式签发的旅行许可。您可以在线申请、缴费，并通过电子邮件获得批准，无需前往大使馆。提供电子签证的国家包括<a href="/zh/visa-turkey.html">土耳其</a>、<a href="/zh/visa-india.html">印度</a>、<a href="/zh/visa-vietnam.html">越南</a>、<a href="/zh/visa-cambodia.html">柬埔寨</a>和<a href="/zh/visa-australia.html">澳大利亚</a>等。',
    },
    {
        "q_en": "What is the difference between a visa and an eVisa?",
        "q_zh": "签证和电子签证有什么区别？",
        "a_zh": "传统签证需要前往大使馆或领事馆提交纸质文件，有时还需要参加面试。电子签证则完全在线申请，处理速度更快（通常24至72小时内），并通过电子邮件发送。",
    },
    {
        "q_en": "What is an ETA (Electronic Travel Authorization)?",
        "q_zh": "什么是ETA（电子旅行许可）？",
        "a_zh": 'ETA是针对免签国家公民的入境前审查。它不是签证，而是与护照关联的旅行许可。使用ETA系统的国家包括<a href="/zh/visa-australia.html">澳大利亚</a>、加拿大、新西兰和英国。欧盟的ETIAS系统将于2026年启用。',
    },
    {
        "q_en": "What is visa-free travel?",
        "q_zh": "什么是免签旅行？",
        "a_zh": "免签旅行是指无需提前申请签证即可入境。您只需在入境时出示护照即可。允许停留时间通常为30至90天。持有强势护照（日本、新加坡、欧盟）的公民可免签进入190多个国家。",
    },
    {
        "q_en": "What is a visa-on-arrival (VOA)?",
        "q_zh": "什么是落地签证（VOA）？",
        "a_zh": '落地签证是在入境口岸（机场或边境）签发的签证，无需提前申请。您出示护照、填写表格、缴纳费用即可获得签证印章。提供落地签的国家包括<a href="/zh/visa-indonesia.html">印度尼西亚</a>、<a href="/zh/visa-nepal.html">尼泊尔</a>和<a href="/zh/visa-jordan.html">约旦</a>等。',
    },
    {
        "q_en": "How do I check if I need a visa?",
        "q_zh": "如何查询是否需要签证？",
        "a_zh": '签证要求取决于您的国籍和目的地。请使用首页的<a href="../index.html">签证查询工具</a>或查看具体的<a href="../destination.html">国家页面</a>。一般来说，强势护照国家（欧盟、美国、英国、日本）的公民可免签进入150多个国家。',
    },
    {
        "q_en": "What is the strongest passport in the world?",
        "q_zh": "世界上最强的护照是哪个？",
        "a_zh": "截至2026年，日本、新加坡及多个欧盟国家的护照被评为最强，可免签或落地签进入190多个国家。亨利护照指数和阿顿资本指数每季度根据旅行自由度对护照进行排名。",
    },

    # ── Category 2: Schengen & European Visas (6) ──
    {
        "q_en": "What is a Schengen visa?",
        "q_zh": "什么是申根签证？",
        "a_zh": '申根签证允许您持单一签证前往27个欧洲国家。适用于180天内最长90天的短期停留。您需要在主要目的地国家（或首次入境国家）的大使馆申请。请参阅<a href="/zh/visa-france.html">法国</a>、<a href="/zh/visa-germany.html">德国</a>、<a href="/zh/visa-spain.html">西班牙</a>和<a href="/zh/visa-italy.html">意大利</a>签证页面。',
    },
    {
        "q_en": "How many countries are in the Schengen Area?",
        "q_zh": "申根区包含多少个国家？",
        "a_zh": "截至2026年，申根区包含27个国家：奥地利、比利时、克罗地亚、捷克、丹麦、爱沙尼亚、芬兰、法国、德国、希腊、匈牙利、冰岛、意大利、拉脱维亚、列支敦士登、立陶宛、卢森堡、马耳他、荷兰、挪威、波兰、葡萄牙、罗马尼亚、斯洛伐克、斯洛文尼亚、西班牙、瑞典和瑞士。",
    },
    {
        "q_en": "Can I visit multiple Schengen countries with one visa?",
        "q_zh": "一个签证可以访问多个申根国家吗？",
        "a_zh": "可以。申根签证允许您在授权停留期间（180天内最多90天）自由往来所有27个申根国家。您必须在主要目的地或首次入境国家的大使馆申请。",
    },
    {
        "q_en": "What is the 90/180 rule for Schengen?",
        "q_zh": "申根的90/180天规则是什么？",
        "a_zh": "90/180天规则是指您在任意180天内最多可在申根区停留90天。这是按滚动方式计算的。用完90天后，您必须离开申根区，等到足够天数「过期」后才能再次入境。",
    },
    {
        "q_en": "What is ETIAS and when does it start?",
        "q_zh": "ETIAS是什么？何时开始实施？",
        "a_zh": "ETIAS（欧洲旅行信息和授权系统）是针对免签旅客进入申根区的新入境前许可制度，将于2026年启用。60多个国家（包括美国、英国、加拿大、澳大利亚、日本）的公民在前往欧洲前需获得ETIAS批准（7欧元，有效期3年）。",
    },
    {
        "q_en": "Can I enter a Schengen country different from my visa country?",
        "q_zh": "可以从签证签发国以外的申根国家入境吗？",
        "a_zh": "可以，但申根签证应由您的主要目的地国家（停留时间最长的国家）签发。如果从其他国家入境，边检可能会询问您的行程。如果各国停留时间相同，请向首次入境国家申请。",
    },

    # ── Category 3: Documents & Application Process (9) ──
    {
        "q_en": "What documents do I need for a visa application?",
        "q_zh": "签证申请需要哪些文件？",
        "a_zh": '常见要求包括：有效护照（有效期6个月以上）、护照照片、填写完整的申请表、旅行行程、酒店预订、财务证明（银行流水）、旅行保险和邀请函（如适用）。请参阅我们的<a href="/zh/visa-documents-checklist.html">文件清单</a>。',
    },
    {
        "q_en": "What size photo is needed for a visa?",
        "q_zh": "签证照片需要什么尺寸？",
        "a_zh": '大多数国家要求35x45毫米白色背景照片。美国要求51x51毫米（2x2英寸）。照片必须是近期拍摄（6个月内），面部表情自然，并符合特定的光线要求。请参阅我们的<a href="/zh/visa-photo-requirements.html">签证照片要求指南</a>。',
    },
    {
        "q_en": "Do I need travel insurance for a visa?",
        "q_zh": "签证申请需要旅行保险吗？",
        "a_zh": '是的，申根签证要求旅行保险最低保额为30,000欧元。许多其他国家也要求或强烈建议购买旅行保险。请参阅我们的<a href="/zh/travel-insurance-for-visa-applications.html">旅行保险指南</a>。',
    },
    {
        "q_en": "How long must my passport be valid for travel?",
        "q_zh": "护照有效期需要多长时间才能出行？",
        "a_zh": "大多数国家要求护照在计划停留期之后至少有6个月有效期。申根国家要求在出境日期后有3个月有效期，并且至少有两页空白页。请务必查看具体国家的要求。",
    },
    {
        "q_en": "What bank statement amount do I need for a visa?",
        "q_zh": "签证申请需要多少银行存款？",
        "a_zh": "要求因国家而异。申根签证需要显示每天50至100欧元的停留费用。美国B1/B2签证需要证明有足够资金（无固定金额）。英国需要显示3至6个月的稳定收入。一般建议银行余额覆盖旅行费用外加30%至50%的缓冲。",
    },
    {
        "q_en": "Is a hotel booking required for a visa application?",
        "q_zh": "签证申请需要酒店预订吗？",
        "a_zh": "大多数签证申请需要提供整个停留期间的住宿证明。可以是酒店预订（不一定需要预付）、Airbnb预订或接待方的信函。申根签证要求覆盖所有住宿夜次。",
    },
    {
        "q_en": "Do I need a return ticket to get a visa?",
        "q_zh": "申请签证需要回程机票吗？",
        "a_zh": "大多数国家在签证申请和入境时要求提供回程或续程旅行证明。可以是已确认的航班预订、巴士票或渡轮票，证明您计划在签证到期前离开。",
    },
    {
        "q_en": "What is an invitation letter for a visa?",
        "q_zh": "签证邀请函是什么？",
        "a_zh": "邀请函是目的地国家的个人或机构邀请您访问的文件。通常包括邀请人的详细信息、您们的关系、访问目的和日期、住宿安排以及经济担保。许多申根签证和商务签证申请都需要邀请函。",
    },
    {
        "q_en": "What are biometrics for a visa?",
        "q_zh": "签证生物识别信息是什么？",
        "a_zh": "生物识别信息包括签证申请时采集的指纹扫描和数码照片。申根国家、英国、美国、加拿大等许多国家都要求提供生物识别信息。这些数据存储在数据库中用于身份验证，通常有效期为5年。",
    },

    # ── Category 4: Fees & Processing Times (6) ──
    {
        "q_en": "How much does a visa cost?",
        "q_zh": "签证费用是多少？",
        "a_zh": '签证费用差异很大。示例：申根签证80欧元、美国B1/B2签证185美元、印度电子签证25至80美元、土耳其电子签证50美元、澳大利亚ETA 20澳元、柬埔寨电子签证36美元。儿童和某些国籍可能享受优惠费率。请参阅<a href="/zh/visa-processing-times.html">处理时间</a>页面。',
    },
    {
        "q_en": "How long does visa processing take?",
        "q_zh": "签证处理需要多长时间？",
        "a_zh": "电子签证通常需要24至72小时。申根签证需要15至45个日历日。美国B1/B2签证根据使馆不同可能需要数周到数月。请务必在出行日期前充分提前申请。",
    },
    {
        "q_en": "How far in advance should I apply for a visa?",
        "q_zh": "应该提前多久申请签证？",
        "a_zh": "电子签证：出行前1至2周。申根签证：提前3至6个月（最早6个月，最迟出发前15天）。美国签证：由于等候时间较长，建议提前3至6个月或更久。旅游旺季可能需要更早申请。",
    },
    {
        "q_en": "Can I get a visa refund if my application is rejected?",
        "q_zh": "签证申请被拒后可以退费吗？",
        "a_zh": "在大多数情况下，无论结果如何，签证费都不予退还。费用是为了支付申请处理成本，而非获批保证。",
    },
    {
        "q_en": "How do I track my visa application status?",
        "q_zh": "如何查询签证申请状态？",
        "a_zh": "大多数使馆和VFS Global办公室提供在线查询服务。您在提交申请时会收到一个参考编号，在使馆或VFS网站输入该编号即可查看状态。部分国家还会在每个处理阶段发送电子邮件或短信通知。",
    },
    {
        "q_en": "What is VFS Global?",
        "q_zh": "VFS Global是什么？",
        "a_zh": "VFS Global是一家代表各国政府处理签证申请的私营公司。他们在全球运营签证申请中心（VAC）。您可以在VFS中心提交文件，而无需直接前往使馆。VFS会在签证费之外收取服务费。",
    },

    # ── Category 5: Extensions, Overstay & Refusal (4) ──
    {
        "q_en": "Can I extend my visa?",
        "q_zh": "签证可以延期吗？",
        "a_zh": '取决于国家和签证类型。部分国家允许延期（例如印度尼西亚落地签可延期30天，泰国旅游签证可延期30天）。申根签证仅在特殊情况下才可延期。详情请参阅<a href="/zh/visa-rejection-reasons.html">签证拒签原因</a>页面。',
    },
    {
        "q_en": "What happens if my visa is refused?",
        "q_zh": "签证被拒后会怎样？",
        "a_zh": "您将收到书面通知，说明拒签原因。常见原因包括资金证明不足、文件不完整或涉嫌移民倾向。通常可以在1至3个月内提出申诉，或补充材料后重新申请。",
    },
    {
        "q_en": "What is overstaying a visa?",
        "q_zh": "什么是签证逾期居留？",
        "a_zh": "逾期居留是指在授权停留期限之后仍留在该国。后果包括罚款（例如泰国每天500泰铢）、遣返、拘留、入境禁令（1至10年）以及日后签证申请困难。请务必遵守签证有效期。",
    },
    {
        "q_en": "What happens if I lose my passport with a valid visa?",
        "q_zh": "丢失了带有有效签证的护照怎么办？",
        "a_zh": "请立即联系最近的本国大使馆申请紧急旅行证件。您需要重新申请签证，因为丢失护照中的签证视为无效。请向警方报案并保留报案副本用于新签证申请。",
    },

    # ── Category 6: Special Visa Types (10) ──
    {
        "q_en": "What is a transit visa?",
        "q_zh": "什么是过境签证？",
        "a_zh": "过境签证允许您在前往最终目的地途中经过某个国家。通常有效期为24至72小时。部分国家即使不出机场也要求过境签证。",
    },
    {
        "q_en": "Can I work on a tourist visa?",
        "q_zh": "持旅游签证可以工作吗？",
        "a_zh": "不可以。旅游签证通常不允许就业。持旅游签证工作在大多数国家属于违法行为，可能导致遣返、罚款和未来签证被拒。就业需要单独的工作签证或工作许可。",
    },
    {
        "q_en": "What is a digital nomad visa?",
        "q_zh": "什么是数字游民签证？",
        "a_zh": '数字游民签证允许远程工作者在某国居住的同时为海外雇主或客户工作。热门国家包括<a href="/zh/visa-portugal.html">葡萄牙</a>、<a href="/zh/visa-spain.html">西班牙</a>、<a href="/zh/visa-thailand.html">泰国</a>、<a href="/zh/visa-colombia.html">哥伦比亚</a>和<a href="/zh/visa-indonesia.html">印度尼西亚</a>。请参阅我们的<a href="/zh/digital-nomad-visas-guide.html">数字游民签证指南</a>。',
    },
    {
        "q_en": "What is a student visa?",
        "q_zh": "什么是学生签证？",
        "a_zh": "学生签证允许您在其他国家的教育机构学习。要求通常包括录取通知书、学费缴纳或奖学金证明、生活费资金证明、健康保险，有时还需要语言能力证书。",
    },
    {
        "q_en": "What is a Working Holiday Visa?",
        "q_zh": "什么是打工度假签证？",
        "a_zh": '打工度假签证（WHV）允许年轻人（通常18至30岁或18至35岁）在其他国家旅行和工作1至2年。热门项目包括<a href="/zh/visa-australia.html">澳大利亚</a>、<a href="/zh/visa-new-zealand.html">新西兰</a>、<a href="/zh/visa-canada.html">加拿大</a>和<a href="/zh/visa-japan.html">日本</a>。',
    },
    {
        "q_en": "What is a Golden Visa?",
        "q_zh": "什么是黄金签证？",
        "a_zh": '黄金签证是颁发给在某国进行重大金融投资（通常为房地产或商业）的投资者的居留许可。热门项目包括<a href="/zh/visa-portugal.html">葡萄牙</a>、<a href="/zh/visa-spain.html">西班牙</a>、<a href="/zh/visa-greece.html">希腊</a>和<a href="/zh/visa-uae.html">阿联酋</a>。投资金额从25万到50万欧元以上不等。',
    },
    {
        "q_en": "What is a long-stay visa (Type D)?",
        "q_zh": "什么是长期居留签证（D类）？",
        "a_zh": "D类签证（国家签证）允许在特定国家停留超过90天。与申根短期签证（C类）不同，D类签证由各国单独签发，用于学习、工作、家庭团聚或退休等目的。",
    },
    {
        "q_en": "What is a multiple-entry visa?",
        "q_zh": "什么是多次入境签证？",
        "a_zh": "多次入境签证允许您在签证有效期内多次出入某国。这对商务旅行者或需要访问邻国的人非常有用。单次入境签证在您离开该国后即失效。",
    },
    {
        "q_en": "Do children need their own visa?",
        "q_zh": "儿童需要单独的签证吗？",
        "a_zh": "是的，在大多数情况下，儿童（包括婴儿）需要单独的签证。部分国家为6岁或12岁以下儿童提供优惠费率。大多数国际旅行要求儿童持有自己的护照。",
    },
    {
        "q_en": "Can dual citizens use either passport for visas?",
        "q_zh": "双重国籍者可以使用任一护照申请签证吗？",
        "a_zh": "可以，双重国籍者可以选择使用哪本护照。建议使用签证条件更优的那本。出入同一国家时务必使用同一本护照。部分国家不承认双重国籍，请查阅两国的相关法律。",
    },

    # ── Category 7: Embassy & Application Process (5) ──
    {
        "q_en": "How do I apply for a visa at an embassy?",
        "q_zh": "如何在使馆申请签证？",
        "a_zh": '步骤：1）在使馆网站查看要求。2）准备文件。3）预约。4）前往提交文件。5）缴纳费用。6）等待处理。7）领取贴有签证的护照。请参阅我们的<a href="/zh/how-to-apply-evisa.html">申请指南</a>。',
    },
    {
        "q_en": "What is a visa interview?",
        "q_zh": "什么是签证面试？",
        "a_zh": "部分国家（尤其是美国、英国和加拿大）要求在使馆进行面试。签证官会询问您的旅行计划、与本国的联系、财务状况和访问目的。请如实回答并携带证明文件。",
    },
    {
        "q_en": "Can I apply for a visa from a country I am not a citizen of?",
        "q_zh": "可以在非国籍国申请签证吗？",
        "a_zh": "可以，在许多情况下，您可以在合法居住的国家的使馆申请。您需要提供合法居住证明（居留许可、长期签证）。部分国家仅接受该国公民或永久居民的申请。",
    },
    {
        "q_en": "What is a visa sticker vs stamp vs e-visa?",
        "q_zh": "签证贴纸、入境章和电子签证有什么区别？",
        "a_zh": "签证贴纸是粘贴在护照页上的实物标签（申根、美国、英国签证）。入境章是出入境管理人员在护照上盖的戳记。电子签证是与护照号码关联的数字许可，无需实物贴纸。",
    },
    {
        "q_en": "Can I travel with a visa in a cancelled passport?",
        "q_zh": "可以使用已注销护照中的签证旅行吗？",
        "a_zh": "在某些情况下可以，前提是签证仍然有效。美国和英国等国家允许您携带新护照和旧护照中的有效签证一起旅行。请查看具体国家的规定，因为部分国家要求将签证转移到新护照。",
    },
]
