# -*- coding: utf-8 -*-
from gram_hsk3 import P,Q
G={}
G[131]={"p":[
 P("像…似的 / A 似的","像 + N + 似的 ／ Adj/V + 似的","Như thể, giống như (khẩu ngữ).",
  ["他高兴得像个孩子似的。|Tā gāoxìng de xiàng ge háizi shìde.|Anh ấy vui như đứa trẻ.","她好像什么都知道似的。|Tā hǎoxiàng shénme dōu zhīdào shìde.|Cô ấy làm như cái gì cũng biết."]),
 P("不然 / 从而","…，不然 + hậu quả ／ …，从而 + kết quả","不然 = nếu không thì (khẩu ngữ của 否则); 从而 = từ đó, nhờ đó (văn viết).",
  ["快走吧，不然赶不上车了。|Kuài zǒu ba, bùrán gǎn bu shàng chē le.|Đi nhanh lên, không thì lỡ xe.","我们改进了流程，从而提高了效率。|Wǒmen gǎijìn le liúchéng, cóng'ér tígāo le xiàolǜ.|Chúng tôi cải tiến quy trình, nhờ đó nâng cao hiệu suất."]),
 P("Thán từ","哎呀 (ngạc nhiên, than) · 哦 (à, ra vậy) · 唉 (thở dài)","Đứng đầu câu, biểu đạt cảm xúc.",
  ["哎呀，我忘带钥匙了！|Āiyā, wǒ wàng dài yàoshi le!|Ôi, tôi quên mang chìa khóa!","哦，原来是这样。|Ò, yuánlái shì zhèyàng.|À, ra là vậy."])],
 "q":[Q("快走吧，＿＿赶不上车了。","不然/从而/似的/哦","不然 = nếu không thì."),
  Q("他高兴得像个孩子＿＿。","似的/一样的似/哈/呀","像…似的."),
  Q("改进了流程，＿＿提高了效率。","从而/不然/然后而/所以而","从而 + kết quả."),
  Q("＿＿，我忘带钥匙了！","哎呀/哦/哈/似的","Than: 哎呀.")]}
G[132]={"p":[
 P("哪怕…也… / 一旦…就…","哪怕 A，也 B ／ 一旦 A，就 B","哪怕 = cho dù (giống 即使, khẩu ngữ hơn); 一旦 = một khi.",
  ["哪怕再忙，也要吃早饭。|Nǎpà zài máng, yě yào chī zǎofàn.|Dù bận mấy cũng phải ăn sáng.","一旦发现故障，就要立即报告。|Yídàn fāxiàn gùzhàng, jiù yào lìjí bàogào.|Một khi phát hiện sự cố phải báo cáo ngay."]),
 P("要不是…就…","要不是 A，(S) 就 B 了","Nếu không phải vì A thì đã B (giả định ngược với sự thật).",
  ["要不是你提醒我，我就忘了。|Yàobúshì nǐ tíxǐng wǒ, wǒ jiù wàng le.|Nếu không nhờ bạn nhắc thì tôi đã quên rồi."]),
 P("毕竟 / 反正 / 总之","毕竟 (dù sao thì, xét cho cùng) ／ 反正 (đằng nào cũng) ／ 总之 (tóm lại)","Phó từ ngữ khí kết luận.",
  ["别怪他了，他毕竟是新来的。|Bié guài tā le, tā bìjìng shì xīn lái de.|Đừng trách cậu ấy, dù sao cũng là người mới.","反正没事，我陪你去吧。|Fǎnzhèng méi shì, wǒ péi nǐ qù ba.|Đằng nào cũng rảnh, tôi đi cùng bạn.","总之，我们要按时完成。|Zǒngzhī, wǒmen yào ànshí wánchéng.|Tóm lại, chúng ta phải hoàn thành đúng hạn."])],
 "q":[Q("＿＿再忙，也要吃早饭。","哪怕/一旦/要不是/反正","哪怕…也…."),
  Q("＿＿发现故障，就要立即报告。","一旦/哪怕/毕竟/总之","一旦…就…."),
  Q("＿＿你提醒我，我就忘了。","要不是/要不/哪怕/一旦","要不是 A，就 B 了."),
  Q("别怪他了，他＿＿是新来的。","毕竟/反正/总之/由此","Dù sao thì: 毕竟.")]}
G[133]={"p":[
 P("简直 + (cường điệu)","简直 + V/Adj (+ 了)","Quả thực, đơn giản là (phóng đại).",
  ["这简直太好了！|Zhè jiǎnzhí tài hǎo le!|Cái này quả thực quá tốt!","他简直不敢相信。|Tā jiǎnzhí bù gǎn xiāngxìn.|Anh ấy quả thực không dám tin."]),
 P("过于 / 过分 / 过度","过于 + Adj ／ 过分 (quá đáng) ／ 过度 + V","Quá mức (tiêu cực).",
  ["你过于紧张了。|Nǐ guòyú jǐnzhāng le.|Bạn quá căng thẳng rồi.","不要过度使用电池。|Búyào guòdù shǐyòng diànchí.|Đừng sử dụng pin quá mức."]),
 P("相当 / 格外 / 极其","相当 + Adj (khá) ／ 格外 + Adj (đặc biệt) ／ 极其 + Adj (cực kỳ)","Các mức độ.",
  ["今天格外冷。|Jīntiān géwài lěng.|Hôm nay lạnh đặc biệt.","这个问题极其复杂。|Zhège wèntí jíqí fùzá.|Vấn đề này cực kỳ phức tạp."])],
 "q":[Q("这＿＿太好了！","简直/相对/较/过于","Phóng đại: 简直."),
  Q("你＿＿紧张了，放松一点儿。","过于/简直/格外/相当于","过于 + Adj."),
  Q("今天＿＿冷。(đặc biệt)","格外/过分/相对/较为了","格外 = đặc biệt."),
  Q("不要＿＿使用电池。","过度/过于/极其/相当","过度 + V.")]}
G[134]={"p":[
 P("曾经 + V + 过","S + 曾经 + V + 过","Đã từng (văn viết).",
  ["我曾经在上海工作过。|Wǒ céngjīng zài Shànghǎi gōngzuò guo.|Tôi từng làm việc ở Thượng Hải."]),
 P("自从…以来 / 至今","自从 + thời điểm/sự việc + (以来)，… ／ …至今","Kể từ khi… đến nay.",
  ["自从来到越南以来，他学会了很多。|Zìcóng láidào Yuènán yǐlái, tā xuéhuì le hěn duō.|Từ khi đến Việt Nam, anh ấy đã học được nhiều.","这个问题至今没有解决。|Zhège wèntí zhìjīn méiyǒu jiějué.|Vấn đề này đến nay vẫn chưa giải quyết."]),
 P("早已 / 最初","早已 + V (từ lâu đã) ／ 最初 (ban đầu)","Văn viết.",
  ["他早已离开了公司。|Tā zǎoyǐ líkāi le gōngsī.|Anh ấy đã rời công ty từ lâu.","最初我不习惯。|Zuìchū wǒ bù xíguàn.|Ban đầu tôi không quen."])],
 "q":[Q("我＿＿在上海工作过。","曾经/早已/从前的/至今","曾经 + V + 过."),
  Q("＿＿来到越南以来，他学会了很多。","自从/至今/从前/曾","自从…以来."),
  Q("这个问题＿＿没有解决。","至今/以来/自从/最初","至今 = đến nay."),
  Q("他＿＿离开了公司，你不知道吗？","早已/曾/从不/最初","早已 = từ lâu đã.")]}
G[135]={"p":[
 P("渐渐 / 逐渐 / 逐步","渐渐(地) + V ／ 逐步 + V (theo từng bước có kế hoạch)","Dần dần.",
  ["天渐渐黑了。|Tiān jiànjiàn hēi le.|Trời dần tối.","我们要逐步完善系统。|Wǒmen yào zhúbù wánshàn xìtǒng.|Chúng ta phải từng bước hoàn thiện hệ thống."]),
 P("立即 / 立刻 / 连忙 / 尽快","立即/立刻 + V ／ 连忙 + V (vội vàng, chỉ quá khứ) ／ 尽快 + V","连忙 chỉ dùng kể việc đã xảy ra; không dùng trong câu mệnh lệnh.",
  ["请立即处理。|Qǐng lìjí chǔlǐ.|Xin xử lý ngay.","看到老师，他连忙站起来。|Kàndào lǎoshī, tā liánmáng zhàn qǐlai.|Thấy thầy, cậu ấy vội đứng dậy.","请尽快回复。|Qǐng jǐnkuài huífù.|Xin trả lời sớm nhất có thể."],None,"请连忙处理。|请立即处理。"),
 P("陆续","陆续 + V","Lần lượt, lục tục.",
  ["客人陆续到了。|Kèrén lùxù dào le.|Khách lần lượt đến."])],
 "q":[Q("请＿＿处理这个问题。","立即/连忙/渐渐/陆续","Mệnh lệnh: 立即, không dùng 连忙."),
  Q("天＿＿黑了。","渐渐/立刻/尽快/连忙","Dần dần: 渐渐."),
  Q("客人＿＿到了。","陆续/逐步地/急忙地/尽快","Lần lượt: 陆续."),
  Q("请＿＿回复邮件。","尽快/连忙/渐渐/陆续","尽快 = sớm nhất có thể.")]}
G[136]={"p":[
 P("尽量 / 尽力","尽量 + V (cố hết mức có thể) ／ 尽力 (dốc sức)","尽量 thường đứng trước động từ; 尽力 có thể đứng một mình.",
  ["我会尽量早点儿到。|Wǒ huì jǐnliàng zǎo diǎnr dào.|Tôi sẽ cố đến sớm nhất có thể.","我已经尽力了。|Wǒ yǐjīng jìnlì le.|Tôi đã cố hết sức rồi."]),
 P("亲自 / 独自 / 单独","亲自 + V (đích thân) ／ 独自 + V (một mình) ／ 单独 + V (riêng)","Cách thức thực hiện.",
  ["经理亲自来检查。|Jīnglǐ qīnzì lái jiǎnchá.|Giám đốc đích thân đến kiểm tra.","我想跟你单独谈谈。|Wǒ xiǎng gēn nǐ dāndú tántan.|Tôi muốn nói chuyện riêng với bạn."]),
 P("随时 / 轻易","随时 + V (bất cứ lúc nào) ／ 不 + 轻易 + V (không dễ dàng)","随时 = lúc nào cũng được.",
  ["有问题随时联系我。|Yǒu wèntí suíshí liánxì wǒ.|Có vấn đề cứ liên hệ tôi bất cứ lúc nào.","他不轻易放弃。|Tā bù qīngyì fàngqì.|Anh ấy không dễ bỏ cuộc."])],
 "q":[Q("我会＿＿早点儿到。","尽量/尽力了/亲自/独自","尽量 + V."),
  Q("经理＿＿来检查。","亲自/单独地/悄悄地了/随手","Đích thân: 亲自."),
  Q("有问题＿＿联系我。","随时/随手/轻易/独自","Bất cứ lúc nào: 随时."),
  Q("他不＿＿放弃。","轻易/随时/亲自/尽力","不轻易 + V.")]}
G[137]={"p":[
 P("似乎 / 仿佛","似乎 + V/Adj (dường như) ／ 仿佛 + (như thể)","Phỏng đoán, văn viết.",
  ["他似乎不太高兴。|Tā sìhū bú tài gāoxìng.|Anh ấy dường như không vui lắm.","我仿佛回到了童年。|Wǒ fǎngfú huídào le tóngnián.|Tôi như thể trở về thời thơ ấu."]),
 P("说不定 / 或许","说不定 + câu ／ 或许 + V","Biết đâu, có lẽ.",
  ["说不定他已经到了。|Shuōbudìng tā yǐjīng dào le.|Biết đâu anh ấy đã đến rồi."]),
 P("可见 / 难以","…，可见… (rút kết luận) ／ 难以 + V hai âm tiết","可见 = có thể thấy; 难以 = khó mà.",
  ["他每天都来，可见他很重视。|Tā měi tiān dōu lái, kějiàn tā hěn zhòngshì.|Anh ấy ngày nào cũng đến, đủ thấy anh ấy rất coi trọng.","这种结果让人难以接受。|Zhè zhǒng jiéguǒ ràng rén nányǐ jiēshòu.|Kết quả này khiến người ta khó mà chấp nhận."])],
 "q":[Q("他＿＿不太高兴。","似乎/可见/难以/偶然","Dường như: 似乎."),
  Q("他每天都来，＿＿他很重视。","可见/似乎/说不定/难得","Rút kết luận: 可见."),
  Q("这种结果让人＿＿接受。","难以/难得/不难/难的","难以 + V."),
  Q("＿＿他已经到了，你打电话问问。","说不定/可见/难以/总共","Biết đâu: 说不定.")]}
G[138]={"p":[
 P("朝 / 沿着","朝 + hướng + V ／ 沿着 + đường + V","朝 = hướng về; 沿着 = dọc theo.",
  ["他朝我走过来。|Tā cháo wǒ zǒu guòlai.|Anh ấy đi về phía tôi.","沿着这条路一直走。|Yánzhe zhè tiáo lù yìzhí zǒu.|Đi dọc con đường này thẳng tới."]),
 P("据 / 依据 / 凭","据 + nguồn (theo) ／ 凭 + N (dựa vào)","据说 = nghe nói; 据统计 = theo thống kê; 凭票入场 = vào cửa bằng vé.",
  ["据统计，故障率下降了。|Jù tǒngjì, gùzhànglǜ xiàjiàng le.|Theo thống kê, tỷ lệ sự cố đã giảm.","凭票入场。|Píng piào rùchǎng.|Vào cửa bằng vé."]),
 P("针对 + vấn đề","针对 + N，… ／ 针对性","Nhằm vào.",
  ["针对这个问题，我们制定了方案。|Zhēnduì zhège wèntí, wǒmen zhìdìng le fāng'àn.|Nhằm vào vấn đề này, chúng tôi đã lập phương án."])],
 "q":[Q("他＿＿我走过来。","朝/沿/距/据","Hướng về: 朝."),
  Q("＿＿统计，故障率下降了。","据/凭/朝/针","据统计."),
  Q("＿＿这个问题，我们制定了方案。","针对/依靠/沿着/朝着","Nhằm vào: 针对."),
  Q("＿＿这条路一直走。","沿着/朝着向/距离/据","Dọc theo: 沿着.")]}
G[139]={"p":[
 P("Lượng từ HSK 5 (1)","一朵花 · 一束花 · 一颗心 · 一匹马 · 一批货 · 一届比赛 · 一阵风","束 = bó; 批 = lô/đợt; 届 = khóa/kỳ; 阵 = cơn.",
  ["我送了她一束花。|Wǒ sòng le tā yí shù huā.|Tôi tặng cô ấy một bó hoa.","这批货明天到。|Zhè pī huò míngtiān dào.|Lô hàng này mai tới.","刮了一阵风。|Guā le yí zhèn fēng.|Thổi qua một cơn gió."]),
 P("Đơn vị đo: 吨","số + 吨","吨 = tấn.",
  ["这辆车能装五吨。|Zhè liàng chē néng zhuāng wǔ dūn.|Xe này chở được 5 tấn."])],
 "q":[Q("我送了她一＿＿花。","束/匹/批/届","Bó hoa: 束."),
  Q("这＿＿货明天到。","批/束/阵/朵","Lô hàng: 批."),
  Q("刮了一＿＿风。","阵/届/批/匹","Cơn gió: 阵."),
  Q("第十＿＿运动会","届/批/阵/册","Kỳ, khóa: 届.")]}
G[140]={"p":[
 P("Lượng từ HSK 5 (2)","一堆东西 · 一伙人 · 一团毛线 · 一类问题 · 第五集","堆 = đống; 伙 = nhóm; 类 = loại; 集 = tập (phim).",
  ["桌子上有一堆文件。|Zhuōzi shàng yǒu yì duī wénjiàn.|Trên bàn có một đống tài liệu.","这类问题很常见。|Zhè lèi wèntí hěn chángjiàn.|Loại vấn đề này rất thường gặp."]),
 P("Đơn vị cấp độ: 级 / 度","số + 级 ／ số + 度","级 = cấp; 度 = độ.",
  ["今天有五级风。|Jīntiān yǒu wǔ jí fēng.|Hôm nay gió cấp 5."])],
 "q":[Q("桌子上有一＿＿文件。","堆/团/伙/集","Đống: 堆."),
  Q("这＿＿问题很常见。","类/代/度/级","Loại: 类."),
  Q("这部电视剧一共四十＿＿。","集/册/代/届","Tập phim: 集."),
  Q("今天有五＿＿风。","级/度/类/堆","Cấp gió: 级.")]}
