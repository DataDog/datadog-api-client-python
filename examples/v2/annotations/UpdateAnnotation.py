"""
Update an annotation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.annotations_api import AnnotationsApi
from datadog_api_client.v2.model.annotation_color import AnnotationColor
from datadog_api_client.v2.model.annotation_create_attributes import AnnotationCreateAttributes
from datadog_api_client.v2.model.annotation_kind import AnnotationKind
from datadog_api_client.v2.model.annotation_request_data import AnnotationRequestData
from datadog_api_client.v2.model.annotation_type import AnnotationType
from datadog_api_client.v2.model.annotation_update_request import AnnotationUpdateRequest

# there is a valid "annotation" in the system
ANNOTATION_DATA_ID = environ["ANNOTATION_DATA_ID"]

body = AnnotationUpdateRequest(
    data=AnnotationRequestData(
        attributes=AnnotationCreateAttributes(
            color=AnnotationColor.GREEN,
            description="Updated annotation.",
            page_id="dashboard:abc-def-xyz",
            start_time=1704067200000,
            type=AnnotationKind.POINT_IN_TIME,
        ),
        type=AnnotationType.ANNOTATION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_annotation"] = True
with ApiClient(configuration) as api_client:
    api_instance = AnnotationsApi(api_client)
    response = api_instance.update_annotation(annotation_id=ANNOTATION_DATA_ID, body=body)

    print(response)
