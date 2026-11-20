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
    from datadog_api_client.v1_20270101.model.formula_apm_resource_stats_query_data_source import (
        FormulaApmResourceStatsQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.apm_resource_stat import ApmResourceStat


class FormulaApmResourceStatsQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_apm_resource_stats_query_data_source import (
            FormulaApmResourceStatsQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.apm_resource_stat import ApmResourceStat

        return {
            "data_source": (FormulaApmResourceStatsQueryDataSource,),
            "env": (str,),
            "group_by": ([str],),
            "name": (str,),
            "operation_name": (str,),
            "peer_service": (str,),
            "primary_tag_name": (str,),
            "primary_tag_value": (str,),
            "resource_name": (str,),
            "service": (str,),
            "stat": (ApmResourceStat,),
            "version": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "env": "env",
        "group_by": "group_by",
        "name": "name",
        "operation_name": "operation_name",
        "peer_service": "peer.service",
        "primary_tag_name": "primary_tag_name",
        "primary_tag_value": "primary_tag_value",
        "resource_name": "resource_name",
        "service": "service",
        "stat": "stat",
        "version": "version",
    }

    def __init__(
        self_,
        data_source: FormulaApmResourceStatsQueryDataSource,
        env: str,
        group_by: List[str],
        name: str,
        operation_name: str,
        service: str,
        stat: ApmResourceStat,
        peer_service: Union[str, UnsetType] = unset,
        primary_tag_name: Union[str, UnsetType] = unset,
        primary_tag_value: Union[str, UnsetType] = unset,
        resource_name: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaApmResourceStatsQueryDataSource

        :param env: Test-only generated schema for the dashboard versioning proof of concept.
        :type env: str

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [str]

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param operation_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type operation_name: str

        :param peer_service: Test-only generated schema for the dashboard versioning proof of concept.
        :type peer_service: str, optional

        :param primary_tag_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type primary_tag_name: str, optional

        :param primary_tag_value: Test-only generated schema for the dashboard versioning proof of concept.
        :type primary_tag_value: str, optional

        :param resource_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type resource_name: str, optional

        :param service: Test-only generated schema for the dashboard versioning proof of concept.
        :type service: str

        :param stat: Test-only generated schema for the dashboard versioning proof of concept.
        :type stat: ApmResourceStat

        :param version: Test-only generated schema for the dashboard versioning proof of concept.
        :type version: str, optional
        """
        if peer_service is not unset:
            kwargs["peer_service"] = peer_service
        if primary_tag_name is not unset:
            kwargs["primary_tag_name"] = primary_tag_name
        if primary_tag_value is not unset:
            kwargs["primary_tag_value"] = primary_tag_value
        if resource_name is not unset:
            kwargs["resource_name"] = resource_name
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.env = env
        self_.group_by = group_by
        self_.name = name
        self_.operation_name = operation_name
        self_.service = service
        self_.stat = stat
