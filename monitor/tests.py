# from django.test import TestCase
import unittest
from unittest.mock import patch
# Create your tests here.
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from unittest.mock import patch
import psutil


class SystemMonitorTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='CS218')

    # Test CPU usage endpoint
    @patch('psutil.cpu_percent')
    def test_cpu_usage_success(self, mock_cpu_percent):
        # Mock the CPU usage to return 50%
        mock_cpu_percent.return_value = 50
        response = self.client.get('/api/cpu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cpu_usage'], '50%')

    @patch('psutil.cpu_percent', side_effect=Exception("CPU error"))
    def test_cpu_usage_failure(self, mock_cpu_percent):
        # Simulate an error during CPU fetch
        response = self.client.get('/api/cpu/')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], 'Could not fetch CPU usage.')

    # Test Memory usage endpoint
    @patch('psutil.virtual_memory')
    def test_memory_usage_success(self, mock_virtual_memory):
        mock_memory = unittest.mock.Mock()
        mock_memory.total = 8000000
        mock_memory.available = 4000000
        mock_memory.percent = 50
        mock_memory.used = 4000000
        mock_memory.free = 4000000
        mock_virtual_memory.return_value = mock_memory
        response = self.client.get('/api/memory/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['memory_usage_percent'], '50%')

    @patch('psutil.virtual_memory', side_effect=Exception("Memory error"))
    def test_memory_usage_failure(self, mock_virtual_memory):
        # Simulate an error during memory fetch
        response = self.client.get('/api/memory/')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], 'Could not fetch memory usage.')

    # Test Disk usage endpoint
    @patch('psutil.disk_usage')
    def test_disk_usage_success(self, mock_disk_usage):
        mock_disk = psutil._common.sdiskusage(total=1000000, used=500000, free=500000, percent=50)
        mock_disk_usage.return_value = mock_disk
        response = self.client.get('/api/disk/')
        self.assertIn('disk_usage_percent', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['disk_usage_percent'], '50%')

    @patch('psutil.disk_usage', side_effect=Exception("Disk error"))
    def test_disk_usage_failure(self, mock_disk_usage):
        # Simulate an error during disk fetch
        response = self.client.get('/api/disk/')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], 'Could not fetch disk usage.')

    # Test Bandwidth usage endpoint
    @patch('psutil.net_io_counters')
    def test_bandwidth_usage_success(self, mock_net_io_counters):
        mock_net_io = psutil._common.snetio(bytes_sent=1000000, bytes_recv=2000000, packets_sent=1000, packets_recv=2000, errin=0, errout=0, dropin=0, dropout=0)
        mock_net_io_counters.return_value = mock_net_io
        response = self.client.get('/api/bandwidth/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bytes_sent'], 1000000)
        self.assertEqual(response.data['bytes_received'], 2000000)

    @patch('psutil.net_io_counters', side_effect=Exception("Bandwidth error"))
    def test_bandwidth_usage_failure(self, mock_net_io_counters):
        # Simulate an error during bandwidth fetch
        response = self.client.get('/api/bandwidth/')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], 'Could not fetch bandwidth usage.')
