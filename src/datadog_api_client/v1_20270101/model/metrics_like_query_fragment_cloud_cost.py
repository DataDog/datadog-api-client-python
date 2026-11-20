# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.metrics_like_query_fragment_cloud_cost_data_source import (
        MetricsLikeQueryFragmentCloudCostDataSource,
    )


class MetricsLikeQueryFragmentCloudCost(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.metrics_like_query_fragment_cloud_cost_data_source import (
            MetricsLikeQueryFragmentCloudCostDataSource,
        )

        return {
            "alias": (str,),
            "data_source": (MetricsLikeQueryFragmentCloudCostDataSource,),
            "filter": (str,),
            "metric_name": (str,),
            "name": (str,),
        }

    attribute_map = {
        "alias": "alias",
        "data_source": "data_source",
        "filter": "filter",
        "metric_name": "metric_name",
        "name": "name",
    }

    def __init__(
        self_,
        data_source: MetricsLikeQueryFragmentCloudCostDataSource,
        metric_name: str,
        name: str,
        alias: Union[str, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: MetricsLikeQueryFragmentCloudCostDataSource

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str, optional

        :param metric_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type metric_name: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if filter is not unset:
            kwargs["filter"] = filter
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.metric_name = metric_name
        self_.name = name
