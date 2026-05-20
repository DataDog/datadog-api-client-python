# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_experimentation_analytics_compute import (
        LLMObsExperimentationAnalyticsCompute,
    )
    from datadog_api_client.v2.model.llm_obs_experimentation_analytics_group_by import (
        LLMObsExperimentationAnalyticsGroupBy,
    )
    from datadog_api_client.v2.model.llm_obs_experimentation_analytics_search import (
        LLMObsExperimentationAnalyticsSearch,
    )
    from datadog_api_client.v2.model.llm_obs_experimentation_analytics_time_range import (
        LLMObsExperimentationAnalyticsTimeRange,
    )


class LLMObsExperimentationAnalyticsAggregate(ModelNormal):
    validations = {
        "compute": {
            "min_items": 1,
        },
        "indexes": {
            "min_items": 1,
        },
        "limit": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_analytics_compute import (
            LLMObsExperimentationAnalyticsCompute,
        )
        from datadog_api_client.v2.model.llm_obs_experimentation_analytics_group_by import (
            LLMObsExperimentationAnalyticsGroupBy,
        )
        from datadog_api_client.v2.model.llm_obs_experimentation_analytics_search import (
            LLMObsExperimentationAnalyticsSearch,
        )
        from datadog_api_client.v2.model.llm_obs_experimentation_analytics_time_range import (
            LLMObsExperimentationAnalyticsTimeRange,
        )

        return {
            "compute": ([LLMObsExperimentationAnalyticsCompute],),
            "dataset_version": (int, none_type),
            "group_by": ([LLMObsExperimentationAnalyticsGroupBy],),
            "indexes": ([str],),
            "limit": (int, none_type),
            "search": (LLMObsExperimentationAnalyticsSearch,),
            "time": (LLMObsExperimentationAnalyticsTimeRange,),
        }

    attribute_map = {
        "compute": "compute",
        "dataset_version": "dataset_version",
        "group_by": "group_by",
        "indexes": "indexes",
        "limit": "limit",
        "search": "search",
        "time": "time",
    }

    def __init__(
        self_,
        compute: List[LLMObsExperimentationAnalyticsCompute],
        indexes: List[str],
        search: LLMObsExperimentationAnalyticsSearch,
        dataset_version: Union[int, none_type, UnsetType] = unset,
        group_by: Union[List[LLMObsExperimentationAnalyticsGroupBy], UnsetType] = unset,
        limit: Union[int, none_type, UnsetType] = unset,
        time: Union[LLMObsExperimentationAnalyticsTimeRange, UnsetType] = unset,
        **kwargs,
    ):
        """
        Analytics aggregation parameters.

        :param compute: List of metric computations to perform.
        :type compute: [LLMObsExperimentationAnalyticsCompute]

        :param dataset_version: Filter to a specific dataset version.
        :type dataset_version: int, none_type, optional

        :param group_by: Fields to group results by.
        :type group_by: [LLMObsExperimentationAnalyticsGroupBy], optional

        :param indexes: Data indexes to query. At least one is required.
        :type indexes: [str]

        :param limit: Maximum number of results to return.
        :type limit: int, none_type, optional

        :param search: Search query for filtering analytics data.
        :type search: LLMObsExperimentationAnalyticsSearch

        :param time: Unix-millisecond time range for filtering analytics data.
        :type time: LLMObsExperimentationAnalyticsTimeRange, optional
        """
        if dataset_version is not unset:
            kwargs["dataset_version"] = dataset_version
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if limit is not unset:
            kwargs["limit"] = limit
        if time is not unset:
            kwargs["time"] = time
        super().__init__(kwargs)

        self_.compute = compute
        self_.indexes = indexes
        self_.search = search
