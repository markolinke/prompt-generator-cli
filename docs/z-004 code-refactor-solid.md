Zdravo Bartol!  

Danas prelazimo na sljedeći korak u našem CLI projektu: **dobra struktura Python koda**. Koristit ćemo **SOLID principe** – to su pravila za pisanje čistog, fleksibilnog koda koji je lak za održavanje. Ovo je super za junior developere, jer ćeš naučiti kako pretvoriti "jednu veliku skriptu" u organizirani projekt.

### Što su SOLID principi? (Jednostavno objašnjenje)

SOLID je akronim za 5 principa (iz OOP programiranja, ali korisno i u Pythonu):
- **S**ingle Responsibility: Svaki modul/klasa radi SAMO JEDNU stvar. (Npr. jedan modul za učitavanje configa, drugi za UI.)
- **O**pen-Closed: Kod je otvoren za proširenje (dodaj novo), ali zatvoren za promjene (ne mijenjaj postojeći kod).
- **L**iskov Substitution: Ako imaš podklase, one moraju moći zamijeniti baznu klasu bez problema.
- **I**nterface Segregation: Bolje mali interfejsi (funkcije) nego jedan veliki.
- **D**ependency Inversion: Visoki moduli (kao main) ne ovise o niskim (kao file reader), nego obrnuto – koristi apstrakcije.

U našem slučaju, fokusirat ćemo se na **S** i **O**, jer su najlakši za početak. Cilj: Razbiti tu veliku `prompt_generator_cli.py` skriptu u više modula (kao što si jučer naučio).

### Analiza trenutne skripte (prompt_generator_cli.py)

Ovo je tvoja skripta iz projekta. Ona je dobra, ali "jedna velika datoteka" (preko 400 linija!). Problemi:
- Krši **S**: Ima sve – boje, parser YAML-a, UI, loading efekte, generiranje prompta... Ako promijeniš jednu stvar, riskiraš slomiti sve.
- Nema **O**: Ako želiš dodati novu funkcionalnost (npr. drugi jezik), moraš mijenjati cijelu skriptu.
- Ostalo: Nema jasnih modula, pa je teško testirati ili ponovno koristiti kod.

Refaktoriramo je u module/pakete: Svaki modul radi jednu stvar.

### Mali hands-on zadatak za danas (zabavan i praktičan)

Cilj: Refaktoriraj skriptu u strukturu sa SOLID principima. Koristi Git (kao jučer): napravi branch `bartolinke/dan4-refactor-solid`.

1. Otvori projekt `prompt-generator-cli` lokalno.
2. Napravi novi branch: `git checkout -b bartolinke/dan4-refactor-solid`.
3. Razbij `prompt_generator_cli.py` u ove module (nove .py datoteke):
   - `colors.py`: Klasa za boje (Colors class). (S: Samo boje.)
   - `config_parser.py`: Funkcije za učitavanje i parsiranje YAML-a (parse_yaml_simple, load_categories). (S: Samo config.)
   - `ui.py`: Funkcije za prikaz menija, inpute, loading efekte (display_menu, get_category_choice, collect_answers, startup_loading_effect, retro_loading_effect, display_prompt_and_ask_continue). (S: Samo UI.)
   - `prompt_generator.py`: Funkcija za generiranje prompta (generate_prompt). (S: Samo logika prompta.)
   - `utils.py`: Ostale pomoćne stvari (copy_to_clipboard). (S: Pomoćne funkcije.)
   - `main.py`: Glavni loop (main funkcija) koji uvozi sve i povezuje. (O: Lako proširivo.)

   Primjer uvoza u `main.py`:
   ```python
   from colors import Colors
   from config_parser import load_categories
   from ui import display_menu, get_category_choice, collect_answers, startup_loading_effect, retro_loading_effect, display_prompt_and_ask_continue
   from prompt_generator import generate_prompt
   from utils import copy_to_clipboard
   ```

4. Testiraj: Pokreni `python main.py` – mora raditi isto kao prije.
5. Dodaj nešto novo (za O princip): U `prompt_generator.py` dodaj opciju za drugi jezik (npr. promijeni "Croatian" u "English" ako korisnik hoće), bez mijenjanja ostalog koda.
6. Commitaj: `git add .`, `git commit -m "Refaktoriranje po SOLID principima"`, `git push origin bartolinke/dan4-refactor-solid`.
7. Napravi pull request prema mainu.

Ovo će biti zabavno jer ćeš vidjeti kako kod postaje "lakši" – kao da si pospremio sobu!

### Ako ti nešto nije jasno?

Otvori Grok/ChatGPT i pitaj ovako:

> "Objasni mi SOLID principe u Pythonu, kao junior developeru koji zna osnove. Daj primjer refaktoriranja jedne velike skripte u module po SOLID-u, s fokusom na Single Responsibility. Koristi primjer CLI alata sa YAML configom i UI-om."

Slobodno koristi AI – važno je da na kraju razumiješ i možeš sam objasniti zašto je SOLID koristan (npr. za timski rad).

Sutra nastavljamo s testiranjem refaktoriranog koda. Super radiš, Bartol! 🚀