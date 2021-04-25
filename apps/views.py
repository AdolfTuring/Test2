from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FunctionSerilizer
from .function import fun_a, fun_b, fun_c, fun_d, fun_e, fun_f


class AppsFunction(APIView):
    def get(self, request, format=None):
        return Response({"massage":"Input list of numbers and list of rules like - {''data'':[1,2,3], ''rule'':['a','b','c']}. Rules in range a-f "})
    def post(self, request, format=None):
        serializer=FunctionSerilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            datas=serializer.validated_data
            data=datas.get('data')
            rule=datas.get('rule')
            ls=['a','b','c','d','e','f']
            for x in data:
                if type(x)!=type(1) and type(x)!= type(1.5): return Response({"massage":"All number must be Int or Float"})
            for x in rule:
                if type(x)!=type('a'): return Response({"massage":"All rules must be Char"})
                elif x not in ls: return Response({"massage":f"Incorect rull -> {x}"})
            if len(data)!=len(rule): return Response({"massage":"Please input rule for every number"})
            ls=[]
            for x in range(len(data)):
                ls.append(eval(f'fun_{rule[x]}({data[x]})'))
            return Response({"result":ls})
        
            
# Create your views here.
