﻿# This file lists for each language code the name under which the language
# and its variants are known to the Microsoft SDK (LANG_* and SUBLANG_*_*).

# E.g. for "en" this allows to produce MAKELANGID(LANG_ENGLISH, SUBLANG_NEUTRAL),
# or for "br" MAKELANGID(LANG_PORTUGUESE, SUBLANG_PORTUGUESE_BRAZILIAN),

# See http://msdn.microsoft.com/en-us/library/dd318693.aspx for the full list.

LangIndex = [
	# code,	UI name,	Language and Sublanguage/Variant/Dialect (nothing if neutral),	Layout (RTL or nothing),
	('af',	'Afrikaans',	('Afrikaans',)),
	('am',	'Armenian (Հայերեն)',	('Armenian',)),
	('ar',	'Arabic (الْعَرَبيّة)',	('Arabic',),	'RTL'),
	('az',	'Azerbaijani (آذربایجان دیلی)',	('Azeri',)),
	('bg',	'Bulgarian (Български)',	('Bulgarian',)),
	('bn',	'Bengali (বাংলা)',	('Bengali',)),
	('br',	'Portuguese - Brazil (Português)',	('Portuguese', 'Brazilian')),
	('bs',	'Bosnian (Bosanski)',	('Bosnian', 'Bosnia Herzegovina Latin')),
	('by',	'Belarusian (Беларуская)',	('Belarusian',)),
	('ca',	'Catalan (Català)',	('Catalan',)),
	('ca-xv',	'Catalan-Valencian (Català-Valencià)',	None,),
	('cn',	'Chinese Simplified (简体中文)',	('Chinese', 'Simplified')),
	('cy',	'Welsh (Cymraeg)',	('Welsh',)),
	('cz',	'Czech (Čeština)',	('Czech',)),
	('de',	'German (Deutsch)',	('German',)),
	('dk',	'Danish (Dansk)',	('Danish',)),
	('el',	'Greek (Ελληνικά)',	('Greek',)),
	('en',	'English',	('English',)),
	('es',	'Spanish (Español)',	('Spanish',)),
	('et',	'Estonian (Eesti)',	('Estonian',)),
	('eu',	'Basque (Euskara)',	('Basque',)),
	('fa',	'Persian (فارسی)',	('Farsi',),	'RTL'),
	('fi',	'Finnish (Suomi)',	('Finnish',)),
	('fr',	'French (Français)',	('French',)),
	('fy-nl',	'Frisian (Frysk)',	('Frisian',)),
	('ga',	'Irish (Gaeilge)',	('Irish',)),
	('gl',	'Galician (Galego)',	('Galician',)),
	('he',	'Hebrew (עברית)',	('Hebrew',),	'RTL'),
	('hi',	'Hindi (हिंदी)',	('Hindi',)),
	('hr',	'Croatian (Hrvatski)',	('Croatian',)),
	('hu',	'Hungarian (Magyar)',	('Hungarian',)),
	('id',	'Indonesian (Bahasa Indonesia)',	('Indonesian',)),
	('it',	'Italian (Italiano)',	('Italian',)),
	('ja',	'Japanese (日本語)',	('Japanese',)),
	('ka',	'Georgian (ქართული)',	('Georgian',)),
	('kr',	'Korean (한국어)',	('Korean',)),
	('ku',	'Kurdish (كوردی)',	('Central Kurdish', 'Central Kurdish Iraq'),	'RTL'),
	('kw',	'Cornish (Kernewek)',	None,),
	('lt',	'Lithuanian (Lietuvių)',	('Lithuanian',)),
	('mk',	'Macedonian (македонски)',	('Macedonian',)),
	('ml',	'Malayalam (മലയാളം)',	('Malayalam',)),
	('mm',	'Burmese (ဗမာ စာ)',	None,),
	('my',	'Malaysian (Bahasa Melayu)',	('Malay',)),
	('ne',	'Nepali (नेपाली)',	('Nepali',)),
	('nl',	'Dutch (Nederlands)',	('Dutch',)),
	('nn',	'Norwegian Neo-Norwegian (Norsk nynorsk)',	('Norwegian', 'Nynorsk')),
	('no',	'Norwegian (Norsk)',	('Norwegian', 'Bokmal')),
	('pa',	'Punjabi (ਪੰਜਾਬੀ)',	('Punjabi',)),
	('pl',	'Polish (Polski)',	('Polish',)),
	('pt',	'Portuguese - Portugal (Português)',	('Portuguese',)),
	('ro',	'Romanian (Română)',	('Romanian',)),
	('ru',	'Russian (Русский)',	('Russian',)),
	('si',	'Sinhala (සිංහල)',	('Sinhalese',)),
	('sk',	'Slovak (Slovenčina)',	('Slovak',)),
	('sl',	'Slovenian (Slovenščina)',	('Slovenian',)),
	('sn',	'Shona (Shona)',	None,),
	('sp-rs',	'Serbian (Latin)',	('Serbian', 'Latin')),
	('sq',	'Albanian (Shqip)',	('Albanian',)),
	('sr-rs',	'Serbian (Cyrillic)',	('Serbian', 'Cyrillic')),
	('sv',	'Swedish (Svenska)',	('Swedish',)),
	('ta',	'Tamil (தமிழ்)',	('Tamil',)),
	('th',	'Thai (ภาษาไทย)',	('Thai',)),
	('tl',	'Tagalog (Tagalog)',	('Filipino',)),
	('tr',	'Turkish (Türkçe)',	('Turkish',)),
	('tw',	'Chinese Traditional (繁體中文)',	('Chinese', 'Traditional')),
	('uk',	'Ukrainian (Українська)',	('Ukrainian',)),
	('uz',	'Uzbek (O\'zbek)',	('Uzbek',)),
	('vn',	'Vietnamese (Việt Nam)',	('Vietnamese',)),
]
