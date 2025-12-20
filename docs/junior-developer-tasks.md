Zadaci za Junior Developera
===========================

Ova lista zadataka dizajnirana je da te progresivno vodi kroz poboljšanja aplikacije, učeći te osnovne principe čistog koda, SOLID principa i dobre prakse.

📋 Pregled zadataka
-------------------

### Nivo 1: Osnove i refaktoriranje (počni ovdje)

#### Zadatak 1: Refaktoriranje hard-coded konfiguracije

**Cilj:** Naučiti o upravljanju konfiguracijom i Single Responsibility Principle

**Opis:** Trenutno je CONFIG_FILE hard-coded na liniji 50. Trebaš:

-   Kreirati modul za upravljanje konfiguracijom koji će čitati konfiguraciju iz environment varijabli ili config datoteke
-   Omogućiti da se config datoteka može mijenjati preko command-line argumenta (npr. --config config/categories/software-development.yaml)
-   Dodati zadanu (default) vrijednost ako ništa nije specificirano

**Koraci:**

1.  Kreiraj config/config_manager.py modul
2.  Implementiraj funkciju get_config_file() koja provjerava:
    -   Command-line argument --config
    -   Environment varijablu PROMPT_GENERATOR_CONFIG
    -   Zadanu vrijednost
3.  Refaktoriraj prompt_generator_cli.py da koristi novi modul
4.  Dodaj argparse za command-line argumente

**Što ćeš naučiti:**

-   Kako organizirati konfiguraciju
-   Korištenje argparse modula
-   Environment varijable u Pythonu
-   Single Responsibility Principle

* * * * *

#### Zadatak 2: Izdvajanje YAML parsera u zaseban modul

**Cilj:** Odvajanje odgovornosti i testabilnost

**Opis:** Funkcija parse_yaml_simple() je duga i kompleksna. Trebaš:

-   Kreirati parsers/yaml_parser.py modul
-   Premjestiti parse_yaml_simple() tamo
-   Dodati osnovne unit testove za parser
-   Razmotriti korištenje pyyaml biblioteke umjesto custom parsera

**Koraci:**

1.  Kreiraj parsers/ direktorij
2.  Kreiraj parsers/yaml_parser.py s funkcijom
3.  Kreiraj tests/ direktorij i tests/test_yaml_parser.py
4.  Napiši 3-5 osnovnih testova (npr. valjani YAML, prazna datoteka, nedostajuća kategorija)
5.  Refaktoriraj glavnu datoteku da koristi novi modul

**Što ćeš naučiti:**

-   Organizacija modula u Pythonu
-   Unit testiranje s unittest ili pytest
-   Koncept dependency injection
-   Kada koristiti vanjske biblioteke nasuprot custom rješenja

* * * * *

#### Zadatak 3: Kreiranje ColorManager klase

**Cilj:** Objektno orijentirano programiranje i enkapsulacija

**Opis:** Klasa Colors je samo zbirka konstanti. Trebaš:

-   Pretvoriti je u ColorManager klasu s metodama
-   Dodati metode poput success(), error(), warning(), info()
-   Omogućiti isključivanje boja (npr. za CI/CD okruženja)
-   Dodati podršku za dark/light mode (ako terminal podržava)

**Koraci:**

1.  Refaktoriraj Colors u ColorManager klasu
2.  Dodaj __init__ metodu koja provjerava podržava li terminal boje
3.  Kreiraj pomoćne metode: print_success(), print_error(), itd.
4.  Refaktoriraj sve pozive kroz aplikaciju
5.  Dodaj --no-color flag

**Što ćeš naučiti:**

-   Dizajn klase i metode
-   Enkapsulacija
-   Detekcija mogućnosti terminala
-   Refaktoriranje postojećeg koda

* * * * *

### Nivo 2: Poboljšanja funkcionalnosti

#### Zadatak 4: Dodavanje validacije unosa

**Cilj:** Defanzivno programiranje i rukovanje greškama

**Opis:** Trenutno aplikacija ne validira korisničke unose. Trebaš:

