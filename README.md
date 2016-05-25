# ddeploy
Pretty much a python 2.7 script intended to be called from a shell script in /usr/bin/. Allows easier management of D/Dlang projects.
Assumes that you have the DMD compiler as well as DUB installed and are on OSX.

Example shell script:
python your/path/to/ddeploy.py "$@"

The "$@" passes command line arguments to ddeploy, like your project directory. Requires that you manually update ddeploy in order to receive updates.

An even better shell script:
python <(curl -s https://raw.githubusercontent.com/cisnerosa2000/ddeploy/master/ddeploy.py) "$@"

This script fetches the most recent commit to the ddeploy github and runs it, ensuring you always have the latest version of ddeploy.