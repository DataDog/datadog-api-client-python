# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.audit_stream_request_columns_items import AuditStreamRequestColumnsItems
    from datadog_api_client.v1_20270101.model.audit_stream_query import AuditStreamQuery
    from datadog_api_client.v1_20270101.model.audit_stream_request_response_format import (
        AuditStreamRequestResponseFormat,
    )


class AuditStreamRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.audit_stream_request_columns_items import (
            AuditStreamRequestColumnsItems,
        )
        from datadog_api_client.v1_20270101.model.audit_stream_query import AuditStreamQuery
        from datadog_api_client.v1_20270101.model.audit_stream_request_response_format import (
            AuditStreamRequestResponseFormat,
        )

        return {
            "columns": ([AuditStreamRequestColumnsItems],),
            "query": (AuditStreamQuery,),
            "response_format": (AuditStreamRequestResponseFormat,),
        }

    attribute_map = {
        "columns": "columns",
        "query": "query",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        columns: List[AuditStreamRequestColumnsItems],
        query: AuditStreamQuery,
        response_format: AuditStreamRequestResponseFormat,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [AuditStreamRequestColumnsItems]

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: AuditStreamQuery

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: AuditStreamRequestResponseFormat
        """
        super().__init__(kwargs)

        self_.columns = columns
        self_.query = query
        self_.response_format = response_format
