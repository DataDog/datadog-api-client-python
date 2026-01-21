"""
Get HAMR organization connection returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.high_availability_multi_region_api import HighAvailabilityMultiRegionApi

configuration = Configuration()
configuration.unstable_operations["get_hamr_org_connection"] = True
with ApiClient(configuration) as api_client:
    api_instance = HighAvailabilityMultiRegionApi(api_client)
    response = api_instance.get_hamr_org_connection()

    print(response)
