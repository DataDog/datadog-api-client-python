# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.dashboard_inline_schema45 import DashboardInlineSchema45
    from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator


class ScatterplotBackendAxisRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dashboard_inline_schema45 import DashboardInlineSchema45
        from datadog_api_client.v1_20270101.model.scalar_aggregator import ScalarAggregator

        return {
            "_query_options": (
                {
                    str: (
                        DashboardInlineSchema45,
                        none_type,
                    )
                },
            ),
            "aggregator": (ScalarAggregator,),
            "q": (str,),
        }

    attribute_map = {
        "_query_options": "_query_options",
        "aggregator": "aggregator",
        "q": "q",
    }

    def __init__(
        self_,
        q: str,
        _query_options: Union[Dict[str, Union[DashboardInlineSchema45, str, float, bool]], UnsetType] = unset,
        aggregator: Union[ScalarAggregator, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema45, none_type,)}, optional

        :param aggregator: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregator: ScalarAggregator, optional

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str
        """
        if _query_options is not unset:
            kwargs["_query_options"] = _query_options
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        super().__init__(kwargs)

        self_.q = q