-   Dodati validaciju za različite tipove pitanja (brojevi, email, datumi, itd.)
-   Omogućiti da YAML definira pravila validacije
-   Prikazati jasne poruke o greškama
-   Omogućiti mehanizam ponovnog pokušaja

**Koraci:**

1.  Proširi YAML strukturu da podržava validation polje:

    YAML

    ```
    - question: Koliko trošiš mjesečno?
      instruction: Iznos u eurima
      validation:
        type: number
        min: 0
        max: 10000
    ```

2.  Kreiraj validators/ modul s klasama validatora
3.  Implementiraj NumberValidator, EmailValidator, RequiredValidator
4.  Integriraj u funkciju collect_answers()
5.  Dodaj logiku ponovnog pokušaja (maks. 3 pokušaja)

**Što ćeš naučiti:**

-   Validacija podataka
-   Strategy pattern (različiti validatori)
-   Najbolje prakse rukovanja greškama
-   Dizajn YAML sheme

* * * * *

#### Zadatak 5: Implementacija upravljanja poviješću/sesijama

**Cilj:** Sloj za perzistenciju i upravljanje podacima

**Opis:** Dodaj mogućnost da korisnik vidi prethodno generirane promptove i može ih ponovo koristiti.

**Koraci:**

1.  Kreiraj storage/ modul
2.  Implementiraj SessionStorage klasu koja čuva:
    -   Vremenski pečat
    -   Kategoriju
    -   Odgovore
    -   Generirani prompt
3.  Koristi JSON datoteku za pohranu (~/.prompt_generator/history.json)
4.  Dodaj opciju u izbornik: "Pogledaj povijest" ili "Učitaj prethodnu sesiju"
5.  Implementiraj --history command-line flag

**Što ćeš naučiti:**

-   File I/O u Pythonu
-   JSON serijalizacija
-   Obrasci perzistencije podataka
-   Upravljanje korisničkim podacima

* * * * *

#### Zadatak 6: Dodavanje funkcionalnosti izvoza

**Cilj:** Rukovanje datotekama i formatiranje

**Opis:** Omogući korisniku da izveze generirani prompt u različite formate.

**Koraci:**

1.  Dodaj opciju nakon generiranja prompta: "Izvesti u datoteku?"
2.  Podržani formati:
    -   Običan tekst (.txt)
    -   Markdown (.md)
    -   JSON (.json) -- s metapodacima
3.  Kreiraj exporters/ modul s klasama TextExporter, MarkdownExporter, JSONExporter
4.  Implementiraj sustav predložaka za markdown formatiranje
5.  Dodaj --export flag za automatski izvoz

**Što ćeš naučiti:**

-   Pisanje datoteka
-   Podrška za više formata
-   Sustavi predložaka
-   Factory pattern (za različite izvoznike)

* * * * *

### Nivo 3: Arhitektura i obrasci dizajna

#### Zadatak 7: Refaktoriranje u arhitekturu Service Layer

**Cilj:** Clean Architecture i odvajanje odgovornosti

**Opis:** Trenutno je sva logika u main() i pomoćnim funkcijama. Trebaš organizirati kod u servise.

**Koraci:**

1.  Kreiraj services/ direktorij
2.  Implementiraj:
    -   CategoryService -- učitavanje i upravljanje kategorijama
    -   PromptService -- generiranje promptova
    -   UIService -- sva logika prikaza
    -   InputService -- sva logika rukovanja korisničkim unosom
3.  Refaktoriraj main() da koristi servise
4.  Svaki servis treba imati jasno definiran sučelje

**Što ćeš naučiti:**

-   Service Layer pattern
-   Dependency Injection
-   Principi Clean Architecture
-   Dizajn sučelja

* * * * *

#### Zadatak 8: Implementacija sustava Template Engine

**Cilj:** Strategy pattern i proširivost

**Opis:** Trenutno je predložak prompta hard-coded. Trebaš napraviti fleksibilan sustav predložaka.

**Koraci:**

1.  Kreiraj templates/ direktorij
2.  Implementiraj TemplateEngine klasu koja:
    -   Učitava datoteke predložaka
    -   Podržava varijable (npr. {{category_name}}, {{answers}})
    -   Omogućava različite predloške za različite kategorije
