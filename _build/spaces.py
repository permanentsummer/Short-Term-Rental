# Generates the Permanent Summer Spaces site (EN / FR / PT) into /spaces/.
# Run from the repo root:  python3 _build/spaces.py
import os, json, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ['en', 'fr', 'pt']
SITE = 'https://permanentsummer.co'
IMG = '/assets/spaces/img/'
lang = 'en'

def X(en, fr, pt): return {'en': en, 'fr': fr, 'pt': pt}
def L(v): return v[lang] if isinstance(v, dict) else v
def url(slug, lg=None):
    lg = lg or lang
    base = '/spaces/' if lg == 'en' else '/spaces/%s/' % lg
    return base + (slug + '/' if slug else '')
def esc(s): return html.escape(s, quote=True)

# ------------------------------------------------------------------ shared copy
C = {
 'products': X('Products', 'Produits', 'Produtos'),
 'estimator': X('Padel estimator', 'Estimateur padel', 'Estimador de padel'),
 'projects': X('Projects', 'Projets', 'Projetos'),
 'blog': X('Blog', 'Blog', 'Blog'),
 'about': X('About', 'À propos', 'Sobre nós'),
 'contact': X('Contact', 'Contact', 'Contacto'),
 'quote': X('Request a quote', 'Demander un devis', 'Pedir orçamento'),
 'start': X('Start a project', 'Démarrer un projet', 'Iniciar um projeto'),
 'discover': X('Discover →', 'Découvrir →', 'Descobrir →'),
 'menu': X('Menu', 'Menu', 'Menu'),
 'home': X('Home', 'Accueil', 'Início'),
 'partners': X('Our European manufacturing partners', 'Nos fabricants partenaires européens', 'Os nossos fabricantes parceiros europeus'),
 'soon': X('COMING SOON', 'BIENTÔT', 'EM BREVE'),
 'soon_items': X('Aquagym equipment<br>Wooden houses', 'Équipements d’aquagym<br>Maisons en bois', 'Equipamento de hidroginástica<br>Casas de madeira'),
 'foot_tag': X('Certified European outdoor equipment for hotels, clubs, developers and public projects.',
               'Équipements extérieurs européens certifiés pour hôtels, clubs, promoteurs et projets publics.',
               'Equipamentos exteriores europeus certificados para hotéis, clubes, promotores e projetos públicos.'),
 'company': X('Company', 'Société', 'Empresa'),
 'group': X('A Permanent Summer company', 'Une société Permanent Summer', 'Uma empresa Permanent Summer'),
 'cta_t': X('Planning an outdoor project?', 'Un projet d’aménagement extérieur ?', 'Tem um projeto de espaço exterior?'),
 'cta_p': X('Answer 4 quick questions and get a first proposal within 48 hours.',
            'Répondez à 4 questions rapides et recevez une première proposition sous 48 heures.',
            'Responda a 4 perguntas rápidas e receba uma primeira proposta em 48 horas.'),
 'cta_b': X('Start my project →', 'Démarrer mon projet →', 'Iniciar o meu projeto →'),
 'faq': X('FAQ', 'FAQ', 'Perguntas frequentes'),
 'faq_t': X('Good questions', 'Bonnes questions', 'Boas perguntas'),
 'faq_p': X('Ask us anything else on WhatsApp or by email.', 'Posez-nous toute autre question sur WhatsApp ou par e-mail.', 'Pergunte-nos o que quiser por WhatsApp ou e-mail.'),
 'standards': X('Standards & certificates', 'Normes & certificats', 'Normas & certificados'),
 'ranges': X('Ranges', 'Gammes', 'Gamas'),
 'gallery': X('Gallery', 'Galerie', 'Galeria'),
 'photo_credit': X('Photos: manufacturer reference installations.', 'Photos : réalisations de référence du fabricant.', 'Fotos: instalações de referência do fabricante.'),
 'made_by': X('Made by', 'Fabriqué par', 'Fabricado por'),
}

