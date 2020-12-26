from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "b1d1ff756amshdae80c43fac4fb5p143f28jsnaca646664475",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

#print(response.text)



# Create your views here.
def helloworld(request):
    mylist = []
    n = int(response['results'])
    for x in range(0, n):
        mylist.append(response['response'][x]['country'])
    
    if request.method == 'POST':
        selected_country = request.POST['selected_country']
        for x in range(0, n):
            if selected_country == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        found = 'yes'
        context = {'found':found,'scountry':selected_country,'mylist':mylist,'new': new, 'active': active, 'critical': critical, 'recovered': recovered, 'total': total, 'deaths': deaths}
        return render(request,'hw.html',context)
    
    found = 'no'
    context = {'mylist' : mylist,'found':found}
    #context = {'response' : response['results'][0]}
    return render(request,'hw.html',context)