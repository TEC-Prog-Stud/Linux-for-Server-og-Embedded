# How to use `pipenv`

- [How to use `pipenv`](#how-to-use-pipenv)
  - [Install](#install)
  - [Start "shell"](#start-shell)
  - [Add some requirements](#add-some-requirements)
  - [Check `Pipfile`](#check-pipfile)
  - [Check `Pipfile.lock`](#check-pipfilelock)
    - [Lås](#lås)
  - [Installer pakker](#installer-pakker)
  - [Fjerne pakker](#fjerne-pakker)
  - [Path](#path)
  - [Problem efter afskaffelse af miniconda](#problem-efter-afskaffelse-af-miniconda)
  - [Kilder](#kilder)

Pipenv er en relitivt ny ting (vist fra 2008), men først rigtigt kommet i fokus i '20erne.

Det virker en del som `npm` eller ligninde.

En alternativ løsning er Anaconda, miniconda eller bare conda. Som jo også har navn fra en slage, lige som Python.

## Install

    cd <some dir where project lives>
    pip install pipenv

## Start "shell"

    pipenv shell

## Add some requirements

    pipenv install sense-emu --dev

## Check `Pipfile`

    cat Pipfile

Pipfile indeholder de pakker der er installeret i denne shell/env/projekt.

## Check `Pipfile.lock`

    cat Pipfile.lock

Jeg tror at `Pipfile.lock` skal tilføjes til `.gitignore` fordi den _altid_ genereres af Pipenv.

### Lås 

    pipenv lock

Opdaterer `Pipfile.lock` med de versioner der aktuelt er installeret. Også sub-afhænigheder.

## Installer pakker

Man kan installere alle pakker i `Pipfile.lock` med kommandoen:

    pipenv install --ignore-pipfile

Som altså ignorerer `Pipfile`, men bruger `Pipfile.lock` i stedet for.

Hvis man ikke har lock filen, f.eks. fordi den ikke er med i git projektet, og bør kunne genereres automatisk, bruger man:

    pipenv install

eller eventuelt 

    pipenv install --dev

hvis der også er installleret dev pakker.

## Fjerne pakker 


## Path

pipenv har behov for path til `$HOME/bin` og `$HOME/.local/bin`. Dette har jeg fikset ved at tilføje:

    # set PATH so it includes user's private bin if it exists
    if [ -d "$HOME/bin" ] ; then
        PATH="$HOME/bin:$PATH"
    fi

    # set PATH so it includes user's private bin if it exists
    if [ -d "$HOME/.local/bin" ] ; then
        PATH="$HOME/.local/bin:$PATH"
    fi

til `~/.bashrc`

Jeg forstår ikke hvorfor installationen ikke har sørget for dette. Måske jeg havde miniconda installeret, og aktiv, mens jeg installerede _pipenv_.

## Problem efter afskaffelse af miniconda

MIniconda var installeret da jeg installerede og oprettede Pipenv, så det hele blev kludret sammen.

Jeg fjerne den aktuelle Pipenv, uden for `pipenv shell` (tast `exit`), og kør:

    pipenv -rm

Og så oprette et ny environment med 

    pipenv --python 3.8

Derefter shell'e ind i det virelle environment igen

    pipenv shell
    
Bemærk at kommando promten får tilføjet et `(kompas)` foran:

    (kompas) soren@soren-HP-ProBook-650-G2:~/Documents/TEC/Linux for Server og Embedded/kompas$ _


## Kilder

* <https://realpython.com/pipenv-guide/#reader-comments>