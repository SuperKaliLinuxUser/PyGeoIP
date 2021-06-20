import pygeoip # pip install pygeoip

DB = pygeoip.GeoIP('GeoLiteCity.dat')

def IP_INFO(IP):
    Data = DB.record_by_addr(IP)
    for Key, Value in Data.items():
        print("{0} : {1}".format(Key, Value))
    
while True:
    cmd = str(input("~ "))
    if cmd == 'quit':
        break
    
    if cmd == 'IP':
        ip = str(input("Enter IP address: "))
        try:
            IP_INFO(ip)
            
        except Exception as Error:
            print(Error)
        
        
        

