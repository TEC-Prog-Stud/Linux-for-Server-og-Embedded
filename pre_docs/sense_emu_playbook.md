# Adventures using sense hat emulator

Se: <https://sense-emu.readthedocs.io/en/v1.1/index.html>

- [Adventures using sense hat emulator](#adventures-using-sense-hat-emulator)
  - [Installation](#installation)
    - [Løsning?](#løsning)
  - [første forsøg](#første-forsøg)
  - [automatisk til og fra](#automatisk-til-og-fra)

## Installation

Jeg har valgt pip-installation, for at gøre installationen mest muligt reproducerbar. Derfor skal man installere nogen support moduler manuelt :-(

Se: <https://sense-emu.readthedocs.io/en/v1.1/install.html#alternate-platforms>

Dog har jeg også valgt pipenv, så min instgallations komando er:

    pipenv install sense-emu --dev

Jeg burde kunne starte gui'en på emulatoren, men der mangler noget:

    $ sense_emu_gui
    
    Traceback (most recent call last):
    File "/home/soren/.local/share/virtualenvs/kompas-pJXt-fLC/bin/sense_emu_gui", line 5, in <module>
        from sense_emu.gui import main
    File "/home/soren/.local/share/virtualenvs/kompas-pJXt-fLC/lib/python3.8/site-packages/sense_emu/gui.py", line 42, in <module>
        import gi
    ModuleNotFoundError: No module named 'gi'

I manualen står der at jeg skal bruge et gui-lib-modul `python3-gi`, så det prøver jeg:

    $ sudo apt install python3-gi
    [sudo] password for soren: 
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    python3-gi is already the newest version (3.36.0-1).
    python3-gi set to manually installed.
    The following packages were automatically installed and are no longer required:
    libpython2-stdlib libpython2.7-minimal libpython2.7-stdlib python2 python2-minimal python2.7 python2.7-minimal python3-appdirs python3-distlib python3-filelock
    python3-importlib-metadata python3-more-itertools python3-virtualenv python3-virtualenv-clone python3-zipp
    Use 'sudo apt autoremove' to remove them.
    0 upgraded, 0 newly installed, 0 to remove and 1 not upgraded.

Ikke så godt...

### Løsning?

Jeg kryber til korset og installerer de binære pakker:

    sudo apt install python-sense-emu python3-sense-emu sense-emu-tools


Jeg burde nok have udeladt python2 pakken (`python-sense-emu`):

    sudo apt install python3-sense-emu sense-emu-tools


## første forsøg

## automatisk til og fra