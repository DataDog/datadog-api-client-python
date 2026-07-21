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
    from datadog_api_client.v2.model.ddsql_tabular_query_fetch_request_data import DdsqlTabularQueryFetchRequestData


class DdsqlTabularQueryFetchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ddsql_tabular_query_fetch_request_data import DdsqlTabularQueryFetchRequestData

        return {
            "data": (DdsqlTabularQueryFetchRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DdsqlTabularQueryFetchRequestData, **kwargs):
        """
        Wrapper for a DDSQL tabular query fetch request.

        :param data: JSON:API resource object for a DDSQL tabular query fetch request.
        :type data: DdsqlTabularQueryFetchRequestData
        """
        super().__init__(kwargs)

        self_.data = data
