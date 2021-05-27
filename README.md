# Kompas med Raspberry Pi

Ideen med dette projekt er at lave et eksemplarisk projekt, til faget `Linux rettet mod Server og Embedded 16744`.

Med appliaktionen kan man bruge en Rapberry Pi med Sense HAT, som kompas.
Det skal altså vises (semi)grafisk i hvilken retning nord er, kontinuerligt.

Programmet skal skrives i python.
Det skal både være muligt at starte programmet fra kommandolinien, og lade det køre som en service.
Der skal være test med ** unittest og integrationstest.
En egentlig brugertest, forventes ikke.  (Men måske...)

Programmet dokumenteres med en webside, delvist genereret i doxygen. 
På websiden skal man kunne aflæse pi'ens aktuelle vinkel til nord, hvilket sker med en service, som kører et api som anvender flask. Websiden har et javascript der requester fra api'et med et defineret interval.

Desuden et par man sider, som også delvist genereres i doxygen.

## Raspbery Pi Sense-hat har et kompas

Egentlig er det et magnetometer, men det bør pege mod nord. Især hvis der ikke er andre kraftige magneter i nærheden.

// hvilken chip?

## UML design

En hurtig måde at udvikle et program design er ved tegne det i uml, på baggrund af en list over hvad der brug for at vi ved og hvilke handlinger der skal gøres med denne viden. Så kan man give objekter ansvar for at kende til denne viden, og foretage handlinger med den.

### Handlinger

* vis retning mod nord
* find retning mod nord
* find grader fra nord (i forhold til den side af raspi'en med usb-stikkene)
* omregn retning i grader til x,y pos på en pixel i kanten.
* tegn pil eller trekant ?
* opfang keybard `ctrl-c`
* opfang SIGTERM
* evt modregn for misvisning

### Ansvar for viden

* vinkel til nord
* mapping til pixel
* forrrige retning
* vinkel for misvisning (hvis misvisningen er linær hele vejen rundt?)

### Objekter

* kompas ? 
  * magnetisk kompas 
    * grundlæggende magnetometer
    * retning
  * visulet kompas
    * visning af retning
    * opdatering af display

### Ansvar

* Magnetisk kompas (`MagneticCompas`)
  * aflæser magnetometeret
  * kender retningen 
  * modregner misvisning
* Visuelt kompas (`DisplayCompas`)
  * omregner fra grader nord til pixel i kanten 
  * aktiverer led/pixel i retnng mod nord
  * deaktiverer pixel sidst aktiveret
  * 

/// uml diagrammer => klasser, sequence
## Test first

I Eksemplet følger vi strategiren test first, hvor vi altså skriver test for en feature først, og derefter implementerer kode så testen opfyldes.

I det endelige resultat kan det være lidt svært at se historikken, men hvis man kigger tilbage i git loggen kan det være det bliver tydeligt. På den anden side betyder denne funktionalitet at vi hele tiden skrive skiftevis test og kode. Derfor ville det være urimelig besværligt at vedligeholde en afskilt branch for testen. Vi ville skulle merge disse branches hele tiden.

### Test typer

Det test vi skriver er primært unittest. Men der er også nogle test hvor vi tester at harwaret reagerer som forventet når vi gør på en bestemt måde med det. Det høre til typen integrationstest.

[The different types of software testing](https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing)

### Design pattern

Vi bygger så hvidt muligt testene med designpatternet `Arrange -> Act -> Assert` design-pattern'et.  
Det betyder, ganske enkelt, at vi først arrangerer de data eller tilstande der forudsættes for at kunne teste den del der er under test (`arrange`). Der efter udføres en handling (`act`), som vi skal teste udfaldet af. Det vil for det meste være den funktion vi skal teste. Til sidst skriver vi de antagelser der skal opfyldes for at det hele virker som det skal, og testen er i orden (`Assert`).  
Se gerne  eksemplet herunder, men bemærk at de ikke bruger python librariet `unittest`, som vi gør i dette projekt eksempel.

[ARRANGE-ACT-ASSERT: A PATTERN FOR WRITING GOOD TESTS](https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/)

## Doxygen muligheder

Doxygen kan både bruges til at lave en beskrivels af hele projektet, semi-autogenreret kode dokumentation, og generere `man`-sider.

### Doxyfile

### HTML header

vi vil gerne have den aktuelle kompasretning, udskrevet som et tal øverst i demomentationen hoved, på web siden. Ved kompasretning forståes som vinklen til nord mod højre.  
Dette gør vi ved at lave et `javascript` i `doxygen`s html header tamplate. Så vi laver en kopi af den originale, og indsætter et script i den. Doxygen skal så bare konfigureres til at inkludere vores version af header-templaten.
Javascriptet, lavet et request hvert x sekundt til endnu en service, som som henter konpasvinklen fra sense hatten.
