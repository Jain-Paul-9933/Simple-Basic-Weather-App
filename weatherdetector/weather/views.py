from django.shortcuts import render
#to set up openweatherapp api key
import json
import urllib.request

def index(request):
    if request.method=='POST':
        city=request.POST.get('city')
        res=urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='
            +city+'&appid=19431f95fe8a0381b648b0638d7f1bac'
            ).read()
        json_data=json.loads(res)
        data={
            "country_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon'])
            +' '+ str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'k',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
            }
    else:
        city=''
        data={}
    return render(request,'index.html',{'city':city,'data':data})