# ------------------------------------------------------------------ products
PRODUCTS = [
 dict(slug='playgrounds', img='monster', name=X('Playgrounds', 'Aires de jeux', 'Parques infantis'),
  short=X('EN 1176 play structures for schools, hotels, parks and residences.', 'Structures de jeux EN 1176 pour écoles, hôtels, parcs et résidences.', 'Estruturas de jogo EN 1176 para escolas, hotéis, parques e condomínios.'),
  h1=X('Playgrounds children love, built to EN 1176.', 'Des aires de jeux que les enfants adorent, conformes EN 1176.', 'Parques infantis que as crianças adoram, conformes à EN 1176.'),
  intro=X('From early-years play to giant themed structures: wooden, steel and HDPE equipment made in Spain, certified and designed for heavy daily use in schools, hotels, public parks and residential projects.',
          'De la petite enfance aux grandes structures thématiques : équipements en bois, acier et PEHD fabriqués en Espagne, certifiés et conçus pour un usage quotidien intensif dans les écoles, hôtels, parcs publics et résidences.',
          'Da primeira infância às grandes estruturas temáticas: equipamentos em madeira, aço e PEAD fabricados em Espanha, certificados e pensados para uso diário intensivo em escolas, hotéis, parques públicos e condomínios.'),
  facts=[(X('EN 1176','EN 1176','EN 1176'),X('play safety standard','norme de sécurité','norma de segurança')),(X('0–14 yrs','0–14 ans','0–14 anos'),X('age ranges covered','tranches d’âge couvertes','faixas etárias')),(X('Inclusive','Inclusif','Inclusivo'),X('wheelchair-accessible ranges','gammes accessibles PMR','gamas acessíveis a cadeiras de rodas')),(X('ISO 9001','ISO 9001','ISO 9001'),X('certified manufacturer','fabricant certifié','fabricante certificado'))],
  ranges=[(X('Multi-play structures','Structures multi-jeux','Estruturas multijogo'),X('Towers, slides, bridges and climbing in wood, steel or HDPE.','Tours, toboggans, passerelles et escalade en bois, acier ou PEHD.','Torres, escorregas, pontes e escalada em madeira, aço ou PEAD.')),
          (X('Early years (0–3)','Petite enfance (0–3)','Primeira infância (0–3)'),X('Low, sensory equipment for nurseries and kids clubs.','Équipements bas et sensoriels pour crèches et mini-clubs.','Equipamentos baixos e sensoriais para creches e kids clubs.')),
          (X('Themed play','Jeux thématiques','Jogos temáticos'),X('Castles, ships and characters that become a landmark.','Châteaux, bateaux et personnages qui deviennent un repère.','Castelos, barcos e personagens que se tornam uma referência.')),
          (X('Swings, spinners & springs','Balançoires, tourniquets & ressorts','Baloiços, carrosséis & molas'),X('The classics, in stainless steel and HDPE.','Les classiques, en inox et PEHD.','Os clássicos, em inox e PEAD.')),
          (X('Inclusive play','Jeux inclusifs','Jogos inclusivos'),X('Wheelchair-accessible equipment for everyone.','Équipements accessibles aux fauteuils roulants.','Equipamentos acessíveis a cadeiras de rodas.')),
          (X('Rope circuits & mazes','Parcours de cordes & labyrinthes','Circuitos de cordas & labirintos'),X('Balance and climbing challenges for older children.','Défis d’équilibre et d’escalade pour les plus grands.','Desafios de equilíbrio e escalada para os mais velhos.'))],
  chips=['EN 1176','EN 1177','ISO 9001','ISO 14001'], gal=['castle','park','wide','ropes','zipline','juga'], logo='agapito',
  faq=[(X('Do you supply certificates for each item?','Fournissez-vous les certificats de chaque équipement ?','Fornecem certificados para cada equipamento?'),X('Yes. Every item comes with its EN 1176 certificate, technical sheet and installation manual.','Oui. Chaque équipement est livré avec son certificat EN 1176, sa fiche technique et sa notice de montage.','Sim. Cada equipamento inclui o certificado EN 1176, ficha técnica e manual de montagem.')),
       (X('Which surfacing do I need under a playground?','Quel sol faut-il sous une aire de jeux ?','Que piso é necessário num parque infantil?'),X('It depends on the fall height of each item. We recommend EPDM rubber or synthetic turf on shock pads; see our safety flooring range.','Cela dépend de la hauteur de chute de chaque jeu. Nous recommandons un sol EPDM ou un gazon sur sous-couche amortissante ; voir nos sols de sécurité.','Depende da altura de queda de cada equipamento. Recomendamos piso EPDM ou relva sobre base amortecedora; veja os nossos pisos de segurança.')),
       (X('Is it suitable near the sea?','Est-ce adapté au bord de mer ?','É adequado junto ao mar?'),X('Yes, with stainless steel, HDPE panels and treated timber. Tell us your site and we will pick the right finishes.','Oui, avec de l’inox, des panneaux PEHD et du bois traité. Indiquez-nous votre site et nous choisirons les bonnes finitions.','Sim, com inox, painéis em PEAD e madeira tratada. Indique-nos o local e escolhemos os acabamentos certos.'))]),
 dict(slug='padel', img='padel-palms', name=X('Padel courts & covers', 'Terrains & couvertures de padel', 'Campos & coberturas de padel'),
  short=X('Classic and panoramic courts, aluminium covers.', 'Terrains classiques et panoramiques, couvertures en aluminium.', 'Campos clássicos e panorâmicos, coberturas em alumínio.')),
 dict(slug='fitness', img='calis', name=X('Outdoor fitness', 'Fitness extérieur', 'Fitness ao ar livre'),
  short=X('Outdoor gyms, calisthenics and senior parks.', 'Salles de sport extérieures, calisthénie et parcs seniors.', 'Ginásios ao ar livre, calistenia e parques seniores.'),
  h1=X('Outdoor gyms people actually use.', 'Des salles de sport en plein air vraiment utilisées.', 'Ginásios ao ar livre que as pessoas realmente usam.'),
  intro=X('Calisthenics parks, street workout, variable-load gyms and senior circuits, certified to EN 16630 and built for public spaces, hotels and residential projects.',
          'Parcs de calisthénie, street workout, appareils à charge variable et parcours seniors, certifiés EN 16630 et conçus pour les espaces publics, hôtels et résidences.',
          'Parques de calistenia, street workout, máquinas de carga variável e circuitos seniores, certificados EN 16630 e pensados para espaços públicos, hotéis e condomínios.'),
  facts=[(X('EN 16630','EN 16630','EN 16630'),X('outdoor fitness standard','norme fitness extérieur','norma de fitness exterior')),(X('EN 16899','EN 16899','EN 16899'),X('parkour standard','norme parkour','norma de parkour')),(X('All ages','Tous âges','Todas as idades'),X('from teens to seniors','des ados aux seniors','dos jovens aos seniores')),(X('Anti-vandal','Antivandale','Antivandalismo'),X('galvanised & stainless','galvanisé & inox','galvanizado & inox'))],
  ranges=[(X('Calisthenics','Calisthénie','Calistenia'),X('Bars, rings and rigs for bodyweight training.','Barres, anneaux et structures pour le poids du corps.','Barras, argolas e estruturas para treino com peso corporal.')),
          (X('Variable-load gym','Musculation à charge variable','Ginásio de carga variável'),X('Real plates and racks, outdoors.','De vrais disques et racks, en plein air.','Discos e racks reais, ao ar livre.')),
          (X('Senior parks','Parcs seniors','Parques seniores'),X('Gentle mobility and balance circuits.','Parcours doux de mobilité et d’équilibre.','Circuitos suaves de mobilidade e equilíbrio.')),
          (X('Parkour & OCR','Parkour & OCR','Parkour & OCR'),X('Obstacle and ninja circuits for teens and adults.','Parcours d’obstacles et ninja pour ados et adultes.','Circuitos de obstáculos e ninja para jovens e adultos.')),
          (X('Fitness trails','Parcours santé','Circuitos de manutenção'),X('Stations along a path, park or resort.','Stations le long d’un chemin, d’un parc ou d’un resort.','Estações ao longo de um percurso, parque ou resort.')),
          (X('Multisport courts','Terrains multisports','Campos polidesportivos'),X('Anti-vandal courts for football and basketball.','Terrains antivandales pour football et basket.','Campos antivandalismo para futebol e basquetebol.'))],
  chips=['EN 16630','EN 16899','ISO 9001'], gal=['calis','calis-wide','gym'], logo='agapito',
  faq=[(X('Can hotel guests use it without a coach?','Les clients d’un hôtel peuvent-ils l’utiliser sans coach ?','Os hóspedes podem usar sem treinador?'),X('Yes. Each station has an instruction panel and QR codes with exercise videos.','Oui. Chaque appareil a un panneau d’instructions et des QR codes avec vidéos d’exercices.','Sim. Cada aparelho tem painel de instruções e códigos QR com vídeos de exercícios.')),
       (X('What surface goes underneath?','Quel sol installer dessous ?','Que piso se coloca por baixo?'),X('EPDM rubber or turf on a shock pad, depending on the equipment and fall height.','Sol EPDM ou gazon sur sous-couche, selon l’équipement et la hauteur de chute.','Piso EPDM ou relva sobre base amortecedora, conforme o equipamento e a altura de queda.'))]),
 dict(slug='urban-furniture', img='benches', name=X('Urban furniture', 'Mobilier urbain', 'Mobiliário urbano'),
  short=X('Benches, tables, bins, planters and bike racks.', 'Bancs, tables, corbeilles, jardinières et range-vélos.', 'Bancos, mesas, papeleiras, floreiras e suportes de bicicletas.'),
  h1=X('Street furniture that lasts.', 'Du mobilier urbain qui dure.', 'Mobiliário urbano que dura.'),
  intro=X('Benches, tables, litter bins, planters, bollards, fountains and bike racks for cities, campuses, resorts and residential projects, including recycled-material series.',
          'Bancs, tables, corbeilles, jardinières, bornes, fontaines et range-vélos pour villes, campus, resorts et résidences, dont des séries en matériaux recyclés.',
          'Bancos, mesas, papeleiras, floreiras, pilaretes, bebedouros e suportes de bicicletas para cidades, campus, resorts e condomínios, incluindo séries em materiais reciclados.'),
  facts=[(X('Recycled','Recyclé','Reciclado'),X('plastic series available','séries en plastique recyclé','séries em plástico reciclado')),(X('Galvanised','Galvanisé','Galvanizado'),X('& stainless steel','& inox','& inox')),(X('Custom','Sur mesure','Personalizado'),X('colours & logos','couleurs & logos','cores & logótipos')),(X('ISO 14001','ISO 14001','ISO 14001'),X('environmental management','management environnemental','gestão ambiental'))],
  ranges=[(X('Benches & tables','Bancs & tables','Bancos & mesas'),X('Wood, recycled plastic, steel and concrete.','Bois, plastique recyclé, acier et béton.','Madeira, plástico reciclado, aço e betão.')),
          (X('Litter bins','Corbeilles','Papeleiras'),X('Single and recycling stations.','Simples et stations de tri.','Simples e estações de reciclagem.')),
          (X('Planters','Jardinières','Floreiras'),X('Modular planters for streets and terraces.','Jardinières modulaires pour rues et terrasses.','Floreiras modulares para ruas e esplanadas.')),
          (X('Bike racks','Range-vélos','Suportes de bicicletas'),X('For bikes and scooters.','Pour vélos et trottinettes.','Para bicicletas e trotinetas.')),
          (X('Bollards','Bornes','Pilaretes'),X('Fixed and removable.','Fixes et amovibles.','Fixos e amovíveis.')),
          (X('Drinking fountains','Fontaines à boire','Bebedouros'),X('Accessible models for parks.','Modèles accessibles pour parcs.','Modelos acessíveis para parques.'))],
  chips=['ISO 9001','ISO 14001'], gal=['benches','juga','park'], logo='agapito', faq=[]),
 dict(slug='shade', img='shade', name=X('Shade sails & nets', 'Voiles & filets d’ombrage', 'Velas & redes de sombra'),
  short=X('UV protection for play areas, terraces and car parks.', 'Protection UV pour aires de jeux, terrasses et parkings.', 'Proteção UV para parques infantis, esplanadas e estacionamentos.'),
  h1=X('Shade that keeps play areas cool.', 'De l’ombre pour garder les aires de jeux fraîches.', 'Sombra que mantém os parques frescos.'),
  intro=X('Tensioned textile sails and high-tenacity UV nets over playgrounds, terraces, pools and car parks, engineered for sun, wind and coastal climates.',
          'Voiles textiles tendues et filets UV haute ténacité pour aires de jeux, terrasses, piscines et parkings, conçus pour le soleil, le vent et les climats côtiers.',
          'Velas têxteis tensionadas e redes UV de alta tenacidade para parques infantis, esplanadas, piscinas e estacionamentos, pensadas para sol, vento e clima costeiro.'),
  facts=[(X('UV','UV','UV'),X('high protection fabrics','tissus haute protection','tecidos de alta proteção')),(X('Custom','Sur mesure','Medida'),X('shapes and colours','formes et couleurs','formas e cores')),(X('Wind','Vent','Vento'),X('engineered fixings','fixations calculées','fixações calculadas')),(X('CE','CE','CE'),X('certified nets','filets certifiés','redes certificadas'))],
  ranges=[(X('Tensioned sails','Voiles tendues','Velas tensionadas'),X('Triangular and square sails on steel posts.','Voiles triangulaires et carrées sur mâts acier.','Velas triangulares e quadradas em postes de aço.')),
          (X('UV shade nets','Filets d’ombrage UV','Redes de sombra UV'),X('Knitted HDPE nets for large areas and car parks.','Filets PEHD tricotés pour grandes surfaces et parkings.','Redes PEAD tricotadas para grandes áreas e estacionamentos.')),
          (X('Playground canopies','Toitures d’aires de jeux','Coberturas de parques'),X('Full covers over play and fitness areas.','Couvertures complètes des zones de jeux et fitness.','Coberturas completas de zonas de jogo e fitness.'))],
  chips=['CE', 'UV'], gal=['shade'], logo=None, faq=[]),
 dict(slug='turf-flooring', img='flooring', name=X('Turf & safety flooring', 'Gazon & sols de sécurité', 'Relva & pisos de segurança'),
  short=X('Padel and sport turf, EPDM impact surfaces, landscaping.', 'Gazon padel et sport, sols amortissants EPDM, paysager.', 'Relva de padel e desporto, pisos EPDM, paisagismo.'),
  h1=X('Surfaces for play, sport and landscape.', 'Des sols pour le jeu, le sport et le paysage.', 'Pisos para jogo, desporto e paisagismo.'),
  intro=X('Impact-absorbing EPDM and rubber surfaces for playgrounds and fitness areas, federation-approved padel turf, sports pitches, putting greens and landscaping turf.',
          'Sols amortissants EPDM et caoutchouc pour aires de jeux et fitness, gazon padel homologué, terrains de sport, putting greens et gazon paysager.',
          'Pisos amortecedores em EPDM e borracha para parques infantis e fitness, relva de padel homologada, campos desportivos, putting greens e relva de paisagismo.'),
  facts=[(X('EN 1177','EN 1177','EN 1177'),X('impact attenuation','absorption des chocs','absorção de impacto')),(X('FEP','FEP','FEP'),X('approved padel turf','gazon padel homologué','relva de padel homologada')),(X('Custom','Sur mesure','Medida'),X('colours and patterns','couleurs et motifs','cores e padrões')),(X('Up to 10 yrs','Jusqu’à 10 ans','Até 10 anos'),X('turf warranty','garantie gazon','garantia da relva'))],
  ranges=[(X('EPDM safety flooring','Sol de sécurité EPDM','Piso de segurança EPDM'),X('Poured-in-place, seamless, any colour.','Coulé sur place, sans joints, toutes couleurs.','Aplicado no local, sem juntas, qualquer cor.')),
          (X('Rubber tiles','Dalles caoutchouc','Placas de borracha'),X('Quick to install, easy to repair.','Rapides à poser, faciles à réparer.','Rápidas de instalar, fáceis de reparar.')),
          (X('Padel turf','Gazon padel','Relva de padel'),X('Textured and fibrillated turf for competition.','Gazon texturé et fibrillé pour la compétition.','Relva texturada e fibrilada para competição.')),
          (X('Sports & multisport turf','Gazon sport & multisport','Relva desportiva & polidesportiva'),X('Football, hockey and school pitches.','Football, hockey et terrains scolaires.','Futebol, hóquei e campos escolares.')),
          (X('Putting greens','Putting greens','Putting greens'),X('Golf greens for hotels and residences.','Greens de golf pour hôtels et résidences.','Greens de golfe para hotéis e condomínios.')),
          (X('Landscape turf','Gazon paysager','Relva de paisagismo'),X('Natural-look turf for gardens and terraces.','Gazon aspect naturel pour jardins et terrasses.','Relva de aspeto natural para jardins e esplanadas.'))],
  chips=['EN 1177', 'FEP'], gal=['flooring','monster','calis'], logo=None, faq=[]),
 dict(slug='seating', img='seats', name=X('Seating & grandstands', 'Sièges & tribunes', 'Cadeiras & bancadas'),
  short=X('Stadium seats and demountable stands.', 'Sièges de stade et tribunes démontables.', 'Cadeiras de estádio e bancadas desmontáveis.'),
  h1=X('Seats and stands for every venue.', 'Des sièges et tribunes pour chaque site.', 'Cadeiras e bancadas para cada recinto.'),
  intro=X('Stadium seats, telescopic and demountable metal grandstands for padel clubs, schools, sports halls and event venues, from a manufacturer that equips major European stadiums.',
          'Sièges de stade, tribunes télescopiques et tribunes métalliques démontables pour clubs de padel, écoles, salles de sport et lieux d’événements, par un fabricant qui équipe de grands stades européens.',
          'Cadeiras de estádio, bancadas telescópicas e bancadas metálicas desmontáveis para clubes de padel, escolas, pavilhões e recintos de eventos, de um fabricante que equipa grandes estádios europeus.'),
  facts=[(X('UEFA / FIFA','UEFA / FIFA','UEFA / FIFA'),X('compliant seat ranges','gammes conformes','gamas conformes')),(X('UV-stable','Stable UV','Estável UV'),X('polypropylene','polypropylène','polipropileno')),(X('Custom','Sur mesure','Personalizado'),X('colours & logos','couleurs & logos','cores & logótipos')),(X('Fire','Feu','Fogo'),X('rated materials','matériaux classés','materiais classificados'))],
  ranges=[(X('Stadium seats','Sièges de stade','Cadeiras de estádio'),X('Fixed and tip-up seats in many colours.','Sièges fixes et rabattables, nombreuses couleurs.','Cadeiras fixas e rebatíveis em várias cores.')),
          (X('Demountable grandstands','Tribunes démontables','Bancadas desmontáveis'),X('Metal stands for clubs and events.','Tribunes métalliques pour clubs et événements.','Bancadas metálicas para clubes e eventos.')),
          (X('Telescopic stands','Tribunes télescopiques','Bancadas telescópicas'),X('Retractable seating for indoor halls.','Gradins rétractables pour salles couvertes.','Bancadas retráteis para pavilhões.'))],
  chips=['UEFA', 'FIFA'], gal=['seats'], logo='daplast', faq=[]),
]
PBY = {p['slug']: p for p in PRODUCTS}

