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
    from datadog_api_client.v1.model.retention_compute import RetentionCompute
    from datadog_api_client.v1.model.retention_data_source import RetentionDataSource
    from datadog_api_client.v1.model.retention_group_by import RetentionGroupBy
    from datadog_api_client.v1.model.retention_search import RetentionSearch


class FormulaAndFunctionRetentionQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.retention_compute import RetentionCompute
        from datadog_api_client.v1.model.retention_data_source import RetentionDataSource
        from datadog_api_client.v1.model.retention_group_by import RetentionGroupBy
        from datadog_api_client.v1.model.retention_search import RetentionSearch

        return {
            "compute": (RetentionCompute,),
            "data_source": (RetentionDataSource,),
            "group_by": ([RetentionGroupBy],),
            "name": (str,),
            "search": (RetentionSearch,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "name": "name",
        "search": "search",
    }

    def __init__(
        self_,
        compute: RetentionCompute,
        data_source: RetentionDataSource,
        name: str,
        search: RetentionSearch,
        group_by: Union[List[RetentionGroupBy], UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions Retention query for defining timeseries and scalar visualizations.

        :param compute: Compute configuration for retention queries.
        :type compute: RetentionCompute

        :param data_source: Data source for retention queries.
        :type data_source: RetentionDataSource

        :param group_by: Group by configuration.
        :type group_by: [RetentionGroupBy], optional

        :param name: Name of the query for use in formulas.
        :type name: str

        :param search: Search configuration for retention queries.
        :type search: RetentionSearch
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.name = name
        self_.search = search
