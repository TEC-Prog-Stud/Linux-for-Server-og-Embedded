# How to use `pipenv`

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

