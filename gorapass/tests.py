import json

from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.test import Client, TestCase

from gorapass.models import Hikes, Stamps, CompletedHikes, CompletedStamps

TEST_STAMPS = [
  {
    "id": 1,
    "stage_number": 18,
    "spp_number": "17",
    "stamp_name": "Kocbekov dom na Korošici",
    "elevation": 1808,
    "elevation_unit": "m",
    "alpine_club": "Celje-Matica",
    "region": "Kamnik",
    "route_type": "Main",
    "lat": 46.35612316,
    "lon": 14.63936863,
    "completed_at_date": "1970-01-01"
  },
    {
    "id": 2,
    "stage_number": 2,
    "spp_number": "2",
    "stamp_name": "Mariborska Koča",
    "elevation": 1068,
    "elevation_unit": "m",
    "alpine_club": "Maribor -- Matica",
    "region": "Pohorje",
    "route_type": "Main",
    "lat": 46.50480045,
    "lon": 15.55446938,
    "completed_at_date": "1970-01-01"
  },
  {
    "id": 3,
    "stage_number": 3,
    "spp_number": "3",
    "stamp_name": "Ruška koča",
    "elevation": 1250,
    "elevation_unit": "m",
    "alpine_club": "Ruše",
    "region": "Pohorje",
    "route_type": "Main",
    "lat": 46.49609727,
    "lon": 15.50826703,
    "completed_at_date": "1970-01-01"
  },
  {
    "id": 4,
    "stage_number": 4,
    "spp_number": "4",
    "stamp_name": "Klopni vrh",
    "elevation": 1340,
    "elevation_unit": "m",
    "alpine_club": "Lovrenc na Pohorju",
    "region": "Pohorje",
    "route_type": "Main",
    "lat": 46.50128609,
    "lon": 15.39536944,
    "completed_at_date": "1970-01-01"
  },
  {
    "id": 5,
    "stage_number": 5,
    "spp_number": "5",
    "stamp_name": "Koča na Pesku",
    "elevation": 1386,
    "elevation_unit": "m",
    "alpine_club": "Oplotnica",
    "region": "Kamnik",
    "route_type": "Main",
    "lat": 46.46751022,
    "lon": 15.34388541,
    "completed_at_date": "1970-01-01"
  },


]