G[141]={"p":[
 P("其余 / 各自","其余 + N (số còn lại) ／ 各自 + V (mỗi người tự)","其余的人 = những người còn lại.",
  ["三个人去，其余的留下。|Sān ge rén qù, qíyú de liúxià.|Ba người đi, số còn lại ở lại.","大家各自回家了。|Dàjiā gèzì huí jiā le.|Mọi người ai về nhà nấy."]),
 P("所 + V + 的 (văn viết)","S + 所 + V + 的 + N","Nhấn mạnh tân ngữ của động từ.",
  ["这就是我所知道的。|Zhè jiù shì wǒ suǒ zhīdào de.|Đó là những gì tôi biết."]),
 P("彼此","彼此 + V/之间","Lẫn nhau.",
  ["我们彼此了解。|Wǒmen bǐcǐ liǎojiě.|Chúng tôi hiểu nhau."])],
 "q":[Q("三个人去，＿＿的留下。","其余/其他人/各自/个别","其余 = số còn lại."),
  Q("这就是我＿＿知道的。","所/的所/个/本","所 + V + 的."),
  Q("下班后大家＿＿回家了。","各自/彼此/他人/本人","Ai về nhà nấy: 各自."),
  Q("我们＿＿了解，合作很顺利。","彼此/各自/其余/所","Lẫn nhau: 彼此.")]}
G[142]={"p":[
 P("Thời kỳ: 初期 / 早期 / 近年来","N + 初期/早期 ／ 近年来，…","Mốc thời gian văn viết.",
  ["近年来，电动车发展很快。|Jìnniánlái, diàndòngchē fāzhǎn hěn kuài.|Những năm gần đây xe điện phát triển rất nhanh.","项目初期遇到了很多问题。|Xiàngmù chūqī yùdào le hěn duō wèntí.|Giai đoạn đầu dự án gặp nhiều vấn đề."]),
 P("当前 / 当年","当前 + N ／ 当年 (năm ấy)","当前 = hiện nay; 当年 = năm đó, hồi đó.",
  ["当前的任务是降低成本。|Dāngqián de rènwu shì jiàngdī chéngběn.|Nhiệm vụ hiện nay là giảm chi phí."])],
 "q":[Q("＿＿，电动车发展很快。","近年来/近日的/今日来/当年来","近年来."),
  Q("项目＿＿遇到了很多问题。","初期/初/早/当","Giai đoạn đầu: 初期."),
  Q("＿＿的任务是降低成本。","当前/当年/近期地/早期","Hiện nay: 当前."),
  Q("下个月＿＿，我去出差。","初/前初/期初/早期","月初 = đầu tháng.")]}
G[143]={"p":[
 P("Phong tục Tết: 在 + dịp + V","除夕吃年夜饭 / 过年给压岁钱","Kể phong tục.",
  ["除夕晚上，全家人一起吃年夜饭。|Chúxī wǎnshang, quán jiā rén yìqǐ chī niányèfàn.|Đêm giao thừa cả nhà cùng ăn bữa cơm tất niên.","过年时长辈给孩子压岁钱。|Guònián shí zhǎngbèi gěi háizi yāsuìqián.|Tết người lớn mừng tuổi trẻ con."]),
 P("Kỷ niệm: 周年","số + 周年 ／ …的纪念日","Năm thứ… (kỷ niệm).",
  ["今天是我们结婚十周年。|Jīntiān shì wǒmen jiéhūn shí zhōunián.|Hôm nay kỷ niệm 10 năm ngày cưới của chúng tôi."])],
 "q":[Q("除夕晚上全家人一起吃＿＿。","年夜饭/压岁钱/元旦/婚礼","年夜饭."),
  Q("今天是公司成立十＿＿。","周年/年周/纪念/年代","十周年."),
  Q("过年时长辈给孩子＿＿。","压岁钱/年夜饭/红/礼物钱","压岁钱 = tiền mừng tuổi."),
  Q("一月一日是＿＿。","元旦/除夕/国庆/春节","元旦 = Tết dương lịch.")]}
G[144]={"p":[
 P("Xưng hô họ ngoại / thân mật","姥姥/外婆 (bà ngoại) · 老公/老婆 (chồng/vợ, thân mật)","外 chỉ họ ngoại.",
  ["我周末去看外婆。|Wǒ zhōumò qù kàn wàipó.|Cuối tuần tôi đi thăm bà ngoại.","我老公做饭很好吃。|Wǒ lǎogōng zuò fàn hěn hǎochī.|Chồng tôi nấu ăn rất ngon."]),
 P("Câu giới thiệu trang trọng","这位是 + người + 太太/夫妇","太太 = bà (vợ ai đó), trang trọng.",
  ["这位是王先生和王太太。|Zhè wèi shì Wáng xiānsheng hé Wáng tàitai.|Đây là ông bà Vương."])],
 "q":[Q("bà ngoại","外婆/奶奶/婆外/姥爷","外婆 hoặc 姥姥."),
  Q("这位是王先生和王＿＿。","太太/老婆/夫妇/外婆","Trang trọng: 太太."),
  Q("他们是一对老＿＿。","夫妇/儿女/外公/老公","夫妇 = vợ chồng."),
  Q("父母都希望＿＿过得幸福。","儿女/外婆/太太/夫","儿女 = con cái.")]}
G[145]={"p":[
 P("跟 + người + 谈恋爱 / 分手 / 离婚","跟 + người + 谈恋爱/分手/离婚","Các động từ này không mang tân ngữ người.",
  ["他跟女朋友分手了。|Tā gēn nǚpéngyou fēnshǒu le.|Anh ấy chia tay bạn gái rồi."],None,"他分手女朋友了。|他跟女朋友分手了。"),
 P("对 + người + 很亲切","对 + người + 亲切/热情","Thân thiết, niềm nở.",
  ["老师对我们很亲切。|Lǎoshī duì wǒmen hěn qīnqiè.|Thầy rất thân thiết với chúng tôi."])],
 "q":[Q("他＿＿女朋友分手了。","跟/对/给/向","跟 + người + 分手."),
  Q("他们在＿＿，常常约会。","谈恋爱/恋爱谈/失恋/分手了","谈恋爱."),
  Q("老师对我们很＿＿。","亲切/亲爱/亲/宝贝","亲切 = thân thiết."),
  Q("两个人见面时＿＿了一下。","拥抱/拥/抱拥/亲爱","拥抱 = ôm.")]}
G[146]={"p":[
 P("对 + N + 充满期待/好奇","对 + N + 很好奇/充满期待","Tò mò/mong đợi về.",
  ["孩子对什么都很好奇。|Háizi duì shénme dōu hěn hàoqí.|Trẻ con tò mò về mọi thứ.","我对新工作充满期待。|Wǒ duì xīn gōngzuò chōngmǎn qīdài.|Tôi tràn đầy mong đợi với công việc mới."]),
 P("享受 / 欣赏 + N","享受 + 生活 ／ 欣赏 + 风景/人","享受 = tận hưởng; 欣赏 = thưởng thức, đánh giá cao.",
  ["我很欣赏他的能力。|Wǒ hěn xīnshǎng tā de nénglì.|Tôi rất đánh giá cao năng lực của anh ấy."]),
 P("给 + người + 一个惊喜","给 + người + 惊喜","Tạo bất ngờ.",
  ["我想给她一个惊喜。|Wǒ xiǎng gěi tā yí ge jīngxǐ.|Tôi muốn tạo bất ngờ cho cô ấy."])],
 "q":[Q("孩子＿＿什么都很好奇。","对/给/为/让","对 + N + 好奇."),
  Q("我很＿＿他的能力。","欣赏/享受/满足/乐趣","Đánh giá cao: 欣赏."),
  Q("我想给她一个＿＿。","惊喜/期待/乐观/热爱","给…惊喜."),
  Q("他是个很＿＿的人，从不担心。","乐观/满足/享受/欣赏","乐观 = lạc quan.")]}
G[147]={"p":[
 P("对 + N + 感到遗憾 / 抱怨 + N","对 + N + 感到遗憾 ／ 抱怨 + N","Lấy làm tiếc; phàn nàn.",
  ["对此我们感到很遗憾。|Duì cǐ wǒmen gǎndào hěn yíhàn.|Về việc này chúng tôi rất lấy làm tiếc.","他总是抱怨工作太多。|Tā zǒngshì bàoyuàn gōngzuò tài duō.|Anh ấy luôn phàn nàn việc quá nhiều."]),
 P("犹豫 / 无奈","犹豫 + 要不要 + V ／ 很无奈","Do dự; bất lực.",
  ["我犹豫要不要去。|Wǒ yóuyù yào bu yào qù.|Tôi do dự có nên đi không."]),
 P("糟了 / 糟糕","(真)糟糕！","Hỏng rồi! (khẩu ngữ).",
  ["糟了，我忘带护照了！|Zāo le, wǒ wàng dài hùzhào le!|Chết rồi, tôi quên mang hộ chiếu!"])],
 "q":[Q("对此我们感到很＿＿。","遗憾/抱怨/犹豫/可怕","感到遗憾."),
  Q("我＿＿要不要去。","犹豫/无奈/消极/痛苦","犹豫 + 要不要."),
  Q("＿＿了，我忘带护照了！","糟/疯/苦/怕","糟了!"),
  Q("他总是＿＿工作太多。","抱怨/遗憾/犹豫了/怨","抱怨 + N.")]}
G[148]={"p":[
 P("Câu miêu tả tính cách","S + 是 + 一个 + Adj + 的人","Giới thiệu tính cách.",
  ["她是一个很善良的人。|Tā shì yí ge hěn shànliáng de rén.|Cô ấy là người rất lương thiện.","他工作勤奋，又很虚心。|Tā gōngzuò qínfèn, yòu hěn xūxīn.|Anh ấy làm việc chăm chỉ lại khiêm tốn."]),
 P("Adj + 得 + 不得了 / 极了","能干得很","Khẩu ngữ nhấn mạnh.",
  ["这个孩子调皮得不得了。|Zhège háizi tiáopí de bùdéliǎo.|Đứa bé này nghịch kinh khủng."])],
 "q":[Q("她是一个很＿＿的人。","善良/善良地/良善的/善良得","Adj + 的人."),
  Q("这个孩子调皮＿＿不得了。","得/的/地/了","Adj + 得 + 不得了."),
  Q("他很＿＿，敢一个人去旅行。","大胆/胆小/傻/调皮","大胆 = gan dạ."),
  Q("他工作很＿＿，每天加班。","勤奋/虚心/坚强/大胆","勤奋 = chăm chỉ.")]}
G[149]={"p":[
 P("保持 + 心态 / 精力","保持 + 好的心态 ／ 精力 + 充沛","Giữ tâm thế; tràn đầy năng lượng.",
  ["遇到困难要保持好的心态。|Yùdào kùnnán yào bǎochí hǎo de xīntài.|Gặp khó khăn phải giữ tâm thế tốt."]),
 P("Adj + 意识 / 自觉","有 + 安全意识 ／ 自觉 + V","意识 = ý thức; 自觉 = tự giác.",
  ["员工要有安全意识。|Yuángōng yào yǒu ānquán yìshí.|Nhân viên phải có ý thức an toàn.","他自觉地遵守规定。|Tā zìjué de zūnshǒu guīdìng.|Anh ấy tự giác tuân thủ quy định."]),
 P("控制 + 情绪","控制 + 情绪/成本","Kiểm soát.",
  ["他不能控制自己的情绪。|Tā bù néng kòngzhì zìjǐ de qíngxù.|Anh ấy không kiểm soát được cảm xúc."])],
 "q":[Q("员工要有安全＿＿。","意识/心理/精神/心态","安全意识."),
  Q("遇到困难要保持好的＿＿。","心态/情景/意识/精力了","保持心态."),
  Q("他不能控制自己的＿＿。","情绪/心理学/自觉/精","控制情绪."),
  Q("他＿＿地遵守规定。","自觉/意识/精神/心态","自觉 = tự giác.")]}
G[150]={"p":[
 P("Lượng từ bộ phận cơ thể","一颗牙齿 · 一根手指 · 一双眼睛 · 一对翅膀","颗 = hạt/chiếc răng; 根 = ngón; 对 = đôi.",
  ["我掉了一颗牙。|Wǒ diào le yì kē yá.|Tôi rụng một cái răng."]),
 P("S + bộ phận + 疼/不舒服 (nặng hơn)","胃疼 · 腰疼 · 肌肉酸","Mô tả triệu chứng cụ thể.",
  ["我最近胃不太舒服。|Wǒ zuìjìn wèi bú tài shūfu.|Gần đây dạ dày tôi không thoải mái lắm.","坐久了腰疼。|Zuò jiǔ le yāo téng.|Ngồi lâu đau lưng."])],
 "q":[Q("我掉了一＿＿牙。","颗/根/双/对","Răng: 颗."),
  Q("一＿＿手指","根/颗/双/对","Ngón: 根."),
  Q("坐久了＿＿疼。","腰/胃了/翅膀/大脑","Đau lưng: 腰疼."),
  Q("鸟有一对＿＿。","翅膀/手指/嘴巴/肌肉","Cánh: 翅膀.")]}
G[151]={"p":[
 P("对 + N + 过敏","对 + N + 过敏","Dị ứng với.",
  ["我对海鲜过敏。|Wǒ duì hǎixiān guòmǐn.|Tôi dị ứng hải sản."],None,"我过敏海鲜。|我对海鲜过敏。"),
 P("病情 + 好转 / 加重","病情 + 好转了/加重了","Tình trạng bệnh.",
  ["他的病情已经好转了。|Tā de bìngqíng yǐjīng hǎozhuǎn le.|Bệnh tình của anh ấy đã chuyển biến tốt."]),
 P("着凉 / 失眠","V + 着凉了 ／ 经常失眠","Bị cảm lạnh; mất ngủ.",
  ["别开窗，小心着凉。|Bié kāi chuāng, xiǎoxīn zháoliáng.|Đừng mở cửa sổ, cẩn thận bị lạnh."])],
 "q":[Q("我＿＿海鲜过敏。","对/给/为/让","对 + N + 过敏."),
  Q("他的病情已经＿＿了。","好转/好了转/转好的/疼痛","好转."),
  Q("别开窗，小心＿＿。","着凉/失眠/流感/过敏","着凉 = bị lạnh."),
  Q("最近压力大，我经常＿＿。","失眠/睡眠/疼痛/疾病","失眠 = mất ngủ.")]}
G[152]={"p":[
 P("Quy trình khám bệnh","先挂号，再看门诊 ／ 做手术 ／ 接受治疗","Kể các bước.",
  ["先去挂号，然后排队看医生。|Xiān qù guàhào, ránhòu páiduì kàn yīshēng.|Trước tiên đi lấy số, sau đó xếp hàng khám.","他上周做了手术。|Tā shàng zhōu zuò le shǒushù.|Tuần trước anh ấy phẫu thuật."]),
 P("被 + 诊断为 + bệnh","被 + 诊断为 + N","Được chẩn đoán là.",
  ["他被诊断为胃病。|Tā bèi zhěnduàn wéi wèibìng.|Anh ấy được chẩn đoán đau dạ dày."]),
 P("叫 + 救护车","叫/打电话叫 + 救护车","Gọi xe cấp cứu.",
  ["快叫救护车！|Kuài jiào jiùhùchē!|Mau gọi xe cấp cứu!"])],
 "q":[Q("看病以前要先＿＿。","挂号/手术/诊断/治","挂号 = đăng ký khám."),
  Q("他被诊断＿＿胃病。","为/成/到/是为","诊断为."),
  Q("快叫＿＿！","救护车/急诊/病房/门诊车","救护车."),
  Q("他上周做了＿＿。","手术/治疗了/诊断了/挂号","做手术.")]}
G[153]={"p":[
 P("Rủ đi ăn: 要不 / 不如","要不我们去吃火锅吧 ／ 不如 + V","要不 = hay là; 不如 = chi bằng.",
  ["要不我们去吃火锅吧？|Yàobù wǒmen qù chī huǒguō ba?|Hay là mình đi ăn lẩu nhé?","不如去吃烧烤。|Bùrú qù chī shāokǎo.|Chi bằng đi ăn đồ nướng."]),
 P("A 不如 B (+ Adj)","A 不如 B + Adj","A không bằng B.",
  ["西餐不如中餐好吃。|Xīcān bùrú zhōngcān hǎochī.|Đồ Tây không ngon bằng đồ Trung."])],
 "q":[Q("＿＿我们去吃火锅吧？","要不/要不是/哪怕/如果是","Hay là: 要不."),
  Q("西餐＿＿中餐好吃。","不如/没比/不比如/如不","A 不如 B + Adj."),
  Q("早上喝一杯＿＿。","豆浆/豆腐/火锅/盒饭","豆浆 = sữa đậu nành."),
  Q("我想吃＿＿，特别是螃蟹。","海鲜/点心/西餐/饼","海鲜 = hải sản.")]}
