from django.shortcuts import render
import psutil
import logging
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
#configure logging
logging.basicConfig(filename='system_stats.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#API to get CPU Usage
@api_view(['GET'])
def cpu_usage(request):
    try:
        cpu_percent=psutil.cpu_percent(interval=1)
        logger.info(f'CPU usage requested: {cpu_percent}%')
        return Response({'cpu_usage':cpu_percent})
    except Exception as e: 
        logger.error(f'Error getting CPU usage: {str(e)}')
        return Response({'error': 'Could not fetch CPU usage.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def memory_usage(request):
    try:
        memory=psutil.virtual_memory()
        logger.info('Memory usage requested.')
        return Response({
            'total_memory': memory.total,
            'used_memory' : memory.used,
            'available_memory' : memory.available,
            'memory_usage_percent':memory.percent
        })
    except Exception as e:
        logger.error(f'Error getting memory usage: {str(e)}')
        return Response({'error': 'Could not fetch memory usage.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def disk_usage(request):
    try:
        disk=psutil.disk_usage('/')
        logger.info('disk usage requested')
        return Response({
            'total_disk':disk.total,
            'used_disk': disk.used,
            'free_disk': disk.free,
            'disk_usage_percent': disk.percent,
        })
    except Exception as e:
        logger.error(f'Error getting disk usage: {str(e)}')
        return Response({'error': 'Could not fetch disk usage.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
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