TEST_HIKES = [
    # Hikes for test stamp 1: "Kocbekov dom na Korošici"
    {
        "id": 1,
        "stamp": 1,
        "hike_name": "Planina Podvežak - Kocbekov dom na Korošici",
        "hike_link": "https://www.hribi.net/izlet/planina_podvezak_kocbekov_dom_na_korosici/3/199/237",
        "starting_point": "Planina Podvežak",
        "starting_point_elevation": 1500,
        "starting_point_elevation_units": "m",
        "lat_start": 46.3319,
        "lon_start": 14.6726,
        "ending_point": "Kocbekov dom na Korošici",
        "ending_point_elevation": 1808,
        "ending_point_elevation_units": "m",
        "lat_end": 46.35612316,
        "lon_end": 14.63936863,
        "total_elevation_gain": 460,
        "total_elevation_gain_units": "m",
        "difficulty_level": "lahka označena pot",
        "recommended_equipment_summer": "nan",
        "recommended_equipment_winter": "nan",
        "page_views": 128304,
        "directions_to_start": "Go to the boulder.",
        "hike_description": "Easy when the weather is good.",
        "completed_at_date": "1970-01-01"
    },
    {
        "id": 2,
        "stamp": 1,
        "hike_name": "Robanov kot - Kocbekov dom na Korošici",
        "hike_link": "https://www.hribi.net/izlet/robanov_kot_kocbekov_dom_na_korosici/3/199/1831",
        "starting_point": "Robanov kot",
        "starting_point_elevation": 650,
        "starting_point_elevation_units": "m",
        "lat_start": 46.3948,
        "lon_start": 14.703,
        "ending_point": "Kocbekov dom na Korošici",
        "ending_point_elevation": 1808,
        "ending_point_elevation_units": "m",
        "lat_end": 46.35612316,
        "lon_end": 14.63936863,
        "total_elevation_gain": 1300,
        "total_elevation_gain_units": "m",
        "difficulty_level": "zahtevna označena pot",
        "recommended_equipment_summer": "čelada",
        "recommended_equipment_winter": "čelada, cepin, dereze",
        "page_views": 30907,
        "directions_to_start": "A right after the boulder.",
        "hike_description": "Challenging, but rewarding hike",
        "completed_at_date": "1970-01-01"
    },
    {
        "id": 3,
        "stamp": 1,
        "hike_name": "Za Loncem - Kocbekov dom na Korošici",
        "hike_link": "https://www.hribi.net/izlet/za_loncem_kocbekov_dom_na_korosici/3/199/1264",
        "starting_point": "Za Loncem",
        "starting_point_elevation": 980,
        "starting_point_elevation_units": "m",
        "lat_start": 46.3262,
        "lon_start": 14.6543,
        "ending_point": "Kocbekov dom na Korošici",
        "ending_point_elevation": 1808,
        "ending_point_elevation_units": "m",
        "lat_end": 46.35612316,
        "lon_end": 14.63936863,
        "total_elevation_gain": 1000,
        "total_elevation_gain_units": "m",
        "difficulty_level": "lahka označena pot",
        "recommended_equipment_summer": "nan",
        "recommended_equipment_winter": "cepin, dereze",
        "page_views": 24803,
        "directions_to_start": "A left after the boulder.",
        "hike_description": "A very pretty hike.",
        "completed_at_date": "1970-01-01"
    },
    {
        "id": 4,
        "stamp": 1,
        "hike_name": "Pred Belo - Kocbekov dom na Korošici",
        "hike_link": "https://www.hribi.net/izlet/pred_belo_kocbekov_dom_na_korosici/3/199/1100",
        "starting_point": "Pred Belo",
        "starting_point_elevation": 571,
        "starting_point_elevation_units": "m",
        "lat_start": 46.3188,
        "lon_start": 14.6005,
        "ending_point": "Kocbekov dom na Korošici",
        "ending_point_elevation": 1808,
        "ending_point_elevation_units": "m",
        "lat_end": 46.35612316,
        "lon_end": 14.63936863,
        "total_elevation_gain": 1400,
        "total_elevation_gain_units": "m",
        "difficulty_level": "delno zahtevna označena pot",
        "recommended_equipment_summer": "nan",
        "recommended_equipment_winter": "cepin, dereze",
        "page_views": 20356,
        "directions_to_start": "Zapeljemo se v Kamnik in cesti naprej sledimo proti dolini Kamniške Bistrice. Približno 2km za spodnjo postajo nihalke na Veliko planino pa bomo na desni strani ceste opazili parkirišče in planinske smerokaze za Presedljaj, Konja in Korošico (parkirišče se nahaja za mostom).",
        "hike_description": "S parkirišča se usmerimo na pot v smeri Presedljaja, Korošice, Konja in Ojstrice. Že po nekaj metrih pot zavije v desno, kjer se sprva komaj znatno vzpenja, nato pa se prične spuščati in se po nekaj minutah priključi širokemu kolovozu.",
        "completed_at_date": "1970-01-01"
    },
    # Hikes for test stamp 2: "Mariborska Koča"
    {
        "id": 5,
        "stamp": 2,
        "hike_name": "Zgornja postaja vzpenjače - Mariborska koča",
        "hike_link": "https://www.hribi.net/izlet/zgornja_postaja_vzpenjace_mariborska_koca/4/841/1577",
        "starting_point": "Zgornja postaja vzpenjače",
        "starting_point_elevation": 1040,
        "starting_point_elevation_units": "m",
        "lat_start": 46.516,
        "lon_start": 15.5785,
        "ending_point": "Mariborska koča",
        "ending_point_elevation": 1086,
        "ending_point_elevation_units": "m",
        "lat_end": 46.50480045,
        "lon_end": 15.55446938,
        "total_elevation_gain": 85,
        "total_elevation_gain_units": "m",
        "difficulty_level": "lahka označena pot",
        "recommended_equipment_summer": "nan",
        "recommended_equipment_winter": "cepin, dereze",
        "page_views": 3639,
        "directions_to_start": "a) Štajersko avtocesto zapustimo na izvozu za Slivnico in Rogozo, nato pa sledimo oznakam za Pohorje in Areh. Pot naprej nas vodi skozi Spodnje in Zgornje Hoče, Slivniško Pohorje, za naselji pa sledimo oznakam za Areh, višje pa oznakam za Mariborsko kočo in hotel Bellevue. Parkiramo na parkirišču med zgornjo postajo vzpenjače in hotelom Bellevue. b) Štajersko avtocesto zapustimo na izvozu za Slivnico in Rogozo, nato pa sledimo oznakam za smučišče Mariborsko Pohorje. Parkiramo na obrobju naselja Zgornje Radvanje, na velikem parkirišču ob vznožju smučišča, nato pa se sprehodimo do spodnje postaje vzpenjače (cena povratne vožnje za odraslo osebo je 6 eur - november 2022), s katero se odpeljemo do hotela Bellevue, kjer se prične opisana pot.",
        "hike_description": "Pri zgornji postaji vzpenjače opazimo planinske smerne table, mi pa se usmerimo desno v smeri Mariborske koče in Ruške koče na Arehu. Malo naprej se v desno odcepi kratka pot k bližnji cerkvi sv. Bolfenka, mi pa nadaljujemo po markirani poti, ki se nadaljuje vzporedno z asfaltno cesto. Po omenjeni poti se zložno do zmerno vzpenjamo, za manjšim Marijinim kipom pa se pot razcepi. Nadaljujemo rahlo levo v smeri Mariborske koče (naravnost Mariborski razglednik...) ter v nadaljevanju prečimo pobočja proti levi in sledimo markacijam. Po nekaj minutah prečenja se povsem približamo asfaltni cesti, nato pa se rahlo vzpnemo in pri naselju počitniških hišic najprej dosežemo makadamsko, nato pa še asfaltno cesto. Ko dosežemo asfaltno cesto se nam z desne priključi še pot, ki vodi mimo Mariborskega razglednika, mi pa nadaljujemo naravnost in po nekaj 10 korakih nadaljnje hoje prispemo do naslednjega križišča, kjer pa gremo desno. Sledi le še približno 100 m hoje in prispemo do Mariborske koče, od katere se nam odpre lep pogled v smeri vzhodnih Karavank. Opis in slike se nanašajo na stanje novembra 2022.",
        "completed_at_date": "1970-01-01"
    },
    {
        "id": 6,
        "stamp": 2,
        "hike_name": "Sp. postaja Pohorske vzpenjače - Mariborska koča (Jonatanka)",
        "hike_link": "https://www.hribi.net/izlet/sp_postaja_pohorske_vzpenjace_mariborska_koca_jonatanka/4/841/2072",
        "starting_point": "Sp. postaja Pohorske vzpenjače",
        "starting_point_elevation": 328,
        "starting_point_elevation_units": "m",
        "lat_start": 46.5339,
        "lon_start": 15.5991,
        "ending_point": "Mariborska koča",
        "ending_point_elevation": 1086,
        "ending_point_elevation_units": "m",
        "lat_end": 46.50480045,
        "lon_end": 15.55446938,
        "total_elevation_gain": 820,
        "total_elevation_gain_units": "m",
        "difficulty_level": "lahka neoznačena steza",
        "recommended_equipment_summer": "nan",
        "recommended_equipment_winter": "nan",
        "page_views": 34382,
        "directions_to_start": "Spodnja postaja Pohorske vzpenjače se nahaja na južni strani Maribora v Radvanju. Do nje lahko pridemo iz več smeri, v Mariboru so na važnejših križiščih smerokazi ali ikone za Pohorje. Če se pripeljemo v Maribor po južni vpadnici, sledimo tej skozi Hoče in pri semaforiziranem križišču pri trgovskih centrih zavijemo levo (smer Radvanje), nadaljujemo po Lackovi cesti in sledimo smerokazom. Do spodnje postaje vozi tudi mestni avtobus št.6.",
        "hike_description": "Na zahodni strani parkirišča preko lesenega mostička prečimo potok, takoj nato po desni stani obidemo manjši ribnik in zavijemo v gozd. Za pravilno smer po številnih stezicah nam kot orientacijsko vodilo služi potok na naši levi strani, od katerega se lahko tudi oddaljimo, vendar ne preveč. Po poti se polagoma vzpenjamo skozi gozd, dokler ne pridemo do makadamske ceste (* 15 min). Tu zavijemo na desno in v nadaljevanju poti hodimo po njej, prečimo traso kabinske žičnice nad nami, z desne strani ceste opazimo izvir potoka, po nadaljnjih 100 m poti pa zavijemo s ceste desno v gozd, kot nam označuje kažipot za Sv. Bolfenk in Bellevue. (* 5 min).\r\nSteza se pne skozi bukov gozd navzgor in nas hitro privede do široke utrjene poti, po kateri zavijemo v desno. To traso uporabljajo za spust tudi gorski kolesarji, bodimo pozorni nanje, za njih so tudi nameščene skakalnice na desni strani. Sprva položna pot preraste v strmino in po levem robu prispemo na manjšo vzpetino nad 4. stebrom vzpenjače, katerega opazimo pod seboj (* 10 min). \r\nS tega mesta imamo za nadaljevanje poti  dve možnosti:\r\n*** Lahko nadaljujemo kar naravnost po dobro vidni poti po trasi smučarske proge, imenovani Jonatanka, pot se najprej malce spusti, nato pa se začne kar strmo in neprekinjeno vzpenjati, dokler ne pridemo do gozdička, ki razcepi dosedanjo enotno traso v dve poseki v obliki črke Y. Gozdiček obidemo po desni strani in pridemo do kolovoza, ki pravokotno preči traso, vzporedno ob kolovozu teče potoček. Ta pot je sicer nekaj krajša od druge, v nadaljevanju navedene variante, vendar je tudi bolj strma ter dolgočasna.\r\n*** Lahko pa zavijemo levo v gozd in sledimo stezici, ki se pne desno navzgor. Za orientacijo uporabimo poglobljen kolovoz na naši levi strani, ki poteka vzporedno s potjo. Na mestu, kjer se kolovoz konča, naša steza zavije desno. Pešpot postane bolj položna in nas privede do širše gozdne poti, kateri sledimo navkreber, dokler ne pridemo iz gozda na plano ter se priključimo poti iz predhodne variante malce pod razcepom (* 25min).\r\nZa nadaljevanje poti od razcepa izberemo eno izmed variant:\r\n*** Prečimo kolovoz, nekaj minut strmo navkreber, pot se nato malce izravna in s tega mesta že opazimo zgornjo postajo vzpenjače. Nadaljujemo po dobri vidni poti po poseki, sledi še zelo strm vzpon in mimo bivše tribune FIS-a prispemo do zgornje postaje vzpenjače. Nekoč so tu potekala tekmovanja ženskega smučanja, iz tega razloga se med pohodniki za ta del poti uporablja ime »stara Fiska«.\r\n*** Lahko pa nadaljujemo skozi gozdiček levo navzgor po kolovozu, prispemo do Jonatanke, po kateri zavijemo desno navkreber in levo mimo spodnje postaje vlečnice Bolfenk. Po dobro vidni poti po travniku med zmernim vzponom ves čas sledimo robu gozda na naši desni strani, del poti je tudi vzporeden kolesarski poti (previdnost!), ko postane pot položnejša in zavije desno, zagledamo tudi zgornjo postajo vzpenjače. (* 20 min). \r\nOd zgornje postaje vzpenjače sledimo markirani poti, ki nas vodi od zahodnega roba parkirišča po stezi, vzporedno s cesto, pot nato zavije desno v gozd. Ko prispemo do razpotja, kjer markirana pot zavija levo k Mariborski koči, mi izkoristimo priliko in nadaljujemo kar naravnost in po travniku navzgor do razglednega stolpa ( * 20 min). Pot nadaljujemo po položni markirani poti skozi gozd na zahod v smeri Areha, bodimo pozorni na označen odcep za Mariborsko kočo  (* 5 min). Tukaj zavijemo levo navzdol in sledimo sicer redkim markacijam po dobro vidni poti,  malce pred koncem prispemo do asfaltne ceste, v križišču desno in v nekaj minutah smo na cilju. (* 15 min).",
        "completed_at_date": "1970-01-01"
    },
    {
        "id": 7,
        "stamp": 2,
        "hike_name": "Dom Planinka - Mariborska koča (mimo slapu)",
        "hike_link": "https://www.hribi.net/izlet/dom_planinka_mariborska_koca_mimo_slapu/4/841/1574",
        "starting_point": "Dom Planinka",
        "starting_point_elevation": 890,
        "starting_point_elevation_units": "m",
        "lat_start": 46.4935,
        "lon_start": 15.568,
        "ending_point": "Mariborska koča",
        "ending_point_elevation": 1086,
        "ending_point_elevation_units": "m",
        "lat_end": 46.50480045,
        "lon_end": 15.55446938,
        "total_elevation_gain": 250,
        "total_elevation_gain_units": "m",
        "difficulty_level": "lahka označena pot",
        "recommended_equipment_summer": "nan",
        "recommended_equipment_winter": "nan",
        "page_views": 2419,
        "directions_to_start": "S štiripasovne ceste med Mariborom in Slivnico, v semaforiziranem križišču zavijemo desno v smeri vasi Hoče (iz slivniške smeri pa levo). Cesti naprej sledimo skozi Spodnje in Zgornje Hoče proti Slivniškem Pohorju. V zgornjem delu vasi Slivniško Pohorje, se ostro desno navzgor odcepi cesta k domu Planinka. Ta cesta pa nas po 100m pripelje do križišča pri baru na Prepihu. Tu zavijemo desno proti Planinki in parkiramo na parkirišču ob cesti. Na parkirišču pred Planinko in barom na Prepihu je dovoljeno parkirati le gostom.",
        "hike_description": "S parkirišča se vrnemo do križišča in pot nadaljujemo mimo bara na Prepihu do naslednjega križišča, kjer nas oznake za Mariborsko kočo usmerijo na levo cesto. Po nekaj minutah hoje se cesta konča in pot nadaljujemo po kolovozu, ki gre v strnjen smrekov gozd. Sledi 15 minutna hoja po prijetnem kolovozu, na koncu katerega stopimo na asfaltirano cesto. Nadaljujemo desno v smeri slapu do križišča, kjer nas oznake za slap Skalca usmerijo levo, na peš pot, ki se začne spuščati. Po 5 minutah spusta pa nas pot pripelje do Framskega slapu (slap Skalca). Od slapa se vrnemo nazaj do križišča in pot nadaljujemo po cesti v smeri Mariborske koče. Že kmalu pa nas markacije usmerijo levo na travnik, kjer je več poti. Pazljivo pogledamo kje je markacija in po krajšem vzponu čez travnik pridemo v gozd, kjer se pot za krajši čas strmeje vzpne in nas nato v nekaj minutah pripelje do Mariborske koče.",
        "completed_at_date": "1970-01-01"
    },
    {
        "id": 8,
        "stamp": 2,
        "hike_name": "Sp. postaja Pohorske vzpenjače - Mariborska koča (Čopka)",
        "hike_link": "https://www.hribi.net/izlet/sp_postaja_pohorske_vzpenjace_mariborska_koca_copka/4/841/2075",
        "starting_point": "Sp. postaja Pohorske vzpenjače",
        "starting_point_elevation": 328,
        "starting_point_elevation_units": "m",
        "lat_start": 46.5339,
        "lon_start": 15.5991,
        "ending_point": "Mariborska koča",
        "ending_point_elevation": 1086,
        "ending_point_elevation_units": "m",
        "lat_end": 46.50480045,
        "lon_end": 15.55446938,
        "total_elevation_gain": 758,
        "total_elevation_gain_units": "m",
        "difficulty_level": "lahka neoznačena steza",
        "recommended_equipment_summer": "nan",
        "recommended_equipment_winter": "nan",
        "page_views": 23848,
        "directions_to_start": "Spodnja postaja Pohorske vzpenjače se nahaja na južni strani Maribora v Radvanju, ob njej je urejeno veliko parkirišče. Do nje lahko pridemo iz več smeri, v Mariboru so na važnejših križiščih smerokazi ali ikone za Pohorje. Če se pripeljemo v Maribor po južni vpadnici, sledimo tej skozi Hoče in pri semaforiziranem križišču pri trgovskih centrih zavijemo levo (smer Radvanje), nadaljujemo po Lackovi cesti in sledimo smerokazom. Do spodnje postaje vozi tudi mestni avtobus št.6.",
        "hike_description": "S parkirišča preko betonskega mostička prečimo potok, zgradbo spodnje postaje Pohorske vzpenjače obidemo po desni strani in nadaljujemo pot navkreber po dobro vidni pešpoti po travniku vzporedno s traso krožno-kabinske žičnice. Nad 2. stebrom pot zavije desno, obide gozd in se zasuče v levo. Strmina malce popusti, hodimo po Čopovi progi ali v žargonu »po Čopki« ter prispemo do Trikotne jase (* 25 min).  Tukaj se nahaja višinski poligon (adrenalinski park), malce naprej je zgornja postaja sedežnice Radvanje ter spodnja postaja sedežnice Poštela, urejeno je tudi poletno sankališče. Pri adrenalinskem parku zavijemo desno navzgor po travniku, pot postane strmejša, na severno stran se nam odpira razgled na Maribor in njegovo daljno okolico, prispemo do koče Luka (* 25 min). Ob koči, ki je gostinski objekt, je ob ograji nameščena pipa s pitno vodo, na odprti terasi so klopi in mize.Po sredini  travnika ali ob robu gozda nadaljujemo pot navkreber, na vrhu se pri reklamnem panoju na vzpetini Habakuk pot zasuče desno (* 15 min). Strmina popusti, udobna pot sledi trasi sedežnice Sleme in nas privede do zgornje postaje Pohorske vzpenjače (20 * min).Nadaljnja pot je orientacijsko nezahtevna, na zahodni strani parkirišča pri zgornji postaji vzpenjače zavijemo levo in sledimo markacijam. Lagodna pot nato zavije desno v gozd, na razpotju nas smerokaz usmeri levo (s tega mesta je 5 minut hoje navkreber do Mariborskega razglednika), del  poti hodimo tudi po Rozikini gozdni učni poti (rumeno modre markacije), steza poteka nad Aparthotelom Pohorje (bivši Železničarski dom), se za trenutek približa cesti in takoj nato spet zavije v gozd ter nas skozi naselje počitniških hiš pripelje do Mariborske koče (* 40 min).V nasprotju z Jonatanko je opisana pot položnejša in pogosteje obiskana, sploh do Trikotne jase ali do koče Luka bomo srečavali mnogo rekreativcev in sprehajalcev.",
        "completed_at_date": "1970-01-01"
    },
]