# ------------------------------------------------------------------ layout
def head(title, desc, slug, extra=''):
    alt = ''.join('<link rel="alternate" hreflang="%s" href="%s%s">' % (lg, SITE, url(slug, lg)) for lg in LANGS)
    alt += '<link rel="alternate" hreflang="x-default" href="%s%s">' % (SITE, url(slug, 'en'))
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{url(slug)}">
{alt}
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}{url(slug)}">
<meta property="og:image" content="{SITE}{IMG}wide.jpg">
<meta name="theme-color" content="#B4532F">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="/assets/spaces/site.css">
{extra}
</head>
<body>
'''

def header(slug, active=''):
    dd = ''.join(f'<a href="{url(p["slug"])}">{L(p["name"])}</a>' for p in PRODUCTS)
    langs = ''.join(f'<a href="{url(slug, lg)}" hreflang="{lg}" lang="{lg}" class="{"on" if lg == lang else ""}">{lg.upper()}</a>' for lg in LANGS)
    on = lambda k: ' class="on"' if active == k else ''
    return f'''<header class="top"><div class="wrap">
<a class="logo" href="{url('')}"><i aria-hidden="true"></i><span><b>Permanent Summer</b><small>SPACES</small></span></a>
<nav class="nav" id="nav" aria-label="Main">
<details><summary>{L(C['products'])} ▾</summary><div class="dd">{dd}</div></details>
<a href="{url('padel')}#estimator"{on('est')}>{L(C['estimator'])}</a>
<a href="{url('projects')}"{on('projects')}>{L(C['projects'])}</a>
<a href="{url('blog')}"{on('blog')}>{L(C['blog'])}</a>
<a href="{url('about')}"{on('about')}>{L(C['about'])}</a>
<a href="{url('contact')}"{on('contact')}>{L(C['contact'])}</a>
</nav>
<div class="tr"><div class="lang" aria-label="Language">{langs}</div><a class="btn" href="{url('contact')}">{L(C['quote'])}</a>
<button class="burger" type="button" aria-label="{L(C['menu'])}" aria-controls="nav" aria-expanded="false"><span></span><span></span><span></span></button></div>
</div></header>
<main>
'''

def footer(js_t=None):
    prods = ''.join(f'<a href="{url(p["slug"])}">{L(p["name"])}</a>' for p in PRODUCTS)
    t = '<script>window.PS_T=%s</script>' % json.dumps(js_t, ensure_ascii=False) if js_t else ''
    wa = X('Chat with us on WhatsApp', 'Discuter sur WhatsApp', 'Falar connosco no WhatsApp')
    return f'''</main>
<footer class="foot"><div class="wrap">
<div class="cols">
<div style="max-width:340px"><b style="font-size:20px">Permanent Summer Spaces</b><span>{L(C['foot_tag'])}</span></div>
<div><b>{L(C['products'])}</b>{prods}</div>
<div><b>{L(C['company'])}</b><a href="{url('projects')}">{L(C['projects'])}</a><a href="{url('blog')}">{L(C['blog'])}</a><a href="{url('about')}">{L(C['about'])}</a><a href="{url('contact')}">{L(C['contact'])}</a></div>
<div><b>{L(C['contact'])}</b><a href="mailto:spaces@permanentsummer.co">spaces@permanentsummer.co</a><a href="tel:+351924477353">+351 924 477 353</a><a href="https://wa.me/351924477353">WhatsApp</a><span>Altura, Portugal</span></div>
</div>
<div class="bot"><span>Permanent Summer Lda · NIF 516416804 · Altura, Portugal</span><a href="/">{L(C['group'])}</a></div>
</div></footer>
<a class="wa" href="https://wa.me/351924477353" aria-label="{L(wa)}"><svg width="28" height="28" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3-.2.2-.8.8-.8 1.9s.8 2.2.9 2.4c.1.2 1.6 2.5 4 3.5 1.5.6 2.1.7 2.8.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg></a>
{t}<script src="/assets/spaces/site.js" defer></script>
</body>
</html>
'''

def logos():
    return f'<div class="logos"><span>{L(C["partners"])}</span>' + ''.join(
        f'<img src="{IMG}logo-{k}.png" alt="{n}" loading="lazy" width="200" height="60">' for k, n in
        [('agapito', 'Industrias Agapito'), ('verdepadel', 'Verde Padel'), ('daplast', 'Daplast'), ('realturf', 'Realturf')]) + '</div>'

def cta():
    return f'<section class="sec"><div class="wrap"><div class="cta"><div><b>{L(C["cta_t"])}</b><span class="muted">{L(C["cta_p"])}</span></div><a class="btn" href="{url("contact")}">{L(C["cta_b"])}</a></div></div></section>'

def faqblock(items):
    if not items: return ''
    q = ''.join(f'<details><summary>{L(a)}</summary><p>{L(b)}</p></details>' for a, b in items)
    return f'<section class="sec"><div class="wrap faq"><div style="display:flex;flex-direction:column;gap:12px;align-items:flex-start"><span class="pill">{L(C["faq"])}</span><h2>{L(C["faq_t"])}</h2><p class="muted">{L(C["faq_p"])}</p></div><div>{q}</div></div></section>'

def img(k, alt, cls='', lazy=True, w=1600, h=1200):
    return f'<img src="{IMG}{k}.jpg" alt="{esc(alt)}"{" class=%s" % cls if cls else ""}{" loading=lazy" if lazy else ""} width="{w}" height="{h}">'

# ------------------------------------------------------------------ pages
def page_home():
    s = header('')
    s += f'''<section class="hero">{img('wide', L(X('Wooden playground at an international school in Mauritius','Aire de jeux en bois dans une école internationale à Maurice','Parque infantil em madeira numa escola internacional na Maurícia')), lazy=False)}
<div class="in"><div class="txt"><span class="cap">{L(X('PROJECT · ÉCOLE DU NORD, MAURITIUS','PROJET · ÉCOLE DU NORD, MAURICE','PROJETO · ÉCOLE DU NORD, MAURÍCIA'))}</span>
<h1>{L(X('Outdoor spaces, made in Europe.','Des espaces extérieurs, fabriqués en Europe.','Espaços exteriores, fabricados na Europa.'))}</h1>
<p>{L(X('Certified playgrounds, padel courts, fitness parks and urban furniture for hotels, clubs, developers and public projects.','Aires de jeux, terrains de padel, parcs de fitness et mobilier urbain certifiés pour hôtels, clubs, promoteurs et projets publics.','Parques infantis, campos de padel, parques de fitness e mobiliário urbano certificados para hotéis, clubes, promotores e projetos públicos.'))}</p></div>
<div class="ctas"><a class="btn light" href="#products">{L(X('Explore products','Voir les produits','Ver produtos'))}</a><a class="btn" href="{url('contact')}">{L(C['start'])}</a></div></div></section>
<div class="wrap" style="padding-top:36px">{clients()}</div>
<section id="products" class="sec" style="padding-top:40px"><div class="wrap">
<div class="head center" style="flex-direction:column;justify-content:center"><span class="pill">{L(X('Product lines','Gammes de produits','Linhas de produtos'))}</span><h2>{L(X('Everything for your outdoor project','Tout pour votre projet extérieur','Tudo para o seu projeto exterior'))}</h2></div>
<div class="g4">'''
    for p in PRODUCTS:
        s += f'<a class="card" href="{url(p["slug"])}">{img(p["img"], L(p["name"]))}<div class="b"><h3>{L(p["name"])}</h3><p>{L(p["short"])}</p><span class="more">{L(C["discover"])}</span></div></a>'
    s += f'<div class="card soon"><span class="pill" style="background:#fff">{L(C["soon"])}</span><h3>{L(C["soon_items"])}</h3></div></div></div></section>'
    why = [(X('Certified to EN standards','Certifié selon les normes EN','Certificado pelas normas EN'), X('EN 1176 playgrounds, EN 16630 fitness, from ISO 9001 and ISO 14001 manufacturers.','Aires de jeux EN 1176, fitness EN 16630, fabricants ISO 9001 et ISO 14001.','Parques EN 1176, fitness EN 16630, de fabricantes ISO 9001 e ISO 14001.')),
           (X('Built for sun, salt and wind','Conçu pour le soleil, le sel et le vent','Feito para sol, sal e vento'), X('Anti-corrosion finishes and site-specific wind reports for coastal and tropical projects.','Finitions anticorrosion et rapports de vent pour les projets côtiers et tropicaux.','Acabamentos anticorrosão e relatórios de vento para projetos costeiros e tropicais.')),
           (X('Tender-ready paperwork','Dossiers prêts pour les appels d’offres','Documentação pronta para concursos'), X('Technical sheets, certificates, packing lists and customs codes for every order.','Fiches techniques, certificats, listes de colisage et codes douaniers pour chaque commande.','Fichas técnicas, certificados, listas de embalagem e códigos aduaneiros em cada encomenda.')),
           (X('Supply or full project','Fourniture ou projet complet','Fornecimento ou projeto completo'), X('Supply only, or supply with supervised installation by the manufacturer’s specialists.','Fourniture seule, ou avec installation supervisée par les spécialistes du fabricant.','Só fornecimento, ou com instalação supervisionada pelos especialistas do fabricante.'))]
    s += '<section class="sec"><div class="wrap g4 why">' + ''.join(f'<div><h3>{L(a)}</h3><p>{L(b)}</p></div>' for a, b in why) + '</div></section>'
    s += f'''<section class="sec"><div class="wrap"><div class="band"><div class="in"><h2>{L(X('How much does a padel court cost?','Combien coûte un terrain de padel ?','Quanto custa um campo de padel?'))}</h2>
<p>{L(X('Pick a model, the number of courts and a cover. Get an indicative budget instantly.','Choisissez un modèle, le nombre de terrains et une couverture. Obtenez un budget indicatif immédiatement.','Escolha o modelo, o número de campos e a cobertura. Obtenha um orçamento indicativo de imediato.'))}</p>
<a class="btn light" href="{url('padel')}#estimator">{L(X('Open the estimator →','Ouvrir l’estimateur →','Abrir o estimador →'))}</a></div>{img('panoramix', 'Panoramic padel court')}</div></div></section>'''
    aud = [(X('Hotels & resorts','Hôtels & resorts','Hotéis & resorts'), X('Kids clubs, padel and fitness that match a premium guest experience.','Mini-clubs, padel et fitness à la hauteur d’une expérience haut de gamme.','Kids clubs, padel e fitness à altura de uma experiência premium.')),
           (X('Padel & sports clubs','Clubs de padel & de sport','Clubes de padel & desporto'), X('Courts, covers, turf and grandstands with wind reports.','Terrains, couvertures, gazon et tribunes avec rapports de vent.','Campos, coberturas, relva e bancadas com relatórios de vento.')),
           (X('Developers & architects','Promoteurs & architectes','Promotores & arquitetos'), X('Community playgrounds, gyms and street furniture specified to EN standards.','Aires de jeux, salles de sport et mobilier urbain conformes aux normes EN.','Parques, ginásios e mobiliário urbano especificados segundo as normas EN.')),
           (X('Public sector','Secteur public','Setor público'), X('Parks, schools and cities, with tender documentation.','Parcs, écoles et villes, avec les dossiers d’appels d’offres.','Parques, escolas e cidades, com documentação para concursos.'))]
    s += f'<section class="sec"><div class="wrap"><div class="head"><div class="t"><span class="pill">{L(X("Who we work with","Nos clients","Com quem trabalhamos"))}</span><h2>{L(X("Spaces people use every day","Des espaces utilisés chaque jour","Espaços usados todos os dias"))}</h2></div></div><div class="g4">' + ''.join(f'<div class="card" style="padding:26px;gap:8px"><h3>{L(a)}</h3><p class="muted" style="font-size:15px">{L(b)}</p></div>' for a, b in aud) + '</div></div></section>'
    s += f'''<section class="sec"><div class="wrap"><div class="head"><div class="t"><span class="pill">{L(C['projects'])}</span><h2>{L(X('Recent projects','Projets récents','Projetos recentes'))}</h2></div><a href="{url('projects')}" style="font-weight:700;text-decoration:none">{L(X('See all projects →','Voir tous les projets →','Ver todos os projetos →'))}</a></div>