3.  Kreiraj zadanu datoteku predloška
4.  Omogući da YAML definira putanju do custom predloška
5.  Dodaj nasljeđivanje predložaka (osnovni predložak + specifičan za kategoriju)

**Što ćeš naučiti:**

-   Sustavi predložaka
-   Strategy pattern
-   Konfiguracija temeljena na datotekama
-   Nasljeđivanje predložaka

* * * * *

#### Zadatak 9: Dodavanje sustava za logiranje

**Cilj:** Promatranje i otkrivanje grešaka

**Opis:** Dodaj profesionalan sustav logiranja umjesto print naredbi.

**Koraci:**

1.  Zamijeni sve print() pozive s modulom logging
2.  Kreiraj utils/logger.py s konfiguracijom
3.  Implementiraj različite razine loga:
    -   DEBUG: detaljne informacije
    -   INFO: normalni tijek
    -   WARNING: potencijalni problemi
    -   ERROR: greške
4.  Dodaj logiranje u datoteku (logs/prompt_generator.log)
5.  Dodaj --verbose i --quiet flagove
6.  Logiraj sve korisničke akcije (za otkrivanje grešaka)

**Što ćeš naučiti:**

-   Python modul logging
-   Razine loga i najbolje prakse
-   Rotacija datoteka loga
-   Tehnike otkrivanja grešaka

* * * * *

#### Zadatak 10: Kreiranje sustava za plugine

**Cilj:** Proširivost i Open/Closed Principle

**Opis:** Omogući dodavanje custom funkcionalnosti preko sustava plugina.

**Koraci:**

1.  Definiraj baznu klasu/sučelje Plugin
2.  Kreiraj plugins/ direktorij
3.  Implementiraj učitavač plugina koji:
    -   Skenira plugins/ mapu
    -   Učitava Python module
    -   Registrira hook-ove (npr. before_prompt_generation, after_answer_collected)
4.  Kreiraj 2-3 primjera plugina:
    -   StatisticsPlugin -- prikuplja statistike o korištenju
    -   AutoCompletePlugin -- predlaže odgovore na temelju prethodnih
    -   TranslationPlugin -- prevodi promptove
5.  Dokumentiraj kako napraviti custom plugin

**Što ćeš naučiti:**

-   Arhitektura plugina
-   Dinamičko učitavanje modula
-   Sustav hook-ova
-   Open/Closed Principle
-   Dizajn proširivosti

* * * * *

🎯 Preporučeni redoslijed
-------------------------

Za početak, preporučujem ovaj redoslijed:

1.  **Zadatak 1** -- najlakši, uvod u refaktoriranje
2.  **Zadatak 2** -- uvod u testiranje
3.  **Zadatak 3** -- OOP koncepti
4.  **Zadatak 4** -- praktična funkcionalnost
5.  **Zadatak 7** -- arhitektura (važno!)
6.  **Zadatak 9** -- logiranje (važno za produkciju)
7.  Ostali zadaci po interesu

📚 Resursi za učenje
--------------------

-   **SOLID principi:** Clean Code by Robert C. Martin
-   **Python best practices:** Real Python tutorials
-   **Testing:** pytest documentation
-   **Architecture:** "Architecture Patterns with Python" by Harry Percival

💡 Savjeti
----------

-   **Commit često:** Svaki zadatak u zaseban commit s jasnom porukom
-   **Piši testove:** Čak i za jednostavne funkcije
-   **Dokumentiraj:** Dodaj docstrings za sve funkcije i klase
-   **Pitaj za code review:** Prije merge-a, traži povratne informacije
-   **Refaktoriraj:** Ako vidiš dupliciranje, refaktoriraj odmah

✅ Checklist prije početka
-------------------------

-   Pročitao si cijeli kod i razumiješ ga
-   Postavio si razvojno okruženje
-   Instalirao si pytest za testiranje
-   Kreirao si feature branch za prvi zadatak
-   Pročitao si SOLID principe (barem osnovno)

* * * * *

**Sretno! 🚀**