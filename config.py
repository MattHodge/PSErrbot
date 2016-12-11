import logging
import os

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

# BACKEND = 'Text'  # Errbot will start in text mode (console only mode) and will answer commands from there.
BACKEND = 'Slack'

# check if running in docker
BOT_DATA_DIR = r'/errbot/data' if os.path.isfile('/.dockerenv') else r'./data'
BOT_EXTRA_PLUGIN_DIR = r'/errbot/plugins' if os.path.isfile('/.dockerenv') else r'./plugins'
BOT_LOG_FILE = r'/errbot/errbot.log' if os.path.isfile('/.dockerenv') else r'./errbot.log'

BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@hodge',)

BOT_ALT_PREFIXES = ('@bender',)
BOT_ALT_PREFIX_SEPARATORS = (':', ',', ';')
BOT_ALT_PREFIX_CASEINSENSITIVE = True

# for slack
CHATROOM_PRESENCE = ()

BOT_IDENTITY = {
    'token': os.environ.get('SLACK_API_KEY'),
}

DIVERT_TO_PRIVATE = ('help', 'about', 'status')

# Decativated: Flows, ChatRoom
CORE_PLUGINS = ('ACLs', 'Backup', 'Health', 'Help', 'Plugins', 'Utils', 'VersionChecker')

ACCESS_CONTROLS = {
    'Health*': {'allowrooms': ('#bot-admin',)},
    'uptime': {'allowusers': BOT_ADMINS},
    'plugins:*': {'allowusers': BOT_ADMINS},
}

HIDE_RESTRICTED_COMMANDS = False

SUPPRESS_CMD_NOT_FOUND = True