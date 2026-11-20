# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class QueryValueBackendRequest20270101OneOf4460686496(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "_query_options": (
                {
                    str: (
                        DashboardInlineSchema3,
                        none_type,
                    )
                },
            ),
            "aggregator": (ScalarAggregator,),
            "comparison": (ComparisonRequest,),
            "conditional_formats": ([ThresholdFormattingRule],),
            "q": (str,),
        }

    attribute_map = {
        "_query_options": "_query_options",
        "aggregator": "aggregator",
        "comparison": "comparison",
        "conditional_formats": "conditional_formats",
        "q": "q",
    }

    def __init__(
        self_,
        q: str,
        _query_options: Union[Dict[str, Union[DashboardInlineSchema3, str, float, bool]], UnsetType] = unset,
        aggregator: Union[ScalarAggregator, UnsetType] = unset,
        comparison: Union[ComparisonRequest, UnsetType] = unset,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema3, none_type,)}, optional

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param comparison: Test-only generated schema for the dashboard versioning proof of concept.
        :type comparison: ComparisonRequest, optional

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str
        """
        if _query_options is not unset:
            kwargs["_query_options"] = _query_options
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if comparison is not unset:
            kwargs["comparison"] = comparison
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        super().__init__(kwargs)

        self_.q = q
