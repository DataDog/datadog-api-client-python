"""
Create an annotation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.annotations_api import AnnotationsApi
from datadog_api_client.v2.model.annotation_color import AnnotationColor
from datadog_api_client.v2.model.annotation_create_attributes import AnnotationCreateAttributes
from datadog_api_client.v2.model.annotation_create_request import AnnotationCreateRequest
from datadog_api_client.v2.model.annotation_kind import AnnotationKind
from datadog_api_client.v2.model.annotation_request_data import AnnotationRequestData
from datadog_api_client.v2.model.annotation_type import AnnotationType

body = AnnotationCreateRequest(
    data=AnnotationRequestData(
        attributes=AnnotationCreateAttributes(
            color=AnnotationColor.BLUE,
            description="Deployed v2.3.1 to production.",
            page_id="dashboard:abc-def-xyz",
            start_time=1704067200000,
            type=AnnotationKind.POINT_IN_TIME,
            widget_ids=[
                "1234567890",
            ],
        ),
        type=AnnotationType.ANNOTATION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_annotation"] = True
with ApiClient(configuration) as api_client:
    api_instance = AnnotationsApi(api_client)
    response = api_instance.create_annotation(body=body)

    print(response)
