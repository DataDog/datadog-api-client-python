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
    from datadog_api_client.v1_20270101.model.formula_apm_dependency_stats_query_data_source import (
        FormulaApmDependencyStatsQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.apm_dependency_stat import ApmDependencyStat


class FormulaApmDependencyStatsQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_apm_dependency_stats_query_data_source import (
            FormulaApmDependencyStatsQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.apm_dependency_stat import ApmDependencyStat

        return {
            "data_source": (FormulaApmDependencyStatsQueryDataSource,),
            "env": (str,),
            "is_upstream": (bool,),
            "name": (str,),
            "operation_name": (str,),
            "primary_tag_name": (str,),
            "primary_tag_value": (str,),
            "resource_name": (str,),
            "service": (str,),
            "stat": (ApmDependencyStat,),
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
        data_source: FormulaApmDependencyStatsQueryDataSource,
        env: str,
        name: str,
        operation_name: str,
        resource_name: str,
        service: str,
        stat: ApmDependencyStat,
        is_upstream: Union[bool, UnsetType] = unset,
        primary_tag_name: Union[str, UnsetType] = unset,
        primary_tag_value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaApmDependencyStatsQueryDataSource

        :param env: Test-only generated schema for the dashboard versioning proof of concept.
        :type env: str

        :param is_upstream: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_upstream: bool, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param operation_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type operation_name: str

        :param primary_tag_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type primary_tag_name: str, optional

        :param primary_tag_value: Test-only generated schema for the dashboard versioning proof of concept.
        :type primary_tag_value: str, optional

        :param resource_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type resource_name: str

        :param service: Test-only generated schema for the dashboard versioning proof of concept.
        :type service: str

        :param stat: Test-only generated schema for the dashboard versioning proof of concept.
        :type stat: ApmDependencyStat
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
