# B1.14 Домашнее задание 2

# У нас есть полученные из json логи сервера интернет-магазина в виде списка словарей.
# Вот файл с данными. В файле данные уже загружены в переменную events
# Вам нужно посчитать различные параметры на их основе.

# Посмотрим, из чего состоят события (элементы в списке events):

events = [
    {
        "timestamp": 1555296301000,
        "referer": "https://b24-d2wt09.bitrix24.shop/katalog/item/dress-spring-ease/",
        "location": "https://b24-d2wt09.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:PvFIq25Zl1esub4LGUQ75xAuoYH0XAlj",
        "eventType": "itemViewEvent",
        "item_id": "bx_40480796_7_52eccb44ded0bb34f72b273e9a62ef02",
        "item_price": 2331,
        "item_url": "https://b24-d2wt09.bitrix24.shop/katalog/item/t-shirt-mens-purity/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": True,
        "userAgentName": "TEST_UserAgentName",
    },
    {
        "timestamp": 1555296307000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/shoes/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:FXHVwNkP:mxfFGJmjiIyctuvBoJSdMSnADToYhxqI",
        "eventType": "itemViewEvent",
        "item_id": "bx_olfpSowC_VamiijSFNHkNdwaGlPQSYiYQXdWZfmFb",
        "item_price": 3991,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/sports-suit-breath-sports/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296314000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/item/slippers-pink-paradise/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:lmyaADLD:oWkiARNaZswQRoWebhnsBYrAWhnAkGEA",
        "eventType": "itemViewEvent",
        "item_id": "bx_rawfmwIx_BlzxbhGxIDmggObWZfIuTikNhrnvXAmq",
        "item_price": 8077,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/dress-nightlife/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296315000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/item/slippers-pink-paradise/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:dAtUuHct:UCTakFYzQHrvAHfoXcmQnWtNBHalzCeT",
        "eventType": "itemViewEvent",
        "item_id": "bx_xpquvgIr_uBYrrLdFEMrqsyEGMqgsJTtnuyeyZAXr",
        "item_price": 704,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/t-shirt-mens-purity/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296322000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/t-shirts/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:EbVCtAYF:TKbcptzZYKGKBCRzjGIfbojjhNoXXFwu",
        "eventType": "itemViewEvent",
        "item_id": "bx_WEpJouEp_RIXLTRMhVimqPmwQONbDxdJAKqptFOCZ",
        "item_price": 11907,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/dress-spring-ease/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296328000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/t-shirts/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:OjlkBYIW:MxGlLbPPneiCYRndxqrAxeDXnKuPPeDa",
        "eventType": "itemViewEvent",
        "item_id": "bx_ffPnsEbc_iZlJqqKrQKddSQADzzEMghVyxBHZhyLE",
        "item_price": 6189,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/t-shirt-men-s-fire/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296337000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/t-shirts/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:fMdKiTIv:tVPLABaRpyWbdTrmIUjMQQhhXqgBFGpY",
        "eventType": "itemViewEvent",
        "item_id": "bx_qwNzcpQs_lSwngPmhmivDaTPXNPMzEctYNcfhsKyA",
        "item_price": 4593,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/dress-red-fairy/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": True,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296343000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/item/women-s-t-shirt-purity/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:PKoZxIPE:gNPZwBfmPMxrKkYahppOmtCAmOstEPpy",
        "eventType": "itemViewEvent",
        "item_id": "bx_ZVcqVjEJ_qqyvmgdArCkVGchRudEsZPpBJVnHiNDn",
        "item_price": 8209,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/sports-suit-pink-vortex/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296346000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/shoes/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:GyJIIwdl:DvPVrCdjwTmRoehKfagowzuOFGGnfSNa",
        "eventType": "itemBuyEvent",
        "item_id": "bx_olfpSowC_VamiijSFNHkNdwaGlPQSYiYQXdWZfmFb",
        "item_price": 9856,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/sports-suit-breath-sports/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296349000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/t-shirts/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:dTzjuEBl:WnBmXZhZsmNjtZSFljPjjnTqUrJfqrMb",
        "eventType": "itemBuyEvent",
        "item_id": "bx_rawfmwIx_BlzxbhGxIDmggObWZfIuTikNhrnvXAmq",
        "item_price": 2954,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/dress-nightlife/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": True,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296354000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/item/women-s-t-shirt-purity/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:vtObiIeo:tSwGBHUEZjhkiOggnybhlDISoIGDcezd",
        "eventType": "itemBuyEvent",
        "item_id": "bx_WEpJouEp_RIXLTRMhVimqPmwQONbDxdJAKqptFOCZ",
        "item_price": 10704,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/dress-spring-ease/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296361000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/item/slippers-pink-paradise/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:kUrRfZYy:xAakhuCDrlJPgCsndxkPKsKfjorHkWWr",
        "eventType": "itemViewEvent",
        "item_id": "bx_ZVcqVjEJ_qqyvmgdArCkVGchRudEsZPpBJVnHiNDn",
        "item_price": 10900,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/sports-suit-pink-vortex/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296370000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/item/slippers-pink-paradise/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:khvifvoR:VqfYjtShxuVmzQWfBvLOHJznFwlCvrqD",
        "eventType": "itemViewEvent",
        "item_id": "bx_xYWcsdEE_ZKyKjjAvFovyWUFpEnOqvUYGKtkliDhK",
        "item_price": 12783,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/sports-suit-gentle-warmth/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296378000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/t-shirts/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:dwAdJJcZ:lrRHfWrqyKKrZANtAsornWdQGsDSelNk",
        "eventType": "itemViewEvent",
        "item_id": "bx_DcRsBXTA_CljLtnNGjByBfgJHrAWGjnasEmgBgMjJ",
        "item_price": 6362,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/t-shirt-female-temptation/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296385000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/item/slippers-pink-paradise/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:mpNNKIKN:yCEoGlCmazcVHaHUltaQafjsTyEMXwYE",
        "eventType": "itemViewEvent",
        "item_id": "bx_xYWcsdEE_ZKyKjjAvFovyWUFpEnOqvUYGKtkliDhK",
        "item_price": 9462,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/sports-suit-gentle-warmth/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296394000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/item/women-s-t-shirt-purity/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:IHcoKHDP:eRWjNebByskVUsxNssfwnygTgkXDXIJG",
        "eventType": "itemViewEvent",
        "item_id": "bx_ffPnsEbc_iZlJqqKrQKddSQADzzEMghVyxBHZhyLE",
        "item_price": 6049,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/t-shirt-men-s-fire/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": True,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296396000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/shoes/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:JWAfSMgD:wVsnzbMnxvXtDliPbPBzRfDfOCpPJAah",
        "eventType": "itemBuyEvent",
        "item_id": "bx_WEpJouEp_RIXLTRMhVimqPmwQONbDxdJAKqptFOCZ",
        "item_price": 13854,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/dress-spring-ease/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296400000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/t-shirts/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:upEqcqhO:LzOhaioMaPmmWDZayRiMMJPHrUfRJmtI",
        "eventType": "itemViewEvent",
        "item_id": "bx_ZVcqVjEJ_qqyvmgdArCkVGchRudEsZPpBJVnHiNDn",
        "item_price": 5917,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/sports-suit-pink-vortex/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296407000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/clothes/t-shirts/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:fNWvXXLl:ZupadXKsJBtajgDvhRFuTdrgCyLYJPVe",
        "eventType": "itemViewEvent",
        "item_id": "bx_rawfmwIx_BlzxbhGxIDmggObWZfIuTikNhrnvXAmq",
        "item_price": 7648,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/dress-nightlife/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
    {
        "timestamp": 1555296412000,
        "referer": "https://b24-mu3bxs.bitrix24.shop//katalog/item/dress-spring-ease/",
        "location": "https://b24-mu3bxs.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:ZkqGQvRx:UvQwYCDmtIKeOQZRINuztfmrLKgDflQI",
        "eventType": "itemBuyEvent",
        "item_id": "bx_olfpSowC_VamiijSFNHkNdwaGlPQSYiYQXdWZfmFb",
        "item_price": 1419,
        "item_url": "https://b24-mu3bxs.bitrix24.shop//katalog/item/sports-suit-breath-sports/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": False,
        "userAgentName": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    },
]

### Ваш код пишите ниже этой линии

# Посчитайте общее число каждого типа событий.
# События различаются по ключу "eventType", и у него могут быть разные значения.
# Для каждого значения посчитайте их количество (в штуках, не в процентах) для предоставленного вида событий.
# Проще всего эту задачу решить если составить словарь, ключами которого будут возможные варианты поля eventType,
# а значениями - количество таких событий. Можно сначала подсмотреть какие типы бывают,
# обойдя все сообщения и напечатав их тип, а потом создать словарик и наполнить его, перебирая все сообщения в списке.


# --------------------- 2.1
# Число событий с типом itemViewEvent
# Число событий с типом itemBuyEvent

itemViewEvent_qty = 0
itemBuyEvent_qty = 0

for event in events:
    if event["eventType"] == "itemViewEvent":
        itemViewEvent_qty += 1
    if event["eventType"] == "itemBuyEvent":
        itemBuyEvent_qty += 1

print("itemViewEvent_qty = ", itemViewEvent_qty)
print("itemBuyEvent_qty = ", itemBuyEvent_qty)

# --------------------- 2.2
# Есть ли среди сообщений дубликаты cобытий? Дубли помечаются в сообщениях ключом detectedDuplicate.
# Есть ли среди этих данных дубли?

detectedDuplicateKey = False
for event in events:
    if event["detectedDuplicate"]:
        detectedDuplicateKey = True

print("detectedDuplicateKey = ", detectedDuplicateKey)

# --------------------- 2.3
# Найдите событие, которое случилось самым первым по времени (у него минимальный timestamp)
# и введите sessionId такого события (без кавычек):
timestamp_list = []
timestamp_min = 0
sessionId_min = ""
key = True

for event in events:
    if key:
        timestamp_min = event["timestamp"]
        sessionId_min = str(event["sessionId"])
        key = False
    timestamp_list.append(event["timestamp"])
    if timestamp_min > event["timestamp"]:
        timestamp_min = event["timestamp"]
        sessionId_min = str(event["sessionId"])

print(timestamp_list)
print(min(timestamp_list))
print(timestamp_min)
print(sessionId_min)

# --------------------- 2.4
# Посчитайте общую сумму ("item_price") всех продуктов, которые просматривали
# (каждое событие — один просмотр), чему она равна? В ответ введите целое число.

item_price_sum = 0
for event in events:
    item_price_sum += event["item_price"]

print("item_price_sum = ", item_price_sum)


# --------------------- 2.5
# Определите событие, которое является первым для сессии (это можно определить по ключу "firstInSession").
# В нашем наборе событий такое событие одно.

# Укажите pageViewId этого события. (без кавычек)

for event in events:
    if event["firstInSession"]:
        print("pageViewId = ", event["pageViewId"])



