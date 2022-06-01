# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuditLogsEventsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.audit_logs_event import AuditLogsEvent
        from datadog_api_client.v2.model.audit_logs_response_links import AuditLogsResponseLinks
        from datadog_api_client.v2.model.audit_logs_response_metadata import AuditLogsResponseMetadata

        return {
            "data": ([AuditLogsEvent],),
            "links": (AuditLogsResponseLinks,),
            "meta": (AuditLogsResponseMetadata,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(self, *args, **kwargs):
        """
        Response object with all events matching the request and pagination information.

        :param data: Array of events matching the request.
        :type data: [AuditLogsEvent], optional

        :param links: Links attributes.
        :type links: AuditLogsResponseLinks, optional

        :param meta: The metadata associated with a request.
        :type meta: AuditLogsResponseMetadata, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuditLogsEventsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
