#                              --- SELECTORI PROPRIETATI ---

STATUS_PROPRIETATE = [
    ('Activă', 'Activă'), ('Incompletă', 'Incompletă'), ('Retrasă', 'Retrasă'), ('Pierdută', 'Pierdută')
]

TIP_PROPRIETATE = [
    ('apartment', 'Apartament'), ('house', 'Casă'), ('terrain', 'Teren'), ('commercial_space', 'Spațiu comercial'),
    ('office_space', 'Spațiu de birouri'), ('industrial_space', 'Spațiu industrial')
]

TIP_TRANZACTIE = [
    ('Vânzare', 'Vânzare'), ('Închiriere', 'Închiriere')
]

TIP_PROPRIETAR = [
    ('Persoană fizică', 'Persoană fizică'), ('Persoană juridică', 'Persoană juridică')
]

MONEDA = [
    ('euro', '€'), ('lei', 'RON'),
]

COTA_TVA = [
    ('Nu se aplică TVA', 'Nu se aplică TVA'), ('TVA inclus', 'TVA inclus'), ('+ 9% TVA', '+ 9% TVA'),
    ('+ 19% TVA', '+ 19% TVA'),
]

TIP_IMOBIL_ANSAMBLU = [
    ('Bloc de apartamente', 'Bloc de apartamente'), ('Bloc de garsoniere', 'Bloc de garsoniere'),
    ('Bloc mixt', 'Bloc mixt'), ('Vilă de apartamente', 'Vilă de apartamente'), ('Case / Vile', 'Case / Vile')
]

TIP_APARTAMENT = [
    ('Apartament', 'Apartament'), ('Garsonieră', 'Garsonieră'), ('Penthouse', 'Penthouse')
]

DESTINATIE_AP = [
    ('Rezidențială', 'Rezidențială'), ('Comercială', 'Comercială'), ('Birouri', 'Birouri')
]

COMPARTIMENTARE_AP = [
    ('Decomandat', 'Decomandat'),
    ('Semidecomandat', 'Semidecomandat'),
    ('Nedecomandat', 'Nedecomandat'),
    ('Circular', 'Circular'),
    ('Vagon', 'Vagon')
]

ETAJ_AP = [
    ('Demisol', 'Demisol'), ('Parter', 'Parter'), ('Parter înalt', 'Parter înalt'), ('1', '1'), ('2', '2'), ('3', '3'),
    ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'),
    ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'),
    ('Mansardă', 'Mansardă'), ('Ultimele 2 etaje', 'Ultimele 2 etaje')
]

ORIENTARE = [
    ('Nord', 'Nord'), ('Sud', 'Sud'), ('Vest', 'Vest'), ('Est', 'Est'),
    ('Nord-Vest', 'Nord-Vest'), ('Nord-Est', 'Nord-Est'), ('Sud-Vest', 'Sud-Vest'), ('Sud-Est', 'Sud-Est'),
    ('Nord-Sud', 'Nord-Sud'), ('Vest-Est', 'Vest-Est')
]

CONFORT = [
    ('Lux', 'Lux'), ('1', '1'), ('2', '2'), ('3', '3')
]

FINISAJE = [
    ('Finisat modern', 'Finisat modern'), ('Finisat', 'Finisat'), ('Finisat clasic', 'Finisat clasic'),
    ('Semifinisat', 'Semifinisat'), ('Necesită renovare', 'Necesită renovare'), ('Nefinisat', 'Nefinisat')
]

TIP_IMOBIL_AP = [
    ('Bloc de apartamente', 'Bloc de apartamente'), ('Bloc de garsoniere', 'Bloc de garsoniere'),
    ('Bloc mixt', 'Bloc mixt'), ('Vilă de apartamente', 'Vilă de apartamente')
]

DOTARI = [
    ('Aer condiționat', 'Aer condiționat'), ('Aeroterme', 'Aeroterme'), ('Dressing', 'Dressing'),
    ('Jacuzzi', 'Jacuzzi'), ('Scară interioară', 'Scară interioară'), ('Șemineu', 'Șemineu'),
    ('Sistem de alarmă', 'Sistem de alarmă')
]

IZOLATII_TERMICE = [
    ('Izolație exterioară', 'Izolație exterioară'), ('Izolație interioară', 'Izolație interioară')
]

