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
    from datadog_api_client.v1.model.guided_table_metrics_query_data_source import GuidedTableMetricsQueryDataSource


class GuidedTableMetricsQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_metrics_query_data_source import GuidedTableMetricsQueryDataSource

        return {
            "alias": (str,),
            "data_source": (GuidedTableMetricsQueryDataSource,),
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
        data_source: GuidedTableMetricsQueryDataSource,
        metric_name: str,
        name: str,
        alias: Union[str, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A metrics (or cloud cost) query fragment used as source data for a guided table. Group-by and time/space aggregation are defined separately.

        :param alias: Display alias for the query.
        :type alias: str, optional

        :param data_source: Metrics data source.
        :type data_source: GuidedTableMetricsQueryDataSource

        :param filter: Filter string to apply to the metric query.
        :type filter: str, optional

        :param metric_name: Name of the metric to query.
        :type metric_name: str

        :param name: Variable name used to reference this query in columns and formulas.
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