G[154]={"p":[
 P("Động từ nấu nướng","切 · 炒 · 煮 · 蒸 · 烤 · 洗","Chế biến.",
  ["先把土豆切成块。|Xiān bǎ tǔdòu qiē chéng kuài.|Trước hết thái khoai tây thành miếng.","番茄炒鸡蛋很好吃。|Fānqié chǎo jīdàn hěn hǎochī.|Cà chua xào trứng rất ngon."]),
 P("把 + N + V + 成 + hình dạng","把 + N + 切成 + 片/块/丝","Biến đổi hình dạng.",
  ["把黄瓜切成片。|Bǎ huángguā qiē chéng piàn.|Thái dưa chuột thành lát."])],
 "q":[Q("把土豆切＿＿块。","成/到/为了/给","切成."),
  Q("多吃＿＿对身体好。","蔬菜/果实了/种子/土豆们","蔬菜 = rau."),
  Q("番茄＿＿鸡蛋很好吃。","炒/切/洗/烤了","Xào: 炒."),
  Q("一个＿＿","橘子/玉米粒/蔬菜们/果实的","一个橘子.")]}
G[155]={"p":[
 P("Câu tồn tại trong phòng","nơi + 放着/摆着/挂着 + N","Mô tả phòng.",
  ["卧室里放着一张床和一个柜子。|Wòshì lǐ fàngzhe yì zhāng chuáng hé yí ge guìzi.|Trong phòng ngủ đặt một cái giường và một cái tủ.","书架上摆着很多书。|Shūjià shàng bǎizhe hěn duō shū.|Trên giá sách bày rất nhiều sách."]),
 P("Lượng từ đồ dùng","一床被子 · 一盏台灯 · 一张床单","盏 = ngọn đèn.",
  ["书桌上有一盏台灯。|Shūzhuō shàng yǒu yì zhǎn táidēng.|Trên bàn có một ngọn đèn bàn."])],
 "q":[Q("书架上摆＿＿很多书。","着/了/过/在","Tồn tại: V + 着."),
  Q("一＿＿台灯","盏/张/床/个儿","Đèn: 盏."),
  Q("我在＿＿看书。","书房/卧书/阳书/书架里","书房 = phòng đọc."),
  Q("晚上睡觉要盖＿＿。","被子/床单/柜子/窗台","被子 = chăn.")]}
G[156]={"p":[
 P("交 + 租金/押金","交 + 房租/押金/物业费","Nộp.",
  ["租房要先交一个月押金。|Zū fáng yào xiān jiāo yí ge yuè yājīn.|Thuê nhà phải nộp trước một tháng tiền cọc."]),
 P("V + 一下 + câu hỏi gián tiếp","问一下 + 怎么… ／ 了解一下 + …","Hỏi thăm thông tin.",
  ["我想了解一下这套公寓的租金。|Wǒ xiǎng liǎojiě yíxià zhè tào gōngyù de zūjīn.|Tôi muốn tìm hiểu tiền thuê căn hộ này."]),
 P("正在 + 装修","房子 + 正在装修","Đang sửa sang.",
  ["新房子正在装修。|Xīn fángzi zhèngzài zhuāngxiū.|Nhà mới đang được sửa sang."])],
 "q":[Q("租房要先交一个月＿＿。","押金/租金了/住宿/物业","押金 = tiền cọc."),
  Q("新房子正在＿＿。","装修/修装/住房/房屋","装修."),
  Q("请写一下你的＿＿。","住址/住宿/房屋/公寓们","住址 = địa chỉ."),
  Q("我想＿＿一下这套公寓的租金。","了解/明白了/认识/知了","了解一下.")]}
G[157]={"p":[
 P("打扮 + 得 + Adj","打扮 + 得 + 很漂亮","Ăn mặc, trang điểm.",
  ["她今天打扮得很漂亮。|Tā jīntiān dǎban de hěn piàoliang.|Hôm nay cô ấy ăn diện rất đẹp."]),
 P("系 + 领带 / 围巾, 戴 + 手套","系领带 · 围围巾 · 戴手套","系 (jì) = thắt.",
  ["他穿西装，系着领带。|Tā chuān xīzhuāng, jìzhe lǐngdài.|Anh ấy mặc vest, thắt cà vạt.","冬天要戴手套。|Dōngtiān yào dài shǒutào.|Mùa đông phải đeo găng tay."]),
 P("风格 / 样式 + 很 + Adj","这件衣服的样式很新","Kiểu dáng, phong cách.",
  ["我喜欢简单的风格。|Wǒ xǐhuan jiǎndān de fēnggé.|Tôi thích phong cách đơn giản."])],
 "q":[Q("她今天打扮＿＿很漂亮。","得/的/地/了","打扮得."),
  Q("他穿西装，＿＿着领带。","系/戴/穿/挂","Thắt cà vạt: 系."),
  Q("冬天要＿＿手套。","戴/穿/系/拿着","戴手套."),
  Q("我喜欢简单的＿＿。","风格/服装们/打扮着/围巾","风格 = phong cách.")]}
G[158]={"p":[
 P("Lượng từ động vật","一只兔子 · 一条蛇 · 一头猪/大象 · 一匹马","只 cho phần lớn con vật nhỏ; 条 cho con dài; 头 cho gia súc lớn.",
  ["动物园里有一头大象。|Dòngwùyuán lǐ yǒu yì tóu dàxiàng.|Trong sở thú có một con voi.","草地上有一条蛇。|Cǎodì shàng yǒu yì tiáo shé.|Trên bãi cỏ có một con rắn."]),
 P("像 + con vật + 一样","像 + 猴子 + 一样 + Adj","So sánh hình ảnh.",
  ["他像猴子一样灵活。|Tā xiàng hóuzi yíyàng línghuó.|Anh ấy nhanh nhẹn như khỉ."])],
 "q":[Q("一＿＿大象","头/只/条/匹","Voi: 头."),
  Q("一＿＿蛇","条/只/头/匹","Rắn: 条."),
  Q("一＿＿兔子","只/条/头/匹","Thỏ: 只."),
  Q("他像猴子＿＿灵活。","一样/似/相同/像","像…一样.")]}
G[159]={"p":[
 P("Thời tiết khắc nghiệt","下暴雨 · 起雾 · 有大雾","起雾 = có sương mù.",
  ["今天早上起雾了。|Jīntiān zǎoshang qǐ wù le.|Sáng nay có sương mù.","明天有暴雨，注意安全。|Míngtiān yǒu bàoyǔ, zhùyì ānquán.|Mai có mưa to, chú ý an toàn."]),
 P("Lượng từ địa hình","一片沙漠 · 一条河流 · 一个湖","片 = vùng rộng.",
  ["这是一片很大的沙漠。|Zhè shì yí piàn hěn dà de shāmò.|Đây là một vùng sa mạc rất lớn."])],
 "q":[Q("今天早上起＿＿了。","雾/雨/风暴/天空","起雾."),
  Q("这是一＿＿很大的沙漠。","片/条/个/座","Vùng: 片."),
  Q("明天有＿＿，注意安全。","暴雨/天空/陆地/湖","暴雨 = mưa to."),
  Q("鸟在＿＿飞。","空中/空/陆地里/河流","在空中.")]}
G[160]={"p":[
 P("Từ ly hợp và bổ ngữ trong trồng trọt","浇水 · 晒太阳 · 种 + 树/菜","种 (zhòng) = trồng; 晒 = phơi.",
  ["我每天给花浇水。|Wǒ měi tiān gěi huā jiāo shuǐ.|Ngày nào tôi cũng tưới hoa.","把衣服拿出去晒晒。|Bǎ yīfu ná chūqu shàishai.|Mang quần áo ra phơi đi."]),
 P("Adj + 了 (thay đổi trạng thái)","冻 + 了 ／ 湿 + 了","Biến đổi.",
  ["下雨了，衣服都湿了。|Xià yǔ le, yīfu dōu shī le.|Mưa rồi, quần áo ướt hết."])],
 "q":[Q("我每天给花＿＿水。","浇/洒水/喝/种","浇水."),
  Q("把衣服拿出去＿＿。","晒晒/湿湿/冻冻/生长","Phơi: 晒."),
  Q("下雨了，衣服都＿＿了。","湿/晒/冻/升温","Ướt: 湿."),
  Q("春天是＿＿的季节。","种植/种子了/洒/冻","种植 = trồng trọt.")]}
G[161]={"p":[
 P("发生 + 车祸","发生了 + 车祸/事故","Xảy ra tai nạn.",
  ["路口发生了一起车祸。|Lùkǒu fāshēng le yì qǐ chēhuò.|Ở ngã tư xảy ra một vụ tai nạn."]),
 P("Lượng từ: 起 (vụ), 节 (toa), 列 (đoàn tàu)","一起事故 · 第三节车厢 · 一列火车","起 = vụ (sự việc).",
  ["我的座位在第五节车厢。|Wǒ de zuòwèi zài dì wǔ jié chēxiāng.|Chỗ ngồi của tôi ở toa thứ 5."])],
 "q":[Q("路口发生了一＿＿车祸。","起/个次/件/场儿","Vụ: 起."),
  Q("我的座位在第五＿＿车厢。","节/列/辆/个","Toa: 节."),
  Q("一＿＿火车","列/节/辆/条","Đoàn tàu: 列."),
  Q("请到三号＿＿上车。","站台/车厢/铁路/车主","站台 = sân ga.")]}
G[162]={"p":[
 P("往返 / 单程","往返 + nơi ／ 往返票","Khứ hồi.",
  ["我买了一张往返票。|Wǒ mǎi le yì zhāng wǎngfǎn piào.|Tôi mua một vé khứ hồi."]),
 P("步行 + thời gian","步行 + 十分钟 ／ 步行去","Đi bộ (văn viết).",
  ["从这里步行到车站只要五分钟。|Cóng zhèlǐ bùxíng dào chēzhàn zhǐ yào wǔ fēnzhōng.|Từ đây đi bộ đến ga chỉ mất 5 phút."]),
 P("禁止 + 通行","禁止通行 ／ 行人 + 请走…","Biển báo giao thông.",
  ["前方施工，禁止通行。|Qiánfāng shīgōng, jìnzhǐ tōngxíng.|Phía trước thi công, cấm lưu thông."])],
 "q":[Q("我买了一张＿＿票。","往返/返往/来去/长途的","往返票."),
  Q("从这里＿＿到车站只要五分钟。","步行/行步/走行/行走着","步行."),
  Q("前方施工，禁止＿＿。","通行/行人/路人/线路","禁止通行."),
  Q("坐＿＿汽车去外地。","长途/往返/路线/行走","长途汽车.")]}
G[163]={"p":[
 P("预订 / 预约","预订 + 房间/票 ／ 预约 + 时间/医生","预订 = đặt trước (đồ, chỗ); 预约 = đặt lịch hẹn.",
  ["我在网上预订了酒店。|Wǒ zài wǎngshàng yùdìng le jiǔdiàn.|Tôi đặt khách sạn trên mạng.","看医生要先预约。|Kàn yīshēng yào xiān yùyuē.|Khám bệnh phải đặt lịch trước."]),
 P("当地的特产 / 特色","N + 的特色 ／ 当地特产","Đặc sản, nét đặc sắc.",
  ["这是我们当地的特产。|Zhè shì wǒmen dāngdì de tèchǎn.|Đây là đặc sản địa phương chúng tôi."])],
 "q":[Q("我在网上＿＿了酒店。","预订/预约了约/订预/游览","Đặt phòng: 预订."),
  Q("看医生要先＿＿。","预约/预订/行程/游览","Đặt lịch: 预约."),
  Q("这是我们当地的＿＿。","特产/特色地/夜市了/户外","特产 = đặc sản."),
  Q("这次旅行的＿＿很紧。","行程/旅行社/游览了/预订","行程 = lịch trình.")]}
G[164]={"p":[
 P("Giảm giá: 打折 / 优惠","享受 + 优惠 ／ 打 + 折扣","享受优惠 = được ưu đãi.",
  ["会员可以享受九折优惠。|Huìyuán kěyǐ xiǎngshòu jiǔ zhé yōuhuì.|Hội viên được ưu đãi giảm 10%."]),
 P("涨价 / 降价 + số lượng","涨了 + số ／ 物价上涨","Tăng/giảm giá.",
  ["汽油又涨价了。|Qìyóu yòu zhǎngjià le.|Xăng lại tăng giá.","最近物价上涨得很快。|Zuìjìn wùjià shàngzhǎng de hěn kuài.|Gần đây vật giá tăng rất nhanh."])],
 "q":[Q("会员可以享受九折＿＿。","优惠/折扣地/促销了/售价","享受优惠."),
  Q("汽油又＿＿了。","涨价/价涨/物价/消费","涨价."),
  Q("最近＿＿上涨得很快。","物价/售价们/消费者/便利店","物价 = vật giá."),
  Q("超市在＿＿，很多东西打折。","促销/优惠了/消费/涨价","促销 = khuyến mãi.")]}
G[165]={"p":[
 P("跟 + người + 做生意/交易","跟 + 客户 + 做生意","Làm ăn với ai.",
  ["我们跟这家公司做了十年生意。|Wǒmen gēn zhè jiā gōngsī zuò le shí nián shēngyi.|Chúng tôi làm ăn với công ty này 10 năm."]),
 P("降低成本，提高利润","降低 + 成本 ／ 提高 + 利润","Cặp từ hay dùng trong kinh doanh.",
  ["我们必须降低成本，提高利润。|Wǒmen bìxū jiàngdī chéngběn, tígāo lìrùn.|Chúng ta phải giảm chi phí, nâng lợi nhuận."]),
 P("为 + 客户 + 提供 + 服务","为 + N + 提供 + N","Cung cấp cho.",
  ["我们为客户提供维修服务。|Wǒmen wèi kèhù tígōng wéixiū fúwù.|Chúng tôi cung cấp dịch vụ bảo trì cho khách hàng."])],
 "q":[Q("我们＿＿客户提供维修服务。","为/对/让/被","为…提供…."),
  Q("我们必须降低＿＿。","成本/利润/交易/商业","降低成本."),
  Q("我们＿＿这家公司做了十年生意。","跟/对/为/给着","跟…做生意."),
  Q("今年的＿＿增加了20%。","利润/买卖了/商人/老板们","利润 = lợi nhuận.")]}
G[166]={"p":[
 P("Định ngữ chuỗi danh từ","中国的汽车产业 / 优质产品","Danh từ ghép làm định ngữ có thể bỏ 的.",
  ["越南的电动车产业发展很快。|Yuènán de diàndòngchē chǎnyè fāzhǎn hěn kuài.|Ngành xe điện Việt Nam phát triển nhanh."]),
 P("生产 + 产品 ／ 产量 + 增加","生产 + N ／ 产量 + 达到 + số","Sản xuất, sản lượng.",
  ["这家工厂每年生产十万辆车。|Zhè jiā gōngchǎng měi nián shēngchǎn shí wàn liàng chē.|Nhà máy này mỗi năm sản xuất 100.000 xe."])],
 "q":[Q("这家工厂每年＿＿十万辆车。","生产/产量/产业/产品","生产 + N."),
  Q("我们的＿＿质量很好。","产品/生产了/工业化/繁荣","产品 = sản phẩm."),
  Q("这是一家大型＿＿。","企业/产业们/品牌化/工业的","企业 = doanh nghiệp."),
  Q("经济很＿＿。","繁荣/优质的/产量/品牌","繁荣 = phồn vinh.")]}
G[167]={"p":[
 P("Ngân hàng: 存 / 取 / 转","在 + 账户 + 里存钱 ／ 把钱转到 + 账户","Giao dịch.",
  ["我把钱转到你的账户了。|Wǒ bǎ qián zhuǎn dào nǐ de zhànghù le.|Tôi đã chuyển tiền vào tài khoản của bạn."]),
 P("汇率 / 兑换","人民币 + 对 + 越南盾 + 的汇率","Tỷ giá.",
  ["今天人民币对越南盾的汇率是多少？|Jīntiān rénmínbì duì Yuènándùn de huìlǜ shì duōshao?|Hôm nay tỷ giá nhân dân tệ với đồng Việt Nam là bao nhiêu?"]),
 P("交 + 税 / 买 + 保险","交税 ／ 买保险","Nộp thuế, mua bảo hiểm.",
  ["公司给员工买了保险。|Gōngsī gěi yuángōng mǎi le bǎoxiǎn.|Công ty mua bảo hiểm cho nhân viên."])],
 "q":[Q("我把钱转＿＿你的账户了。","到/给/成/在了","转到 + tài khoản."),
  Q("人民币＿＿越南盾的汇率是多少？","对/给/跟着/比较","A 对 B 的汇率."),
  Q("公司给员工买了＿＿。","保险/税/资金/黄金","买保险."),
  Q("请输入你的银行＿＿。","账号/存款了/汇率/资金","账号 = số tài khoản.")]}
G[168]={"p":[
 P("投 + 简历","向 + 公司 + 投简历","Nộp hồ sơ.",
  ["我向三家公司投了简历。|Wǒ xiàng sān jiā gōngsī tóu le jiǎnlì.|Tôi gửi CV cho ba công ty."]),
 P("待遇 + Adj / 负责 + 业务","待遇很好 ／ 负责 + 业务","Đãi ngộ; phụ trách mảng.",
  ["这家公司待遇不错。|Zhè jiā gōngsī dàiyù búcuò.|Công ty này đãi ngộ tốt.","我负责海外业务。|Wǒ fùzé hǎiwài yèwù.|Tôi phụ trách mảng kinh doanh nước ngoài."]),
 P("向 + 领导 + 汇报","向 + người + 汇报","Báo cáo lên cấp trên.",
  ["我每周向领导汇报工作。|Wǒ měi zhōu xiàng lǐngdǎo huìbào gōngzuò.|Hàng tuần tôi báo cáo công việc với lãnh đạo."])],
 "q":[Q("我每周＿＿领导汇报工作。","向/对着/给了/跟着","向 + người + 汇报."),
  Q("我＿＿三家公司投了简历。","向/对/在/让","向…投简历."),
  Q("我负责海外＿＿。","业务/待遇/总部/单元","负责业务."),
  Q("这家公司的＿＿不错。","待遇/职工们/机构/领导的","待遇 = đãi ngộ.")]}
