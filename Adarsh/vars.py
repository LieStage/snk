# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID',"4682685"))
    API_HASH = str(getenv('API_HASH',"3eba5d471162181b8a3f7f5c0a23c307"))
    BOT_TOKEN = str(getenv('BOT_TOKEN',"5553062054:AAEwtZ2XWJHF42qQc5Bi-5VkO5t2Si3YXc8"))
    name = str(getenv('SESSION_NAME', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL','-1001539366814'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "945284066").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = str(getenv('APP_NAME','unfortunate-malissa-aakash2021-cap.koyeb.app'))
    OWNER_USERNAME = str(getenv('OWNER_USERNAME',"FLIGHER"))
   # if 'DYNO' in environ:
       # ON_HEROKU = True
       # APP_NAME = str(getenv('APP_NAME',"filetolinktb")) #
    
  #  else:
    ON_HEROKU = False 
    
    #FQDN = str(getenv('FQDN',BIND_ADRESS)) if not ON_HEROKU or getenv(FQDN) else APP_NAME + "koyeb.app"
    FQDN = str(getenv('FQDN',APP_NAME))
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL',"mongodb+srv://video:merge@cluster0.km7eaiw.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "lion_stage"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