DOTARI_IMOBIL = [
    ('Acces persoane cu dizabilități', 'Acces persoane cu dizabilități'), ('Acoperiș', 'Acoperiș'),
    ('Interfon', 'Interfon'), ('Parcare biciclete', 'Parcare biciclete'), ('Pază', 'Pază'), ('Piscină', 'Piscină'),
    ('Spălătorie', 'Spălătorie'), ('Spații agrement', 'Spații agrement'), ('Supraveghere video', 'Supraveghere video'),
    ('Telecomandă poartă acces auto', 'Telecomandă poartă acces auto'),
    ('Telecomandă poartă garaj', 'Telecomandă poartă garaj'), ('Uscătorie', 'Uscătorie'),
    ('Videointerfon', 'Videointerfon')
]

PARCARE = [
    ('Garaj', 'Garaj'), ('Garaj subteran', 'Garaj subteran'), ('Parcare acoperită', 'Parcare acoperită'),
    ('Parcare deschisă', 'Parcare deschisă')
]

SISTEM_INCALZIRE = [
    ('Calorifere', 'Calorifere'), ('Centrală cu lemne', 'Centrală cu lemne'),
    ('Centrală cu peleți', 'Centrală cu peleți'), ('Centrală imobil', 'Centrală imobil'),
    ('Centrală proprie', 'Centrală proprie'), ('Încălzire diesel', 'Încălzire diesel'),
    ('Încălzire în pardoseală', 'Încălzire în pardoseală'), ('Pompă de căldură', 'Pompă de căldură'),
    ('Sobă / Teracotă', 'Sobă / Teracotă'), ('Termoficare', 'Termoficare'), ('Ventiloconvectoare', 'Ventiloconvectoare')
]

USA_INTRARE = [
    ('Ușă intrare lemn', 'Ușă intrare lemn'), ('Ușă intrare metal', 'Ușă intrare metal'),
    ('Ușă intrare pal', 'Ușă intrare pal'), ('Ușă intrare PVC', 'Ușă intrare PVC')
]

USI_INTERIOR = [
    ('Uși interior celulare', 'Uși interior celulare'), ('Uși interior lemn', 'Uși interior lemn'),
    ('Uși interior MDF', 'Uși interior MDF'), ('Uși interior cu panel', 'Uși interior cu panel'),
    ('Uși interior PVC', 'Uși interior PVC'), ('Uși interior sticlă', 'Uși interior sticlă')
]

MOBILIER = [
    ('Mobilat complet', 'Mobilat complet'), ('Mobilat lux', 'Mobilat lux'), ('Mobilat parțial', 'Mobilat parțial'),
    ('Nemobilat', 'Nemobilat')
]

BUCATARIE = [
    ('Bucătărie deschisă', 'Bucătărie deschisă'), ('Bucătărie închisă', 'Bucătărie închisă'),
    ('Bucătărie mobilată', 'Bucătărie mobilată'), ('Bucătărie parțial mobilată', 'Bucătărie parțial mobilată'),
    ('Bucătărie parțial utilată', 'Bucătărie parțial utilată'), ('Bucătărie utilată', 'Bucătărie utilată'),
    ('Chicinetă', 'Chicinetă')
]

FERESTRE = [
    ('Ferestre aluminiu', 'Ferestre aluminiu'), ('Ferestre lemn', 'Ferestre lemn'), ('Ferestre PVC', 'Ferestre PVC'),
    ('Geamuri cu izolație fonică', 'Geamuri cu izolație fonică'),
    ('Geamuri cu protecție UV', 'Geamuri cu protecție UV'), ('Geamuri termopan', 'Geamuri termopan'),
    ('Geamuri tripan', 'Geamuri tripan')
]

ALTE_SPATII = [
    ('Grădină proprie', 'Grădină proprie'), ('Boxă la subsol', 'Boxă la subsol'), ('Curte', 'Curte'),
    ('Curte comună', 'Curte comună'), ('Debara', 'Debara'), ('Lift', 'Lift'),
    ('Loc de joacă copii', 'Loc de joacă copii'), ('Magazie', 'Magazie'), ('Pivniță', 'Pivniță'),
    ('Zonă barbeque', 'Zonă barbeque')
]

STADIU_CONSTRUCTIE = [
    ('Finalizată', 'Finalizată'), ('La gri', 'La gri'), ('La roșu', 'La roșu'), ('Structură', 'Structură'),
    ('Proiect', 'Proiect'), ('În construcție', 'În construcție'), ('De demolat', 'De demolat')
]

MATERIALE = [
    ('Beton', 'Beton'), ('Cărămidă', 'Cărămidă'), ('BCA', 'BCA'), ('Metal', 'Metal'), ('Lemn', 'Lemn'),
    ('Altele', 'Altele'), ('Cadre', 'Cadre'), ('Plăci', 'Plăci'), ('Monolit', 'Monolit')
]

