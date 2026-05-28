"""
Delete an annotation returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.annotations_api import AnnotationsApi

# there is a valid "annotation" in the system
ANNOTATION_DATA_ID = environ["ANNOTATION_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_annotation"] = True
with ApiClient(configuration) as api_client:
    api_instance = AnnotationsApi(api_client)
    api_instance.delete_annotation(
        annotation_id=ANNOTATION_DATA_ID,
    )
