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
    from datadog_api_client.v2.model.ddsql_tabular_query_fetch_request_attributes import (
        DdsqlTabularQueryFetchRequestAttributes,
    )
    from datadog_api_client.v2.model.ddsql_tabular_query_fetch_request_type import DdsqlTabularQueryFetchRequestType


class DdsqlTabularQueryFetchRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ddsql_tabular_query_fetch_request_attributes import (
            DdsqlTabularQueryFetchRequestAttributes,
        )
        from datadog_api_client.v2.model.ddsql_tabular_query_fetch_request_type import DdsqlTabularQueryFetchRequestType

        return {
            "attributes": (DdsqlTabularQueryFetchRequestAttributes,),
            "type": (DdsqlTabularQueryFetchRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: DdsqlTabularQueryFetchRequestAttributes, type: DdsqlTabularQueryFetchRequestType, **kwargs
    ):
        """
        JSON:API resource object for a DDSQL tabular query fetch request.

        :param attributes: Attributes describing which previously submitted DDSQL query to fetch.
        :type attributes: DdsqlTabularQueryFetchRequestAttributes

        :param type: JSON:API resource type for a DDSQL tabular query fetch request.
        :type type: DdsqlTabularQueryFetchRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
