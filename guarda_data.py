import requests
import json
from concurrent.futures import ThreadPoolExecutor

class JPS:
    def requester(self):
        N=21224
        url = "https://integration.jps.go.cr/api/App/nuevostiempos/"
        for num in reversed(range(N + 1)) : 
            r = requests.get(url+str(num))   
            print(r.content, end = "\n")
            break

    def requester(self):
        N = 21224
        end_num = 17621
        url = "https://integration.jps.go.cr/api/App/nuevostiempos/"
        
        def make_request(num):
            try:
                r = requests.get(url + str(num))
                print(f"Request for {num} completed with status code {r.status_code}")
                return r.content
            except requests.RequestException as e:
                print(f"Error making request for {num}: {e}")
                return None
        
        with ThreadPoolExecutor(max_workers=15) as executor:
            results = list(executor.map(make_request, reversed(range(N, end_num - 1, -1))))
            results = list(set(results))

        for result in results:
            if result is not None:
                self.method_procesador(result)

    def method_procesador(self,val):
        objeto = json.loads(val)    
        if not objeto["manana"] is None:
            self.escritor(objeto["manana"]["numero"])
        if not objeto["mediaTarde"] is None:
            self.escritor(objeto["mediaTarde"]["numero"])
        if not objeto["tarde"] is None:
            self.escritor(objeto["tarde"]["numero"])
       
    def escritor(self, val):
        #print(val)
        with open('readme.txt', 'a') as f:
            f.write(str(val)+"\n")

obj = JPS()
obj.requester();