TIP_CASA = [
    ('Individuală', 'Individuală'), ('Vilă', 'Vilă'), ('Calcan', 'Calcan'),
    ('Duplex', 'Duplex'), ('Triplex', 'Triplex'), ('Înșiruită', 'Înșiruită')
]

ACOPERIS = [
    ('Tablă', 'Tablă'), ('Țiglă', 'Țiglă'), ('Șindrilă', 'Șindrilă'), ('Terasă', 'Terasă')
]

TIP_TEREN = [
    ('Construcții', 'Construcții'), ('Agricol', 'Agricol'), ('Pădure', 'Pădure')
]

DESTINATIE_TEREN = [
    ('Rezidențială', 'Rezidențială'), ('Comercială', 'Comercială'), ('Industrială', 'Industrială'),
    ('Agricolă', 'Agricolă'), ('Horeca / Retail', 'Horeca / Retail'), ('Spital / Clinică', 'Spital / Clinică'),
    ('Benzinărie', 'Benzinărie'), ('Spălătorie auto', 'Spălătorie auto'), ('De vacanță', 'De vacanță')
]

UNITATE_SUPRAFATA = [
    ('mp', 'mp'), ('ar', 'ar'), ('ha', 'ha')
]

CLASIFICARE_TEREN = [
    ('Intravilan', 'Intravilan'), ('Extravilan', 'Extravilan')
]

DESCHIDERE = [
    ('Șosea', 'Șosea'), ('Drum principal', 'Drum principal'), ('DN', 'DN'), ('Autostradă', 'Autostradă'),
    ('Șoseaua de centură', 'Șoseaua de centură'), ('Lac', 'Lac'), ('Pădure', 'Pădure'),
    ('Drum de servitute', 'Drum de servitute')
]

FACILITATI_TEREN = [
    ('Apă', 'Apă'), ('Canalizare', 'Canalizare'), ('Curent', 'Curent'), ('Gaz', 'Gaz'), ('Irigații', 'Irigații'),
    ('Utilități în zonă', 'Utilități în zonă')
]

ALTE_FACILITATI = [
    ('Acces auto', 'Acces auto'), ('Construcție demolabilă', 'Construcție demolabilă'), ('La șosea', 'La șosea'),
    ('Oportunitate de investiții', 'Oportunitate de investiții'), ('Parcelabil', 'Parcelabil'),
    ('Studiu Geo', 'Studiu Geo'), ('Teren împrejmuit', 'Teren împrejmuit')
]

TIP_IMOBIL_SPATIU = [
    ('Bloc de apartamente', 'Bloc de apartamente'), ('Clădire birouri', 'Clădire birouri'),
    ('Casă / Vilă', 'Casă / Vilă'), ('Centru comercial', 'Centru comercial'), ('Hală / Depozit', 'Hală / Depozit'),
    ('Stradal', 'Stradal')
]

TRAFIC_PIETONAL = [
    ('Intens', 'Intens'), ('Moderat', 'Moderat'), ('Fără trafic pietonal', 'Fără trafic pietonal')
]

COMPARTIMENTARE_SPATIU = [
    ('Open-space', 'Open-space'), ('Compartimentat', 'Compartimentat'),
    ('Parțial compartimentat', 'Parțial compartimentat'), ('Flexibil', 'Flexibil')
]

DESTINATIE_SP_COMERCIAL = [
    ('Comercială', 'Comercială'), ('Birouri', 'Birouri'), ('Horeca / Retail', 'Horeca / Retail'),
    ('Magazin prezentare', 'Magazin prezentare'), ('Showroom', 'Showroom'), ('Bancă', 'Bancă'),
    ('Farmacie', 'Farmacie')
]

ETAJ_SPATIU = [
    ('Demisol', 'Demisol'), ('Parter', 'Parter'), ('Parter înalt', 'Parter înalt'), ('Mezanin', 'Mezanin'), ('1', '1'),
    ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
    ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'),
    ('19', '19'), ('20', '20'), ('Mansardă', 'Mansardă'), ('Ultimele 2 etaje', 'Ultimele 2 etaje')
]

ELEMENTE_ECO = [
    ('Building management system', 'Building management system'),
    ('Certificare Green Building', 'Certificare Green Building'),
    ('Echipamente moderne / silențioase', 'Echipamente moderne / silențioase'),
    ('Fațadă ventilată', 'Fațadă ventilată'), ('Incărcător auto electrice', 'Incărcător auto electrice'),
    ('Panouri solare', 'Panouri solare'), ('Parcare biciclete', 'Parcare biciclete'),
    ('Sistem electric inteligent', 'Sistem electric inteligent'),
    ('Sistem inteligent ascensoare', 'Sistem inteligent ascensoare')
]

