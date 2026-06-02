"""
Get widgets from an image returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.stegadography_api import StegadographyApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StegadographyApi(api_client)
    response = api_instance.get_stegadography_widgets(
        image=open("fixtures/stegadography/image.png", "rb"),
    )

    print(response)
