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
    from datadog_api_client.v2.model.security_monitoring_user import SecurityMonitoringUser
    from datadog_api_client.v2.model.security_monitoring_critical_asset_severity import (
        SecurityMonitoringCriticalAssetSeverity,
    )


class SecurityMonitoringCriticalAssetAttributes(ModelNormal):
    validations = {
        "version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_user import SecurityMonitoringUser
        from datadog_api_client.v2.model.security_monitoring_critical_asset_severity import (
            SecurityMonitoringCriticalAssetSeverity,
        )

        return {
            "creation_author_id": (int,),
            "creation_date": (int,),
            "creator": (SecurityMonitoringUser,),
            "enabled": (bool,),
            "query": (str,),
            "rule_query": (str,),
            "severity": (SecurityMonitoringCriticalAssetSeverity,),
            "tags": ([str],),
            "update_author_id": (int,),
            "update_date": (int,),
            "updater": (SecurityMonitoringUser,),
            "version": (int,),
        }

    attribute_map = {
        "creation_author_id": "creation_author_id",
        "creation_date": "creation_date",
        "creator": "creator",
        "enabled": "enabled",
        "query": "query",
        "rule_query": "rule_query",
        "severity": "severity",
        "tags": "tags",
        "update_author_id": "update_author_id",
        "update_date": "update_date",
        "updater": "updater",
        "version": "version",
    }

    def __init__(
        self_,
        creation_author_id: Union[int, UnsetType] = unset,
        creation_date: Union[int, UnsetType] = unset,
        creator: Union[SecurityMonitoringUser, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        rule_query: Union[str, UnsetType] = unset,
        severity: Union[SecurityMonitoringCriticalAssetSeverity, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        update_author_id: Union[int, UnsetType] = unset,
        update_date: Union[int, UnsetType] = unset,
        updater: Union[SecurityMonitoringUser, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of the critical asset.

        :param creation_author_id: ID of user who created the critical asset.
        :type creation_author_id: int, optional

        :param creation_date: A Unix millisecond timestamp given the creation date of the critical asset.
        :type creation_date: int, optional

        :param creator: A user.
        :type creator: SecurityMonitoringUser, optional

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

        :param update_author_id: ID of user who updated the critical asset.
        :type update_author_id: int, optional

        :param update_date: A Unix millisecond timestamp given the update date of the critical asset.
        :type update_date: int, optional

        :param updater: A user.
        :type updater: SecurityMonitoringUser, optional

        :param version: The version of the critical asset; it starts at 1, and is incremented at each update.
        :type version: int, optional
        """
        if creation_author_id is not unset:
            kwargs["creation_author_id"] = creation_author_id
        if creation_date is not unset:
            kwargs["creation_date"] = creation_date
        if creator is not unset:
            kwargs["creator"] = creator
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
        if update_author_id is not unset:
            kwargs["update_author_id"] = update_author_id
        if update_date is not unset:
            kwargs["update_date"] = update_date
        if updater is not unset:
            kwargs["updater"] = updater
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
