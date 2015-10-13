# coding=utf8
from django.shortcuts import render_to_response
import requests
import json

# Create your views here.
ligong_url = 'http://scc.whut.edu.cn/getdate.ashx'
ligong_url2 = 'http://scc.whut.edu.cn/vjread.aspx'


def index(request):
    data = {'year': 2015, 'month': 10}
    r = requests.post(ligong_url, data=data)
    a = r.text.split('},{')
    a[0] = a[0][2:]
    a[len(a)-1] = a[len(a)-1][:-2]
    for i in range(0, len(a)):
        a[i] = a[i][:-1]
        a[i] = a[i].replace('status:false,', '').replace('status:true,', '').replace('msg:"', '').replace('vjread.aspx', ligong_url2)
   
    return render_to_response('index.html', locals())
