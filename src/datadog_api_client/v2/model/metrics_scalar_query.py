# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.metrics_aggregator import MetricsAggregator
    from datadog_api_client.v2.model.metrics_data_source import MetricsDataSource


class MetricsScalarQuery(ModelNormal):
    validations = {
        "cross_org_uuids": {
            "max_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metrics_aggregator import MetricsAggregator
        from datadog_api_client.v2.model.metrics_data_source import MetricsDataSource

        return {
            "aggregator": (MetricsAggregator,),
            "cross_org_uuids": ([str],),
            "data_source": (MetricsDataSource,),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "name": "name",
        "query": "query",
    }

    def __init__(
        self_,
        aggregator: MetricsAggregator,
        data_source: MetricsDataSource,
        query: str,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A query against Datadog custom metrics or Cloud Cost data sources.

        :param aggregator: The type of aggregation that can be performed on metrics-based queries.
        :type aggregator: MetricsAggregator

        :param cross_org_uuids: Organization UUIDs to query when using `cross-organization visibility </account_management/org_settings/cross_org_visibility/>`_. Limited to one organization UUID.
        :type cross_org_uuids: [str], optional

        :param data_source: A data source that is powered by the Metrics platform.
        :type data_source: MetricsDataSource

        :param name: The variable name for use in formulas.
        :type name: str, optional

        :param query: A classic metrics query string.
        :type query: str
        """
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.aggregator = aggregator
        self_.data_source = data_source
        self_.query = query
