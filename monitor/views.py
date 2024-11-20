#from django.shortcuts import render
import psutil
import logging
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from .authentication import SharedAPIKeyAuthentication

# Create your views here.
#configure logging
logging.basicConfig(filename='system_stats.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@api_view(['GET'])
@authentication_classes([SharedAPIKeyAuthentication])
def cpu_usage(request):
    try:
        cpu_percent=psutil.cpu_percent(interval=1)
        logger.info(f'CPU usage requested: {cpu_percent}%')
        return Response({'cpu_usage': f'{cpu_percent}%'})
    except Exception as e: 
        logger.error(f'Error getting CPU usage: {str(e)}')
        return Response({'error': 'Could not fetch CPU usage.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([SharedAPIKeyAuthentication])
def memory_usage(request):
    try:
        memory_usage=psutil.virtual_memory()
        logger.info('Memory usage requested.')
        return Response({
            'total_memory': memory_usage.total,
            'used_memory' : memory_usage.used,
            'available_memory' : memory_usage.available,
            'memory_usage_percent': f'{memory_usage.percent}%'
        })
    except Exception as e:
        logger.error(f'Error getting memory usage: {str(e)}')
        return Response({'error': 'Could not fetch memory usage.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([SharedAPIKeyAuthentication])
def disk_usage(request):
    try:
        disk=psutil.disk_usage('/')
        logger.info('disk usage requested')
        return Response({
            'total_disk':disk.total,
            'used_disk': disk.used,
            'free_disk': disk.free,
            'disk_usage_percent': f'{disk.percent}%',
        })
    except Exception as e:
        logger.error(f'Error getting disk usage: {str(e)}')
        return Response({'error': 'Could not fetch disk usage.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([SharedAPIKeyAuthentication])
def bandwidth_usage(request):
    try:
        net_io = psutil.net_io_counters()
        logger.info('Bandwidth usage requested.')
        return Response({
            'bytes_sent': net_io.bytes_sent,
            'bytes_received': net_io.bytes_recv
        })
    except Exception as e:
        logger.error(f'Error getting bandwidth usage: {str(e)}')
        return Response({'error': 'Could not fetch bandwidth usage.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
