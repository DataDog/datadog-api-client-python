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
    from datadog_api_client.v2.model.aggregated_waterfall_response_attributes import (
        AggregatedWaterfallResponseAttributes,
    )
    from datadog_api_client.v2.model.aggregated_waterfall_request_type import AggregatedWaterfallRequestType


class AggregatedWaterfallResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aggregated_waterfall_response_attributes import (
            AggregatedWaterfallResponseAttributes,
        )
        from datadog_api_client.v2.model.aggregated_waterfall_request_type import AggregatedWaterfallRequestType

        return {
            "attributes": (AggregatedWaterfallResponseAttributes,),
            "id": (str,),
            "type": (AggregatedWaterfallRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AggregatedWaterfallResponseAttributes,
        id: str,
        type: AggregatedWaterfallRequestType,
        **kwargs,
    ):
        """
        Data envelope for an aggregated waterfall response.

        :param attributes: Attributes of an aggregated waterfall response.
        :type attributes: AggregatedWaterfallResponseAttributes

        :param id: Hash-based unique identifier for this aggregation.
        :type id: str

        :param type: The JSON:API type for aggregated waterfall requests.
        :type type: AggregatedWaterfallRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
