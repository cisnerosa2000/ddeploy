# ddeploy
Pretty much a python 2.7 script intended to be called from a shell script in /usr/bin/. Allows easier management of D/Dlang projects.
Assumes that you have the DMD compiler as well as DUB installed and are on OSX.

Example shell script:

python your/path/to/ddeploy.py "$@"


The "$@" passes command line arguments to ddeploy, like your project directory. Requires that you manually update ddeploy in order to receive updates.



An even better shell script:

python <(curl -s https://raw.githubusercontent.com/cisnerosa2000/ddeploy/master/ddeploy.py) "$@"

This script fetches the most recent commit to the ddeploy github and runs it, ensuring you always have the latest version of ddeploy. Keep in mind it is a little slower than the first script (depending on your internet speed). Again, the "$@" passes command line arguments to ddeploy. 


The only command line argument that ddeploy takes is optional. If you specify an absolute folder path, it will use that path as the place to find and create and work with your D projects. If not it will default to the hard-coded file path which is my personal D directory. I highly doubt they're exactly the same. For example, if I have a project folder called 'D\_Projects' in my desktop, I could run 'python ddeploy.py /users/my\_username/desktop/D\_projects' 

D expects your projects to be in this directory.