ALTE_FACILITATI_SP_COM = [
    ('Acces persoane cu dizabilități', 'Acces persoane cu dizabilități'),
    ('Acces secundar marfă', 'Acces secundar marfă'), ('Afișare logo pe clădire', 'Afișare logo pe clădire'),
    ('Centrală termică', 'Centrală termică'), ('Contorizare separată', 'Contorizare separată'),
    ('Grupuri sanitare amenajate și utilate', 'Grupuri sanitare amenajate și utilate'),
    ('Posibilitate terasă', 'Posibilitate terasă'), ('Sistem de alarmă', 'Sistem de alarmă'),
    ('Sistem de ventilație', 'Sistem de ventilație'), ('Vestiar', 'Vestiar')
]

CLASA_SP_BIROURI = [
    ('A', 'A'), ('B', 'B'), ('C', 'C')
]

SERVICII_ASIGURATE = [
    ('Acces persoane cu dizabilități', 'Acces persoane cu dizabilități'),
    ('Administrare și management imobiliar', 'Administrare și management imobiliar'),
    ('Afișare logo pe clădire', 'Afișare logo pe clădire'),
    ('Consumabile grupuri sociale', 'Consumabile grupuri sociale'), ('Contorizare separată', 'Contorizare separată'),
    ('Curățenie exterioară', 'Curățenie exterioară'), ('Curățenie parcare', 'Curățenie parcare'),
    ('Curățenie spații comune', 'Curățenie spații comune'), ('Îndepărtarea zăpezii', 'Îndepărtarea zăpezii'),
    ('Îngrijirea spațiilor verzi', 'Îngrijirea spațiilor verzi'), ('Salubritate', 'Salubritate'),
    ('Servicii de întreținere și reparații lifturi', 'Servicii de întreținere și reparații lifturi'),
    ('Sistem de ventilație', 'Sistem de ventilație'), ('Vestiar', 'Vestiar')
]

SIGURANTA_SECURITATE = [
    ('Acces securizat parcare', 'Acces securizat parcare'), ('Cameră server', 'Cameră server'), ('CCTV', 'CCTV'),
    ('Control acces securizat pe bază de cartele', 'Control acces securizat pe bază de cartele'),
    ('Control al accesului pe zone', 'Control al accesului pe zone'),
    ('Detectoare de fum / incendiu', 'Detectoare de fum / incendiu'),
    ('Extinctoare sprinkler', 'Extinctoare sprinkler'), ('Pază permanentă', 'Pază permanentă'),
    ('Recepție', 'Recepție'), ('Semaforizare parcare', 'Semaforizare parcare'),
    ('Server room cu rack, ventilație, control acces', 'Server room cu rack, ventilație, control acces'),
    ('Sistem de alarmă', 'Sistem de alarmă'), ('Sistem de evacuare', 'Sistem de evacuare'),
    ('Sisteme de securitate integrate BMS', 'Sisteme de securitate integrate BMS')
]

IT_C = [
    ('Internet', 'Internet'), ('Posibilitatea alegerii operator date', 'Posibilitatea alegerii operator date'),
    ('Posibilitatea alegerii operator telefonie', 'Posibilitatea alegerii operator telefonie'),
    ('Sistem modern de telecomunicații', 'Sistem modern de telecomunicații'), ('Telefon', 'Telefon')
]

SISTEM_ELECTRIC = [
    ('Control electric individual pe zona de birou', 'Control electric individual pe zona de birou'),
    ('Generator de urgență', 'Generator de urgență'),
    ('Necesită surse suplimentare de energie', 'Necesită surse suplimentare de energie'),
    ('Sursă principală de alimentare', 'Sursă principală de alimentare'), ('Sursa UPS', 'Sursa UPS')
]

ARHITECTURA = [
    ('Cortină de sticlă', 'Cortină de sticlă'), ('Ferestre care se deschid', 'Ferestre care se deschid'),
    ('Ferestre înclinate', 'Ferestre înclinate'), ('Gresie', 'Gresie'),
    ('Grupuri sanitare amenajate și utilate', 'Grupuri sanitare amenajate și utilate'),
    ('Lift cu destinație programată', 'Lift cu destinație programată'), ('Mochetă', 'Mochetă'), ('Parchet', 'Parchet'),
    ('Podea înălțată', 'Podea înălțată'), ('Post trafo', 'Post trafo'), ('Tavan fals', 'Tavan fals')
]

