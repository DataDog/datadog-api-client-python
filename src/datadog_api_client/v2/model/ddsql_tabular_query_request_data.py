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
    from datadog_api_client.v2.model.ddsql_tabular_query_request_attributes import DdsqlTabularQueryRequestAttributes
    from datadog_api_client.v2.model.ddsql_tabular_query_request_type import DdsqlTabularQueryRequestType


class DdsqlTabularQueryRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ddsql_tabular_query_request_attributes import (
            DdsqlTabularQueryRequestAttributes,
        )
        from datadog_api_client.v2.model.ddsql_tabular_query_request_type import DdsqlTabularQueryRequestType

        return {
            "attributes": (DdsqlTabularQueryRequestAttributes,),
            "type": (DdsqlTabularQueryRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: DdsqlTabularQueryRequestAttributes, type: DdsqlTabularQueryRequestType, **kwargs):
        """
        JSON:API resource object for a DDSQL tabular query execution request.

        :param attributes: Attributes describing the DDSQL query to execute.
        :type attributes: DdsqlTabularQueryRequestAttributes

        :param type: JSON:API resource type for a DDSQL tabular query request.
        :type type: DdsqlTabularQueryRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