<div class="feat"><div class="ph">{img('wide','Playground')}{img('bridge','Balance bridge')}{img('gauge','Early-years equipment')}</div><div class="b"><span class="pill" style="align-self:flex-start">{L(X('Education · Mauritius','Éducation · Maurice','Educação · Maurícia'))}</span><h3 style="font-size:28px">{L(X('École du Nord, international school','École du Nord, école internationale','École du Nord, escola internacional'))}</h3><p class="muted">{L(X('Wooden play towers with stainless steel slides, a balance bridge and early-years equipment, supplied from Spain and installed on a coastal site.','Tours de jeux en bois avec toboggans inox, pont d’équilibre et équipements petite enfance, fournis depuis l’Espagne et installés sur un site côtier.','Torres de jogo em madeira com escorregas em inox, ponte de equilíbrio e equipamentos para a primeira infância, fornecidos a partir de Espanha num local costeiro.'))}</p></div></div>{logos()}</div></section>'''
    s += cta()
    return (L(X('Permanent Summer Spaces | Playgrounds, padel courts & outdoor fitness made in Europe','Permanent Summer Spaces | Aires de jeux, padel & fitness extérieur fabriqués en Europe','Permanent Summer Spaces | Parques infantis, padel & fitness exterior fabricados na Europa')),
            L(X('Certified European playgrounds, padel courts and covers, outdoor fitness, urban furniture, shade, turf and seating for hotels, clubs, developers and public projects.','Aires de jeux, terrains et couvertures de padel, fitness extérieur, mobilier urbain, ombrage, gazon et tribunes européens certifiés pour hôtels, clubs, promoteurs et projets publics.','Parques infantis, campos e coberturas de padel, fitness, mobiliário urbano, sombra, relva e bancadas europeus certificados para hotéis, clubes, promotores e projetos públicos.')),
            s, None)

def page_product(p):
    if p['slug'] == 'padel': return page_padel(p)
    s = header(p['slug'])
    s += f'<div class="wrap"><div class="crumb"><a href="{url("")}">{L(C["home"])}</a> / {L(C["products"])} / <b style="color:var(--tx)">{L(p["name"])}</b></div>'
    s += f'<div class="phero"><div class="txt"><span class="pill">{L(p["name"])}</span><h1>{L(p["h1"])}</h1><p>{L(p["intro"])}</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" href="{url("contact")}?p={p["slug"]}">{L(C["quote"])}</a><a class="btn soft" href="#ranges">{L(C["ranges"])}</a></div></div>{img(p["img"], L(p["name"]), lazy=False)}</div>'
    s += '<div class="facts">' + ''.join(f'<div><b>{L(a)}</b><span>{L(b)}</span></div>' for a, b in p['facts']) + '</div></div>'
    s += f'<section id="ranges" class="sec"><div class="wrap"><div class="head"><div class="t"><span class="pill">{L(C["ranges"])}</span><h2>{L(X("What we supply","Ce que nous fournissons","O que fornecemos"))}</h2></div><div class="chips" aria-label="{L(C["standards"])}">' + ''.join(f'<span>{c}</span>' for c in p['chips']) + '</div></div><div class="g3">'
    s += ''.join(f'<div class="card" style="padding:26px;gap:8px"><h3>{L(a)}</h3><p class="muted" style="font-size:15px">{L(b)}</p></div>' for a, b in p['ranges']) + '</div></div></section>'
    if p['gal']:
        s += f'<section class="sec"><div class="wrap"><div class="head"><div class="t"><span class="pill">{L(C["gallery"])}</span></div>'
        if p['logo']:
            s += f'<span class="muted" style="display:flex;align-items:center;gap:12px">{L(C["made_by"])} <img src="{IMG}logo-{p["logo"]}.png" alt="{p["logo"]}" style="height:30px;width:auto;opacity:.8" loading="lazy"></span>'
        s += '</div><div class="gal">' + ''.join(f'<figure>{img(g, L(p["name"]))}</figure>' for g in p['gal']) + f'</div><p class="muted" style="font-size:13px;margin-top:12px">{L(C["photo_credit"])}</p></div></section>'
    s += faqblock(p['faq']) + cta()
    return (f'{L(p["name"])} | Permanent Summer Spaces', L(p['intro'])[:158], s, None)

def page_padel(p):
    s = header('padel', 'est')
    s += f'<div class="wrap"><div class="crumb"><a href="{url("")}">{L(C["home"])}</a> / {L(C["products"])} / <b style="color:var(--tx)">{L(p["name"])}</b></div>'
    s += f'''<div class="phero"><div class="txt"><span class="pill">{L(p['name'])}</span><h1>{L(X('Professional padel courts, made in Spain.','Des terrains de padel professionnels, fabriqués en Espagne.','Campos de padel profissionais, fabricados em Espanha.'))}</h1>