CLIMATIZARE_BIROU = [
    ('Aport de aer proaspăt', 'Aport de aer proaspăt'), ('Centrală termică', 'Centrală termică'),
    ('Control individual AC pentru fiecare zonă de birou', 'Control individual AC pentru fiecare zonă de birou'),
    ('Sistem climatizare 2 țevi', 'Sistem climatizare 2 țevi'),
    ('Sistem climatizare 4 țevi', 'Sistem climatizare 4 țevi'),
    ('Unități Split', 'Unități Split'), ('Ventilație mecanică', 'Ventilație mecanică')
]

FACILITATI_CLADIRE_PROXIMITATI = [
    ('Stație de autobuz în apropiere', 'Stație de autobuz în apropiere'), ('Cafenea la parter', 'Cafenea la parter'),
    ('Centru comercial în apropiere', 'Centru comercial în apropiere'),
    ('Restaurant în clădire', 'Restaurant în clădire'),
    ('Stație de metrou în apropiere', 'Stație de metrou în apropiere'),
    ('Stație de tramvai în apropiere', 'Stație de tramvai în apropiere')
]

TIP_SP_INDUSTRIAL = [
    ('Producție grea', 'Producție grea'), ('Producție ușoară', 'Producție ușoară'),
    ('Depozit distribuție', 'Depozit distribuție'), ('Depozit general', 'Depozit general'),
    ('Cercetare și dezvoltare', 'Cercetare și dezvoltare'), ('Centru de date', 'Centru de date'),
    ('Showroom', 'Showroom')
]

DESTINATIE_SP_INDUSTRIAL = [
    ('Producție', 'Producție'), ('Depozitare', 'Depozitare'), ('Prezentare', 'Prezentare')
]

ETAJ_SP_INDUSTRIAL = [
    ('Demisol', 'Demisol'), ('Parter', 'Parter'), ('Parter înalt', 'Parter înalt'),
    ('1', '1'), ('2', '2'), ('3', '3'), ('Mansardă', 'Mansardă')
]

ALTE_FACILITATI_SP_IND = [
    ('Acces auto', 'Acces auto'), ('Acces camion', 'Acces camion'),
    ('Construcție demolabilă', 'Construcție demolabilă'), ('Curent trifazic (380V)', 'Curent trifazic (380V)'),
    ('La șosea', 'La șosea'), ('Luminatoare', 'Luminatoare'),
    ('Oportunitate de investiții', 'Oportunitate de investiții'), ('Panouri solare', 'Panouri solare'),
    ('Pod rulant', 'Pod rulant'), ('Posibilitate de compartimentare', 'Posibilitate de compartimentare'),
    ('Sistem de alarmă', 'Sistem de alarmă'), ('Teren împrejmuit', 'Teren împrejmuit'),
    ('Uși de acces', 'Uși de acces'), ('Vestiar', 'Vestiar')
]

JUDETE = [
    ('Alba', 'Alba'), ('Argeș', 'Argeș'), ('Arad', 'Arad'), ('București', 'București'), ('Bacău', 'Bacău'),
    ('Bihor', 'Bihor'), ('Bistrița-Năsăud', 'Bistrița-Năsăud'), ('Brăila', 'Brăila'), ('Botoșani', 'Botoșani'),
    ('Brașov', 'Brașov'), ('Buzău', 'Buzău'), ('Cluj', 'Cluj'), ('Călărași', 'Călărași'),
    ('Caraș-Severin', 'Caraș-Severin'), ('Constanța', 'Constanța'), ('Covasna', 'Covasna'), ('Dâmbovița', 'Dâmbovița'),
    ('Dolj', 'Dolj'), ('Gorj', 'Gorj'), ('Galați', 'Galați'), ('Giurgiu', 'Giurgiu'), ('Hunedoara', 'Hunedoara'),
    ('Harghita', 'Harghita'), ('Ilfov', 'Ilfov'), ('Ialomița', 'Ialomița'), ('Iași', 'Iași'), ('Mehedinți', 'Mehedinți'),
    ('Maramureș', 'Maramureș'), ('Mureș', 'Mureș'), ('Neamț', 'Neamț'), ('Olt', 'Olt'), ('Prahova', 'Prahova'),
    ('Sibiu', 'Sibiu'), ('Sălaj', 'Sălaj'), ('Satu-Mare', 'Satu-Mare'), ('Suceava', 'Suceava'), ('Tulcea', 'Tulcea'),
    ('Timiș', 'Timiș'), ('Teleorman', 'Teleorman'), ('Vâlcea', 'Vâlcea'), ('Vrancea', 'Vrancea'), ('Vaslui', 'Vaslui')
]
