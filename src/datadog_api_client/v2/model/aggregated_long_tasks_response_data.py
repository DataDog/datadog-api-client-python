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
    from datadog_api_client.v2.model.aggregated_long_tasks_response_attributes import (
        AggregatedLongTasksResponseAttributes,
    )
    from datadog_api_client.v2.model.aggregated_long_tasks_request_type import AggregatedLongTasksRequestType


class AggregatedLongTasksResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aggregated_long_tasks_response_attributes import (
            AggregatedLongTasksResponseAttributes,
        )
        from datadog_api_client.v2.model.aggregated_long_tasks_request_type import AggregatedLongTasksRequestType

        return {
            "attributes": (AggregatedLongTasksResponseAttributes,),
            "id": (str,),
            "type": (AggregatedLongTasksRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AggregatedLongTasksResponseAttributes,
        id: str,
        type: AggregatedLongTasksRequestType,
        **kwargs,
    ):
        """
        Data envelope for an aggregated long tasks response.

        :param attributes: Attributes of an aggregated long tasks response.
        :type attributes: AggregatedLongTasksResponseAttributes

        :param id: Hash-based unique identifier for this aggregation.
        :type id: str

        :param type: The JSON:API type for aggregated long tasks requests.
        :type type: AggregatedLongTasksRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