G[169]={"p":[
 P("从事 + ngành / 担任 + chức vụ","从事 + 工作 ／ 担任 + 职位","Làm nghề; đảm nhiệm.",
  ["他从事技术工作十年了。|Tā cóngshì jìshù gōngzuò shí nián le.|Anh ấy làm kỹ thuật 10 năm rồi.","她担任部门经理。|Tā dānrèn bùmén jīnglǐ.|Cô ấy giữ chức trưởng phòng."]),
 P("对 + người + 进行培训","对 + 员工 + 进行培训 ／ 参加培训","Đào tạo.",
  ["公司对新员工进行了培训。|Gōngsī duì xīn yuángōng jìnxíng le péixùn.|Công ty đã đào tạo nhân viên mới."]),
 P("在 + nơi + 实习","在 + 公司 + 实习","Thực tập.",
  ["我在一家工厂实习了三个月。|Wǒ zài yì jiā gōngchǎng shíxí le sān ge yuè.|Tôi thực tập ở một nhà máy ba tháng."])],
 "q":[Q("他＿＿技术工作十年了。","从事/担任/实习/聘请","从事 + 工作."),
  Q("她＿＿部门经理。","担任/从事/培训/劳动","担任 + chức vụ."),
  Q("公司＿＿新员工进行了培训。","对/给/为/让","对…进行培训."),
  Q("他有很强的专业＿＿。","技能/本领们/人力/劳动着","技能 = kỹ năng.")]}
G[170]={"p":[
 P("召开 / 主持 / 出席 + hội nghị","召开 + 会议 ／ 主持 + 会议 ／ 出席 + 会议","Tổ chức; chủ trì; có mặt.",
  ["公司下周召开年度大会。|Gōngsī xià zhōu zhàokāi niándù dàhuì.|Tuần sau công ty tổ chức đại hội thường niên.","会议由王经理主持。|Huìyì yóu Wáng jīnglǐ zhǔchí.|Cuộc họp do giám đốc Vương chủ trì."]),
 P("跟 + bên + 签订 + 协议/合同","跟/与 + N + 签订 + 合同","Ký kết.",
  ["我们跟客户签订了服务协议。|Wǒmen gēn kèhù qiāndìng le fúwù xiéyì.|Chúng tôi đã ký thỏa thuận dịch vụ với khách hàng."]),
 P("在会上发言","在 + 会上 + 发言/讲话","Phát biểu tại cuộc họp.",
  ["他在会上发了言。|Tā zài huì shàng fā le yán.|Anh ấy đã phát biểu tại cuộc họp."])],
 "q":[Q("会议＿＿王经理主持。","由/被/让/从","由 + người + 主持."),
  Q("我们＿＿客户签订了协议。","跟/对/向着/为","跟…签订."),
  Q("公司下周＿＿年度大会。","召开/出席/发言/主持着","召开 + 会议."),
  Q("他在会上发了＿＿。","言/讲话/发言/话讲","发言 tách: 发了言.")]}
G[171]={"p":[
 P("由 + thành viên + 组成","N + 由 + thành phần + 组成","Gồm có, được tạo thành từ.",
  ["我们的团队由十个人组成。|Wǒmen de tuánduì yóu shí ge rén zǔchéng.|Đội của chúng tôi gồm 10 người."]),
 P("跟 + bên + 合作","跟/与 + N + 合作","Hợp tác với.",
  ["我们跟V-Green合作了三年。|Wǒmen gēn V-Green hézuò le sān nián.|Chúng tôi đã hợp tác với V-Green ba năm."]),
 P("组织 + hoạt động","组织 + 活动/培训","Tổ chức.",
  ["公司组织员工去旅游。|Gōngsī zǔzhī yuángōng qù lǚyóu.|Công ty tổ chức cho nhân viên đi du lịch."])],
 "q":[Q("我们的团队＿＿十个人组成。","由/被/从/让","由…组成."),
  Q("我们＿＿V-Green合作了三年。","跟/对/给/向","跟…合作."),
  Q("公司＿＿员工去旅游。","组织/组成/组合/成员","组织 + hoạt động."),
  Q("他是我们团队的＿＿。","成员/集体/群体/组合了","成员 = thành viên.")]}
G[172]={"p":[
 P("制定 + 方案/计划 ／ 采取 + 措施","制定 + 方案 ／ 采取 + 措施 ／ 执行 + 计划","Cặp kết hợp văn bản công việc.",
  ["我们制定了新的维护方案。|Wǒmen zhìdìng le xīn de wéihù fāng'àn.|Chúng tôi đã lập phương án bảo trì mới.","必须采取有效措施。|Bìxū cǎiqǔ yǒuxiào cuòshī.|Phải áp dụng biện pháp hiệu quả."],"Rất hữu ích cho báo cáo: 制定方案 → 采取措施 → 执行/实施 → 评估效果."),
 P("采用 vs 采取","采用 + 技术/方法 ／ 采取 + 措施/行动","采用 = dùng (cụ thể); 采取 = áp dụng (hành động, biện pháp).",
  ["我们采用了新技术。|Wǒmen cǎiyòng le xīn jìshù.|Chúng tôi áp dụng công nghệ mới."])],
 "q":[Q("我们＿＿了新的维护方案。","制定/采取/执行着/措施","制定方案."),
  Q("必须＿＿有效措施。","采取/采用/制定/执行到","采取措施."),
  Q("我们＿＿了新技术。","采用/采取/实行/制订了","采用技术."),
  Q("这个计划从下个月开始＿＿。","实施/制定/措施/方案","实施 = thực thi.")]}
G[173]={"p":[
 P("促进 / 推动 + phát triển","促进/推动 + N + 的发展","Thúc đẩy.",
  ["新政策推动了电动车的发展。|Xīn zhèngcè tuīdòng le diàndòngchē de fāzhǎn.|Chính sách mới thúc đẩy sự phát triển của xe điện."]),
 P("提升 + 水平/质量 ／ 改进 + 方法","提升 + N ／ 改进 + N","Nâng cao; cải tiến.",
  ["我们需要改进服务流程，提升客户满意度。|Wǒmen xūyào gǎijìn fúwù liúchéng, tíshēng kèhù mǎnyìdù.|Chúng ta cần cải tiến quy trình dịch vụ, nâng cao mức hài lòng của khách hàng."]),
 P("促使 + người + V","A + 促使 + B + V","Khiến cho, thúc giục.",
  ["这次事故促使公司加强管理。|Zhè cì shìgù cùshǐ gōngsī jiāqiáng guǎnlǐ.|Sự cố này khiến công ty tăng cường quản lý."])],
 "q":[Q("新政策＿＿了电动车的发展。","推动/提升到/改革/改进了","推动发展."),
  Q("我们需要＿＿服务流程。","改进/促使/推广了/带动","改进流程."),
  Q("这次事故＿＿公司加强管理。","促使/促进/推进/提升","促使 + người + V."),
  Q("我们要＿＿客户满意度。","提升/推广/带动/改革","提升 + mức độ.")]}
G[174]={"p":[
 P("违反 + quy định / 违法","违反 + 规定/法律 ／ 违法","Vi phạm.",
  ["违反交通规定要罚款。|Wéifǎn jiāotōng guīdìng yào fákuǎn.|Vi phạm luật giao thông bị phạt tiền."]),
 P("被 + 罚 + số tiền","被 + 罚了 + số tiền","Bị phạt bao nhiêu.",
  ["他被罚了五百块。|Tā bèi fá le wǔbǎi kuài.|Anh ấy bị phạt 500 tệ."]),
 P("有 + 权利 + V","有权(利) + V","Có quyền.",
  ["每个人都有权利知道真相。|Měi ge rén dōu yǒu quánlì zhīdào zhēnxiàng.|Mỗi người đều có quyền biết sự thật."])],
 "q":[Q("＿＿交通规定要罚款。","违反/违法了/合法/证据","违反 + 规定."),
  Q("他被罚＿＿五百块。","了/到/给/成","被罚了 + số tiền."),
  Q("每个人都有＿＿知道真相。","权利/权力了/法院/证据","有权利 + V."),
  Q("这种做法是＿＿的。","合法/违反/罚款/证据","合法 = hợp pháp.")]}
G[175]={"p":[
 P("为 + 人民 + 服务","为人民服务","Khẩu hiệu thường gặp.",
  ["政府要为人民服务。|Zhèngfǔ yào wèi rénmín fúwù.|Chính phủ phải phục vụ nhân dân."]),
 P("Cách gọi dân chúng","人民 (nhân dân) · 居民 (cư dân) · 市民 (thị dân) · 老百姓 (dân thường)","Khác nhau về ngữ cảnh.",
  ["小区居民对物业很满意。|Xiǎoqū jūmín duì wùyè hěn mǎnyì.|Cư dân khu rất hài lòng với ban quản lý."])],
 "q":[Q("政府要为人民＿＿。","服务/办/管理到/工作着","为人民服务."),
  Q("小区＿＿对物业很满意。","居民/人民们/政治/总统","居民 = cư dân."),
  Q("这个政策受到了＿＿的欢迎。","大众/政府/主席/政治","大众 = công chúng."),
  Q("他是国家＿＿。","主席/居民/大众/百姓","主席 = chủ tịch.")]}
G[176]={"p":[
 P("做 / 进行 + 实验","做实验 ／ 对 + N + 进行实验/试验","实验 = thí nghiệm; 试验 = thử nghiệm.",
  ["我们对新电池进行了试验。|Wǒmen duì xīn diànchí jìnxíng le shìyàn.|Chúng tôi đã thử nghiệm pin mới."]),
 P("研发 / 研制 + sản phẩm","研发 + 新产品 ／ 研制 + 设备","Nghiên cứu phát triển.",
  ["公司正在研发新一代换电柜。|Gōngsī zhèngzài yánfā xīn yí dài huàndiànguì.|Công ty đang nghiên cứu phát triển tủ đổi pin thế hệ mới."]),
 P("从 + 理论 + 上 + 说","从 + N + 上 + 说/看","Xét về mặt….",
  ["从理论上说，这是可行的。|Cóng lǐlùn shàng shuō, zhè shì kěxíng de.|Về lý thuyết, việc này khả thi."])],
 "q":[Q("我们＿＿新电池进行了试验。","对/给/让/被","对…进行试验."),
  Q("公司正在＿＿新一代产品。","研发/实验/理论/化学","研发 = R&D."),
  Q("从理论＿＿说，这是可行的。","上/中/里/下","从…上说."),
  Q("学生在＿＿里做实验。","实验室/实验/科研/物理","实验室.")]}
G[177]={"p":[
 P("用 + 工具 + V","用 + 工具 + V","Dùng gì để làm.",
  ["请用这个工具拆开设备。|Qǐng yòng zhège gōngjù chāikāi shèbèi.|Hãy dùng dụng cụ này tháo thiết bị."]),
 P("Lượng từ máy móc","一台机器 · 一套设备 · 一件工具","台 = máy; 套 = bộ.",
  ["我们新买了一套检测设备。|Wǒmen xīn mǎi le yí tào jiǎncè shèbèi.|Chúng tôi mới mua một bộ thiết bị kiểm tra."]),
 P("由 + 机器人 + 完成","N + 由 + 机器 + 完成","Do máy thực hiện.",
  ["这道工序由机器人完成。|Zhè dào gōngxù yóu jīqìrén wánchéng.|Công đoạn này do robot thực hiện."])],
 "q":[Q("一＿＿检测设备","套/台/把/件","Bộ: 套."),
  Q("请＿＿这个工具拆开设备。","用/以/对/把用","用 + công cụ + V."),
  Q("这道工序＿＿机器人完成。","由/被/从/给","由…完成."),
  Q("这是一个＿＿家居系统。","智能/人工的/高科技了/机器","智能 = thông minh.")]}
G[178]={"p":[
 P("在 + 网上 + 搜索 / 下载","在网上 + 搜索/下载 + N","Thao tác mạng.",
  ["我在网上搜索资料。|Wǒ zài wǎngshàng sōusuǒ zīliào.|Tôi tìm tài liệu trên mạng.","请下载最新版本的软件。|Qǐng xiàzài zuìxīn bǎnběn de ruǎnjiàn.|Hãy tải phiên bản phần mềm mới nhất."]),
 P("软件 vs 硬件","软件 (phần mềm) ／ 硬件 (phần cứng)","Phân biệt khi báo lỗi.",
  ["这是软件问题，不是硬件问题。|Zhè shì ruǎnjiàn wèntí, bú shì yìngjiàn wèntí.|Đây là lỗi phần mềm, không phải phần cứng."])],
 "q":[Q("这是＿＿问题，重启一下就好了。","软件/硬件/网络化/在线的","Lỗi phần mềm: 软件."),
  Q("请＿＿最新版本的软件。","下载/浏览/搜/上网","下载 = tải xuống."),
  Q("我在网上＿＿资料。","搜索/下载了载/硬件/计算","搜索 = tìm kiếm."),
  Q("这个课程可以＿＿学习。","在线/网络/浏览器/计算机","在线 = trực tuyến.")]}
G[179]={"p":[
 P("扫 + 二维码","扫 + 二维码 + V","Quét mã QR.",
  ["请扫二维码付款。|Qǐng sǎo èrwéimǎ fùkuǎn.|Vui lòng quét mã QR để thanh toán."]),
 P("先注册，再登录","先 + 注册 + 账号，再 + 登录","Đăng ký, đăng nhập.",
  ["新用户需要先注册。|Xīn yònghù xūyào xiān zhùcè.|Người dùng mới cần đăng ký trước."]),
 P("把 + N + 升级/更新 + 到 + phiên bản","把 + 系统 + 升级到 + 最新版本","Nâng cấp.",
  ["我们把固件升级到了最新版本。|Wǒmen bǎ gùjiàn shēngjí dào le zuìxīn bǎnběn.|Chúng tôi đã nâng cấp firmware lên bản mới nhất."])],
 "q":[Q("请＿＿二维码付款。","扫/刷/打/看着","扫二维码."),
  Q("我们把系统升级＿＿了最新版本。","到/成/给/在","升级到."),
  Q("新用户需要先＿＿。","注册/登录了/开通了/平台","注册 = đăng ký."),
  Q("请输入密码＿＿。","登录/注册了/升级/用户","登录 = đăng nhập.")]}
G[180]={"p":[
 P("考试 + 及格 / 被 + 录取","考试及格了 ／ 被 + trường + 录取","Đỗ; được tuyển.",
  ["他被北京大学录取了。|Tā bèi Běijīng Dàxué lùqǔ le.|Cậu ấy được Đại học Bắc Kinh tuyển.","这次考试我及格了。|Zhè cì kǎoshì wǒ jígé le.|Kỳ thi này tôi đạt."]),
 P("Cấp độ: 初级 · 中级 · 高级","初级/中级/高级 + 水平/课程","Sơ, trung, cao cấp.",
  ["我现在是初级水平。|Wǒ xiànzài shì chūjí shuǐpíng.|Hiện tôi ở trình độ sơ cấp."])],
 "q":[Q("他＿＿北京大学录取了。","被/让/把/给","被…录取."),
  Q("这次考试我＿＿了。","及格/格及/题目/试卷","及格 = đạt."),
  Q("我现在是＿＿水平。","初级/初/级初/初期","初级 = sơ cấp."),
  Q("HSK 5 要求掌握 2500 个＿＿。","词汇/题目/试卷/报到","词汇 = từ vựng.")]}
G[181]={"p":[
 P("Lượng từ nghệ thuật","一首诗 · 一幅画 · 一部作品","首 = bài (thơ, nhạc); 幅 = bức.",
  ["他写了一首诗。|Tā xiě le yì shǒu shī.|Ông ấy viết một bài thơ.","墙上挂着一幅国画。|Qiáng shàng guàzhe yì fú guóhuà.|Trên tường treo một bức tranh Trung Quốc."]),
 P("据说 / 传说","据说 + câu ／ 传说中的 + N","Nghe nói; truyền thuyết.",
  ["据说这个地方有很多神话传说。|Jùshuō zhège dìfang yǒu hěn duō shénhuà chuánshuō.|Nghe nói nơi này có nhiều thần thoại truyền thuyết."])],
 "q":[Q("他写了一＿＿诗。","首/幅/篇/部","Thơ: 首."),
  Q("墙上挂着一＿＿画。","幅/首/张开/部","Tranh: 幅."),
  Q("＿＿这个地方有很多传说。","据说/说据/传说/神话","据说 = nghe nói."),
  Q("写＿＿要用毛笔。","书法/美术/图画/文学","书法 = thư pháp.")]}