class HikesTestCase(TestCase):
    """Tests for accessing hikes from hikes/* endpoints"""
    def setUp(self):
        """Populate test database with test hikes and stamps"""
        Stamps.objects.create(**TEST_STAMPS[0])
        for hike in TEST_HIKES:
            hike_data = hike | { 'stamp': Stamps.objects.get(pk=1) }
            Hikes.objects.create(**hike_data)
        HikesTestCase.client = Client()

    def test_hikes_endpoint(self):
        """GET requests to the hikes endpoint give us a 200 status"""
        response = HikesTestCase.client.get('/gorapass/hikes')
        self.assertEqual(response.status_code, 200)

    def test_hike_endpoint(self):
        """Fetching a single hike from 'hikes/<hike_id>' gives us JSON with correct attributes"""
        # Fetch the hike
        response = HikesTestCase.client.get('/gorapass/hikes/1')
        self.assertEqual(response.status_code, 200)
        # Compare response data with data used to create the hike
        data = json.loads(response.content)
        self.assertEqual(data, TEST_HIKES[0])

    def test_single_filter_hikes(self):
        """POST requests with selectors will give us the matching hikes"""
        selectors = [
            {
                "attribute_name": "ending_point",
                "attribute_value": "Kocbekov dom na Korošici",
                "filter_type": "exact",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = HikesTestCase.client.post('/gorapass/hikes', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        expected = TEST_HIKES[:4]

        self.assertEqual(expected, data)

    def test_multiple_filter_hikes(self):
        """POST requests with multiple selectors will give us the matching hikes"""
        selectors = [
            {
                "attribute_name": "ending_point",
                "attribute_value": "Kocbekov dom na Korošici",
                "filter_type": "exact",
            },
            {
                "attribute_name": "total_elevation_gain",
                "attribute_value": 1200,
                "filter_type": "less_than",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = HikesTestCase.client.post('/gorapass/hikes', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        expected = [TEST_HIKES[0], TEST_HIKES[2]]

        self.assertEqual(expected, data)

    def test_partial_filter_works_hikes(self):
        """Selectors with 'partial' filter will match parts of attribute for hikes"""
        selectors = [
            {
                "attribute_name": "hike_name",
                "attribute_value": "Koro",
                "filter_type": "partial",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = HikesTestCase.client.post('/gorapass/hikes', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        expected = TEST_HIKES[:4]

        self.assertEqual(expected, data)

    def test_greater_than_with_less_than_hikes(self):
        """Selectors 'less_than' and 'greater_than' can combine to create a range for hikes"""
        selectors = [
            {
                "attribute_name": "total_elevation_gain",
                "attribute_value": 1000,
                "filter_type": "greater_than",
            },
            {
                "attribute_name": "total_elevation_gain",
                "attribute_value": 2000,
                "filter_type": "less_than",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = HikesTestCase.client.post('/gorapass/hikes', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        expected = [TEST_HIKES[1], TEST_HIKES[3]]

        self.assertEqual(expected, data)

    def test_filters_without_matches_returns_empty_list_hikes(self):
        """Valid selectors for hikes without any matches will return an empty list"""
        selectors = [
            {
                "attribute_name": "starting_point",
                "attribute_value": "random value",
                "filter_type": "exact",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = HikesTestCase.client.post('/gorapass/hikes', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        expected = []

        self.assertEqual(expected, data)

    def test_bad_selector_rejected_hikes(self):
        """Selectors with non-existant 'attribute_name' will return a 400 response for hikes"""
        selectors = [
            {
                "attribute_name": "not_present",
                "attribute_value": "Kocbekov dom na Korošici",
                "filter_type": "exact",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = HikesTestCase.client.post('/gorapass/hikes', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_missing_selector_key_rejected_hikes(self):
        """Selectors missing keys will return a 400 response for hikes"""
        selectors = [
            {
                "attribute_value": "Kocbekov dom na Korošici",
                "filter_type": "exact",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = HikesTestCase.client.post('/gorapass/hikes', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_extra_selector_keys_rejected_hikes(self):
        """Selectors with extra keys will return a 400 response for hikes"""
        selectors = [
            {
                "whoops": "this shouldn't be here",
                "attribute_name": "ending_point",
                "attribute_value": "Kocbekov dom na Korošici",
                "filter_type": "exact"
            }
        ]
        data = json.dumps({ 'selectors': selectors })

        response = HikesTestCase.client.post('/gorapass/hikes', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_filter_type_rejected_hikes(self):
        """Selectors invalid filter type will return a 400 response"""
        selectors = [
            {
                "attribute_name": "ending_point",
                "attribute_value": "Kocbekov dom na Korošici",
                "filter_type": "exact_match" # should be "exact"
            }
        ]
        data = json.dumps({ 'selectors': selectors })

        response = HikesTestCase.client.post('/gorapass/hikes', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)


class UserTestCase(TestCase):
    """Test cases involving a user"""
    def setUp(self):
        """Populate test database with stamps, hikes, and a test user"""
        # Populate test stamps
        for stamp in TEST_STAMPS:
            Stamps.objects.create(**stamp)

        # Populate test hikes
        for hike in TEST_HIKES:
            hike_data = hike | { 'stamp': Stamps.objects.get(pk=1) }
            Hikes.objects.create(**hike_data)

        hike1 = Hikes.objects.get(pk=1)
        hike2 = Hikes.objects.get(pk=2)

        stamp1 = Stamps.objects.get(pk=1)
        stamp2 = Stamps.objects.get(pk=2)

        # Populate test user
        jane = User.objects.create_user('jane_doe', 'jane@doe.com', 'gorapass')
        CompletedHikes.objects.create(hike=hike1, user=jane)
        CompletedHikes.objects.create(hike=hike2, user=jane)
        CompletedStamps.objects.create(stamp=stamp1, user=jane)
        CompletedStamps.objects.create(stamp=stamp2, user=jane)

        # Client for making requests
        UserTestCase.client = Client()

    def test_user_login_ok(self):
        credentials = {
            'username': 'jane_doe',
            'password': 'gorapass',
        }

        data = json.dumps(credentials)
        response = UserTestCase.client.post('/gorapass/users/login', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_user_login_bad_username(self):
        credentials = {
            'username': 'janedoe',
            'password': 'gorapass',
        }

        data = json.dumps(credentials)
        response = UserTestCase.client.post('/gorapass/users/login', data, content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_user_login_bad_password(self):
        credentials = {
            'username': 'jane_doe',
            'password': 'Gorapass',
        }

        data = json.dumps(credentials)
        response = UserTestCase.client.post('/gorapass/users/login', data, content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_user_login_no_username(self):
        credentials = {
            'password': 'gorapass',
        }

        data = json.dumps(credentials)
        response = UserTestCase.client.post('/gorapass/users/login', data, content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_user_login_no_password(self):
        credentials = {
            'username': 'jane_doe',
        }

        data = json.dumps(credentials)
        response = UserTestCase.client.post('/gorapass/users/login', data, content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_user_login_no_credentials(self):
        data = json.dumps({})
        response = UserTestCase.client.post('/gorapass/users/login', data, content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_user_login_no_body(self):
        response = UserTestCase.client.post('/gorapass/users/login')
        self.assertEqual(response.status_code, 400)

    def test_user_page_not_logged_in(self):
        response = UserTestCase.client.get('/gorapass/users/1')
        self.assertEqual(response.status_code, 401)

    def test_user_page_logged_in(self):
        UserTestCase.client.login(username='jane_doe', password='gorapass')
        response = UserTestCase.client.get('/gorapass/users/1')
        self.assertEqual(response.status_code, 200)

        user = User.objects.get(pk=1)
        user_data = model_to_dict(user)
        user_data.pop('date_joined')
        user_data.pop('last_login')

        response_data = json.loads(response.content)
        response_data.pop('date_joined')
        response_data.pop('last_login')
        self.assertEqual(response_data, user_data)

    def test_other_user_page_logged_in(self):
        UserTestCase.client.login(username='jane_doe', password='gorapass')
        response = UserTestCase.client.get('/gorapass/users/2')
        self.assertEqual(response.status_code, 401)

    def test_fetch_completed_hikes(self):
        UserTestCase.client.login(username='jane_doe', password='gorapass')
        response = UserTestCase.client.get('/gorapass/users/1/completed_hikes')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(TEST_HIKES[0], data[0])

    def test_fetch_completed_stamps(self):
        UserTestCase.client.login(username='jane_doe', password='gorapass')
        response = UserTestCase.client.get('/gorapass/users/1/completed_stamps')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual([TEST_STAMPS[0], TEST_STAMPS[1]], data)

    def test_fetch_completed_stamps_other_user(self):
        """Trying to get another user's completed stamp's data results in redirect to login page."""
        UserTestCase.client.login(username='jane_doe', password='gorapass')
        response = UserTestCase.client.get('/gorapass/users/2/completed_stamps')
        self.assertEqual(response.status_code, 401)

class StampsTestCase(TestCase):
    def setUp(self):
        for stamp in TEST_STAMPS:
            Stamps.objects.create(**stamp)
            StampsTestCase.client = Client()

    def test_stamps_endpoint(self):
        """GET requests to the stamps endpoint gives us a 200 status"""
        # Fetch all stamps
        response = StampsTestCase.client.get("/gorapass/stamps")
        self.assertEqual(response.status_code, 200)

    def test_stamps_endpoint_payload(self):
        """GET requests to the stamps endpoint returns all the stamps"""
        # Make sure total stamps returned is correct length
        response = StampsTestCase.client.get("/gorapass/stamps")
        data = json.loads(response.content)
        self.assertEqual(len(data), len(TEST_STAMPS))

    def test_stamp_endpoint(self):
        """GET requests to the single stamp endpoint gives us a 200 status"""
        # Fetch single stamp
        response = StampsTestCase.client.get("/gorapass/stamps/1")
        self.assertEqual(response.status_code, 200)

        # Check payload
        data = json.loads(response.content)
        self.assertEqual(data, TEST_STAMPS[0])

    def test_single_filter_stamps(self):
        """POST requests with selectors will give us the matching stamps"""
        selectors = [
            {
                "attribute_name": "stamp_name",
                "attribute_value": "Kocbekov dom na Korošici",
                "filter_type": "exact",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = StampsTestCase.client.post('/gorapass/stamps', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)[0]
        expected = TEST_STAMPS[0]

        self.assertEqual(expected, data)

    def test_multiple_filter_stamps(self):
        """POST requests with multiple selectors will give us the matching stamps"""
        selectors = [
            {
                "attribute_name": "region",
                "attribute_value": "Pohorje",
                "filter_type": "exact",
            },
            {
                "attribute_name": "elevation",
                "attribute_value": 1200,
                "filter_type": "greater_than",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = StampsTestCase.client.post('/gorapass/stamps', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        expected = [TEST_STAMPS[2], TEST_STAMPS[3]]

        self.assertEqual(expected, data)

    def test_partial_filter_works_stamps(self):
        """Selectors with 'partial' filter will match parts of attribute for stamps"""
        selectors = [
            {
                "attribute_name": "stamp_name",
                "attribute_value": "Koč",
                "filter_type": "partial",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = StampsTestCase.client.post('/gorapass/stamps', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        expected = [TEST_STAMPS[1], TEST_STAMPS[2], TEST_STAMPS[4]]

        self.assertEqual(expected, data)

    def test_greater_than_with_less_than_stamps(self):
        """Selectors 'less_than' and 'greater_than' can combine to create a range for stamps"""
        selectors = [
            {
                "attribute_name": "elevation",
                "attribute_value": 1200,
                "filter_type": "greater_than",
            },
            {
                "attribute_name": "elevation",
                "attribute_value": 1400,
                "filter_type": "less_than",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = StampsTestCase.client.post('/gorapass/stamps', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        expected = [TEST_STAMPS[2], TEST_STAMPS[3], TEST_STAMPS[4]]

        self.assertEqual(expected, data)

    def test_filters_without_matches_returns_empty_list_stamps(self):
        """Valid selectors for stamps without any matches will return an empty list"""
        selectors = [
            {
                "attribute_name": "elevation",
                "attribute_value": "random value",
                "filter_type": "exact",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = StampsTestCase.client.post('/gorapass/stamps', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        expected = []

        self.assertEqual(expected, data)

    def test_bad_selector_rejected_stamps(self):
        """Selectors with non-existant 'attribute_name' will return a 400 response for stamps"""
        selectors = [
            {
                "attribute_name": "not_present",
                "attribute_value": "Kocbekov dom na Korošici",
                "filter_type": "exact",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = StampsTestCase.client.post('/gorapass/stamps', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_missing_selector_key_rejected_stamps(self):
        """Selectors missing keys will return a 400 response for stamps"""
        selectors = [
            {
                "attribute_value": "Kocbekov dom na Korošici",
                "filter_type": "exact",
            },
        ]
        data = json.dumps({ 'selectors': selectors })

        response = StampsTestCase.client.post('/gorapass/stamps', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_extra_selector_keys_rejected_stamps(self):
        """Selectors with extra keys will return a 400 response for stamps"""
        selectors = [
            {
                "whoops": "this shouldn't be here",
                "attribute_name": "ending_point",
                "attribute_value": "Kocbekov dom na Korošici",
                "filter_type": "exact"
            }
        ]
        data = json.dumps({ 'selectors': selectors })

        response = StampsTestCase.client.post('/gorapass/stamps', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_filter_type_rejected_stamps(self):
        """Selectors invalid filter type will return a 400 response for stamps"""
        selectors = [
            {
                "attribute_name": "ending_point",
                "attribute_value": "Kocbekov dom na Korošici",
                "filter_type": "exact_match" # should be "exact"
            }
        ]
        data = json.dumps({ 'selectors': selectors })

        response = StampsTestCase.client.post('/gorapass/stamps', data, content_type='application/json')
        self.assertEqual(response.status_code, 400)







### response = StampsTestCase.client.post("/gorapass/stamps", '{}', content_type="application/json")
