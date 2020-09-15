import psutil
import file_manager

def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
    listOfProcessObjects = []
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            # Check if process name contains the given name string.
            if processName.lower() in pinfo['name'].lower():
                listOfProcessObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listOfProcessObjects


list_of_games = ['apex', 'rocket', 'battlefield', 'arma3']

list_of_good_programms = ['clion', 'pycharm', 'webstorm', 'cura', 'fusion360']


def kill_games():
    for game in list_of_games:
        listOfProcessIds = findProcessIdByName(game)
        if len(listOfProcessIds) > 0:
            print('Process Exists | PID and other details are')
            for elem in listOfProcessIds:
                processID = elem['pid']
                processName = elem['name']
                print((processID, processName))
                p = psutil.Process(elem['pid'])
                try:
                   p.terminate()  # or p.kill()
                except:
                   print('dont have the rights to end' + processName)
                else:
                   print("terminated " + processName)
        else:
            print('No Running Process found with given text')


def count_time(time_intervall):

    bad = False
    good = False

    for game in list_of_games:
        listOfProcessIds = findProcessIdByName(game)
        if len(listOfProcessIds) > 0:
            bad = True
            break

    for programm in list_of_good_programms:
        listOfProcessIds = findProcessIdByName(programm)
        if len(listOfProcessIds) > 0:

            good = True
            break
    print(int(good*time_intervall),int(bad*time_intervall))

    if file_manager.add_time_to_today(good_add=int(good*time_intervall),bad_add=int(bad*time_intervall)):
        kill_games()


