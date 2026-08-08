log_server = {
    'server1': ['error', 'warning', 'error', 'info'],
    'server2': ['info', 'info', 'warning'],
    'server3': ['error', 'error', 'error', 'critical']
}
JumError = 0
for key, logIssue in log_server.items() :
    print(f"{key} : {len(set(logIssue))} Jenis Log Unik")
    for log in logIssue : 
        if log == 'error' : 
            JumError += 1
print(JumError)
nama_server = 'server'
while True :
                nama_server += str(input('Masukkan nombor Server : ')).lower()
                if nama_server == 'keluar' :
                    print('Terima Kasih')
                    break
                if nama_server in log_server.keys() : 
                      print(f"Jenis Log : {", ".join(set(log_server[nama_server]))}")
                else: 
                      print(f"Server {nama_server} tidak ada dalam senarai")
    