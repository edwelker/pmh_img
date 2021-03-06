import sys, os

sys.stderr = sys.stdout
#print "Content-type: text/plain"
#print

homedir = '/home/welkere'
#the name of the current directory is the same as the env name
env_name =  os.path.basename(os.path.normpath(os.path.dirname(__file__)))

#venv_loc = homedir + '/env/' + env_name
#activate_loc = venv_loc + '/bin/activate_this.py'
#info_parent_loc = homedir + '/python'
#info_loc = info_parent_loc + '/' + env_name
#settings = env_name + '.settings'

venv_loc = '/home/welkere/env/pmh_img'
activate_loc = '/home/welkere/env/pmh_img/bin/activate_this.py'
parent_loc = '/home/welkere/python/pmh_img'
pmh_img_loc = '/home/welkere/python/pmh_img/pmh_img'
settings = 'pmh_img.settings'

os.environ['VIRTUAL_ENV'] = venv_loc 

venv = activate_loc
execfile(venv, dict(__file__=venv))

_project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#print _project_dir

# Add a custom Python path.
sys.path.insert(0, _project_dir)
sys.path.insert(0, pmh_img_loc)
#need to do this explicitly, since _project_dir is gonna be my staff directory,
#because that's where the cgi is 'running'
sys.path.insert(0, parent_loc)
sys.path.insert(0, os.path.dirname(_project_dir))

# Switch to the directory of your project. (Optional.)
os.chdir(pmh_img_loc)

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = settings

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
