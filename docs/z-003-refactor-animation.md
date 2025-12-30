# Upute za Bartola - Treći radni dan

Danas ćemo raditi na **refaktoriranju animacija**. 

Trenutno su animacije (učitavanje aplikacije, generiranje prompta itd.) vjerojatno razbacane po glavnom kodu. To otežava održavanje. Naučit ćemo kako izdvojiti taj dio u zaseban modul – to je klasičan primjer **Single Responsibility Principle** (svaki modul radi samo jednu stvar).

Ovo je super vježba jer ćeš vidjeti kako kod postaje čišći, lakši za čitanje i testiranje.

## 1. Proučavanje: Što trebaš razumjeti prije rada (1-1.5 sat)

1. **Moduli u Pythonu** – kako kreirati i importati vlastite module.
2. **Single Responsibility Principle** – zašto je važno da jedan modul radi samo jednu stvar.
3. **Kako prebaciti funkcije u novi modul** bez da se kod pokvari.

### Preporučeni materijal:
- Kratki članak ili video: “Python modules explained for beginners”.
- “Single Responsibility Principle simple explanation” (traži na YouTubeu, 5-10 min video).

### Ako ti nešto nije jasno
(npr. “Kako točno importati funkciju iz drugog modula?”):  
Odi na Grok/ChatGPT i postavi:  
> "Objasni mi kao junior developeru kako kreirati novi Python modul (npr. animations.py), prebaciti u njega funkcije iz main.py i importati ih natrag. Daj jednostavan primjer prije i poslije."

Ili za SRP:  
> "Objasni mi Single Responsibility Principle na primjeru animacija u CLI aplikaciji. Zašto je bolje imati zaseban modul za animacije?"

## 2. Praktični zadatak: Refaktoriranje animacija (hands-on)

Radimo u istom repozitoriju **prompt-generator-cli**. **Sve radimo na novom branchu!**

### Korak po korak:

1. **Napravi novi feature branch**  
   - Ime brancha: `bartolinke/dan3-animacije`  
   - U GitHub Desktop-u ili terminalu: `git checkout -b bartolinke/dan3-animacije`

2. **Kreiraj novi modul za animacije**  
   - Napravi datoteku `animations.py` u korijenu projekta (ili u folderu `utils/` ako želiš bolju organizaciju).  
   - Ako napraviš folder, dodaj praznu `__init__.py` datoteku.

3. **Pronađi sve animacije u postojećem kodu**  
   - Traži funkcije ili kod koji radi animacije (npr. spinning loader, typing efekt, učitavanje aplikacije, generiranje prompta).  
   - Vjerojatno koristi biblioteke poput `time.sleep()`, `sys.stdout.write()`, `print("\r...", end="")` ili možda `rich`/`alive-progress`.

4. **Prebaci ih u animations.py**  
   - Kopiraj cijele funkcije u novi modul.  
   - Primjeri funkcija koje trebaš prebaciti:  
     - loading_animation()  
     - generating_animation()  
     - ili slično – ovisi o trenutnom kodu.  
   - Ako su animacije inline (bez funkcija), prvo ih pretvori u funkcije, pa prebaci.

5. **Importaj i koristi u glavnom kodu**  
   - U `prompt_generator_cli.py` ili `main.py` dodaj:  
     ```python
     from animations import loading_animation, generating_animation  # ili kako se zovu
     ```  
   - Zamijeni stare pozive novim importanim funkcijama.

6. **Testiraj detaljno** (zabavan dio!)  
   - Pokreni program više puta.  
   - Provjeri da li se animacije ponašaju **točno isto** kao prije (brzina, izgled, ne smije biti grešaka).  
   - Ako nešto ne radi, usporedi stari i novi kod liniju po liniju.

7. **Commitaj, pushaj i napravi Pull Request**  
   - Commit poruke npr.:  
     - "refactor: prebačene animacije u zaseban modul animations.py"  
     - "style: mala poboljšanja u animacijama" (ako si nešto popravio)  
   - Pushaj branch `bartolinke/dan3-animacije`  
   - Na GitHubu napravi PR prema mainu i dodaj opis:  
     > "Izvukao sam sve animacije u zaseban modul animations.py radi bolje organizacije i Single Responsibility Principle."

## Na kraju dana
- Pošalji mi link na Pull Request.
- U svoj privatni repo za izvještaje dodaj:
  - Što si novo naučio (moduli, refaktoring, SRP)
  - Koliko animacija si prebacio i jesu li sve radile odmah
  - Jesi li imao problema i kako si ih riješio (AI, čitanje grešaka...)

### Ako zaglaviš
(npr. “Nakon importanja animacija ne radi” ili “Ne znam gdje su točno animacije u kodu”):  
Prvo pokreni program i vidi grešku. Zatim postavi AI-u:  
> "Imam grešku [točno kopiraj grešku]. U projektu prompt-generator-cli prebacio sam animacije u animations.py, ali sada ne radi [opis problema]. Objasni mi korak po korak što provjeriti i popraviti."

Odličan posao, Bartole! Danas ćeš napraviti pravi "clean code" refaktoring i kod će izgledati puno profesionalnije. 🚀