<p>{L(X('Classic and panoramic courts with LED floodlights and federation-approved turf, plus aluminium covers for year-round play. Supplied worldwide, with supervised installation if you need it.','Terrains classiques et panoramiques avec éclairage LED et gazon homologué, et couvertures en aluminium pour jouer toute l’année. Livrés dans le monde entier, avec installation supervisée si besoin.','Campos clássicos e panorâmicos com iluminação LED e relva homologada, e coberturas em alumínio para jogar todo o ano. Entregues em todo o mundo, com instalação supervisionada se precisar.'))}</p>
<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" href="#estimator">{L(X('Estimate my budget','Estimer mon budget','Estimar o meu orçamento'))}</a><a class="btn soft" href="{url('contact')}?p=padel">{L(C['quote'])}</a></div></div>{img('padel-palms', 'Panoramic padel court', lazy=False)}</div>'''
    facts = [(X('From €21,040','Dès 21 040 €','Desde 21 040 €'), X('per court, excl. VAT, ex-works','par terrain, HT, départ usine','por campo, sem IVA, à saída de fábrica')), (X('~5 weeks','~5 semaines','~5 semanas'), X('production from order','de fabrication','de produção')), (X('10–12 mm','10–12 mm','10–12 mm'), X('tempered safety glass','verre trempé de sécurité','vidro temperado de segurança')), (X('FEP-approved','Homologué FEP','Homologada FEP'), X('textured padel turf','gazon padel texturé','relva de padel texturada'))]
    s += '<div class="facts">' + ''.join(f'<div><b>{L(a)}</b><span>{L(b)}</span></div>' for a, b in facts) + '</div></div>'
    M = [('Olimpia', 'olimpia', X('Classic court','Terrain classique','Campo clássico'), X('A reliable classic with mesh and 10 mm glass. The best value for clubs and hotels.','Un classique fiable avec grillage et verre 10 mm. Le meilleur rapport qualité-prix pour clubs et hôtels.','Um clássico fiável com rede e vidro de 10 mm. A melhor relação qualidade-preço para clubes e hotéis.'), [X('10 mm tempered glass','Verre trempé 10 mm','Vidro temperado 10 mm'), X('Classic steel structure','Structure acier classique','Estrutura clássica em aço'), X('8 LED floodlights','8 projecteurs LED','8 projetores LED')], '21,040'),
         ('Panoramix', 'panoramix', X('Panoramic court','Terrain panoramique','Campo panorâmico'), X('Uninterrupted glass on the side walls for spectators and premium venues.','Vitrage continu sur les côtés pour les spectateurs et les sites premium.','Vidro contínuo nas laterais para espectadores e espaços premium.'), [X('12 mm tempered glass','Verre trempé 12 mm','Vidro temperado 12 mm'), X('Panoramic structure','Structure panoramique','Estrutura panorâmica'), X('8 LED floodlights','8 projecteurs LED','8 projetores LED')], '23,570'),
         ('Brutux', 'brutux', X('Reinforced panoramic','Panoramique renforcé','Panorâmico reforçado'), X('Reinforced pillars and anti-corrosion paint. Our pick for seaside and windy sites.','Poteaux renforcés et peinture anticorrosion. Notre choix pour le bord de mer et les sites venteux.','Pilares reforçados e pintura anticorrosão. A nossa escolha para locais junto ao mar e com vento.'), [X('12 mm tempered glass','Verre trempé 12 mm','Vidro temperado 12 mm'), X('Reinforced pillars','Poteaux renforcés','Pilares reforçados'), X('Anti-corrosion finish','Finition anticorrosion','Acabamento anticorrosão')], '26,820')]
    fr_price = lambda v: v.replace(',', ' ') if lang != 'en' else v
    s += f'<section class="sec"><div class="wrap"><div class="head"><div class="t"><span class="pill">{L(X("Court models","Modèles","Modelos"))}</span><h2>{L(X("Choose your court","Choisissez votre terrain","Escolha o seu campo"))}</h2></div><p class="muted">{L(X("Every model includes the structure, glass, 8 LED floodlights, 2 entrances and textured turf with silica.","Chaque modèle comprend la structure, le verre, 8 projecteurs LED, 2 entrées et le gazon texturé avec silice.","Cada modelo inclui estrutura, vidro, 8 projetores LED, 2 entradas e relva texturada com sílica."))}</p></div><div class="g3">'
    for n, k, t, d, feat, pr in M:
        s += f'<div class="model">{img(k, n)}<div class="b"><div style="display:flex;justify-content:space-between;align-items:baseline;gap:8px"><h3 style="font-size:26px">{n}</h3><span class="muted" style="font-size:13px;font-weight:700">{L(t)}</span></div><p class="muted" style="font-size:15px">{L(d)}</p><ul class="list">' + ''.join(f'<li>{L(f)}</li>' for f in feat) + f'</ul><div class="pr"><span>{L(X("From","Dès","Desde"))} <b>€{fr_price(pr)}</b> {L(X("excl. VAT","HT","sem IVA"))}</span><a href="#estimator" style="font-weight:700;text-decoration:none">{L(X("Estimate →","Estimer →","Estimar →"))}</a></div></div></div>'
    s += '</div></div></section>'
    s += f'''<section class="sec"><div class="wrap covers"><div class="cgal">{img('cover-ext','Covered padel court')}{img('cover-int','Inside a covered padel court')}{img('cover-terrace','Covered courts with terrace')}</div>
<div style="display:flex;flex-direction:column;gap:18px;align-items:flex-start"><span class="pill">{L(X('Covers','Couvertures','Coberturas'))}</span><h2>{L(X('Play all year, whatever the weather.','Jouez toute l’année, quel que soit le temps.','Jogue todo o ano, faça o tempo que fizer.'))}</h2>
<p class="muted" style="font-size:17px">{L(X('Aluminium structures (EN AW 6061-T6) with M2 fire-rated PVC canvas, rated for 100 km/h winds. In cyclone zones the canvas is removed in a few hours and the structure stays.','Structures en aluminium (EN AW 6061-T6) avec toile PVC classée M2, prévues pour des vents de 100 km/h. En zone cyclonique, la toile se retire en quelques heures et la structure reste.','Estruturas em alumínio (EN AW 6061-T6) com lona PVC classe M2, dimensionadas para ventos de 100 km/h. Em zonas de ciclones a lona retira-se em poucas horas e a estrutura fica.'))}</p>
<div class="g2" style="width:100%"><div class="box"><b style="font-size:18px">One-Pro</b><span class="muted" style="font-size:14px">{L(X('Tight cover · 10.55 × 20.50 m','Couverture ajustée · 10,55 × 20,50 m','Cobertura ajustada · 10,55 × 20,50 m'))}</span><span style="font-size:14px">{L(X('From','Dès','Desde'))} <b>€{fr_price('59,800')}</b> + {L(X('assembly','montage','montagem'))}</span></div>
<div class="box"><b style="font-size:18px">One-Pro XL</b><span class="muted" style="font-size:14px">{L(X('Court + covered walkway · 15 × 22.5 m','Terrain + circulation couverte · 15 × 22,5 m','Campo + circulação coberta · 15 × 22,5 m'))}</span><span style="font-size:14px">{L(X('From','Dès','Desde'))} <b>€{fr_price('64,690')}</b> + {L(X('assembly','montage','montagem'))}</span></div></div>
<span class="muted" style="font-size:14px">{L(X('5-year structure warranty · 24-month canvas warranty · production 2–4 months','Garantie structure 5 ans · toile 24 mois · fabrication 2 à 4 mois','Garantia estrutura 5 anos · lona 24 meses · produção 2 a 4 meses'))}</span></div></div></section>'''
    # estimator
    def radio(name, val, label, checked=False):
        return f'<label class="opt"><input type="radio" name="{name}" value="{val}"{" checked" if checked else ""}><span>{label}</span></label>'
    s += f'''<section class="sec"><div class="wrap"><form id="est" class="est" onsubmit="return false" aria-labelledby="estT"><div id="estimator">
<h2 id="estT" style="margin-bottom:26px">{L(X('Estimate your budget','Estimez votre budget','Estime o seu orçamento'))}</h2>
<fieldset><legend>{L(X('MODEL','MODÈLE','MODELO'))}</legend><div class="opts">{radio('model','olimpia','Olimpia',True)}{radio('model','panoramix','Panoramix')}{radio('model','brutux','Brutux')}</div></fieldset>
<fieldset><legend>{L(X('NUMBER OF COURTS','NOMBRE DE TERRAINS','NÚMERO DE CAMPOS'))}</legend><div class="qty"><button type="button" id="minus" aria-label="−1">−</button><output id="qty" aria-live="polite">1</output><button type="button" id="plus" aria-label="+1">+</button></div></fieldset>
<fieldset><legend>{L(X('COVER','COUVERTURE','COBERTURA'))}</legend><div class="opts">{radio('cover','none',L(X('No cover','Sans couverture','Sem cobertura')),True)}{radio('cover','pro','One-Pro')}{radio('cover','xl','One-Pro XL')}</div>
<label style="display:flex;gap:10px;align-items:center;margin-top:12px;font-weight:600"><input type="checkbox" id="flap" style="width:18px;height:18px;accent-color:#fff"> {L(X('Add a shading flap to the cover','Ajouter un volet d’ombrage','Adicionar aba de sombra'))}</label></fieldset>
<fieldset><legend>{L(X('INSTALLATION','INSTALLATION','INSTALAÇÃO'))}</legend><div class="opts">{radio('inst','no',L(X('Supply only','Fourniture seule','Só fornecimento')))}{radio('inst','yes',L(X('Supervised installation','Installation supervisée','Instalação supervisionada')),True)}</div></fieldset>
</div>
<div class="res" aria-live="polite"><span class="k">{L(X('INDICATIVE BUDGET','BUDGET INDICATIF','ORÇAMENTO INDICATIVO'))}</span><div class="price" id="price">€0</div>
<span class="muted" style="font-size:14px">{L(X('Excl. VAT · ex-works Spain · ±5%','HT · départ usine Espagne · ±5 %','Sem IVA · à saída de fábrica em Espanha · ±5%'))}</span><ul id="incl"></ul>
<p class="small">{L(X('Not included: transport, unloading crane, foundations and civil works, import duties and VAT. Transport is quoted for your exact site.','Non inclus : transport, grue de déchargement, fondations et génie civil, droits d’importation et TVA. Le transport est chiffré pour votre site.','Não incluído: transporte, grua de descarga, fundações e construção civil, direitos de importação e IVA. O transporte é orçamentado para o seu local.'))}</p>
<p class="small" id="lead" style="border:0;padding:0"></p><button class="btn" type="button" id="estSend">{L(X('Get my firm quote','Obtenir mon devis ferme','Obter orçamento firme'))}</button></div></form></div></section>'''
    s += f'''<section class="sec"><div class="wrap"><div class="head"><div class="t"><span class="pill">{L(X('How we deliver','Livraison','Como entregamos'))}</span><h2>{L(X('Supply only, or supply + installation','Fourniture seule, ou fourniture + installation','Só fornecimento, ou fornecimento + instalação'))}</h2></div></div><div class="g2">
<div class="card" style="padding:32px;gap:10px"><h3 style="font-size:24px">{L(X('Supply only','Fourniture seule','Só fornecimento'))}</h3><p class="muted">{L(X('Courts are produced to order and delivered ex-works or to your port, with packing lists, certificates and customs codes. Your local contractor installs them.','Les terrains sont fabriqués sur commande et livrés départ usine ou à votre port, avec listes de colisage, certificats et codes douaniers. Votre entreprise locale les installe.','Os campos são produzidos por encomenda e entregues à saída de fábrica ou no seu porto, com listas de embalagem, certificados e códigos aduaneiros. O seu empreiteiro local instala.'))}</p></div>
<div class="card" style="padding:32px;gap:10px"><h3 style="font-size:24px">{L(X('Supervised installation','Installation supervisée','Instalação supervisionada'))}</h3><p class="muted">{L(X('Two specialists from the manufacturer come to site and install the courts with your local crew, so the job is done right first time.','Deux spécialistes du fabricant viennent sur site et installent les terrains avec votre équipe locale, pour un travail bien fait du premier coup.','Dois especialistas do fabricante vêm ao local e instalam os campos com a sua equipa local, para ficar bem feito à primeira.'))}</p></div></div></div></section>'''
    F = [(X('How long does it take?','Quels sont les délais ?','Quanto tempo demora?'), X('About 5 weeks of production for courts and 2–4 months for covers, plus shipping to your site.','Environ 5 semaines de fabrication pour les terrains et 2 à 4 mois pour les couvertures, plus le transport.','Cerca de 5 semanas de produção para os campos e 2 a 4 meses para as coberturas, mais o transporte.')),
         (X('Can courts go near the sea or in cyclone zones?','Peut-on installer un terrain en bord de mer ou en zone cyclonique ?','Os campos podem ficar junto ao mar ou em zonas de ciclones?'), X('Yes. We recommend Brutux with anti-corrosion paint, and covers whose canvas can be removed before a cyclone.','Oui. Nous recommandons le Brutux avec peinture anticorrosion, et des couvertures dont la toile se retire avant un cyclone.','Sim. Recomendamos o Brutux com pintura anticorrosão, e coberturas cuja lona se retira antes de um ciclone.')),
         (X('What foundations do I need?','Quelles fondations faut-il ?','Que fundações são precisas?'), X('A flat concrete slab with a slight slope for drainage. We send the technical drawings with your quote.','Une dalle béton plane avec une légère pente pour l’évacuation. Nous envoyons les plans techniques avec le devis.','Uma laje de betão plana com ligeira pendente para drenagem. Enviamos os desenhos técnicos com o orçamento.')),
         (X('How is it shipped?','Comment est-il expédié ?','Como é enviado?'), X('In containers from Valencia. Unloading needs a crane on site, arranged by the client.','En conteneurs depuis Valence. Le déchargement nécessite une grue sur site, à la charge du client.','Em contentores a partir de Valência. A descarga requer uma grua no local, a cargo do cliente.'))]
    s += faqblock(F) + f'<div class="wrap">{logos()}</div>' + cta()
    T = {'sep': ',' if lang == 'en' else ' ',
         'l_court': L(X('court, 8 LED floodlights, 2 entrances, textured turf with silica','terrain, 8 projecteurs LED, 2 entrées, gazon texturé avec silice','campo, 8 projetores LED, 2 entradas, relva texturada com sílica')),
         'l_inst': L(X('Supervised installation (2 specialists per court)','Installation supervisée (2 spécialistes par terrain)','Instalação supervisionada (2 especialistas por campo)')),
         'l_cover': L(X('aluminium cover, M2 canvas, assembly','couverture aluminium, toile M2, montage','cobertura em alumínio, lona M2, montagem')),
         'l_flap': L(X('Shading flap','Volet d’ombrage','Aba de sombra')),
         'l_lead': L(X('Production: about 5 weeks from order.','Fabrication : environ 5 semaines après commande.','Produção: cerca de 5 semanas após encomenda.')),
         'l_lead_cover': L(X('Production: about 5 weeks for courts, 2–4 months for covers. Covers need foundations and a site wind study.','Fabrication : environ 5 semaines pour les terrains, 2 à 4 mois pour les couvertures. Les couvertures nécessitent des fondations et une étude au vent.','Produção: cerca de 5 semanas para campos, 2 a 4 meses para coberturas. As coberturas exigem fundações e estudo de vento.')),
         'mail_intro': L(X('Padel estimate request','Demande de devis padel','Pedido de orçamento de padel')),
         'k_model': L(X('Model','Modèle','Modelo')), 'k_courts': L(X('Courts','Terrains','Campos')), 'k_cover': L(X('Cover','Couverture','Cobertura')),
         'k_inst': L(X('Supervised installation','Installation supervisée','Instalação supervisionada')), 'k_budget': L(X('Indicative budget','Budget indicatif','Orçamento indicativo')),
         'k_name': L(X('Name','Nom','Nome')), 'k_company': L(X('Company','Société','Empresa')), 'k_site': L(X('Site location','Lieu du site','Local')), 'k_phone': L(X('Phone / WhatsApp','Téléphone / WhatsApp','Telefone / WhatsApp'))}
    return (L(X('Padel courts & covers, made in Spain | Permanent Summer Spaces','Terrains & couvertures de padel fabriqués en Espagne | Permanent Summer Spaces','Campos & coberturas de padel fabricados em Espanha | Permanent Summer Spaces')),
            L(X('Classic and panoramic padel courts from €21,040 and aluminium covers. Instant budget estimator, supply worldwide, supervised installation.','Terrains de padel classiques et panoramiques dès 21 040 € et couvertures aluminium. Estimateur de budget, livraison mondiale, installation supervisée.','Campos de padel clássicos e panorâmicos desde 21 040 € e coberturas em alumínio. Estimador de orçamento, entrega mundial, instalação supervisionada.')),
            s, T)

