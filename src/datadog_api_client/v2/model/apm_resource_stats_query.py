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
    from datadog_api_client.v2.model.apm_resource_stats_data_source import ApmResourceStatsDataSource
    from datadog_api_client.v2.model.apm_resource_stat_name import ApmResourceStatName


class ApmResourceStatsQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.apm_resource_stats_data_source import ApmResourceStatsDataSource
        from datadog_api_client.v2.model.apm_resource_stat_name import ApmResourceStatName

        return {
            "data_source": (ApmResourceStatsDataSource,),
            "env": (str,),
            "group_by": ([str],),
            "name": (str,),
            "operation_name": (str,),
            "primary_tag_name": (str,),
            "primary_tag_value": (str,),
            "resource_name": (str,),
            "service": (str,),
            "stat": (ApmResourceStatName,),
        }

    attribute_map = {
        "data_source": "data_source",
        "env": "env",
        "group_by": "group_by",
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
        data_source: ApmResourceStatsDataSource,
        env: str,
        name: str,
        service: str,
        stat: ApmResourceStatName,
        group_by: Union[List[str], UnsetType] = unset,
        operation_name: Union[str, UnsetType] = unset,
        primary_tag_name: Union[str, UnsetType] = unset,
        primary_tag_value: Union[str, UnsetType] = unset,
        resource_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A query for APM resource statistics such as latency, error rate, and hit count, grouped by resource name.

        :param data_source: A data source for APM resource statistics queries.
        :type data_source: ApmResourceStatsDataSource

        :param env: The environment to query.
        :type env: str

        :param group_by: Tag keys to group results by.
        :type group_by: [str], optional

        :param name: The variable name for use in formulas.
        :type name: str

        :param operation_name: The APM operation name.
        :type operation_name: str, optional

        :param primary_tag_name: Name of the second primary tag used within APM. Required when ``primary_tag_value`` is specified. See https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog
        :type primary_tag_name: str, optional

        :param primary_tag_value: Value of the second primary tag by which to filter APM data. ``primary_tag_name`` must also be specified.
        :type primary_tag_value: str, optional

        :param resource_name: The resource name to filter by.
        :type resource_name: str, optional

        :param service: The service name to filter by.
        :type service: str

        :param stat: The APM resource statistic to query.
        :type stat: ApmResourceStatName
        """
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if operation_name is not unset:
            kwargs["operation_name"] = operation_name
        if primary_tag_name is not unset:
            kwargs["primary_tag_name"] = primary_tag_name
        if primary_tag_value is not unset:
            kwargs["primary_tag_value"] = primary_tag_value
        if resource_name is not unset:
            kwargs["resource_name"] = resource_name
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.env = env
        self_.name = name
        self_.service = service
        self_.stat = stat