G[182]={"p":[
 P("在 + 片中 + 扮演 + vai","在 + phim + 中 + 扮演 + 角色","Đóng vai.",
  ["她在片中扮演一位医生。|Tā zài piàn zhōng bànyǎn yí wèi yīshēng.|Trong phim cô ấy đóng vai một bác sĩ."]),
 P("为 + người + 鼓掌","为 + N + 鼓掌 ／ 响起 + 掌声","Vỗ tay.",
  ["观众为他鼓掌。|Guānzhòng wèi tā gǔzhǎng.|Khán giả vỗ tay cho anh ấy.","台下响起了热烈的掌声。|Tái xià xiǎngqǐ le rèliè de zhǎngshēng.|Dưới khán đài vang lên tràng pháo tay nồng nhiệt."])],
 "q":[Q("观众＿＿他鼓掌。","为/对/给了/向着","为…鼓掌."),
  Q("她在片中扮演一位医生，这是她的第一个＿＿。","角色/歌曲/动画/影片","角色 = vai diễn."),
  Q("台下响起了热烈的＿＿。","掌声/鼓掌/歌词/歌曲声","掌声 = tiếng vỗ tay."),
  Q("我喜欢看自然＿＿。","纪录片/动画了/角色/影视剧了","纪录片 = phim tài liệu.")]}
G[183]={"p":[
 P("Tỉ số: 以 + tỉ số + 战胜","A 以 + tỉ số + 战胜/赢了 + B","Thắng với tỉ số.",
  ["我们以三比一战胜了对手。|Wǒmen yǐ sān bǐ yī zhànshèng le duìshǒu.|Chúng tôi thắng đối thủ 3–1."]),
 P("获得 + 冠军 / 进入 + 决赛","获得 + 冠军 ／ 进入 + 决赛","Vô địch; vào chung kết.",
  ["他们进入了决赛，最后获得了冠军。|Tāmen jìnrù le juésài, zuìhòu huòdé le guànjūn.|Họ vào chung kết và cuối cùng giành chức vô địch."])],
 "q":[Q("我们＿＿三比一战胜了对手。","以/用于/在/对","以 + tỉ số."),
  Q("他们获得了＿＿。","冠军/决赛了/比分/对手","获得冠军."),
  Q("\"3–1\" đọc là:","三比一/三对一了/一比三/三一比","三比一."),
  Q("运动员每天都要＿＿。","训练/胜/比分/赛场","训练 = tập luyện.")]}
G[184]={"p":[
 P("Bị động nghĩa: 展出 / 举行","N + 在 + nơi + 展出 ／ 开幕式 + 在 + nơi + 举行","Câu bị động không cần 被.",
  ["这些作品在博物馆展出。|Zhèxiē zuòpǐn zài bówùguǎn zhǎnchū.|Những tác phẩm này được trưng bày ở bảo tàng.","开幕式明天上午举行。|Kāimùshì míngtiān shàngwǔ jǔxíng.|Lễ khai mạc diễn ra sáng mai."]),
 P("开展 + hoạt động / 展开 + thảo luận","开展 + 活动/工作 ／ 展开 + 讨论/调查","开展 = triển khai; 展开 = mở ra, bắt đầu.",
  ["我们开展了安全检查活动。|Wǒmen kāizhǎn le ānquán jiǎnchá huódòng.|Chúng tôi đã triển khai hoạt động kiểm tra an toàn."])],
 "q":[Q("我们＿＿了安全检查活动。","开展/展开了开/展示/展出","开展活动."),
  Q("这些作品在博物馆＿＿。","展出/开展/开幕/展开","展出 = trưng bày."),
  Q("大家对这个问题＿＿了讨论。","展开/开展/展览/展示","展开讨论."),
  Q("＿＿明天上午举行。","开幕式/开幕/展览会了/展现","开幕式.")]}
G[185]={"p":[
 P("受到 + 好评 / 得到 + 评价","受到 + 好评 ／ 对 + N + 的评价","Được đánh giá tốt.",
  ["这款产品受到了用户的好评。|Zhè kuǎn chǎnpǐn shòudào le yònghù de hǎopíng.|Sản phẩm này được người dùng đánh giá tốt."]),
 P("Nguồn tin: 据 + 报道","据 + 媒体 + 报道，…","Theo đưa tin.",
  ["据新闻报道，明天有台风。|Jù xīnwén bàodào, míngtiān yǒu táifēng.|Theo bản tin, mai có bão."])],
 "q":[Q("这款产品受到了用户的＿＿。","好评/评价了/宣传/话题","受到好评."),
  Q("＿＿新闻报道，明天有台风。","据/凭/根/由","据…报道."),
  Q("这本书已经＿＿了。","出版/印刷了印/传播/宣传了","出版 = xuất bản."),
  Q("这个＿＿最近很热。","话题/标题了/评/宣传着","话题 = chủ đề.")]}
G[186]={"p":[
 P("用 + từ + 来 + 形容/表达","用 + N + 来 + 形容/表达 + N","Dùng gì để diễn tả.",
  ["我不知道用什么词来形容。|Wǒ bù zhīdào yòng shénme cí lái xíngróng.|Tôi không biết dùng từ gì để diễn tả.","用汉语表达自己的想法。|Yòng Hànyǔ biǎodá zìjǐ de xiǎngfǎ.|Dùng tiếng Hán diễn đạt suy nghĩ của mình."]),
 P("把 A 比喻成 B","把 + A + 比喻成 + B","Ví A như B.",
  ["人们常把时间比喻成金钱。|Rénmen cháng bǎ shíjiān bǐyù chéng jīnqián.|Người ta thường ví thời gian như tiền bạc."]),
 P("概括 + 一下","请概括一下 + N","Tóm tắt.",
  ["请概括一下这篇文章的内容。|Qǐng gàikuò yíxià zhè piān wénzhāng de nèiróng.|Hãy tóm tắt nội dung bài này."])],
 "q":[Q("我不知道用什么词来＿＿。","形容/描述着/语气/用法","形容 = miêu tả."),
  Q("人们常把时间比喻＿＿金钱。","成/为了/到/给","比喻成."),
  Q("请＿＿一下这篇文章的内容。","概括/表达了/讲述着/语音","概括 = tóm tắt."),
  Q("这个词的＿＿很多。","用法/语气们/语音的/描述","用法 = cách dùng.")]}
G[187]={"p":[
 P("从 + góc độ + 来 + 思考","从 + N + 的角度 + 来 + 思考","Suy nghĩ từ góc độ.",
  ["从客户的角度来思考问题。|Cóng kèhù de jiǎodù lái sīkǎo wèntí.|Suy nghĩ vấn đề từ góc độ khách hàng."]),
 P("改变 + 观念 / 提高 + 思维","改变 + 观念 ／ 有逻辑","Thay đổi quan niệm.",
  ["我们需要改变传统观念。|Wǒmen xūyào gǎibiàn chuántǒng guānniàn.|Chúng ta cần thay đổi quan niệm truyền thống.","他说话很有逻辑。|Tā shuōhuà hěn yǒu luójí.|Anh ấy nói chuyện rất logic."])],
 "q":[Q("从客户的角度＿＿思考问题。","来/去/上/着","从…来思考."),
  Q("我们需要改变传统＿＿。","观念/思考了/想象/记忆","改变观念."),
  Q("他说话很有＿＿。","逻辑/概念了/思想地/智慧着","有逻辑."),
  Q("这个问题需要认真＿＿。","思考/思维/观念/记忆","思考 = suy nghĩ.")]}
G[188]={"p":[
 P("有 + 悠久的历史","有 + số + 年的历史 ／ 历史悠久","Có lịch sử lâu đời.",
  ["这座城市有一千多年的历史。|Zhè zuò chéngshì yǒu yìqiān duō nián de lìshǐ.|Thành phố này có lịch sử hơn 1000 năm.","中国文化历史悠久。|Zhōngguó wénhuà lìshǐ yōujiǔ.|Văn hóa Trung Quốc có lịch sử lâu đời."]),
 P("保持 / 继承 + 传统","保持/继承 + 传统","Giữ gìn truyền thống.",
  ["我们要继承优秀的传统。|Wǒmen yào jìchéng yōuxiù de chuántǒng.|Chúng ta phải kế thừa truyền thống tốt đẹp."])],
 "q":[Q("这座城市有一千多年的＿＿。","历史/古代/古老/悠久","有…的历史."),
  Q("中国文化历史＿＿。","悠久/长久的/古老地/传统","历史悠久."),
  Q("我们要继承优秀的＿＿。","传统/经典了/现代化/近代","继承传统."),
  Q("这是一部＿＿作品，很多人都读过。","经典/古/近代的了/现代化","经典 = kinh điển.")]}
G[189]={"p":[
 P("Bị động nghĩa: 建于 / 建成","N + 建于 + năm ／ N + 已经建成","Được xây vào; đã xây xong.",
  ["这座大厦建于2010年。|Zhè zuò dàshà jiàn yú èr líng yī líng nián.|Tòa nhà này xây năm 2010.","新的换电站已经建成了。|Xīn de huàndiànzhàn yǐjīng jiànchéng le.|Trạm đổi pin mới đã xây xong."]),
 P("建立 vs 建设 vs 建筑","建立 + 关系/制度 ／ 建设 + 城市/国家 ／ 建筑 (công trình)","Phân biệt nghĩa.",
  ["我们跟客户建立了良好的关系。|Wǒmen gēn kèhù jiànlì le liánghǎo de guānxì.|Chúng tôi đã xây dựng quan hệ tốt với khách hàng."])],
 "q":[Q("这座大厦建＿＿2010年。","于/在了/到/从","建于."),
  Q("我们跟客户＿＿了良好的关系。","建立/建设/建筑/修建","建立关系."),
  Q("新的换电站已经建＿＿了。","成/好成/完成/造","建成."),
  Q("北京有很多老＿＿。","胡同/广场们/大厦地/建造","胡同 = ngõ cổ.")]}
G[190]={"p":[
 P("实现 + 目标/梦想","实现 + 梦想/目标","Thực hiện.",
  ["他终于实现了自己的梦想。|Tā zhōngyú shíxiàn le zìjǐ de mèngxiǎng.|Cuối cùng anh ấy đã thực hiện được ước mơ."]),
 P("克服 + 困难 ／ 争取 + 机会","克服 + 困难 ／ 争取 + N","Vượt qua; tranh thủ.",
  ["我们克服了很多困难。|Wǒmen kèfú le hěn duō kùnnán.|Chúng tôi đã vượt qua nhiều khó khăn.","我会争取这次机会。|Wǒ huì zhēngqǔ zhè cì jīhuì.|Tôi sẽ cố giành lấy cơ hội này."]),
 P("对 + N + 做出贡献","对/为 + N + 做出 + 贡献","Đóng góp cho.",
  ["他为公司做出了很大贡献。|Tā wèi gōngsī zuòchū le hěn dà gòngxiàn.|Anh ấy đóng góp lớn cho công ty."])],
 "q":[Q("他终于＿＿了自己的梦想。","实现/达成到/成就/收获","实现梦想."),
  Q("我们＿＿了很多困难。","克服/争取/贡献/实现了","克服困难."),
  Q("他为公司做出了很大＿＿。","贡献/成就了/成果地/收获着","做出贡献."),
  Q("我会＿＿这次机会。","争取/克服/前途/达成了","争取机会.")]}
G[191]={"p":[
 P("导致 + hậu quả xấu","A + 导致 + B","Dẫn đến (thường là kết quả xấu).",
  ["电池过热导致设备停机。|Diànchí guòrè dǎozhì shèbèi tíngjī.|Pin quá nhiệt dẫn đến thiết bị ngừng hoạt động."],"Dùng nhiều trong báo cáo RCA: 根本原因 → 导致 → 后果."),
 P("对 + N + 造成 + 损失/危害","对 + N + 造成 + 损失 ／ 给 + N + 带来 + 风险","Gây ra thiệt hại.",
  ["这次故障给公司造成了很大损失。|Zhè cì gùzhàng gěi gōngsī zàochéng le hěn dà sǔnshī.|Sự cố này gây thiệt hại lớn cho công ty."]),
 P("有害 / 对 + N + 有害","N + 对 + N + 有害","Có hại cho.",
  ["吸烟对健康有害。|Xīyān duì jiànkāng yǒuhài.|Hút thuốc có hại cho sức khỏe."])],
 "q":[Q("电池过热＿＿设备停机。","导致/后果/损失/有害","导致 = dẫn đến."),
  Q("这次故障给公司造成了很大＿＿。","损失/损害着/威胁了/风险的","造成损失."),
  Q("吸烟对健康＿＿。","有害/危害了/威胁/破坏","有害."),
  Q("投资有＿＿，要小心。","风险/后果的/危害着/损害","有风险.")]}
G[192]={"p":[
 P("防止 + điều xấu","防止 + N/V","Phòng ngừa.",
  ["定期检查可以防止事故发生。|Dìngqī jiǎnchá kěyǐ fángzhǐ shìgù fāshēng.|Kiểm tra định kỳ có thể phòng ngừa sự cố."]),
 P("保持 / 保存 / 保留","保持 + trạng thái ／ 保存 + dữ liệu ／ 保留 + ý kiến","Phân biệt: giữ gìn trạng thái / lưu trữ / giữ lại.",
  ["请保持安静。|Qǐng bǎochí ānjìng.|Xin giữ yên lặng.","文件要保存好。|Wénjiàn yào bǎocún hǎo.|Tài liệu phải lưu giữ cẩn thận.","我保留我的意见。|Wǒ bǎoliú wǒ de yìjiàn.|Tôi bảo lưu ý kiến của mình."])],
 "q":[Q("请＿＿安静。","保持/保存/保留/防","保持 + trạng thái."),
  Q("文件要＿＿好。","保存/保持/爱护着/防止","保存 + tài liệu."),
  Q("定期检查可以＿＿事故发生。","防止/保留/平安/爱护","防止."),
  Q("我＿＿我的意见。","保留/保存/保持了/保","保留意见.")]}
G[193]={"p":[
 P("Kích thước: 宽 / 长 / 厚 + số","N + 宽/长/高 + số + 米","Cách nói kích thước.",
  ["这条路宽二十米。|Zhè tiáo lù kuān èrshí mǐ.|Con đường này rộng 20 m.","桌子的宽度是一米。|Zhuōzi de kuāndù shì yì mǐ.|Chiều rộng của bàn là 1 m."]),
 P("Hình dạng: 圆的 / 弯弯的 / 直直的","AA的 làm vị ngữ","Miêu tả hình dạng sinh động.",
  ["月亮圆圆的。|Yuèliang yuányuán de.|Mặt trăng tròn vành vạnh.","这条路弯弯的。|Zhè tiáo lù wānwān de.|Con đường này quanh co."])],
 "q":[Q("这条路＿＿二十米。","宽/宽度是了/宽的/度","N + 宽 + số."),
  Q("月亮＿＿的。","圆圆/圆的圆/圆圆圆/圆了","AA的."),
  Q("桌子的＿＿是一米。","宽度/宽/厚/窄的","宽度 = chiều rộng."),
  Q("这条路很＿＿，车不能过。","窄/宽/直/平","窄 = hẹp.")]}
G[194]={"p":[
 P("Tính từ đánh giá cao","伟大 · 巨大 · 完美 · 良好 · 优美","Thường đi với danh từ trừu tượng.",
  ["我们取得了巨大的成功。|Wǒmen qǔdé le jùdà de chénggōng.|Chúng tôi đạt thành công to lớn.","双方保持良好的合作关系。|Shuāngfāng bǎochí liánghǎo de hézuò guānxì.|Hai bên duy trì quan hệ hợp tác tốt đẹp."]),
 P("Adj + 的 + N (cặp kết hợp cố định)","伟大的人物 · 完整的资料 · 优美的风景","Kết hợp danh–tính.",
  ["请提供完整的资料。|Qǐng tígōng wánzhěng de zīliào.|Vui lòng cung cấp tài liệu đầy đủ."])],
 "q":[Q("我们取得了＿＿的成功。","巨大/高大/伟/大大","巨大的成功."),
  Q("双方保持＿＿的合作关系。","良好/优良/完美的了/好","良好的关系."),
  Q("请提供＿＿的资料。","完整/完美/伟大/强大","完整 = đầy đủ."),
  Q("这里的风景很＿＿。","优美/优良/强大/伟大","风景优美.")]}
