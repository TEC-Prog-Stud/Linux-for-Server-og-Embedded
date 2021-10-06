# Kompas med Raspberry Pi

- [Kompas med Raspberry Pi](#kompas-med-raspberry-pi)
  - [Raspberry Pi Sense-hat har et kompas](#raspberry-pi-sense-hat-har-et-kompas)
  - [UML design](#uml-design)
    - [Handlinger](#handlinger)
    - [Ansvar for viden](#ansvar-for-viden)
    - [Objekter](#objekter)
    - [Ansvar](#ansvar)
  - [Test first](#test-first)
    - [Test typer](#test-typer)
    - [Design patten](#design-patten)
  - [Doxygen muligheder](#doxygen-muligheder)
    - [Doxy file](#doxy-file)
    - [HTML header](#html-header)

Ideen med dette projekt er at lave et eksemplarisk projekt, til faget `Linux rettet mod Server og Embedded 16744`.

Med applikationen kan man bruge en Raspberry Pi med SenseHAT, som kompas.
Det skal altså vises (semi)grafisk i hvilken retning nord er, kontinuerligt.

Programmet skal skrives i python.
Det skal både være muligt at starte programmet fra kommandolinien, og lade det køre som en service.
Der skal være test med ** unittest og integrationstest.
En egentlig brugertest, forventes ikke.  (Men måske...)

Programmet dokumenteres med en webside, delvist genereret i doxygen. 
På websiden skal man kunne aflæse pi'ens aktuelle vinkel til nord, hvilket sker med en service, som kører et api som anvender flask. Websiden har et javascript der "requester" fra api'et med et defineret interval.
Se https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#implementing-our-api og https://whitefoxcreative.com/developers/ajax/using-ajax-to-reload-only-a-div/

Desuden et par man sider, som også delvist genereres i doxygen.

## Raspberry Pi Sense-hat har et kompas

Egentlig er det et magnetometer, men det bør pege mod nord. Især hvis der ikke er andre kraftige magneter i nærheden.

// TODO: hvilken chip, er kompas?

HArdwaret kan tilsyneladende emuleres med dette: <https://sense-emu.readthedocs.io/en/v1.1/install.html>

// TODO Check det ()Sense-emu ud!

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
  * visuelt kompas
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

// TODO: uml diagrammer => sequence


<!--

@startuml

class MagneticCompas {
    -angle
    -misrepresentation
    setMisrepresentation()
    getAngle()
    getCorrectedAngle()
}

class DisplayCompas {
    currentPixelX
    currentPixelY
    -previeusPixelX
    -previeusPixelY

    {x, y} angleToPixel(angle)
    setCurrentPixel(x, y)
}

@enduml

-->

![README](https://www.plantuml.com/plantuml/svg/PP312eCm38RlVOeU5RPtSBYhiCCEynXga49jfOb34TzzDIBJhQVc-__cJreGG-IXSqeP1qIwWjOZMrE6hWVIizBfNC6t3hThPobY7v7GCx0DNZ0XLxz2belK8j_Mvz-o336YOMnslkpfTqkzW-aKReRazlom8xhN7wctgLBks-901zUPrKhWF5xqj6ZPvnb4oQJ8zpNAG_DiTSju1Vec_T87 "README")


## Test first

I Eksemplet følger vi strategien "test first", hvor vi altså skriver test for en feature først, og derefter implementerer kode så testen opfyldes.

I det endelige resultat kan det være lidt svært at se historikken, men hvis man kigger tilbage i git loggen kan det være det bliver tydeligt. På den anden side betyder denne funktionalitet at vi hele tiden skrive skiftevis test og kode. Derfor ville det være urimelig besværligt at vedligeholde en adskilt branch for testen. Vi ville skulle flette (merge) disse branches hele tiden.

### Test typer

Det test vi skriver er primært unittest. Men der er også nogle test hvor vi tester at hardware'et reagerer som forventet når vi gør på en bestemt måde med det. Det høre til typen integrationstest.

[The different types of software testing](https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing)

### Design patten

Vi bygger så hvidt muligt testene med design patten'et `Arrange -> Act -> Assert` design-pattern'et.  
Det betyder, ganske enkelt, at vi først arrangerer de data eller tilstande der forudsættes for at kunne teste den del der er under test (`arrange`). Der efter udføres en handling (`act`), som vi skal teste udfaldet af. Det vil for det meste være den funktion vi skal teste. Til sidst skriver vi de antagelser der skal opfyldes for at det hele virker som det skal, og testen er i orden (`Assert`).  
Se gerne  eksemplet herunder, men bemærk at de ikke bruger python librariet `unittest`, som vi gør i dette projekt eksempel.

[ARRANGE-ACT-ASSERT: A PATTERN FOR WRITING GOOD TESTS](https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/)

## Doxygen muligheder

Doxygen kan både bruges til at lave en beskrivelse af hele projektet, semi-autogenereret kode dokumentation, og generere `man`-sider.

### Doxy file

### HTML header

vi vil gerne have den aktuelle kompasretning, udskrevet som et tal øverst i dokumentationen hoved, på web siden. Ved kompasretning forstås som vinklen til nord mod højre.  
Dette gør vi ved at lave et `javascript` i `doxygen`s html header tamplate. Så vi laver en kopi af den originale, og indsætter et script i den. Doxygen skal så bare konfigureres til at inkludere vores version af header-template'en.
Javascriptet, lavet et request hvert x sekund til endnu en service, som som henter kompasvinklen fra senseHAT'en.