P_ = lambda slug, sec, name, logo, link, n, d: dict(slug=slug, sec=sec, name=name, logo=logo, link=link, n=n, d=d)
PROJ = [
 P_('edn', X('Education · Mauritius','Éducation · Maurice','Educação · Maurícia'), 'École du Nord', 'edn', 'https://ecoledunord.net/', 5, X('Wooden playsets with stainless steel slides, a balance bridge and early-years equipment for an international school of 1,300+ pupils.','Structures de jeux en bois avec toboggans inox, pont d’équilibre et équipements petite enfance pour une école internationale de plus de 1 300 élèves.','Estruturas de jogo em madeira com escorregas em inox, ponte de equilíbrio e equipamentos de primeira infância para uma escola internacional com mais de 1 300 alunos.')),
 P_('metro', X('Transport · Public','Transport · Public','Transportes · Público'), 'Metro Express', 'metro', 'https://mauritiusmetroexpress.mu/', 4, X('Urban park under the light-rail viaduct: playground, outdoor fitness and street furniture.','Parc urbain sous le viaduc du métro léger : aire de jeux, fitness extérieur et mobilier urbain.','Parque urbano sob o viaduto do metro ligeiro: parque infantil, fitness ao ar livre e mobiliário urbano.')),
 P_('croisette', X('Retail','Commerce','Comércio'), 'La Croisette Grand Baie', 'croisette', 'https://gblc.mu/', 6, X('Shopping-centre playground: play towers, slides, balance bridge and educational panels on safety flooring.','Aire de jeux de centre commercial : tours, toboggans, pont d’équilibre et panneaux éducatifs sur sol amortissant.','Parque infantil de centro comercial: torres, escorregas, ponte de equilíbrio e painéis educativos sobre piso de segurança.')),
 P_('cascavelle', X('Retail · Mixed-use','Commerce · Mixte','Comércio · Misto'), 'Cascavelle', 'cascavelle', 'https://cascavelle.mu/', 6, X('Themed pirate-ship playground with sensory and educational panels on synthetic turf.','Aire de jeux thème bateau pirate avec panneaux sensoriels et éducatifs sur gazon synthétique.','Parque infantil temático de barco pirata com painéis sensoriais e educativos sobre relva sintética.')),
 P_('azuri', X('Smart city · Developer','Smart city · Promoteur','Smart city · Promotor'), 'Azuri Smart City', 'azuri', 'https://azuri.mu/', 0, X('Supply and installation of benches and litter bins across the smart-city development.','Fourniture et installation de bancs et corbeilles dans la ville intelligente.','Fornecimento e instalação de bancos e papeleiras na cidade inteligente.')),
 P_('northfields', X('Education','Éducation','Educação'), 'Northfields International School', 'northfields', 'https://www.northfieldsinternational.school/', 0, X('Golf putting green in synthetic turf.','Putting green en gazon synthétique.','Putting green em relva sintética.')),
 P_('nsld', X('Social housing','Logement social','Habitação social'), 'NSLD', 'nsld', 'https://nsld.mu/en/', 0, X('Community playgrounds built into social housing estates across Mauritius.','Aires de jeux intégrées aux résidences de logement social à Maurice.','Parques infantis integrados em bairros de habitação social na Maurícia.')),
 P_('nhdc', X('Public housing','Logement public','Habitação pública'), 'NHDC', 'nhdc', 'https://nhdcmauritius.com/', 0, X('Playground equipment for a housing development: swings, slide, carousel and see-saw.','Équipements de jeux pour un programme de logement : balançoires, toboggan, tourniquet et bascule.','Equipamentos infantis para um empreendimento habitacional: baloiços, escorrega, carrossel e balancé.')),
 P_('rmclub', X('Sport · Padel','Sport · Padel','Desporto · Padel'), 'RM Club Grand Baie', 'rmclub', 'https://www.rmclub.mu/grand-baie/fr/club.php', 0, X('Padel courts, padel turf and covered-court project.','Terrains de padel, gazon padel et projet de couverture.','Campos de padel, relva de padel e projeto de cobertura.')),
 P_('wellness', X('Wellness · Public tender','Bien-être · Appel d’offres','Bem-estar · Concurso público'), X('Municipal wellness park','Parc bien-être municipal','Parque de bem-estar municipal'), None, None, 0, X('Outdoor gym, calisthenics area and senior park.','Salle de sport extérieure, espace calisthénie et parc seniors.','Ginásio exterior, zona de calistenia e parque sénior.')),
]
PIMG = '/assets/spaces/img/proj/'

def clients(title=True):
    s = '<div class="clients">'
    if title: s += f'<span>{L(X("Trusted by","Ils nous font confiance","Confiam em nós"))}</span>'
    s += '<div class="cl">'
    for p in PROJ:
        if not p['logo']: continue
        s += f'<a href="{url("projects")}#{p["slug"]}" data-proj="{p["slug"]}" title="{esc(L(p["name"]))}"><img src="{IMG}client-{p["logo"]}.png" alt="{esc(L(p["name"]))}" loading="lazy"></a>'
    return s + '</div></div>' + dialogs()

def dialogs():
    out = ''
    for p in PROJ:
        if not p['logo']: continue
        ph = ''.join(f'<img src="{PIMG}{p["slug"]}-{i}.jpg" alt="{esc(L(p["name"]))} {i}" loading="lazy">' for i in range(1, p['n'] + 1))
        ph = f'<div class="pd-gal">{ph}</div>' if ph else f'<p class="muted">{L(X("Photos coming soon.","Photos bientôt disponibles.","Fotos em breve."))}</p>'
        sl = p['slug']
        out += (f'<dialog class="pd" id="pd-{sl}" aria-labelledby="pdt-{sl}"><div class="pd-in"><div class="pd-h"><img src="{IMG}client-{p["logo"]}.png" alt="" class="pd-logo">'
                f'<div><span class="w">{L(p["sec"])}</span><h2 id="pdt-{sl}">{L(p["name"])}</h2></div>'
                f'<button type="button" class="pd-x" aria-label="{L(X("Close","Fermer","Fechar"))}">&times;</button></div>'
                f'<p class="muted">{L(p["d"])}</p>{ph}<div style="display:flex;gap:12px;flex-wrap:wrap">'
                f'<a class="btn" href="{url("contact")}">{L(X("Start a similar project","Démarrer un projet similaire","Iniciar um projeto semelhante"))}</a>'
                f'<a class="btn soft" href="{p["link"]}" target="_blank" rel="noopener">{L(X("Client website ↗","Site du client ↗","Site do cliente ↗"))}</a></div></div></dialog>')
    return out

def page_projects():
    s = header('projects', 'projects')
    s += f'<div class="wrap" style="padding-top:40px"><div class="head"><div class="t"><span class="pill">{L(C["projects"])}</span><h1>{L(X("Trusted by public and private clients","La confiance de clients publics et privés","A confiança de clientes públicos e privados"))}</h1></div><p class="muted">{L(X("Schools, developers, public bodies and clubs across Mauritius. Click a logo to see the project.","Écoles, promoteurs, organismes publics et clubs à Maurice. Cliquez sur un logo pour voir le projet.","Escolas, promotores, entidades públicas e clubes na Maurícia. Clique num logótipo para ver o projeto."))}</p></div>{clients(False)}</div>'
    for p in PROJ:
        if not p['n']: continue
        lg = f'<img src="{IMG}client-{p["logo"]}.png" alt="" style="height:56px;width:auto;align-self:flex-start">' if p['logo'] else ''
        gal = ''.join(f'<img src="{PIMG}{p["slug"]}-{i}.jpg" alt="{esc(L(p["name"]))} {i}" loading="lazy" width="1600" height="1200">' for i in range(1, p['n'] + 1))
        s += f'<section class="sec" id="{p["slug"]}"><div class="wrap"><div class="pj"><div class="pj-t">{lg}<span class="w">{L(p["sec"])}</span><h2>{L(p["name"])}</h2><p class="muted">{L(p["d"])}</p><a href="{p["link"]}" target="_blank" rel="noopener" style="font-weight:700;text-decoration:none">{L(X("Client website ↗","Site du client ↗","Site do cliente ↗"))}</a></div><div class="pj-g">{gal}</div></div></div></section>'
    cards = ''
    for p in PROJ:
        if p['n']: continue
        lg = f'<img src="{IMG}client-{p["logo"]}.png" alt="" style="height:44px;width:auto;align-self:flex-start;margin-bottom:6px" loading="lazy">' if p['logo'] else ''
        nm = f'<a href="{p["link"]}" target="_blank" rel="noopener" style="color:var(--tx);text-decoration:none">{L(p["name"])}</a>' if p['link'] else L(p['name'])
        cards += f'<div id="{p["slug"]}">{lg}<span class="w">{L(p["sec"])}</span><b>{nm}</b><p>{L(p["d"])}</p></div>'
    s += f'<section class="sec"><div class="wrap"><h2 style="font-size:32px;margin-bottom:24px">{L(X("More projects","Autres projets","Outros projetos"))}</h2><div class="proj">{cards}</div></div></section>'
    s += cta()
    return (L(X('Projects | Permanent Summer Spaces','Projets | Permanent Summer Spaces','Projetos | Permanent Summer Spaces')), L(X('Playgrounds, urban furniture, outdoor fitness and padel projects for schools, developers, cities and clubs.','Projets d’aires de jeux, mobilier urbain, fitness extérieur et padel pour écoles, promoteurs, villes et clubs.','Projetos de parques infantis, mobiliário urbano, fitness e padel para escolas, promotores, cidades e clubes.')), s, None)

ART = dict(slug='padel-court-cost', img='padel-palms',
    cat=X('PADEL · GUIDE','PADEL · GUIDE','PADEL · GUIA'),
    title=X('How much does a padel court really cost?','Combien coûte vraiment un terrain de padel ?','Quanto custa realmente um campo de padel?'),
    lead=X('Court models, covers, foundations, shipping and installation: every cost line explained, with real price ranges.','Modèles, couvertures, fondations, transport et installation : chaque poste expliqué, avec de vrais prix.','Modelos, coberturas, fundações, transporte e instalação: cada custo explicado, com preços reais.'))

def page_blog():
    s = header('blog', 'blog')
    s += f'<div class="wrap" style="padding-top:40px"><div class="head"><div class="t"><span class="pill">{L(C["blog"])}</span><h1>{L(X("Guides & insights","Guides & conseils","Guias & conselhos"))}</h1><p class="muted" style="font-size:19px">{L(X("Practical advice for hotels, clubs, developers and architects planning outdoor spaces.","Conseils pratiques pour hôtels, clubs, promoteurs et architectes qui aménagent des espaces extérieurs.","Conselhos práticos para hotéis, clubes, promotores e arquitetos que planeiam espaços exteriores."))}</p></div></div>'
    s += f'<a class="feat" href="{url("blog/" + ART["slug"])}" style="text-decoration:none;color:var(--tx)">{img(ART["img"], L(ART["title"]), lazy=False)}<div class="b"><span class="w" style="font-size:13px;font-weight:700;color:var(--ac);letter-spacing:.1em">{L(ART["cat"])}</span><h2 style="font-size:36px">{L(ART["title"])}</h2><p class="muted">{L(ART["lead"])}</p><span style="font-weight:700;color:var(--ac)">{L(X("Read the guide →","Lire le guide →","Ler o guia →"))}</span></div></a>'
    nxt = [X('EN 1176 explained: what makes a playground certified','EN 1176 expliquée : ce qui rend une aire de jeux certifiée','EN 1176 explicada: o que torna um parque certificado'), X('Outdoor equipment by the sea: choosing materials that last','Équipements en bord de mer : choisir des matériaux durables','Equipamentos junto ao mar: escolher materiais que duram'), X('How many pallets fit in a 40-foot container?','Combien de palettes dans un conteneur 40 pieds ?','Quantas paletes cabem num contentor de 40 pés?')]
    s += f'<section class="sec" style="padding-top:56px"><h2 style="font-size:24px;margin-bottom:16px">{L(X("Coming soon","Bientôt","Em breve"))}</h2><div class="g3">' + ''.join(f'<div class="card" style="padding:24px"><h3>{L(t)}</h3></div>' for t in nxt) + '</div></section></div>'
    s += cta()
    return (L(X('Blog — guides for outdoor projects | Permanent Summer Spaces','Blog — guides pour vos projets extérieurs | Permanent Summer Spaces','Blog — guias para projetos exteriores | Permanent Summer Spaces')), L(X('Guides on padel court costs, playground standards and outdoor equipment for hotels, clubs and developers.','Guides sur le coût d’un terrain de padel, les normes des aires de jeux et les équipements extérieurs.','Guias sobre custos de campos de padel, normas de parques infantis e equipamentos exteriores.')), s, None)

