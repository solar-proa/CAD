import json


def parse_current_to_sizing(result):
    '''
    Solar Array output for each array
    Mppt output for each array
    Max of (Total battery input current / Total Mppt output current (DC bus))
    L array current result
    
    Pass into derating table
    
    Convert to AWG
    '''
    print(json.dumps(result))