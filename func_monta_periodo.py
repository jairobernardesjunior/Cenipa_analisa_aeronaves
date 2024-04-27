# monta período com a hora
def monta_periodo(ts):
    if (ts.hour > 6) and (ts.hour < 12):
        return '06:00 às 12:00'
    elif (ts.hour > 12) and (ts.hour < 18):
        return '12:00 às 18:00'
    elif (ts.hour > 18):
        return '18:00 às 00:00'    
    else:
        return '00:00 às 06:00' 