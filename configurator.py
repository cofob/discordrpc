import pickle
active_drp = input('ACTIVE DRP: ').strip()
# active_status = input('ACTIVE STATUS: ').strip()
active_status = None
app_id = int(input('APP ID: '))
with open('config', 'wb') as f:
    pickle.dump({'addons': {'drp': active_drp, 'status': active_status}, 'app_id': app_id}, f)
