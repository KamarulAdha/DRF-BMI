from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from decimal import *
getcontext().prec = 2

from bmi import serializers
# Create your views here.


class BMICalculatorAPIView(APIView):
    """APIView for BMI Calculator"""
    serializer_class = serializers.BMISerializer

    def get(self, request, format=None):
        """Returns a list in JSON format"""
        desc = [
            'This endpoint accepts Height(cm) and Weight(kg)',
            'It will take those data to calculate the BMI',
            'Formula for BMI = weight/(height**2)',
        ]

        return Response({'Message': 'Hello & Welcome!', 'Description': desc}, status=status.HTTP_200_OK)


    def post(self, request):
        """POST height and weight"""
        serializer = self.serializer_class(data=request.data)

        def get_bmi_status(bmi):
            if(bmi<18.5):
                return ("Underweight")
            elif(bmi>=18.5 and bmi<=24.9):
                return ("Normal Weight")
            elif(bmi>=25 and bmi<=29.9):
                return ("Overweight")
            else:
                return ("Obesity")

        try:
            if serializer.is_valid():
                height = serializer.validated_data.get('height')
                weight = serializer.validated_data.get('weight')

                newHeight = round(((height/100)**2),2)
                bmi = round((weight/newHeight),2)

                resHeight = f'{height} cm'
                resWeight = f'{weight} kg'
                resBMI = f'{bmi} kg/m2'
                resStatus = get_bmi_status(bmi)

                return Response({'Weight': resWeight, 'Height': resHeight, 'BMI': resBMI, 'Status': resStatus}, status=status.HTTP_200_OK)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # return Response({'Error Message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'Error Message': 'Invalid Parameters'}, status=status.HTTP_400_BAD_REQUEST)
