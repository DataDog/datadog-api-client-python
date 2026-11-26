# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class QueryValueBackendRequest20270101OneOf4460904832(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "aggregator": (ScalarAggregator,),
            "comparison": (ComparisonRequest,),
            "conditional_formats": ([ThresholdFormattingRule],),
            "rum_query": (LogQueryDefinition,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "comparison": "comparison",
        "conditional_formats": "conditional_formats",
        "rum_query": "rum_query",
    }

    def __init__(
        self_,
        rum_query: LogQueryDefinition,
        aggregator: Union[ScalarAggregator, UnsetType] = unset,
        comparison: Union[ComparisonRequest, UnsetType] = unset,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param comparison: Test-only generated schema for the dashboard versioning proof of concept.
        :type comparison: ComparisonRequest, optional

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param rum_query: Test-only generated schema for the dashboard versioning proof of concept.
        :type rum_query: LogQueryDefinition
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if comparison is not unset:
            kwargs["comparison"] = comparison
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        super().__init__(kwargs)

        self_.rum_query = rum_query
