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
    from datadog_api_client.v2.model.ddsql_tabular_query_response_data import DdsqlTabularQueryResponseData
    from datadog_api_client.v2.model.ddsql_tabular_query_response_meta import DdsqlTabularQueryResponseMeta


class DdsqlTabularQueryResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ddsql_tabular_query_response_data import DdsqlTabularQueryResponseData
        from datadog_api_client.v2.model.ddsql_tabular_query_response_meta import DdsqlTabularQueryResponseMeta

        return {
            "data": (DdsqlTabularQueryResponseData,),
            "meta": (DdsqlTabularQueryResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: DdsqlTabularQueryResponseData, meta: DdsqlTabularQueryResponseMeta, **kwargs):
        """
        Response envelope for both the execute and fetch DDSQL tabular query endpoints.
        Carries the JSON:API primary resource and a top-level ``meta`` block with
        request-scoped observability handles.

        :param data: JSON:API resource object for a DDSQL tabular query response.
        :type data: DdsqlTabularQueryResponseData

        :param meta: Top-level JSON:API meta block accompanying every DDSQL tabular query response.
            Carries standard observability handles for client-side correlation.
        :type meta: DdsqlTabularQueryResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