G[195]={"p":[
 P("熬夜 là từ ly hợp","熬 + 了 + 一个通宵/夜 ／ 别熬夜","Thức khuya.",
  ["别经常熬夜，对身体不好。|Bié jīngcháng áoyè, duì shēntǐ bù hǎo.|Đừng thường xuyên thức khuya, có hại cho sức khỏe."]),
 P("定期 / 长期 / 短期","定期 + V ／ 长期/短期 + N","Định kỳ; dài hạn; ngắn hạn.",
  ["设备需要定期维护。|Shèbèi xūyào dìngqī wéihù.|Thiết bị cần bảo trì định kỳ.","这是一个长期项目。|Zhè shì yí ge chángqī xiàngmù.|Đây là một dự án dài hạn."]),
 P("Quý: 第 + số + 季度","第一季度 / 本季度","Quý (trong báo cáo).",
  ["第三季度的业绩很好。|Dì sān jìdù de yèjì hěn hǎo.|Kết quả quý 3 rất tốt."])],
 "q":[Q("设备需要＿＿维护。","定期/长期的/季度/短期地","定期 + V."),
  Q("第三＿＿的业绩很好。","季度/季/度季/期","Quý: 季度."),
  Q("别经常＿＿，对身体不好。","熬夜/半夜/夜间/傍晚","熬夜 = thức khuya."),
  Q("这是一个＿＿项目，要做五年。","长期/定期/短期/日历","长期 = dài hạn.")]}
G[196]={"p":[
 P("Số lớn: 亿","số + 亿 (= 100 triệu)","一亿 = 100.000.000; 十亿 = 1 tỷ.",
  ["中国有十四亿人口。|Zhōngguó yǒu shísì yì rénkǒu.|Trung Quốc có 1,4 tỷ dân."],"1 tỷ (VN) = 十亿; đổi đơn vị rất dễ nhầm."),
 P("平均 / 比例 / 占","平均 + số ／ 占 + 百分之 + số","平均 = bình quân; 占 = chiếm.",
  ["女员工占百分之四十。|Nǚ yuángōng zhàn bǎi fēn zhī sìshí.|Nhân viên nữ chiếm 40%.","平均每天处理五十个工单。|Píngjūn měi tiān chǔlǐ wǔshí ge gōngdān.|Bình quân mỗi ngày xử lý 50 phiếu công việc."]),
 P("在 + phạm vi + 内","在 + N + 范围内","Trong phạm vi.",
  ["温度要控制在合理范围内。|Wēndù yào kòngzhì zài hélǐ fànwéi nèi.|Nhiệt độ phải kiểm soát trong phạm vi hợp lý."])],
 "q":[Q("\"1 tỷ\" nói là:","十亿/一亿/一千万/百亿","1 tỷ = 十亿."),
  Q("女员工＿＿百分之四十。","占/有了/是了/比例","占 = chiếm."),
  Q("温度要控制在合理＿＿内。","范围/程度/比例/面积","在…范围内."),
  Q("＿＿每天处理五十个工单。","平均/总数/比例/含量","Bình quân: 平均.")]}
G[197]={"p":[
 P("缺乏 + N trừu tượng","缺乏 + 经验/信心/资金","Thiếu (trừu tượng, văn viết).",
  ["新员工缺乏经验。|Xīn yuángōng quēfá jīngyàn.|Nhân viên mới thiếu kinh nghiệm."]),
 P("满足 + 需求","满足 + 需求/要求","Đáp ứng.",
  ["这个方案能满足客户的需求。|Zhège fāng'àn néng mǎnzú kèhù de xūqiú.|Phương án này đáp ứng được nhu cầu khách hàng."]),
 P("有必要 / 没有必要 + V","有/没有必要 + V","Cần thiết/không cần thiết.",
  ["没有必要再开会了。|Méiyǒu bìyào zài kāihuì le.|Không cần họp thêm nữa."])],
 "q":[Q("新员工＿＿经验。","缺乏/不足够/需求/充分","缺乏经验."),
  Q("这个方案能＿＿客户的需求。","满足/满意/充足/需要着","满足需求."),
  Q("没有＿＿再开会了。","必要/必需/需/急需","没有必要."),
  Q("我们的时间很＿＿。","充足/缺乏/必需/需求","充足 = dồi dào.")]}
G[198]={"p":[
 P("事实上 / 实际上","事实上，… ／ 现实中","Trên thực tế.",
  ["事实上，问题并不简单。|Shìshí shàng, wèntí bìng bù jiǎndān.|Thực tế, vấn đề không hề đơn giản."]),
 P("并 + 不/没 (nhấn mạnh phủ định)","并 + 不/没 + V/Adj","Bác bỏ suy nghĩ của người khác: hoàn toàn không.",
  ["我并没有说过这句话。|Wǒ bìng méiyǒu shuō guo zhè jù huà.|Tôi hoàn toàn không nói câu đó."]),
 P("处于 + trạng thái","处于 + 状态/阶段","Ở trong (trạng thái).",
  ["设备处于正常工作状态。|Shèbèi chǔyú zhèngcháng gōngzuò zhuàngtài.|Thiết bị ở trạng thái làm việc bình thường."])],
 "q":[Q("＿＿，问题并不简单。","事实上/事物上/现实地/现状下","事实上."),
  Q("我＿＿没有说过这句话。","并/又/再/却并","并 + 没有."),
  Q("设备处于正常工作＿＿。","状态/状况了/现象/形势","处于…状态."),
  Q("这是一种自然＿＿。","现象/事实上/性质的/现状下","自然现象.")]}
G[199]={"p":[
 P("A 跟 B 相似 / 类似","A 跟/与 B 相似 ／ 类似 + N","Tương tự.",
  ["这两个问题很相似。|Zhè liǎng ge wèntí hěn xiāngsì.|Hai vấn đề này rất giống nhau.","以前也发生过类似的故障。|Yǐqián yě fāshēng guo lèisì de gùzhàng.|Trước đây cũng từng xảy ra sự cố tương tự."]),
 P("以 + 形式 + V","以 + N + 的形式 + V","Dưới hình thức.",
  ["会议以视频的形式进行。|Huìyì yǐ shìpín de xíngshì jìnxíng.|Cuộc họp diễn ra dưới hình thức video."])],
 "q":[Q("以前也发生过＿＿的故障。","类似/相似地/类型/形式","类似的 + N."),
  Q("会议＿＿视频的形式进行。","以/用于/为/在于","以…的形式."),
  Q("这两个问题很＿＿。","相似/类型/模式/外观","相似 = giống nhau."),
  Q("这款车的＿＿很漂亮。","外观/形状了/模式/类型地","外观 = ngoại hình.")]}
G[200]={"p":[
 P("把 A 视为/看作/当作 B","把 + A + 视为/看作/当作 + B","Coi A là B.",
  ["我们把客户视为合作伙伴。|Wǒmen bǎ kèhù shì wéi hézuò huǒbàn.|Chúng tôi coi khách hàng là đối tác.","别把我当作外人。|Bié bǎ wǒ dàngzuò wàirén.|Đừng coi tôi là người ngoài."]),
 P("被 + 称为 + N","A + 被 + 称为 + B","Được gọi là.",
  ["北京被称为中国的文化中心。|Běijīng bèi chēng wéi Zhōngguó de wénhuà zhōngxīn.|Bắc Kinh được gọi là trung tâm văn hóa Trung Quốc."]),
 P("体现 + 精神/价值","N + 体现了 + N","Thể hiện.",
  ["这件事体现了团队精神。|Zhè jiàn shì tǐxiàn le tuánduì jīngshén.|Việc này thể hiện tinh thần đồng đội."])],
 "q":[Q("我们把客户视＿＿合作伙伴。","为/成为/作为/当","视为."),
  Q("北京被称＿＿中国的文化中心。","为/作/成/是","称为."),
  Q("这件事＿＿了团队精神。","体现/体会/体验/看作","体现."),
  Q("别把我＿＿外人。","当作/视/称/看","当作.")]}
G[201]={"p":[
 P("确认 / 强调 / 承认 + mệnh đề","确认 + câu ／ 强调 + câu ／ 承认 + câu","Động từ mang mệnh đề làm tân ngữ.",
  ["请确认设备已经断电。|Qǐng quèrèn shèbèi yǐjīng duàndiàn.|Vui lòng xác nhận thiết bị đã ngắt điện.","经理强调安全第一。|Jīnglǐ qiángdiào ānquán dì yī.|Giám đốc nhấn mạnh an toàn là trên hết.","他承认自己错了。|Tā chéngrèn zìjǐ cuò le.|Anh ấy thừa nhận mình sai."]),
 P("赞成 / 否定 + N","赞成 + ý kiến ／ 否定 + N","Tán thành; phủ định.",
  ["我赞成你的看法。|Wǒ zànchéng nǐ de kànfǎ.|Tôi tán thành quan điểm của bạn."])],
 "q":[Q("请＿＿设备已经断电。","确认/确定了/强调着/否认","Xác nhận: 确认."),
  Q("经理＿＿安全第一。","强调/提倡着/请求/承认","Nhấn mạnh: 强调."),
  Q("他＿＿自己错了。","承认/否认了认/赞成/确定","Thừa nhận: 承认."),
  Q("我＿＿你的看法。","赞成/否定/请求/强调","Tán thành: 赞成.")]}
G[202]={"p":[
 P("收集 + 数据/资料 ／ 记录 + 下来","收集 + N ／ 把 + N + 记录下来","Thu thập; ghi lại.",
  ["我们收集了故障数据。|Wǒmen shōují le gùzhàng shùjù.|Chúng tôi đã thu thập dữ liệu sự cố.","请把检查结果记录下来。|Qǐng bǎ jiǎnchá jiéguǒ jìlù xiàlai.|Hãy ghi lại kết quả kiểm tra."]),
 P("对 + đối tượng + 进行调研","对 + N + 进行调研/问卷调查","Khảo sát.",
  ["我们对用户进行了问卷调查。|Wǒmen duì yònghù jìnxíng le wènjuàn diàochá.|Chúng tôi đã khảo sát bảng hỏi với người dùng."])],
 "q":[Q("我们＿＿了故障数据。","收集/寻找到/记载了/录","收集数据."),
  Q("请把结果记录＿＿。","下来/起来/出来/上去","记录下来."),
  Q("我们＿＿用户进行了问卷调查。","对/给/向/为","对…进行调查."),
  Q("会议要＿＿，以后可以听。","录音/记载/问卷/填","录音 = ghi âm.")]}
G[203]={"p":[
 P("属于 / 位于 / 处于","A + 属于 + B ／ A + 位于 + nơi ／ 处于 + trạng thái","Thuộc về; nằm ở; ở trong.",
  ["这个问题属于软件故障。|Zhège wèntí shǔyú ruǎnjiàn gùzhàng.|Vấn đề này thuộc lỗi phần mềm.","公司位于河内市中心。|Gōngsī wèiyú Hénèi shì zhōngxīn.|Công ty nằm ở trung tâm Hà Nội."]),
 P("问题在于… / 与…相关/无关","…的关键在于 + V ／ 与/跟 + N + 相关/无关","Nằm ở chỗ; liên quan.",
  ["成功的关键在于坚持。|Chénggōng de guānjiàn zàiyú jiānchí.|Chìa khóa thành công nằm ở sự kiên trì.","这次故障与天气无关。|Zhè cì gùzhàng yǔ tiānqì wúguān.|Sự cố này không liên quan đến thời tiết."])],
 "q":[Q("公司＿＿河内市中心。","位于/处于/属于/在于","Nằm ở: 位于."),
  Q("这个问题＿＿软件故障。","属于/位于/在于/处在","Thuộc về: 属于."),
  Q("成功的关键＿＿坚持。","在于/处于/位于/属于","在于 = nằm ở chỗ."),
  Q("这次故障＿＿天气无关。","与/对/在/给","与…无关.")]}
G[204]={"p":[
 P("向 + người + 赠送 / 捐","向 + N + 捐 + tiền/vật ／ 赠送 + người + vật","Tặng, quyên góp.",
  ["公司向学校捐了一批电脑。|Gōngsī xiàng xuéxiào juān le yì pī diànnǎo.|Công ty quyên tặng trường một lô máy tính."]),
 P("领取 / 接收 / 接待","领取 + 物品 ／ 接收 + tín hiệu/hàng ／ 接待 + khách","Nhận (đến lấy); tiếp nhận; tiếp đón.",
  ["请到前台领取钥匙。|Qǐng dào qiántái lǐngqǔ yàoshi.|Vui lòng đến lễ tân nhận chìa khóa.","我负责接待客户。|Wǒ fùzé jiēdài kèhù.|Tôi phụ trách tiếp khách."]),
 P("把 + N + 递给/传给 + người","把 + N + 递给 + người","Đưa, chuyền cho.",
  ["请把盐递给我。|Qǐng bǎ yán dì gěi wǒ.|Đưa giúp tôi lọ muối."])],
 "q":[Q("请到前台＿＿钥匙。","领取/接待/赠/捐","领取 = nhận."),
  Q("我负责＿＿客户。","接待/接收/领/递","接待 + khách."),
  Q("请把盐递＿＿我。","给/到/向/对","递给."),
  Q("公司＿＿学校捐了一批电脑。","向/对/被/让","向…捐.")]}
G[205]={"p":[
 P("包括 / 包含 / 含有","N + 包括 + các mục ／ 含有 + thành phần","包括 = bao gồm (liệt kê); 含有 = có chứa.",
  ["费用包括材料费和人工费。|Fèiyòng bāokuò cáiliàofèi hé réngōngfèi.|Chi phí bao gồm vật tư và nhân công.","这种饮料含有很多糖。|Zhè zhǒng yǐnliào hányǒu hěn duō táng.|Loại đồ uống này chứa nhiều đường."]),
 P("由 + thành phần + 构成 / 形成","N + 由 + A 和 B + 构成","Cấu thành từ.",
  ["系统由硬件和软件构成。|Xìtǒng yóu yìngjiàn hé ruǎnjiàn gòuchéng.|Hệ thống gồm phần cứng và phần mềm."]),
 P("从整体上看","从整体/总体上看，…","Nhìn tổng thể.",
  ["从整体上看，项目进展顺利。|Cóng zhěngtǐ shàng kàn, xiàngmù jìnzhǎn shùnlì.|Nhìn chung, dự án tiến triển thuận lợi."])],
 "q":[Q("费用＿＿材料费和人工费。","包括/含有/成分/构成了","包括 + liệt kê."),
  Q("这种饮料＿＿很多糖。","含有/包括/构成/形成","含有 = chứa."),
  Q("系统＿＿硬件和软件构成。","由/被/从/对","由…构成."),
  Q("从＿＿上看，项目进展顺利。","整体/总体的/成分/形成","从整体上看.")]}
G[206]={"p":[
 P("Bổ ngữ kết quả với động tác tay","抓住 · 握紧 · 捡起来 · 扶好","Kết quả của động tác.",
  ["抓住我的手！|Zhuāzhù wǒ de shǒu!|Nắm lấy tay tôi!","他把钱包捡起来了。|Tā bǎ qiánbāo jiǎn qǐlai le.|Anh ấy nhặt ví lên."]),
 P("跟 + người + 握手 / 向 + người + 挥手","跟 + người + 握手 ／ 向 + người + 挥手","Bắt tay; vẫy tay.",
  ["经理跟客户握了握手。|Jīnglǐ gēn kèhù wò le wò shǒu.|Giám đốc bắt tay khách hàng.","他向我挥了挥手。|Tā xiàng wǒ huī le huī shǒu.|Anh ấy vẫy tay với tôi."],None,"他握手我。|他跟我握手。")],
 "q":[Q("经理＿＿客户握了握手。","跟/对/给/向着","跟…握手."),
  Q("他把钱包捡＿＿了。","起来/上来/出去/下去","捡起来."),
  Q("＿＿住我的手！","抓/摸/挥/摇","抓住."),
  Q("老人走路时要有人＿＿着。","扶/伸/摇/捡","扶 = dìu.")]}
G[207]={"p":[
 P("被 + vật + 撞/碰","被 + N + 撞了 ／ 摔倒了","Bị va.",
  ["他被自行车撞了。|Tā bèi zìxíngchē zhuàng le.|Anh ấy bị xe đạp đâm.","路很滑，小心别摔倒。|Lù hěn huá, xiǎoxīn bié shuāidǎo.|Đường trơn, cẩn thận kẻo ngã."]),
 P("碰见 / 躲开 / 追上","V + kết quả: 碰见, 躲开, 追上","Gặp tình cờ; tránh; đuổi kịp.",
  ["我在超市碰见了老同学。|Wǒ zài chāoshì pèngjiàn le lǎo tóngxué.|Tôi tình cờ gặp bạn cũ ở siêu thị.","我追不上他。|Wǒ zhuī bu shàng tā.|Tôi không đuổi kịp anh ấy."])],
 "q":[Q("他＿＿自行车撞了。","被/把/让着/给了","被…撞."),
  Q("我在超市＿＿了老同学。","碰见/撞见了/碰/躲","碰见 = tình cờ gặp."),
  Q("他跑得太快，我追不＿＿。","上/到了/起/下","追不上."),
  Q("路很＿＿，小心别摔倒。","滑/冲/撞/躲","滑 = trơn.")]}
