import json
from django.http import JsonResponse
from api.loadOntology import *


def filter_selector(request):
    my_data = request.POST.get('my_data')
    print(my_data)
    codes = my_data.split(',')
    allData = []
    for code in codes:
        if code == 'all':
            for i in getAllInfluencer():
                allData.append(i)
        elif code == 'youtube':
            for i in getYoutubeData():
                allData.append(i)
        elif code == 'tiktok':
            for i in getTiktokData():
                allData.append(i)
        elif code == 'instagram':
            for i in getInstagramData():
                allData.append(i)
    refinedData = []
    inside = False
    for code in codes:
        if code == 'high':
            inside = True
            print('inside high')
            for i in allData:
                if i['level'] == 'High':
                    refinedData.append(i)
        elif code == 'medium':
            inside = True
            for i in allData:
                if i['level'] == 'Medium':
                    refinedData.append(i)
        elif code == 'low':
            inside = True
            for i in allData:
                if i['level'] == 'Low':
                    refinedData.append(i)
        elif code == 'mediumhigh':
            inside = True
            for i in allData:
                if i['level'] == 'Medium_High':
                    refinedData.append(i)
        elif code == 'mediumlow':
            inside = True
            for i in allData:
                if i['level'] == 'Medium_Low':
                    refinedData.append(i)
    if inside == False:
        refinedData = allData
    response_data = {'data': refinedData}
    return JsonResponse(response_data)
