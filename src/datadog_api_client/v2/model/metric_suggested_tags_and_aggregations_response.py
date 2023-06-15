# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.metric_suggested_aggregations import MetricSuggestedAggregations
from datadog_api_client.v2.model.metric_suggested_aggregations import MetricSuggestedAggregations

if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_suggested_tags_and_aggregations import MetricSuggestedTagsAndAggregations


@dataclass
class MetricSuggestedTagsAndAggregationsResponseJSON:
    id: str
    active_aggregations: Union[MetricSuggestedAggregations, UnsetType] = unset
    active_tags: Union[List[str], UnsetType] = unset


class MetricSuggestedTagsAndAggregationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_suggested_tags_and_aggregations import (
            MetricSuggestedTagsAndAggregations,
        )

        return {
            "data": (MetricSuggestedTagsAndAggregations,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MetricSuggestedTagsAndAggregationsResponseJSON

    def __init__(self_, data: Union[MetricSuggestedTagsAndAggregations, UnsetType] = unset, **kwargs):
        """
        Response object that includes a single metric's actively queried tags and aggregations.

        :param data: Object for a single metric's actively queried tags and aggregations.
        :type data: MetricSuggestedTagsAndAggregations, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
