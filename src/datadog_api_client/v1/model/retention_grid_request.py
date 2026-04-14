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
    from datadog_api_client.v1.model.retention_query import RetentionQuery
    from datadog_api_client.v1.model.retention_grid_request_type import RetentionGridRequestType


class RetentionGridRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.retention_query import RetentionQuery
        from datadog_api_client.v1.model.retention_grid_request_type import RetentionGridRequestType

        return {
            "query": (RetentionQuery,),
            "request_type": (RetentionGridRequestType,),
        }

    attribute_map = {
        "query": "query",
        "request_type": "request_type",
    }

    def __init__(self_, query: RetentionQuery, request_type: RetentionGridRequestType, **kwargs):
        """
        Retention grid widget request.

        :param query: Retention query definition.
        :type query: RetentionQuery

        :param request_type: Request type for retention grid widget.
        :type request_type: RetentionGridRequestType
        """
        super().__init__(kwargs)

        self_.query = query
        self_.request_type = request_type
