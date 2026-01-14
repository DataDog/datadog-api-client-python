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


class SecurityMonitoringCriticalAssetCreateAttributes(ModelNormal):
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
        }

    attribute_map = {
        "enabled": "enabled",
        "query": "query",
        "rule_query": "rule_query",
        "severity": "severity",
        "tags": "tags",
    }

    def __init__(
        self_,
        query: str,
        rule_query: str,
        severity: SecurityMonitoringCriticalAssetSeverity,
        enabled: Union[bool, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the attributes of the critical asset to be created.

        :param enabled: Whether the critical asset is enabled. Defaults to ``true`` if not specified.
        :type enabled: bool, optional

        :param query: The query for the critical asset. It uses the same syntax as the queries to search signals in the Signals Explorer.
        :type query: str

        :param rule_query: The rule query of the critical asset, with the same syntax as the search bar for detection rules. This determines which rules this critical asset will apply to.
        :type rule_query: str

        :param severity: Severity associated with this critical asset. Either an explicit severity can be set, or the severity can be increased or decreased.
        :type severity: SecurityMonitoringCriticalAssetSeverity

        :param tags: List of tags associated with the critical asset.
        :type tags: [str], optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.query = query
        self_.rule_query = rule_query
        self_.severity = severity