def page_article():
    slug = 'blog/' + ART['slug']
    s = header(slug, 'blog')
    nb = lambda v: v if lang == 'en' else v.replace(',', ' ')
    rows = [('Olimpia', X('Classic, 10 mm glass','Classique, verre 10 mm','Clássico, vidro 10 mm'), '21,040'), ('Panoramix', X('Panoramic, 12 mm glass','Panoramique, verre 12 mm','Panorâmico, vidro 12 mm'), '23,570'), ('Brutux', X('Reinforced panoramic','Panoramique renforcé','Panorâmico reforçado'), '26,820')]
    tbl = f'<table><thead><tr><th>{L(X("Model","Modèle","Modelo"))}</th><th>{L(X("Type","Type","Tipo"))}</th><th>{L(X("From (excl. VAT)","Dès (HT)","Desde (sem IVA)"))}</th></tr></thead><tbody>' + ''.join(f'<tr><td><b>{a}</b></td><td>{L(b)}</td><td>€{nb(c)}</td></tr>' for a, b, c in rows) + '</tbody></table>'
    body = {
     'en': f'''<p>“How much is a padel court?” is the first question every hotel, club and developer asks us. The honest answer: the court itself is only part of the budget. Here is every cost line, with the prices we actually quote.</p>
<h2>1. The court</h2><p>A complete court includes the steel structure, tempered glass, mesh, 8 LED floodlights, 2 entrances and textured turf with silica. Prices are per court, ex-works Spain:</p>{tbl}
<p>Panoramic courts cost more but look premium and give spectators a clear view. Near the sea or on windy sites, the reinforced Brutux with anti-corrosion paint is the safer choice.</p>
<h2>2. Installation</h2><p>You can use your own contractor (supply only) or ask for supervised installation: two specialists from the manufacturer install the court with your local crew. We quote supervision at <b>€2,875 per court</b>, travel and accommodation excluded.</p>
<h2>3. A cover (optional)</h2><p>A cover turns a court into a year-round business. An aluminium One-Pro cover starts at <b>€59,800</b>, the larger One-Pro XL at <b>€64,690</b>, plus assembly of about <b>€5,750</b> per cover. A shading flap adds <b>€6,900</b>. Allow 2–4 months of production.</p>
<h2>4. What is not in the price</h2><ul><li><b>Foundations:</b> a flat concrete slab with a slight slope. Cost depends on your site; get a local quote.</li><li><b>Transport:</b> courts ship in containers from Valencia. We quote freight to your exact port or site.</li><li><b>Unloading:</b> a crane on delivery day, arranged by the client.</li><li><b>Import duties and VAT:</b> depend on your country.</li></ul>
<h2>5. A realistic example</h2><p>Two panoramic courts with supervised installation, no cover: about <b>€52,900 – €55,500</b> excl. VAT, ex-works, before slab, transport and duties.</p>
<div class="note">Prices are indicative, excl. VAT and may change with steel and glass prices. Use the <a href="{url('padel')}#estimator">padel estimator</a> for your own configuration, then ask us for a firm quote including transport.</div>''',
     'fr': f'''<p>« Combien coûte un terrain de padel ? » C’est la première question de chaque hôtel, club et promoteur. La réponse honnête : le terrain n’est qu’une partie du budget. Voici chaque poste, avec les prix que nous proposons réellement.</p>
<h2>1. Le terrain</h2><p>Un terrain complet comprend la structure acier, le verre trempé, le grillage, 8 projecteurs LED, 2 entrées et le gazon texturé avec silice. Prix par terrain, départ usine Espagne :</p>{tbl}
<p>Les terrains panoramiques coûtent plus cher mais font plus premium et offrent une vue dégagée aux spectateurs. En bord de mer ou sur un site venteux, le Brutux renforcé avec peinture anticorrosion est le choix le plus sûr.</p>
<h2>2. L’installation</h2><p>Vous pouvez faire appel à votre entreprise (fourniture seule) ou demander une installation supervisée : deux spécialistes du fabricant montent le terrain avec votre équipe locale. Nous chiffrons la supervision à <b>2 875 € par terrain</b>, déplacement et hébergement exclus.</p>
<h2>3. Une couverture (option)</h2><p>Une couverture transforme un terrain en activité à l’année. Une couverture aluminium One-Pro démarre à <b>59 800 €</b>, la One-Pro XL à <b>64 690 €</b>, plus environ <b>5 750 €</b> de montage par couverture. Un volet d’ombrage ajoute <b>6 900 €</b>. Comptez 2 à 4 mois de fabrication.</p>
<h2>4. Ce qui n’est pas compris</h2><ul><li><b>Fondations :</b> une dalle béton plane avec une légère pente. Le coût dépend de votre site ; demandez un devis local.</li><li><b>Transport :</b> expédition en conteneurs depuis Valence. Nous chiffrons le fret jusqu’à votre port ou site.</li><li><b>Déchargement :</b> une grue le jour de la livraison, à la charge du client.</li><li><b>Droits et TVA :</b> selon votre pays.</li></ul>
<h2>5. Un exemple réaliste</h2><p>Deux terrains panoramiques avec installation supervisée, sans couverture : environ <b>52 900 – 55 500 €</b> HT, départ usine, hors dalle, transport et droits.</p>
<div class="note">Prix indicatifs, HT, susceptibles d’évoluer avec le prix de l’acier et du verre. Utilisez l’<a href="{url('padel')}#estimator">estimateur padel</a> pour votre configuration, puis demandez-nous un devis ferme transport compris.</div>''',
     'pt': f'''<p>“Quanto custa um campo de padel?” é a primeira pergunta de cada hotel, clube e promotor. A resposta honesta: o campo é só uma parte do orçamento. Eis cada custo, com os preços que realmente apresentamos.</p>
<h2>1. O campo</h2><p>Um campo completo inclui estrutura em aço, vidro temperado, rede, 8 projetores LED, 2 entradas e relva texturada com sílica. Preços por campo, à saída de fábrica em Espanha:</p>{tbl}
<p>Os campos panorâmicos custam mais, mas têm um aspeto premium e dão aos espectadores uma vista desafogada. Junto ao mar ou em locais com vento, o Brutux reforçado com pintura anticorrosão é a escolha mais segura.</p>
<h2>2. Instalação</h2><p>Pode usar o seu empreiteiro (só fornecimento) ou pedir instalação supervisionada: dois especialistas do fabricante montam o campo com a sua equipa local. A supervisão custa <b>2 875 € por campo</b>, sem viagem e alojamento.</p>
<h2>3. Uma cobertura (opcional)</h2><p>Uma cobertura transforma o campo num negócio para todo o ano. A cobertura One-Pro em alumínio começa nos <b>59 800 €</b>, a One-Pro XL nos <b>64 690 €</b>, mais cerca de <b>5 750 €</b> de montagem por cobertura. Uma aba de sombra acrescenta <b>6 900 €</b>. Conte com 2 a 4 meses de produção.</p>
<h2>4. O que não está incluído</h2><ul><li><b>Fundações:</b> uma laje de betão plana com ligeira pendente. O custo depende do local; peça um orçamento local.</li><li><b>Transporte:</b> envio em contentores a partir de Valência. Orçamentamos o frete até ao seu porto ou local.</li><li><b>Descarga:</b> uma grua no dia da entrega, a cargo do cliente.</li><li><b>Direitos e IVA:</b> dependem do seu país.</li></ul>
<h2>5. Um exemplo realista</h2><p>Dois campos panorâmicos com instalação supervisionada, sem cobertura: cerca de <b>52 900 – 55 500 €</b> sem IVA, à saída de fábrica, sem laje, transporte e direitos.</p>
<div class="note">Preços indicativos, sem IVA, sujeitos a variação com o preço do aço e do vidro. Use o <a href="{url('padel')}#estimator">estimador de padel</a> para a sua configuração e peça-nos um orçamento firme com transporte.</div>'''}[lang]
    s += f'<div class="wrap"><div class="crumb"><a href="{url("")}">{L(C["home"])}</a> / <a href="{url("blog")}">{L(C["blog"])}</a></div><article class="art" style="padding-top:32px"><span style="font-size:13px;font-weight:700;color:var(--ac);letter-spacing:.1em">{L(ART["cat"])}</span><h1 style="margin:12px 0 18px;font-size:clamp(34px,4.5vw,54px)">{L(ART["title"])}</h1><p class="muted" style="font-size:20px">{L(ART["lead"])}</p>{img(ART["img"], L(ART["title"]), lazy=False)}<div style="height:28px"></div>{body}</article></div>'
    s += cta()
    return (f'{L(ART["title"])} | Permanent Summer Spaces', L(ART['lead']), s, None)

def page_about():
    s = header('about', 'about')
    s += f'''<div class="wrap" style="padding-top:40px"><div class="phero" style="padding-top:0"><div class="txt"><span class="pill">{L(C['about'])}</span><h1>{L(X('European quality, delivered where you build.','La qualité européenne, livrée là où vous construisez.','Qualidade europeia, entregue onde constrói.'))}</h1>
<p>{L(X('Permanent Summer Spaces is the outdoor equipment division of Permanent Summer Lda, a Portuguese company based in Altura, Algarve. We work with established manufacturers in Spain, Portugal, France, Italy and Germany to supply certified equipment to hotels, clubs, developers and public bodies in Europe, Mauritius and the Indian Ocean.','Permanent Summer Spaces est la division équipements extérieurs de Permanent Summer Lda, société portugaise basée à Altura, en Algarve. Nous travaillons avec des fabricants reconnus en Espagne, au Portugal, en France, en Italie et en Allemagne pour fournir des équipements certifiés aux hôtels, clubs, promoteurs et collectivités en Europe, à Maurice et dans l’océan Indien.','A Permanent Summer Spaces é a divisão de equipamentos exteriores da Permanent Summer Lda, empresa portuguesa sediada em Altura, no Algarve. Trabalhamos com fabricantes reconhecidos em Espanha, Portugal, França, Itália e Alemanha para fornecer equipamentos certificados a hotéis, clubes, promotores e entidades públicas na Europa, na Maurícia e no Oceano Índico.'))}</p></div>{img('park','Public playground', lazy=False)}</div></div>'''
    vals = [(X('One contact, end to end','Un seul interlocuteur','Um contacto do início ao fim'), X('Specification, production follow-up, export logistics and installation, in English, French and Portuguese.','Spécification, suivi de fabrication, logistique export et installation, en anglais, français et portugais.','Especificação, acompanhamento da produção, logística de exportação e instalação, em inglês, francês e português.')),
            (X('Manufacturers we know','Des fabricants que nous connaissons','Fabricantes que conhecemos'), X('We only work with certified European factories whose products we have specified and installed.','Nous travaillons uniquement avec des usines européennes certifiées dont nous connaissons les produits.','Trabalhamos só com fábricas europeias certificadas cujos produtos conhecemos.')),
            (X('Islands and coasts','Îles et littoral','Ilhas e litoral'), X('Experience with shipping, customs and installation in Mauritius and coastal sites.','Expérience du transport, de la douane et de l’installation à Maurice et en bord de mer.','Experiência em transporte, alfândega e instalação na Maurícia e em zonas costeiras.')),
            (X('Partners & resellers','Partenaires & revendeurs','Parceiros & revendedores'), X('We work with local agents and distributors. Interested? Get in touch.','Nous travaillons avec des agents et distributeurs locaux. Intéressé ? Contactez-nous.','Trabalhamos com agentes e distribuidores locais. Interessado? Contacte-nos.'))]
    s += '<section class="sec"><div class="wrap g4 why">' + ''.join(f'<div><h3>{L(a)}</h3><p>{L(b)}</p></div>' for a, b in vals) + f'</div></section><div class="wrap" style="padding-top:40px">{logos()}</div>' + cta()
    return (L(X('About | Permanent Summer Spaces','À propos | Permanent Summer Spaces','Sobre nós | Permanent Summer Spaces')), L(X('Permanent Summer Spaces supplies certified European outdoor equipment from Portugal to Europe, Mauritius and the Indian Ocean.','Permanent Summer Spaces fournit des équipements extérieurs européens certifiés, du Portugal à l’Europe, Maurice et l’océan Indien.','A Permanent Summer Spaces fornece equipamentos exteriores europeus certificados, de Portugal para a Europa, Maurícia e Oceano Índico.')), s, None)

