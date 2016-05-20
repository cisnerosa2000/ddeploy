import os
#A D deployment script
print "Dlang deployment script. Adrian Cisneros-2016"
print "Enter 'help' for more info.\n"

PATH = "/Users/cisnerosa/Documents/Programming/Languages/D/Projects"
os.chdir(PATH)

def exit(args):
    raise SystemExit(0)
def clear(args):
    rows, columns = os.popen('stty size', 'r').read().split()
    print "\n" * int(rows)
def show_help(args):
    print """
    Available commands and uses:
    
    current <no args>: display current D projects
    clear <no args>: clear the screen
    exit <no args>: exit ddeploy
    help <no args>: show this message again
    create <project_name>: create a new D project with the given name using DUB
    del <project_name>: delete the given project
    build <project_name>: compile the given project
    run <project_name>: run the given project
    dep <project_name>: list all dependencies of give project
    +dep <projectname> <name> <version>: add a dependency to the project
    -dep <project_name> <name>: see above, removes dependency
    open <project_name>: open the main source file of project
    open <project_name> -all: open all source files of project
    open <project_name> <file_name>...: open specified source file(s) of project
    display <project_name>: list all source files in project
    display <project_name> -p: list all product files in project
    """
def display(args):
    name = get_all_args(args)
    if name == None: return
    path = PATH + "/{}/source".format(name[0])
    
    if len(name) > 1 and name[1] == "-p":
        path = PATH + "/{}/products".format(name[0]) 
        
    files = os.listdir(path)
    print "Files in {} dir of {}:".format(path.split("/")[-1],name[0])
    for f in files:
        print ">   " + f
def dependencies(args):
    name = get_args(args)
    if name == None: return
    
    print "Current dependencies for {}: \n".format(name)
    
    pth = PATH + "/{}/dub.sdl".format(name)
    num = 0
    with open(pth,'r') as d:
        for line in d.readlines():
            if line.split(" ")[0] == "dependency":
                print "{}>".format(num),line
                num += 1
    if num == 0:
        print "No dependencies!"
    print
def add_dependency(args):
    arguments = get_all_args(args)
    if arguments == None: return
    project = arguments[0]
    d_name = arguments[1]
    version = arguments[2]
    
    pth = PATH + "/{}/dub.sdl".format(project)
    with open(pth,'a') as d:
        d.write('dependency "{}" version="~>{}"\n'.format(d_name,version))
        d.write("\n")
def remove_dependency(args):
    arguments = get_all_args(args)
    if arguments == None: return
    project = arguments[0]
    d_name = arguments[1]
    
    pth = PATH + "/{}/dub.sdl".format(project)
    lines = []
    with open(pth,'r') as f:
        for line in f.readlines():
            if line.split(" ")[0] != "dependency" or line.split(" ")[1].replace('"','') != d_name:
                lines.append(line)
    with open(pth,'w') as f:
        for line in lines:
            f.write(line)
                
    
    
def open_project(args):
    name = get_all_args(args)
    if name == None: return
    if len(name) == 1:
        path = PATH + "/{}/source/app.d".format(name[0])
        os.system("open {}".format(path))
    elif name[1] == "-all":
        path = PATH + "/{}/source/".format(name[0])
        files = os.listdir(path)
        for f in files:
            if f[-1] == "d":
                p = path + f
                os.system("open {}".format(p))
    elif len(name) > 1:
        for f in name[1:]:
            if f[-1] != "d": f = f[:-1] + "d"
            path = PATH + "/{}/source/{}".format(name[0],f)
            os.system("open {}".format(path))
        
        
        
    
def build(args):
    name = get_args(args)
    if name == None: return
    
    if "products" not in os.listdir(PATH + "/" + name):
        os.mkdir(name + "/products")
    fpath = "{}/source/".format(PATH + "/{}".format(name))
    files = []
    for f in os.listdir(fpath):
        if f[-1] == "d" and f != "app.d":
            path = "-I {}/{}/source/{}".format(PATH,name,f)
            files.append(path)
        elif f[-1] == "d":
            path = "{}/{}/source/{}".format(PATH,name,f)
            files.append(path)
        
    os.chdir(name + "/products")
    string = ""
    for path in files:
        string += (" " + path)
    os.system("dmd {}".format(string))
    os.chdir(PATH)
def run(args):
    name = get_args(args)
    if name == None: return
    exec_path = PATH + "/" + name + "/products"
    
    build(args)
    os.chdir(exec_path)
    os.system("./app")
    os.chdir(PATH)

def current(args):
    projects = os.listdir(PATH)[1:]
    print "PROJECTS:"
    print "-" * 30
    print ":",
    for i in projects: print i + " : ",
    print
    print "-" * 30
def new(args):
    name = get_args(args)
    if name == None: return
    os.system("dub init {}".format(name))
    os.chdir(PATH)
def delete(args):
    name = get_args(args)
    if name == None: return
    print "Are you sure you want to delete {}? It will be gone forever.".format(name)
    if raw_input("y/n: ") == "y":
        os.system("rm -rf {}".format(name))
        print "Deleted project {}".format(name)
        
    else:
        print "Aborted"
def parse(text):
    if text.split(" ")[0] in ACTIONS:
        ACTIONS[text.split(" ")[0]](text)
def get_args(text):
    args = None
    try:
        args = text.split(" ")[1]
    except IndexError:
        print "Invalid arguments"
        return
    return args
def get_all_args(text):
    args = None
    try:
        args = text.split(" ")[1:]
    except IndexError:
        print "Invalid arguments"
        return None
    return args
ACTIONS = {
    "current":current,
    "create":new,
    "del":delete,
    "build":build,
    "run":run,
    "open":open_project,
    "dep":dependencies,
    "+dep":add_dependency,
    "-dep":remove_dependency,
    "display":display,
    "clear":clear,
    "help":show_help,
    "exit":exit,
}
while True:
    parse(raw_input("--> "))
    
