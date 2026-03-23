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
    from datadog_api_client.v2.model.security_monitoring_critical_asset_severity import (
        SecurityMonitoringCriticalAssetSeverity,
    )


class SecurityMonitoringCriticalAssetUpdateAttributes(ModelNormal):
    validations = {
        "version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_critical_asset_severity import (
            SecurityMonitoringCriticalAssetSeverity,
        )

        return {
            "enabled": (bool,),
            "query": (str,),
            "rule_query": (str,),
            "severity": (SecurityMonitoringCriticalAssetSeverity,),
            "tags": ([str],),
            "version": (int,),
        }

    attribute_map = {
        "enabled": "enabled",
        "query": "query",
        "rule_query": "rule_query",
        "severity": "severity",
        "tags": "tags",
        "version": "version",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        rule_query: Union[str, UnsetType] = unset,
        severity: Union[SecurityMonitoringCriticalAssetSeverity, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The critical asset properties to be updated.

        :param enabled: Whether the critical asset is enabled.
        :type enabled: bool, optional

        :param query: The query for the critical asset. It uses the same syntax as the queries to search signals in the Signals Explorer.
        :type query: str, optional

        :param rule_query: The rule query of the critical asset, with the same syntax as the search bar for detection rules. This determines which rules this critical asset will apply to.
        :type rule_query: str, optional

        :param severity: Severity associated with this critical asset. Either an explicit severity can be set, or the severity can be increased or decreased.
        :type severity: SecurityMonitoringCriticalAssetSeverity, optional

        :param tags: List of tags associated with the critical asset.
        :type tags: [str], optional

        :param version: The version of the critical asset being updated. Used for optimistic locking to prevent concurrent modifications.
        :type version: int, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if query is not unset:
            kwargs["query"] = query
        if rule_query is not unset:
            kwargs["rule_query"] = rule_query
        if severity is not unset:
            kwargs["severity"] = severity
        if tags is not unset:
            kwargs["tags"] = tags
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
