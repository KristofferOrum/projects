import os
import glob
import json
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient
from pprint import pprint
with open('settings.json') as data_file:    
    data = json.load(data_file)

#get folders in dir
directories = glob.glob("/Users/kristofferorum/Dropbox/projects/[0-9][0-9][0-9][0-9]*")
localNames = [ os.path.basename(os.path.normpath(element)).split(' ', 1 ) for element in directories]


# get notebooks from evernote
evernoteNames = []
dev_token = data['settings']['EvernoteToken']
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username
noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
# List all of the notebooks in the user's account
notebooks = noteStore.listNotebooks()
print "Found ", len(notebooks), " notebooks:"
for notebook in notebooks:
	temp = notebook.name.split(' ', 1 ) 
	if len(temp) == 1:
		print "short"
		temp.append("")
	print temp
	id = temp[0]
	if len(temp[0]) == 4 and temp[0].isdigit():	
		print "!"
		#temp.append = " "
		evernoteNames.append([temp[0],temp[1]])	
		#evernoteNames.append [temp[0],temp[1]]		
print evernoteNames