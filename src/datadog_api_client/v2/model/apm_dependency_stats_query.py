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
    from datadog_api_client.v2.model.apm_dependency_stats_data_source import ApmDependencyStatsDataSource
    from datadog_api_client.v2.model.apm_dependency_stat_name import ApmDependencyStatName


class ApmDependencyStatsQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.apm_dependency_stats_data_source import ApmDependencyStatsDataSource
        from datadog_api_client.v2.model.apm_dependency_stat_name import ApmDependencyStatName

        return {
            "data_source": (ApmDependencyStatsDataSource,),
            "env": (str,),
            "is_upstream": (bool,),
            "name": (str,),
            "operation_name": (str,),
            "primary_tag_name": (str,),
            "primary_tag_value": (str,),
            "resource_name": (str,),
            "service": (str,),
            "stat": (ApmDependencyStatName,),
        }

    attribute_map = {
        "data_source": "data_source",
        "env": "env",
        "is_upstream": "is_upstream",
        "name": "name",
        "operation_name": "operation_name",
        "primary_tag_name": "primary_tag_name",
        "primary_tag_value": "primary_tag_value",
        "resource_name": "resource_name",
        "service": "service",
        "stat": "stat",
    }

    def __init__(
        self_,
        data_source: ApmDependencyStatsDataSource,
        env: str,
        name: str,
        operation_name: str,
        resource_name: str,
        service: str,
        stat: ApmDependencyStatName,
        is_upstream: Union[bool, UnsetType] = unset,
        primary_tag_name: Union[str, UnsetType] = unset,
        primary_tag_value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A query for APM dependency statistics between services, such as call latency and error rates.

        :param data_source: A data source for APM dependency statistics queries.
        :type data_source: ApmDependencyStatsDataSource

        :param env: The environment to query.
        :type env: str

        :param is_upstream: Determines whether stats for upstream or downstream dependencies should be queried.
        :type is_upstream: bool, optional

        :param name: The variable name for use in formulas.
        :type name: str

        :param operation_name: The APM operation name.
        :type operation_name: str

        :param primary_tag_name: The name of the second primary tag used within APM; required when ``primary_tag_value`` is specified. See https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog.
        :type primary_tag_name: str, optional

        :param primary_tag_value: Filter APM data by the second primary tag. ``primary_tag_name`` must also be specified.
        :type primary_tag_value: str, optional

        :param resource_name: The resource name to filter by.
        :type resource_name: str

        :param service: The service name to filter by.
        :type service: str

        :param stat: The APM dependency statistic to query.
        :type stat: ApmDependencyStatName
        """
        if is_upstream is not unset:
            kwargs["is_upstream"] = is_upstream
        if primary_tag_name is not unset:
            kwargs["primary_tag_name"] = primary_tag_name
        if primary_tag_value is not unset:
            kwargs["primary_tag_value"] = primary_tag_value
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.env = env
        self_.name = name
        self_.operation_name = operation_name
        self_.resource_name = resource_name
        self_.service = service
        self_.stat = stat
