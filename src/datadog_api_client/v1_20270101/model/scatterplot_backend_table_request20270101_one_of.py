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
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request_any_of_any_of_item_request_type import (
        ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request_any_of_any_of_item_response_format import (
        ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat,
    )


class ScatterplotBackendTableRequest20270101OneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request_any_of_any_of_item_request_type import (
            ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType,
        )
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request_any_of_any_of_item_response_format import (
            ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat,
        )

        return {
            "ddsql_query": (str,),
            "request_type": (ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType,),
            "response_format": (ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat,),
        }

    attribute_map = {
        "ddsql_query": "ddsql_query",
        "request_type": "request_type",
        "response_format": "response_format",
    }

    def __init__(
        self_,
        ddsql_query: str,
        request_type: ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType,
        response_format: ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param ddsql_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type ddsql_query: str

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: ScatterplotBackendTableRequestAnyOfAnyOfItemRequestType

        :param response_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type response_format: ScatterplotBackendTableRequestAnyOfAnyOfItemResponseFormat
        """
        super().__init__(kwargs)

        self_.ddsql_query = ddsql_query
        self_.request_type = request_type
        self_.response_format = response_format
