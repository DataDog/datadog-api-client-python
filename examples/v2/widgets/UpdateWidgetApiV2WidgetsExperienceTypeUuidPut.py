"""
Update a widget returns "Successful Response" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.widgets_api import WidgetsApi
from datadog_api_client.v2.model.create_or_update_widget_request_attributes import CreateOrUpdateWidgetRequestAttributes
from datadog_api_client.v2.model.create_or_update_widget_request_jsonapi_request_document import (
    CreateOrUpdateWidgetRequestJSONAPIRequestDocument,
)
from datadog_api_client.v2.model.create_or_update_widget_request_resource_object_request import (
    CreateOrUpdateWidgetRequestResourceObjectRequest,
)
from datadog_api_client.v2.model.definition import Definition
from datadog_api_client.v2.model.error_links import ErrorLinks
from datadog_api_client.v2.model.error_source import ErrorSource
from datadog_api_client.v2.model.widget_error_input import WidgetErrorInput
from datadog_api_client.v2.model.widget_experience_type import WidgetExperienceType
from datadog_api_client.v2.model.widget_links import WidgetLinks
from datadog_api_client.v2.model.widget_resource_object_input import WidgetResourceObjectInput
from datadog_api_client.v2.model.widget_type import WidgetType
from uuid import UUID

body = CreateOrUpdateWidgetRequestJSONAPIRequestDocument(
    data=CreateOrUpdateWidgetRequestResourceObjectRequest(
        attributes=CreateOrUpdateWidgetRequestAttributes(
            definition=Definition(
                requests=[
                    dict(
                        [
                            (
                                "queries",
                                "[{'data_source': 'metrics', 'name': 'query1', 'query': 'avg:system.cpu.user{*}'}]",
                            ),
                            ("response_format", "timeseries"),
                        ]
                    ),
                ],
                time=dict([("type", "live"), ("unit", "day"), ("value", "30")]),
                title="My Timeseries Widget",
                type=WidgetType.TIMESERIES,
            ),
            tags=[],
        ),
        id=None,
        lid=None,
        links=WidgetLinks(
            described_by=None,
            first=None,
            last=None,
            next=None,
            prev=None,
            related=None,
            self=None,
        ),
        meta=None,
        relationships=None,
        type="",
    ),
    errors=[
        WidgetErrorInput(
            code=None,
            detail=None,
            id=None,
            links=ErrorLinks(
                about="",
            ),
            meta=None,
            source=ErrorSource(
                header=None,
                parameter=None,
                pointer=None,
            ),
            status=None,
            title=None,
        ),
    ],
    included=[
        WidgetResourceObjectInput(
            attributes=None,
            id="",
            links=WidgetLinks(
                described_by=None,
                first=None,
                last=None,
                next=None,
                prev=None,
                related=None,
                self=None,
            ),
            meta=None,
            relationships=None,
            type="",
        ),
    ],
    links=WidgetLinks(
        described_by=None,
        first=None,
        last=None,
        next=None,
        prev=None,
        related=None,
        self=None,
    ),
    meta=None,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = WidgetsApi(api_client)
    response = api_instance.update_widget_api_v2_widgets_experience_type_uuid_put(
        uuid=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), experience_type=WidgetExperienceType.CCM_REPORTS, body=body
    )

    print(response)