def page_contact():
    s = header('contact', 'contact')
    W = [(X('Hotel / resort','Hôtel / resort','Hotel / resort'), X('Kids club, padel, fitness','Mini-club, padel, fitness','Kids club, padel, fitness')), (X('Padel / sports club','Club de padel / sport','Clube de padel / desporto'), X('Courts, covers, turf, stands','Terrains, couvertures, gazon, tribunes','Campos, coberturas, relva, bancadas')),
         (X('Developer / architect','Promoteur / architecte','Promotor / arquiteto'), X('Residential or mixed-use','Résidentiel ou mixte','Residencial ou misto')), (X('School','École','Escola'), X('Playgrounds and sport','Aires de jeux et sport','Parques e desporto')),
         (X('Public sector','Secteur public','Setor público'), X('Parks, tenders, cities','Parcs, appels d’offres, villes','Parques, concursos, cidades')), (X('Reseller / agent','Revendeur / agent','Revendedor / agente'), X('Become a partner','Devenir partenaire','Tornar-se parceiro'))]
    who = ''.join(f'<button type="button" data-who="{esc(L(a))}" aria-pressed="false"><b>{L(a)}</b><span>{L(b)}</span></button>' for a, b in W)
    prods = ''.join(f'<button type="button" data-prod="{esc(L(p["name"]))}" data-slug="{p["slug"]}" aria-pressed="false"><i aria-hidden="true"></i>{L(p["name"])}</button>' for p in PRODUCTS)
    prods += f'<button type="button" data-prod="{L(X("Not sure yet","Je ne sais pas encore","Ainda não sei"))}" aria-pressed="false"><i aria-hidden="true"></i>{L(X("Not sure yet","Je ne sais pas encore","Ainda não sei"))}</button>'
    chips = lambda k, vals: '<div class="chipsel">' + ''.join(f'<button type="button" data-k="{k}" data-v="{esc(L(v))}" aria-pressed="false">{L(v)}</button>' for v in vals) + '</div>'
    when = [X('Within 3 months','Sous 3 mois','Em 3 meses'), X('3–6 months','3–6 mois','3–6 meses'), X('6–12 months','6–12 mois','6–12 meses'), X('Just exploring','Je me renseigne','Só a explorar')]
    svc = [X('Supply only','Fourniture seule','Só fornecimento'), X('Supply + installation','Fourniture + installation','Fornecimento + instalação'), X('Not sure yet','Je ne sais pas encore','Ainda não sei')]
    bud = [X('Under €25k','Moins de 25 k€','Menos de 25 mil €'), X('€25–100k','25–100 k€','25–100 mil €'), X('€100–250k','100–250 k€','100–250 mil €'), X('€250k+','250 k€ +','250 mil € +')]
    stl = [X('Who you are','Qui vous êtes','Quem é'), X('What you need','Vos besoins','O que precisa'), X('Your project','Votre projet','O seu projeto'), X('Your details','Vos coordonnées','Os seus dados')]
    st = lambda n: L(X(f'STEP {n} OF 4', f'ÉTAPE {n} SUR 4', f'PASSO {n} DE 4'))
    fld = lambda id_, lab, typ, ph, full='': f'<label class="fld {full}" for="{id_}">{L(lab)}<input id="{id_}" type="{typ}" placeholder="{esc(L(ph))}" autocomplete="{ {"f_name":"name","f_company":"organization","f_email":"email","f_phone":"tel"}.get(id_,"off") }"></label>'
    nx = [(X('Within 48 hours:','Sous 48 heures :','Em 48 horas:'), X('a first proposal with product options and indicative prices.','une première proposition avec options produits et prix indicatifs.','uma primeira proposta com opções de produtos e preços indicativos.')), (X('Then:','Ensuite :','Depois:'), X('technical sheets, certificates and a layout for your site.','fiches techniques, certificats et implantation pour votre site.','fichas técnicas, certificados e implantação para o seu local.')), (X('If useful:','Si besoin :','Se útil:'), X('a short call or WhatsApp to fine-tune the project.','un court appel ou WhatsApp pour affiner le projet.','uma chamada curta ou WhatsApp para afinar o projeto.'))]
    s += f'''<div class="gf" id="gf"><div class="side"><div style="display:flex;flex-direction:column;gap:12px"><span style="font-size:13px;font-weight:700;letter-spacing:.14em;color:var(--soft)">{L(C['start']).upper()}</span><h1 style="font-size:36px">{L(X('Tell us about your space.','Parlez-nous de votre espace.','Fale-nos do seu espaço.'))}</h1><p>{L(X('4 quick steps. You get a first proposal with product options and indicative prices within 48 hours.','4 étapes rapides. Vous recevez une première proposition avec options et prix indicatifs sous 48 heures.','4 passos rápidos. Recebe uma primeira proposta com opções e preços indicativos em 48 horas.'))}</p></div>
<ol class="steps">''' + ''.join(f'<li><i>{i+1}</i>{L(x)}</li>' for i, x in enumerate(stl)) + f'''</ol>
<div class="ct"><b>{L(X('Prefer to talk?','Vous préférez parler ?','Prefere falar?'))}</b><a href="mailto:spaces@permanentsummer.co">spaces@permanentsummer.co</a><a href="https://wa.me/351924477353">+351 924 477 353 · WhatsApp</a></div></div>
<div class="main"><div class="bar"><i style="width:25%"></i></div>
<div class="step on" data-step="1"><span class="n">{st(1)}</span><h2>{L(X('Who are you?','Qui êtes-vous ?','Quem é?'))}</h2><div class="choice">{who}</div></div>
<div class="step" data-step="2"><span class="n">{st(2)}</span><h2>{L(X('What do you need?','De quoi avez-vous besoin ?','O que precisa?'))}</h2><p class="muted">{L(X('Choose one or more.','Choisissez un ou plusieurs.','Escolha um ou mais.'))}</p><div class="checks">{prods}</div></div>
<div class="step" data-step="3"><span class="n">{st(3)}</span><h2>{L(X('About the project','Le projet','Sobre o projeto'))}</h2>
{fld('f_site', X('Where is the site?','Où se trouve le site ?','Onde fica o local?'), 'text', X('City, country','Ville, pays','Cidade, país'))}
<div class="fld">{L(X('When do you need it?','Pour quand ?','Para quando?'))}{chips('when', when)}</div>
<div class="fld">{L(X('What service do you need?','Quel service ?','Que serviço?'))}{chips('svc', svc)}</div>
<div class="fld">{L(X('Budget range (optional)','Budget (facultatif)','Orçamento (opcional)'))}{chips('budget', bud)}</div></div>
<div class="step" data-step="4"><span class="n">{st(4)}</span><h2>{L(X('How can we reach you?','Comment vous joindre ?','Como o contactamos?'))}</h2><div class="f2">
{fld('f_name', X('Name','Nom','Nome'), 'text', X('Your name','Votre nom','O seu nome'))}{fld('f_company', X('Company','Société','Empresa'), 'text', X('Hotel, club, firm…','Hôtel, club, entreprise…','Hotel, clube, empresa…'))}
{fld('f_email', X('Email','E-mail','E-mail'), 'email', X('you@company.com','vous@societe.com','voce@empresa.com'))}{fld('f_phone', X('Phone / WhatsApp','Téléphone / WhatsApp','Telefone / WhatsApp'), 'tel', X('+351 …','+33 …','+351 …'))}
<label class="fld full" for="f_msg">{L(X('Anything else? (optional)','Autre chose ? (facultatif)','Mais alguma coisa? (opcional)'))}<textarea id="f_msg" rows="4" placeholder="{esc(L(X('Site size, quantities, plans you can share…','Surface, quantités, plans…','Área, quantidades, plantas…')))}"></textarea></label></div></div>
<div class="step" data-step="5"><div class="fin"><span class="ok" aria-hidden="true">✓</span><h2>{L(X('Thank you, almost done.','Merci, c’est presque fini.','Obrigado, está quase.'))}</h2>
<p class="muted">{L(X('Your email app has opened with your request. Just press send. No email app? Send it on WhatsApp instead:','Votre messagerie s’est ouverte avec votre demande : il suffit d’envoyer. Pas de messagerie ? Envoyez-la sur WhatsApp :','A sua aplicação de e-mail abriu com o pedido: basta enviar. Sem e-mail? Envie por WhatsApp:'))} <a id="waLink" href="https://wa.me/351924477353" style="font-weight:700">WhatsApp →</a></p>
<p><b id="sum"></b></p>''' + ''.join(f'<div class="nx"><i>{i+1}</i><span><b>{L(a)}</b> {L(b)}</span></div>' for i, (a, b) in enumerate(nx)) + f'''</div></div>
<p class="err" id="err" role="alert"></p>
<div class="navb"><button type="button" class="back" id="back">← {L(X('Back','Retour','Voltar'))}</button><button type="button" class="btn" id="next">→</button></div></div></div>'''
    T = {'f_next': L(X('Continue →','Continuer →','Continuar →')), 'f_send': L(X('Send my request','Envoyer ma demande','Enviar pedido')),
         'e_prod': L(X('Choose at least one product.','Choisissez au moins un produit.','Escolha pelo menos um produto.')),
         'e_proj': L(X('Please choose a timing and a service.','Choisissez un délai et un service.','Escolha um prazo e um serviço.')),
         'e_contact': L(X('Please enter your name and a valid email.','Indiquez votre nom et un e-mail valide.','Indique o seu nome e um e-mail válido.')),
         'k_who': L(X('Profile','Profil','Perfil')), 'k_need': L(X('Products','Produits','Produtos')), 'k_site': L(X('Site','Site','Local')), 'k_when': L(X('Timing','Délai','Prazo')),
         'k_svc': L(X('Service','Service','Serviço')), 'k_budget': L(X('Budget','Budget','Orçamento')), 'k_name': L(X('Name','Nom','Nome')), 'k_company': L(X('Company','Société','Empresa')), 'k_phone': L(X('Phone','Téléphone','Telefone'))}
    return (L(X('Start a project | Permanent Summer Spaces','Démarrer un projet | Permanent Summer Spaces','Iniciar um projeto | Permanent Summer Spaces')), L(X('Tell us about your outdoor project in 4 quick steps and get a first proposal within 48 hours.','Décrivez votre projet extérieur en 4 étapes et recevez une première proposition sous 48 heures.','Descreva o seu projeto exterior em 4 passos e receba uma primeira proposta em 48 horas.')), s, T)

# ------------------------------------------------------------------ build
def write(slug, fn):
    title, desc, body, T = fn()
    extra = ''
    if slug == '':
        extra = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "Organization", "name": "Permanent Summer Spaces",
            "parentOrganization": {"@type": "Organization", "name": "Permanent Summer Lda", "url": SITE + "/"}, "url": SITE + "/spaces/", "email": "spaces@permanentsummer.co",
            "telephone": "+351924477353", "address": {"@type": "PostalAddress", "addressLocality": "Altura", "addressRegion": "Algarve", "addressCountry": "PT"}}) + '</script>'
    out = head(title, desc, slug, extra) + body + footer(T)
    path = os.path.join(ROOT, url(slug).strip('/'), 'index.html')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(out)
    return url(slug)

PAGES = [('', page_home)] + [(p['slug'], (lambda p=p: page_product(p))) for p in PRODUCTS] + [('projects', page_projects), ('blog', page_blog), ('blog/' + ART['slug'], page_article), ('about', page_about), ('contact', page_contact)]
urls = []
for lg in LANGS:
    lang = lg
    for slug, fn in PAGES:
        urls.append(write(slug, fn))
json.dump(urls, open(os.path.join(ROOT, '_build', 'spaces-urls.json'), 'w'), indent=0)
print(len(urls), 'pages')
