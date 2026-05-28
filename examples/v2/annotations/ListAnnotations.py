"""
List annotations returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.annotations_api import AnnotationsApi

# there is a valid "annotation" in the system
ANNOTATION_DATA_ATTRIBUTES_PAGE_ID = environ["ANNOTATION_DATA_ATTRIBUTES_PAGE_ID"]

configuration = Configuration()
configuration.unstable_operations["list_annotations"] = True
with ApiClient(configuration) as api_client:
    api_instance = AnnotationsApi(api_client)
    response = api_instance.list_annotations(
        page_id=ANNOTATION_DATA_ATTRIBUTES_PAGE_ID,
        start_time=1704067200000,
        end_time=1704153600000,
    )

    print(response)