G[208]={"p":[
 P("Mức độ màu: 浅 / 深","浅/深 + 色 ／ 浅蓝色","Nhạt; đậm.",
  ["我喜欢浅色的衣服。|Wǒ xǐhuan qiǎnsè de yīfu.|Tôi thích quần áo màu nhạt."]),
 P("光线 + 太暗 / 不好","光线 + Adj","Ánh sáng.",
  ["这里光线太暗，看不清楚。|Zhèlǐ guāngxiàn tài àn, kàn bu qīngchu.|Ở đây ánh sáng quá tối, không nhìn rõ."]),
 P("Adj + 了 + 起来 (bắt đầu)","红了起来 / 暗了下来","Biến đổi màu sắc, ánh sáng.",
  ["天渐渐暗了下来。|Tiān jiànjiàn àn le xiàlai.|Trời dần tối lại."])],
 "q":[Q("我喜欢＿＿色的衣服。","浅/暗/白白/光","浅色 = màu nhạt."),
  Q("这里光线太＿＿，看不清楚。","暗/浅/明/白","暗 = tối."),
  Q("天渐渐暗了＿＿。","下来/上来/出去/过去","暗下来."),
  Q("一盏＿＿","灯/灯光/光线/光明","一盏灯.")]}
G[209]={"p":[
 P("强烈 / 激烈 / 热烈","强烈 + 要求/感觉 ／ 激烈 + 竞争 ／ 热烈 + 欢迎","Kết hợp cố định.",
  ["市场竞争很激烈。|Shìchǎng jìngzhēng hěn jīliè.|Cạnh tranh thị trường rất khốc liệt.","热烈欢迎各位来宾！|Rèliè huānyíng gè wèi láibīn!|Nhiệt liệt chào mừng các vị khách!"]),
 P("给 + người + 带来刺激","刺激 (kích thích, mạo hiểm)","Cảm giác mạnh.",
  ["坐过山车很刺激。|Zuò guòshānchē hěn cìjī.|Đi tàu lượn rất kích thích."])],
 "q":[Q("市场竞争很＿＿。","激烈/热烈/强烈的了/刺激了","激烈的竞争."),
  Q("＿＿欢迎各位来宾！","热烈/激烈/强烈/平静","热烈欢迎."),
  Q("客户＿＿要求更换设备。","强烈/热烈/激烈/舒适","强烈要求."),
  Q("他的心情很＿＿。","平静/激烈/臭/丑","平静 = bình tĩnh.")]}
G[210]={"p":[
 P("提高 + 效率 / 保持 + 稳定","提高效率 ／ 保持稳定","Cặp từ báo cáo vận hành.",
  ["新系统大大提高了工作效率。|Xīn xìtǒng dàdà tígāo le gōngzuò xiàolǜ.|Hệ thống mới nâng cao đáng kể hiệu suất.","设备运行很稳定。|Shèbèi yùnxíng hěn wěndìng.|Thiết bị vận hành rất ổn định."]),
 P("连续 + số + thời gian / 持续 + V","连续 + 三天 ／ 持续 + 增长","Liên tục.",
  ["销量连续三个月增长。|Xiāoliàng liánxù sān ge yuè zēngzhǎng.|Doanh số tăng liên tục ba tháng.","高温持续了一周。|Gāowēn chíxù le yì zhōu.|Nắng nóng kéo dài một tuần."])],
 "q":[Q("新系统大大提高了工作＿＿。","效率/高效/迅速/稳定","提高效率."),
  Q("销量＿＿三个月增长。","连续/持续着/加速/迅速","连续 + thời gian."),
  Q("设备运行很＿＿。","稳定/连续/效率/无效","稳定 = ổn định."),
  Q("高温＿＿了一周。","持续/连续/缓慢/加速","持续 = kéo dài.")]}
G[211]={"p":[
 P("有助于 / 有利于 + N/V","A + 有助于/有利于 + B","Có lợi cho, giúp ích cho.",
  ["运动有助于减轻压力。|Yùndòng yǒuzhù yú jiǎnqīng yālì.|Vận động giúp giảm căng thẳng.","这项政策有利于企业发展。|Zhè xiàng zhèngcè yǒulì yú qǐyè fāzhǎn.|Chính sách này có lợi cho doanh nghiệp."]),
 P("利用 + N + V","利用 + 时间/资源 + V","Tận dụng.",
  ["我利用周末学习汉语。|Wǒ lìyòng zhōumò xuéxí Hànyǔ.|Tôi tận dụng cuối tuần học tiếng Hán."]),
 P("发挥 + 优势","发挥 + 优势/作用","Phát huy.",
  ["我们要发挥自己的优势。|Wǒmen yào fāhuī zìjǐ de yōushì.|Chúng ta phải phát huy ưu thế của mình."])],
 "q":[Q("运动＿＿减轻压力。","有助于/有利/利用/有益于了","有助于 + V."),
  Q("我＿＿周末学习汉语。","利用/应用/用途/有利","利用 + thời gian."),
  Q("我们要发挥自己的＿＿。","优势/利益/用途/有力","发挥优势."),
  Q("这项技术被广泛＿＿。","应用/利用于/用途/有利","广泛应用.")]}
G[212]={"p":[
 P("调整 / 更换 / 代替","调整 + 计划/参数 ／ 更换 + 零件 ／ 用 A 代替 B","Điều chỉnh; thay thế.",
  ["我们需要调整维护计划。|Wǒmen xūyào tiáozhěng wéihù jìhuà.|Chúng ta cần điều chỉnh kế hoạch bảo trì.","请更换损坏的零件。|Qǐng gēnghuàn sǔnhuài de língjiàn.|Vui lòng thay linh kiện hỏng.","可以用电子版代替纸质版。|Kěyǐ yòng diànzǐbǎn dàitì zhǐzhìbǎn.|Có thể dùng bản điện tử thay bản giấy."]),
 P("扩大 / 加深 + N","扩大 + 范围/规模 ／ 加深 + 理解","Mở rộng; làm sâu sắc.",
  ["公司决定扩大业务范围。|Gōngsī juédìng kuòdà yèwù fànwéi.|Công ty quyết định mở rộng phạm vi kinh doanh."]),
 P("Hậu tố -化","现代化 · 自动化 · 国际化 · 智能化","Biến thành, hóa.",
  ["工厂正在实现自动化。|Gōngchǎng zhèngzài shíxiàn zìdònghuà.|Nhà máy đang tự động hóa."])],
 "q":[Q("请＿＿损坏的零件。","更换/调/变动了/转变着","更换零件."),
  Q("可以用电子版＿＿纸质版。","代替/更换/转变/调整","用 A 代替 B."),
  Q("公司决定＿＿业务范围。","扩大/加深/变动/调整到","扩大范围."),
  Q("工厂正在实现自动＿＿。","化/性/感/度","自动化.")]}
G[213]={"p":[
 P("开发 / 设计 / 发明","开发 + 产品/软件 ／ 设计 + N ／ 发明 + N","Phát triển; thiết kế; phát minh.",
  ["他们开发了一个新的应用。|Tāmen kāifā le yí ge xīn de yìngyòng.|Họ phát triển một ứng dụng mới.","这个换电柜是我们自己设计的。|Zhège huàndiànguì shì wǒmen zìjǐ shèjì de.|Tủ đổi pin này do chúng tôi tự thiết kế."]),
 P("自己 + 创业","自己 + 创业 ／ 创业 + 的 + N","Khởi nghiệp.",
  ["他辞职后开始自己创业。|Tā cízhí hòu kāishǐ zìjǐ chuàngyè.|Sau khi nghỉ việc anh ấy bắt đầu tự khởi nghiệp."]),
 P("设立 / 设置","设立 + 机构/基金 ／ 设置 + 密码/参数","Thành lập; cài đặt.",
  ["请设置一个新密码。|Qǐng shèzhì yí ge xīn mìmǎ.|Vui lòng đặt mật khẩu mới."])],
 "q":[Q("他辞职后开始自己＿＿。","创业/创造/开发了/发起了","创业 = khởi nghiệp."),
  Q("请＿＿一个新密码。","设置/设立/设计/开发","设置密码."),
  Q("这个产品是我们自己＿＿的。","设计/设置/设立了/创作着","设计."),
  Q("公司在越南＿＿了分公司。","设立/设置/创作/发明","设立 + 机构.")]}
G[214]={"p":[
 P("承担 + 责任/费用","承担 + 责任/费用/风险","Gánh vác.",
  ["由此产生的费用由客户承担。|Yóu cǐ chǎnshēng de fèiyòng yóu kèhù chéngdān.|Chi phí phát sinh từ đó do khách hàng chịu.","我愿意承担责任。|Wǒ yuànyì chéngdān zérèn.|Tôi sẵn sàng chịu trách nhiệm."],"Câu mẫu hay gặp trong hợp đồng/SLA: …由…承担."),
 P("面临 + thách thức / 对待 + N","面临 + 挑战/压力 ／ 认真对待 + N","Đối mặt; đối xử.",
  ["公司面临很大的挑战。|Gōngsī miànlín hěn dà de tiǎozhàn.|Công ty đang đối mặt thách thức lớn.","我们要认真对待客户的投诉。|Wǒmen yào rènzhēn duìdài kèhù de tóusù.|Phải nghiêm túc xử lý khiếu nại của khách hàng."]),
 P("敢于 + V / 下决心 + V","敢于 + V ／ 下决心 + V","Dám; quyết tâm.",
  ["他下决心要学好汉语。|Tā xià juéxīn yào xuéhǎo Hànyǔ.|Anh ấy quyết tâm học tốt tiếng Hán."])],
 "q":[Q("由此产生的费用由客户＿＿。","承担/承受/负担着/面临","承担费用."),
  Q("公司＿＿很大的挑战。","面临/面对着临/对待/承受了","面临挑战."),
  Q("我们要认真＿＿客户的投诉。","对待/面对着/待/承担","对待投诉."),
  Q("他下＿＿要学好汉语。","决心/决定了/全力/用力","下决心.")]}
G[215]={"p":[
 P("忙碌 / 闲","忙碌的 + N ／ 闲下来","Bận rộn; rảnh.",
  ["忙碌了一天，终于闲下来了。|Mánglù le yì tiān, zhōngyú xián xiàlai le.|Bận rộn cả ngày, cuối cùng cũng rảnh."]),
 P("在 + 业余时间 + V","在业余时间 + V","Thời gian rảnh.",
  ["我在业余时间学习汉语。|Wǒ zài yèyú shíjiān xuéxí Hànyǔ.|Tôi học tiếng Hán vào thời gian rảnh."]),
 P("在 + 信封上 + 贴邮票","在 + N + 上 + 贴 + N","Dán.",
  ["别忘了在信封上贴邮票。|Bié wàng le zài xìnfēng shàng tiē yóupiào.|Đừng quên dán tem lên phong bì."])],
 "q":[Q("我在＿＿时间学习汉语。","业余/闲/忙碌/居住","业余时间."),
  Q("忙了一天，终于闲＿＿了。","下来/起来/出来/上去","闲下来."),
  Q("别忘了在信封上贴＿＿。","邮票/邮局/信/票邮","贴邮票."),
  Q("他们＿＿在城市里。","居住/生存/忙碌/业余","居住 = sinh sống.")]}
G[216]={"p":[
 P("Từ trưởng thành: 成长 / 成熟 / 成年","成长 (lớn lên) ／ 成熟 (chín chắn) ／ 成年 (trưởng thành, đủ tuổi)","Phân biệt.",
  ["孩子在快乐中成长。|Háizi zài kuàilè zhōng chéngzhǎng.|Trẻ lớn lên trong niềm vui.","他比以前成熟多了。|Tā bǐ yǐqián chéngshú duō le.|Anh ấy chín chắn hơn trước nhiều."]),
 P("Nói giảm: 去世","N + 去世了","Qua đời (lịch sự hơn 死).",
  ["他爷爷去年去世了。|Tā yéye qùnián qùshì le.|Ông anh ấy mất năm ngoái."]),
 P("上了年纪","上了年纪 / 年纪大了","Lớn tuổi.",
  ["奶奶上了年纪，身体不太好。|Nǎinai shàng le niánjì, shēntǐ bú tài hǎo.|Bà đã lớn tuổi, sức khỏe không tốt lắm."])],
 "q":[Q("他比以前＿＿多了。","成熟/成长/成年了/成人","成熟 = chín chắn."),
  Q("他爷爷去年＿＿了。(lịch sự)","去世/死去了/命/一代","去世."),
  Q("孩子在快乐中＿＿。","成长/成熟/成年/成人","成长 = lớn lên."),
  Q("奶奶上了＿＿，身体不太好。","年纪/年龄的/成年/一代","上了年纪.")]}
G[217]={"p":[
 P("在 + 地区 + 内 / 当地","在 + N + 地区 ／ 当地 + N","Khu vực; địa phương.",
  ["我们在北部地区有一百多个换电站。|Wǒmen zài běibù dìqū yǒu yìbǎi duō ge huàndiànzhàn.|Chúng tôi có hơn 100 trạm đổi pin ở khu vực phía Bắc.","我们跟当地政府合作。|Wǒmen gēn dāngdì zhèngfǔ hézuò.|Chúng tôi hợp tác với chính quyền địa phương."]),
 P("A 是 B 的省会","A 是 B 的省会/首都","Thủ phủ, thủ đô.",
  ["广州是广东的省会。|Guǎngzhōu shì Guǎngdōng de shěnghuì.|Quảng Châu là thủ phủ của Quảng Đông."])],
 "q":[Q("广州是广东的＿＿。","省会/首都/城区/地区","省会 = thủ phủ tỉnh."),
  Q("我们跟＿＿政府合作。","当地/本地区/地理/四周的","当地 = địa phương."),
  Q("我们在北部＿＿有一百多个站。","地区/区/四周/中外","北部地区."),
  Q("这个城市的＿＿位置很好。","地理/当地/区域了/城区","地理位置.")]}
G[218]={"p":[
 P("被 + người + 骗/骂/抢","被 + N + V + 了","Bị lừa, bị mắng, bị cướp.",
  ["他被人骗了一万块。|Tā bèi rén piàn le yí wàn kuài.|Anh ấy bị lừa mất 10.000 tệ.","手机被抢了。|Shǒujī bèi qiǎng le.|Điện thoại bị cướp."]),
 P("欠 + người + tiền","A + 欠 + B + số tiền","Nợ.",
  ["我还欠他五百块。|Wǒ hái qiàn tā wǔbǎi kuài.|Tôi còn nợ anh ấy 500 tệ."]),
 P("怪 + người","别怪 + người ／ 都怪 + người","Trách.",
  ["这不能怪你。|Zhè bù néng guài nǐ.|Việc này không thể trách bạn."])],
 "q":[Q("他被人＿＿了一万块。","骗/欠/抢着/怪","被骗."),
  Q("我还＿＿他五百块。","欠/借给/骗/搞","欠 + người + tiền."),
  Q("这不能＿＿你。","怪/骂/搞/迷","怪 = trách."),
  Q("他喝＿＿了，不能开车。","醉/迷/怪/搞","喝醉.")]}
G[219]={"p":[
 P("办理 + 手续 / 按照 + 程序","办理手续 ／ 按照程序 + V","Thủ tục; quy trình.",
  ["请按照操作程序进行。|Qǐng ànzhào cāozuò chéngxù jìnxíng.|Vui lòng thực hiện theo quy trình thao tác.","入住前要先登记。|Rùzhù qián yào xiān dēngjì.|Trước khi nhận phòng phải đăng ký."]),
 P("在 + 环节 + 上 + 出问题","在 + 哪个环节 + 出了问题","Khâu nào có vấn đề.",
  ["我们要找出是哪个环节出了问题。|Wǒmen yào zhǎochū shì nǎge huánjié chū le wèntí.|Chúng ta phải tìm ra khâu nào có vấn đề."])],
 "q":[Q("请按照操作＿＿进行。","程序/手续/环节/手段","操作程序."),
  Q("要找出是哪个＿＿出了问题。","环节/程序上/登记/手段","环节 = khâu."),
  Q("入住前要先＿＿。","登记/操作/试用/存放","登记."),
  Q("这是＿＿杯子，用完就扔。","一次性/试用的了/存放/手段","一次性 = dùng một lần.")]}
G[220]={"p":[
 P("Ngôn ngữ lịch sự","尊敬的 + 客户/领导 ／ 欢迎前来 + V","Mở đầu thư, thông báo trang trọng.",
  ["尊敬的客户，您好！|Zūnjìng de kèhù, nín hǎo!|Kính gửi quý khách hàng!","欢迎各位前来参观。|Huānyíng gè wèi qiánlái cānguān.|Hoan nghênh quý vị đến tham quan."]),
 P("催 + người + V","催 + người + V","Giục ai làm gì.",
  ["客户在催我们交货。|Kèhù zài cuī wǒmen jiāohuò.|Khách hàng đang giục chúng tôi giao hàng."]),
 P("等待 / 等候","请 + 稍等/等候 ／ 等待 + kết quả","Văn viết của 等.",
  ["请在门外等候。|Qǐng zài mén wài děnghòu.|Vui lòng đợi bên ngoài."])],
 "q":[Q("＿＿的客户，您好！","尊敬/尊重的/敬/尊","尊敬的…."),
  Q("客户在＿＿我们交货。","催/等/看望/告别","催 + người + V."),
  Q("请在门外＿＿。","等候/等待着候/前来/看望","等候."),
  Q("周末我去医院＿＿朋友。","看望/看见/看来/看作","看望 = thăm.")]}
