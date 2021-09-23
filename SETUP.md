## Mapper

Koden er organiseret så de egentlige programfiler ligger i undermappen `src` (eller under-mapper derunder).
Mappen `src` har en fil `__init__.py`. Denne er en tom fil som markerer for python, at mappen indeholder et _Module_.

UnitTests er placeret i mappen `test`. Her gælder det samme, at der er en tom fil `__init__.py`.
// TODO: Check om `__init__.py` er nødvendig i test

## Ørige mapper

### .vscode

I `.vscode`  ligger `extensions.json` med anbefalede udviddelser. Samt `settings.json` og `launch.json`, med opsætninger til at køre python og python test.

### demo

Er et demo projekt jeg har fundet inspiration til på nettet, og hurtigt flikket sammen, uden design overvejser.
Se bl.a. <https://projects.raspberrypi.org/en/projects/compass-maze/2>

### html_template

Filen header.html er taget fra Doxygen distributionen, og kan includeres ind i generering af html docs med DoxyGen. I header.html, kan indsættes javascript til at opdatere temperatur eller andet sjovt fra SenseHat'en.

### øvrige filer

* `calibrate.md` beskriver hvordan man kalibrerer magnetometeret...

* Doxyfile er indstillinger til Doxygen  
   // FIXME skal nok flyttes til en undermappe