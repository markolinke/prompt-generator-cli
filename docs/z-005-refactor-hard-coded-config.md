# Upute za Bartola - Configuration refactor

Danas nastavljamo na projektu **prompt-generator-cli**. Cilj je da program postane fleksibilniji – umjesto da je putanja do konfiguracijske datoteke "zakucana" u kodu (hard-coded), naučit ćemo kako to učiniti promjenjivim i profesionalnim načinom.

Ovo je važan korak jer u stvarnim projektima konfiguracija mora biti lako promjenjiva bez mijenjanja koda (npr. za različite korisnike ili okoline).

## 1. Proučavanje: Što trebaš razumjeti prije rada (1-1.5 sat)

Pročitaj i shvati sljedeće koncepte:

1. **argparse** – Python modul za parsiranje command-line argumenata.
2. **Environment varijable** – kako ih postaviti i čitati u Pythonu (os.environ).
3. **Single Responsibility Principle** – kratko: svaki modul/datoteka treba raditi samo jednu stvar.

### Preporučeni materijal:
- argparse: pročitaj službenu Python dokumentaciju – https://docs.python.org/3/howto/argparse.html (samo prvi primjeri, dovoljno 15-20 min).
- Environment varijable: potraži “Python os.environ tutorial” ili postavi AI-u pitanje dolje.
- Single Responsibility: kratki video ili članak “Single Responsibility Principle explained simply”.

### Ako ti nešto nije jasno
(npr. “Kako točno radi argparse?”):  
Odi na Grok/ChatGPT i postavi:  
> "Objasni mi argparse u Pythonu kao junior developeru. Daj mi jednostavan primjer programa koji prima argument --config i ispiše njegovu vrijednost. Objasni i što su positional i optional argumenti."

Ili za environment varijable:  
> "Kako u Pythonu pročitati environment varijablu? Daj primjer gdje ako varijabla PROMPT_GENERATOR_CONFIG postoji, uzme nju, inače default vrijednost 'config/default.yaml'."

## 2. Praktični zadatak: Refaktoriranje konfiguracije (hands-on)

Radit ćemo u istom repozitoriju. **Sve radimo na novom branchu!**.

Evo što želimo promijeniti

1. Korisnik po ulasku u aplikaciju dobiva na izbor koju konfiguraciju želi (koju tematiku)
  - Aplikacija treba dinamički učitati koje sve datoteke postoje u config/categories direktoriju, pa ih dati korisniku na izbor (npr. menu 1, 2, 3...)
  - Korisnik odabere tematiku, nakon toga ide aplikacija kao i do sada

2. Moguće je preskočiti ovo biranje tako da se aplikaciju pokreće s "komand argumentima"
  - Npr pokrenuti app s `python main.py --file free-time-hr` preskace odabir datoteke i odmah ucitava datoteku free-time-hr.yaml
  - Za ovo se koristi `argparse`, odn parser argumenata
  - Googlaj:
     - Sto je to argparse u Pythonu
     - Sto su to argumenti
     - Sto je to parser
  

### Korak po korak:

1. **Napravi novi feature branch**  
   - Ime brancha: `bartolinke/maint-config-refactor`  
   - Provjeri kako se branch zove: sadrzi 1. **tvoje ime**, i **kratki opis**
   - Prouci "Git naming conventions"

2. **Kreiraj novi direktorij i modul**  
   - Napravi folder `config/` (ako već ne postoji).  
   - Unutra napravi datoteku `__init__.py` (može biti prazna) i `config_manager.py`.
   - Pitaj se "Sto je to modul u pythonu"

3. **Implementiraj config_manager.py**  
   - Treba imati funkciju koja vraća putanju do YAML datoteke. Kako bi se ta funkcija zvala? Na primjer, `get_config_path()`
   - Logika (redoslijed provjere):  
     1. Ako je specificiran command-line argument `--config`, uzmi taj.  
     2. Ako postoji environment varijabla `PROMPT_GENERATOR_CONFIG`, uzmi nju.  
     3. Inače vrati default: `'config/categories/software-development.yaml'`  
   - Koristi `os.environ.get()` za environment varijable.

4. **Dodaj argparse u main datoteku** (vjerojatno `prompt_generator_cli.py` ili `main.py`)  

```python
import argparse

parser = argparse.ArgumentParser(description="Prompt Generator CLI")
parser.add_argument('--config', type=str, help='Putanja do konfiguracijske YAML datoteke')
args = parser.parse_args()
```

5. **Refaktoriraj glavni kod**  
   - Umjesto hard-coded `CONFIG_FILE = "config/categories/software-development.yaml"`  
   - Napisi kod koji koristi tu funkciju. Na primjer....

```python
from config.config_manager import get_config_path
config_file = get_config_path(args.config)
```

6. **Testiraj lokalno na više načina** (zabavan dio!)  
   - Pokreni bez argumenata → treba koristiti default.  
   - Pokreni sa `python main.py --config druga-konfig` (ovo znači da se koristi `config/categories/druga-config.yaml` datoteka
   - Postavi environment varijablu i pokreni program:  
     - Windows: `set PROMPT_GENERATOR_CONFIG=config/categories/treca.yaml`  
     - Mac/Linux: `export PROMPT_GENERATOR_CONFIG=config/categories/treca.yaml`

7. **Commitaj, pushaj i napravi Pull Request**  
   - Provjeri koji su sve elementi dobrog opisa git commita
   - Nesto poput: `MAINT - dodan config manager s podrškom za --config i env var`
   - Ovaj branch je i dalje "lokalan", sto sada zelimo s njim (da zavrsi u mainu)
   - Kako to uciniti? (Pushaj branch, napravi pull request, dodaj kratki opis)

## Na kraju dana
- Pošalji mi link na Pull Request.
- U evidenciju rada dodaj:
  - Što si novo naučio (argparse, env vars, SRP)
  - Kako si testirao da sve radi
  - Jesi li imao problema i kako si ih riješio

### Ako zaglaviš
(npr. “Ne radi mi argparse” ili “Kako importati modul iz podfoldera?”):  
Prvo pročitaj grešku. Zatim postavi AI-u:  
> "Imam grešku [kopiraj grešku točno]. Radim na prompt-generator-cli projektu, dodajem argparse i config_manager. Objasni mi korak po korak što nije u redu i kako popraviti."

Super posao dosad, Bartole! Danas ćeš napraviti pravi profesionalni refaktoring – ponosi se time! 🚀

Evo ti kompletne upute za treći dan u čistom Markdown formatu – možeš kopirati i poslati Bartolu direktno.
