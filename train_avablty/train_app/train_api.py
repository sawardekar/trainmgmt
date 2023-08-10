from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Compartment, SeatAvabilty
import logging, traceback

logger = logging.getLogger('django')


@csrf_exempt
@api_view(['GET'])
def check_seat(request):
    try:
        get_data = request.query_params
        train_id = get_data.get('train_id', None)
        if train_id:
            result = {}
            seat_list = SeatAvabilty.objects.select_related().filter(train_id=train_id,status='Open').all()
            result["train_id"] = train_id
            result['seat_available'] = {}
            if seat_list:
                for i in seat_list:
                    comp = i.comp_id_id
                    seat_no = i.seat_no
                    comp_obj = Compartment.objects.select_related().filter(comp_id=comp)
                    comp_name = comp_obj[0].name if comp_obj else ''
                    if comp_name and comp_name not in result['seat_available']:
                        result['seat_available'][comp_name] = []
                    result['seat_available'][comp_name].append(seat_no)

            return Response({
                "success": True,
                "data": {
                    "result": result
                }
            })
    except Exception as e:
        logger.error('Error while fetching check_seat method. Error:{} stacktrace:{}'.format(e, traceback.format_exc()))
        return Response({
            "success": False,
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def available_seat(request):
    try:
        train_id = request.data.get("train_id",None)
        members = request.data.get("members",None)
        message={}
        if train_id:
            result = {}
            seat_list = SeatAvabilty.objects.select_related().filter(train_id=train_id,status='Open').all()
            result["train_id"] = train_id
            result['seat_available']={}
            if seat_list:
                for i in seat_list:
                    comp = i.comp_id_id
                    seat_no = i.seat_no

                    comp_obj = Compartment.objects.select_related().filter(comp_id=comp)

                    comp_name = comp_obj[0].name if comp_obj else ''
                    if comp_name and comp_name not in result['seat_available']:
                        result['seat_available'][comp_name] =[]
                    result['seat_available'][comp_name].append(seat_no)

            len_first=0
            len_second=0
            len_general=0

            for key,val in result.items():
                if isinstance(val,dict):
                    if "First Class" in val:
                        len_first = len(val["First Class"])
                    if "Second Class" in val:
                        len_second = len(val["Second Class"])
                    if "General" in val:
                        len_general = len(val["General"])
            total_len = len_first+len_second+len_general

            if total_len>members:
                message["message"] = "We have seats available"
            else:
                message["message"] = "We have seats enough available for First Class {}, Second Class {}, General Class {}".\
                    format(len_first,len_second,len_general)

            return Response({
                "success": True,
                "data": {
                    "result": message
                }
            })

    except Exception as e:
        logger.error('Error while fetching available_seat method. Error:{} stacktrace:{}'.format(e, traceback.format_exc()))
        return Response({
            "success": False,
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def update_seats(request):
    try:
        data = request.data
        seat_list=[]
        for i in data:
            seat_obj = SeatAvabilty.objects.filter(train_id=i['train_id'], comp_id=i['comp_id'], seat_no=i['seat_no'])
            if seat_obj:
                SeatAvabilty.objects.filter(seat_id=seat_obj[0].seat_id).update(
                    user_name=i['user_name'], user_pancard=i['user_pancard'], user_mobile=i['user_mobile'])
                seat_list.append(seat_obj[0].seat_id)

        return Response({
            "success": True,
            "data": seat_list
        })

    except Exception as e:
        logger.error('Error while fetching update_seats method. Error:{} stacktrace:{}'.format(e, traceback.format_exc()))
        return Response({
            "success": False,
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def book_seats(request):
    try:
        seat_list = request.data.get('seat_list',[])
        payment_status = request.data.get('payment_status',None)
        if seat_list and payment_status == 'paid':
            SeatAvabilty.objects.filter(seat_id__in=seat_list).update(
                status='Reserved')

        return Response({
            "success": True,
            "data": "Seat are reserved"
        })

    except Exception as e:
        logger.error('Error while fetching book_seats method. Error:{} stacktrace:{}'.format(e, traceback.format_exc()))
        return Response({
            "success": False,
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)