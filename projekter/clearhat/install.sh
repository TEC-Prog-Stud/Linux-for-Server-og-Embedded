# run this script with `sudo install.sh`
# fir it must be executable: `chmod o+x ./install.sh`

cp ./clearhat.py /usr/bin/clearhat
chmod a+x /usr/bin/clearhat

# asumes that pandoc is installed... `sudo apt install pandoc`
pandoc clearhat.1.md -s -t man -o clearhat.1
gzip ./clearhat.1
cp ./clearhat.1.gz /usr/share/man/man1/
mandb
