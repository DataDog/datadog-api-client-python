"""
Get widgets from an image returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.stegadography_api import StegadographyApi

configuration = Configuration()
configuration.unstable_operations["get_widgets_from_image"] = True
with ApiClient(configuration) as api_client:
    api_instance = StegadographyApi(api_client)
    response = api_instance.get_widgets_from_image()

    print(response)
