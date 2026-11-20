# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.ddsql_table_request_request_type import DDSQLTableRequestRequestType
    from datadog_api_client.v1_20270101.model.ddsql_table_request_response_format import DDSQLTableRequestResponseFormat


class DDSQLTableRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.ddsql_table_request_request_type import DDSQLTableRequestRequestType
        from datadog_api_client.v1_20270101.model.ddsql_table_request_response_format import (
            DDSQLTableRequestResponseFormat,
        )

        return {
            "ddsql_query": (str,),
            "request_type": (DDSQLTableRequestRequestType,),
            "response_format": (DDSQLTableRequestResponseFormat,),
        }

    attribute_map = {
        "ddsql_query": "ddsql_query",
        "request_type": "request_type",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        ddsql_query: str,
        request_type: DDSQLTableRequestRequestType,
        response_format: DDSQLTableRequestResponseFormat,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: DDSQLTableRequestRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: DDSQLTableRequestResponseFormat
        """
        super().__init__(kwargs)

        self_.ddsql_query = ddsql_query
        self_.request_type = request_type
        self_.response_format = response_format