G[221]={"p":[
 P("分别 + V","A 和 B + 分别 + V","Lần lượt, riêng từng người.",
  ["我和他分别负责北部和南部。|Wǒ hé tā fēnbié fùzé běibù hé nánbù.|Tôi và anh ấy lần lượt phụ trách miền Bắc và miền Nam."]),
 P("分布 / 分配 / 集中","N + 分布在 + nơi ／ 分配 + 任务 ／ 集中 + 精力","Phân bố; phân công; tập trung.",
  ["换电站主要分布在城市中心。|Huàndiànzhàn zhǔyào fēnbù zài chéngshì zhōngxīn.|Trạm đổi pin chủ yếu phân bố ở trung tâm thành phố.","经理给每个人分配了任务。|Jīnglǐ gěi měi ge rén fēnpèi le rènwu.|Giám đốc phân công nhiệm vụ cho mỗi người."])],
 "q":[Q("我和他＿＿负责北部和南部。","分别/分配/分布/集中","分别 + V."),
  Q("换电站主要＿＿在城市中心。","分布/分别/分配/集合","分布在."),
  Q("经理给每个人＿＿了任务。","分配/分布/分别/排列","分配任务."),
  Q("请大家＿＿精力完成项目。","集中/集合/整齐/排列","集中精力.")]}
G[222]={"p":[
 P("深入 + V / 深刻 + N","深入 + 调查/了解 ／ 深刻的 + 印象/影响","Sâu sát; sâu sắc.",
  ["我们需要深入了解客户的需求。|Wǒmen xūyào shēnrù liǎojiě kèhù de xūqiú.|Cần tìm hiểu sâu nhu cầu khách hàng.","这次经历给我留下了深刻的印象。|Zhè cì jīnglì gěi wǒ liúxià le shēnkè de yìnxiàng.|Trải nghiệm này để lại ấn tượng sâu sắc."]),
 P("广泛 + V / 重大 + N","广泛 + 应用/关注 ／ 重大 + 意义/事故","Rộng rãi; trọng đại.",
  ["这项技术得到了广泛应用。|Zhè xiàng jìshù dédào le guǎngfàn yìngyòng.|Công nghệ này được ứng dụng rộng rãi.","这是一次重大事故。|Zhè shì yí cì zhòngdà shìgù.|Đây là một sự cố nghiêm trọng."])],
 "q":[Q("我们需要＿＿了解客户的需求。","深入/深刻/深厚/深远","深入 + V."),
  Q("这次经历给我留下了＿＿的印象。","深刻/深入/深远/广泛","深刻的印象."),
  Q("这项技术得到了＿＿应用。","广泛/广大/普及/重大","广泛应用."),
  Q("这是一次＿＿事故。","重大/广大/深厚/普及","重大事故.")]}
G[223]={"p":[
 P("反映 vs 反应","反映 + 问题/情况 (phản ánh) ／ 反应 (phản ứng)","Hay nhầm.",
  ["客户向我们反映了这个问题。|Kèhù xiàng wǒmen fǎnyìng le zhège wèntí.|Khách hàng đã phản ánh vấn đề này với chúng tôi.","他的反应很快。|Tā de fǎnyìng hěn kuài.|Phản ứng của anh ấy rất nhanh."]),
 P("出自 / 来源于","N + 出自 + nguồn ／ 来源于 + N","Xuất phát từ.",
  ["这句话出自《论语》。|Zhè jù huà chūzì «Lúnyǔ».|Câu này xuất phát từ Luận Ngữ."]),
 P("如今 (ngày nay)","如今 + câu","Văn viết của 现在, thường đối lập với quá khứ.",
  ["如今电动车越来越普及。|Rújīn diàndòngchē yuèláiyuè pǔjí.|Ngày nay xe điện ngày càng phổ biến."])],
 "q":[Q("客户向我们＿＿了这个问题。","反映/反应/反/来源","反映问题."),
  Q("他的＿＿很快。","反应/反映/规律/来源","反应 = phản ứng."),
  Q("这句话＿＿《论语》。","出自/来源/原有/规律","出自 + nguồn."),
  Q("＿＿电动车越来越普及。","如今/原来/原有/以来","如今 = ngày nay.")]}
G[224]={"p":[
 P("节省 / 花费 + N","节省 + 时间/成本 ／ 花费 + tiền/thời gian","Tiết kiệm; tiêu tốn.",
  ["换电比充电节省时间。|Huàndiàn bǐ chōngdiàn jiéshěng shíjiān.|Đổi pin tiết kiệm thời gian hơn sạc.","这个项目花费了很多资金。|Zhège xiàngmù huāfèi le hěn duō zījīn.|Dự án này tiêu tốn nhiều vốn."]),
 P("给 + N + 带来便利","给 + N + 带来 + 便利","Mang lại thuận tiện.",
  ["换电站给司机带来了很大的便利。|Huàndiànzhàn gěi sījī dàilái le hěn dà de biànlì.|Trạm đổi pin mang lại thuận tiện lớn cho tài xế."])],
 "q":[Q("换电比充电＿＿时间。","节省/花费/燃烧/高档","节省时间."),
  Q("换电站给司机带来了很大的＿＿。","便利/方便的利/节省/中介","带来便利."),
  Q("这个项目＿＿了很多资金。","花费/节省/烧/燃烧","花费 + tiền."),
  Q("汽油＿＿会产生二氧化碳。","燃烧/烧着了/节省/花费","燃烧 = đốt cháy.")]}
G[225]={"p":[
 P("预计 / 预测 + kết quả","预计 + câu ／ 据预测，…","Dự kiến; dự báo.",
  ["预计下个月完成安装。|Yùjì xià ge yuè wánchéng ānzhuāng.|Dự kiến tháng sau hoàn thành lắp đặt.","据预测，明年需求会增加。|Jù yùcè, míngnián xūqiú huì zēngjiā.|Theo dự báo, năm sau nhu cầu sẽ tăng."]),
 P("事先 + V / 应当 + V","事先 + 通知/准备 ／ 应当 + V","Trước đó; nên (văn viết).",
  ["有变化请事先通知我们。|Yǒu biànhuà qǐng shìxiān tōngzhī wǒmen.|Có thay đổi xin báo trước cho chúng tôi."]),
 P("采取行动 / 付诸实践","采取 + 行动 ／ 在实践中 + V","Hành động; thực tiễn.",
  ["我们必须立即采取行动。|Wǒmen bìxū lìjí cǎiqǔ xíngdòng.|Chúng ta phải hành động ngay."])],
 "q":[Q("＿＿下个月完成安装。","预计/预报/事先/尝试","Dự kiến: 预计."),
  Q("有变化请＿＿通知我们。","事先/预先计/预测/应当了","事先 + V."),
  Q("我们必须立即采取＿＿。","行动/行为/实践/尝试","采取行动."),
  Q("天气＿＿说明天有雨。","预报/预计/预测地/事先","天气预报.")]}
G[226]={"p":[
 P("宝贵 / 珍贵 + N","宝贵的 + 意见/时间 ／ 珍贵的 + 礼物/回忆","Quý báu.",
  ["谢谢您宝贵的意见。|Xièxie nín bǎoguì de yìjiàn.|Cảm ơn ý kiến quý báu của ngài.","这是一份珍贵的礼物。|Zhè shì yí fèn zhēnguì de lǐwù.|Đây là một món quà quý giá."]),
 P("对 + người + 保守秘密","对 + người + 保密 ／ 保守秘密","Giữ bí mật.",
  ["请对这件事保密。|Qǐng duì zhè jiàn shì bǎomì.|Hãy giữ bí mật việc này."]),
 P("独立 + V","独立 + 完成/生活","Độc lập.",
  ["他能独立完成工作。|Tā néng dúlì wánchéng gōngzuò.|Anh ấy có thể độc lập hoàn thành công việc."])],
 "q":[Q("谢谢您＿＿的意见。","宝贵/珍贵/私人/最佳","宝贵的意见."),
  Q("请＿＿这件事保密。","对/给/为/向着","对…保密."),
  Q("他能＿＿完成工作。","独立/私人/主人/秘密","独立 + V."),
  Q("这是我的＿＿问题，不想说。","私人/独立/知名/宝","私人 = riêng tư.")]}
G[227]={"p":[
 P("A 和 B 之间的差距/差别","A 和 B 之间 + 有 + 差距","Khoảng cách, chênh lệch.",
  ["我们和竞争对手之间还有差距。|Wǒmen hé jìngzhēng duìshǒu zhījiān hái yǒu chājù.|Giữa chúng ta và đối thủ vẫn còn khoảng cách."]),
 P("在 + bối cảnh + 下","在 + N + 的背景下，…","Trong bối cảnh.",
  ["在经济发展的背景下，…|Zài jīngjì fāzhǎn de bèijǐng xià, …|Trong bối cảnh kinh tế phát triển, …"]),
 P("向 + người + 报告 / 写报告","向 + người + 报告 ／ 写 + 一份报告","Báo cáo.",
  ["我要写一份事故报告。|Wǒ yào xiě yí fèn shìgù bàogào.|Tôi phải viết một báo cáo sự cố."])],
 "q":[Q("我们和对手之间还有＿＿。","差距/差别了/难度/对象","有差距."),
  Q("在经济发展的背景＿＿，…","下/中/里/上","在…的背景下."),
  Q("我要写一＿＿事故报告。","份/本/张/篇儿","一份报告."),
  Q("这个项目的＿＿很大。","难度/差别/背后/表面","难度 = độ khó.")]}
G[228]={"p":[
 P("为了 + mục tiêu + 而 + 奋斗","为 + N + 而 + 奋斗/努力","Phấn đấu vì.",
  ["他为了梦想而奋斗。|Tā wèile mèngxiǎng ér fèndòu.|Anh ấy phấn đấu vì ước mơ."]),
 P("据说 / 提起","据说 + câu ／ 提起 + N","Nghe nói; nhắc đến.",
  ["据说他要升职了。|Jùshuō tā yào shēngzhí le.|Nghe nói anh ấy sắp được thăng chức.","一提起家乡，他就很激动。|Yì tíqǐ jiāxiāng, tā jiù hěn jīdòng.|Hễ nhắc đến quê hương là anh ấy xúc động."])],
 "q":[Q("他为了梦想＿＿奋斗。","而/就/才/且","为了…而…."),
  Q("＿＿他要升职了。","据说/说据/提起/愿","据说 = nghe nói."),
  Q("一＿＿家乡，他就很激动。","提起/提到起/向上/争","一提起…就…."),
  Q("这是我一生的＿＿。","事业/大事业了/艰苦/向上","事业 = sự nghiệp.")]}
G[229]={"p":[
 P("挑选 / 挑","挑选 + N ／ 挑 + 一个","Chọn lựa.",
  ["你可以随便挑。|Nǐ kěyǐ suíbiàn tiāo.|Bạn cứ tự do chọn.","我们挑选了最好的方案。|Wǒmen tiāoxuǎn le zuì hǎo de fāng'àn.|Chúng tôi chọn phương án tốt nhất."]),
 P("Động từ một âm tiết đa nghĩa","处 (chǔ: xử lý, chung sống) · 守 (giữ) · 登 (leo, đăng) · 藏 (giấu)","Học theo cụm.",
  ["他很好相处。|Tā hěn hǎo xiāngchǔ.|Anh ấy rất dễ hòa đồng.","我们要守时。|Wǒmen yào shǒushí.|Chúng ta phải đúng giờ.","他把钱藏起来了。|Tā bǎ qián cáng qǐlai le.|Anh ấy giấu tiền đi rồi."])],
 "q":[Q("我们＿＿了最好的方案。","挑选/挑起/选挑/藏","挑选 = chọn lựa."),
  Q("他很好相＿＿。","处/守/切/合","相处."),
  Q("他把钱＿＿起来了。","藏/守/挑/登","藏起来."),
  Q("我们要＿＿时。","守/处/合/切","守时 = đúng giờ.")]}
G[230]={"p":[
 P("Văn phong thông báo: 宣布 / 公布 / 发布","宣布 + quyết định ／ 公布 + kết quả ／ 发布 + tin, sản phẩm","Phân biệt.",
  ["公司宣布了新的政策。|Gōngsī xuānbù le xīn de zhèngcè.|Công ty công bố chính sách mới.","考试结果明天公布。|Kǎoshì jiéguǒ míngtiān gōngbù.|Kết quả thi công bố ngày mai.","新产品将在下月发布。|Xīn chǎnpǐn jiāng zài xià yuè fābù.|Sản phẩm mới sẽ ra mắt tháng sau."]),
 P("接受 + 采访 / 发表 + bài","接受 + 记者的采访 ／ 发表 + 文章/讲话","Nhận phỏng vấn; đăng bài.",
  ["经理接受了记者的采访。|Jīnglǐ jiēshòu le jìzhě de cǎifǎng.|Giám đốc đã nhận lời phỏng vấn của phóng viên."])],
 "q":[Q("公司＿＿了新的政策。","宣布/公布结果/发表了/报道着","宣布 + quyết định."),
  Q("考试结果明天＿＿。","公布/宣布了/采访/直播","公布 + kết quả."),
  Q("经理接受了记者的＿＿。","采访/报道/发布/留言","接受采访."),
  Q("他在杂志上＿＿了一篇文章。","发表/发布/公布/宣布","发表文章.")]}
G[231]={"p":[
 P("把 + hàng + 运到 + nơi","把 + N + 运到/送到 + nơi","Vận chuyển đến.",
  ["我们把电池运到了仓库。|Wǒmen bǎ diànchí yùndào le cāngkù.|Chúng tôi đã chở pin đến kho."]),
 P("销量 + 增长 / 下降","销量 + 增长了 + %","Doanh số.",
  ["今年的销量增长了百分之三十。|Jīnnián de xiāoliàng zēngzhǎng le bǎi fēn zhī sānshí.|Doanh số năm nay tăng 30%."]),
 P("打包 / 包装","把 + N + 打包/包装好","Đóng gói.",
  ["请把东西包装好再寄。|Qǐng bǎ dōngxi bāozhuāng hǎo zài jì.|Hãy đóng gói đồ cẩn thận rồi gửi."])],
 "q":[Q("我们把电池运＿＿了仓库。","到/给/成/于","运到."),
  Q("今年的＿＿增长了30%。","销量/销售了/出售/品质","销量 = doanh số."),
  Q("请把东西＿＿好再寄。","包装/包裹了/配送/运","包装好."),
  Q("这家店提供送货上门＿＿。","服务/配送了服/销售的/运","送货上门服务.")]}
G[232]={"p":[
 P("Bằng cấp: 学历","有 + 本科/硕士 + 学历","Trình độ học vấn.",
  ["这个职位要求本科以上学历。|Zhège zhíwèi yāoqiú běnkē yǐshàng xuélì.|Vị trí này yêu cầu trình độ đại học trở lên."]),
 P("念书 / 念 + năm","念 + 大学/几年级","Đi học (khẩu ngữ).",
  ["他在念大学三年级。|Tā zài niàn dàxué sān niánjí.|Cậu ấy đang học năm 3 đại học."]),
 P("吸收 + kiến thức","吸收 + 知识/经验","Tiếp thu.",
  ["要多吸收别人的经验。|Yào duō xīshōu biérén de jīngyàn.|Phải tiếp thu nhiều kinh nghiệm của người khác."])],
 "q":[Q("这个职位要求本科以上＿＿。","学历/学年/学分/学科","学历 = trình độ học vấn."),
  Q("他在＿＿大学三年级。","念/读书/念书/学习书","念 + 大学."),
  Q("要多＿＿别人的经验。","吸收/吸引/收到/接收","吸收经验."),
  Q("这门课有四个＿＿。","学分/学历/学年/学科们","学分 = tín chỉ.")]}
G[233]={"p":[
 P("Giới thiệu nghề nghiệp","S + 是 + một + nghề ／ 当 + nghề","当 = làm (nghề).",
  ["他当了十年工程师。|Tā dāng le shí nián gōngchéngshī.|Anh ấy làm kỹ sư 10 năm.","她想当导演。|Tā xiǎng dāng dǎoyǎn.|Cô ấy muốn làm đạo diễn."]),
 P("培养 + 人才","培养 + 人才","Đào tạo nhân tài.",
  ["公司很重视培养人才。|Gōngsī hěn zhòngshì péiyǎng réncái.|Công ty rất coi trọng đào tạo nhân tài."]),
 P("被 + 誉为 + N","A + 被誉为 + B","Được mệnh danh là (văn viết).",
  ["他被誉为最优秀的工程师。|Tā bèi yù wéi zuì yōuxiù de gōngchéngshī.|Anh ấy được mệnh danh là kỹ sư giỏi nhất."])],
 "q":[Q("他＿＿了十年工程师。","当/做成/是了/担","当 + nghề."),
  Q("公司很重视培养＿＿。","人才/人物/人类/明星","培养人才."),
  Q("他被＿＿为最优秀的工程师。","誉/称为/叫/说","被誉为."),
  Q("考＿＿要参加国家考试。","公务员/秘书/主任/导演","公务员 = công chức.")]}
