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
    from datadog_api_client.v2.model.security_monitoring_user import SecurityMonitoringUser


class SecurityMonitoringSuppressionAttributes(ModelNormal):
    validations = {
        "version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_user import SecurityMonitoringUser

        return {
            "creation_date": (int,),
            "creator": (SecurityMonitoringUser,),
            "data_exclusion_query": (str,),
            "description": (str,),
            "enabled": (bool,),
            "expiration_date": (int,),
            "name": (str,),
            "rule_query": (str,),
            "suppression_query": (str,),
            "update_date": (int,),
            "updater": (SecurityMonitoringUser,),
            "version": (int,),
        }

    attribute_map = {
        "creation_date": "creation_date",
        "creator": "creator",
        "data_exclusion_query": "data_exclusion_query",
        "description": "description",
        "enabled": "enabled",
        "expiration_date": "expiration_date",
        "name": "name",
        "rule_query": "rule_query",
        "suppression_query": "suppression_query",
        "update_date": "update_date",
        "updater": "updater",
        "version": "version",
    }

    def __init__(
        self_,
        creation_date: Union[int, UnsetType] = unset,
        creator: Union[SecurityMonitoringUser, UnsetType] = unset,
        data_exclusion_query: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        expiration_date: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        rule_query: Union[str, UnsetType] = unset,
        suppression_query: Union[str, UnsetType] = unset,
        update_date: Union[int, UnsetType] = unset,
        updater: Union[SecurityMonitoringUser, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of the suppression rule.

        :param creation_date: A Unix millisecond timestamp given the creation date of the suppression rule.
        :type creation_date: int, optional

        :param creator: A user.
        :type creator: SecurityMonitoringUser, optional

        :param data_exclusion_query: An exclusion query on the input data of the security rules, which could be logs, Agent events, or other types of data based on the security rule. Events matching this query are ignored by any detection rules referenced in the suppression rule.
        :type data_exclusion_query: str, optional

        :param description: A description for the suppression rule.
        :type description: str, optional

        :param enabled: Whether the suppression rule is enabled.
        :type enabled: bool, optional

        :param expiration_date: A Unix millisecond timestamp giving an expiration date for the suppression rule. After this date, it won't suppress signals anymore.
        :type expiration_date: int, optional

        :param name: The name of the suppression rule.
        :type name: str, optional

        :param rule_query: The rule query of the suppression rule, with the same syntax as the search bar for detection rules.
        :type rule_query: str, optional

        :param suppression_query: The suppression query of the suppression rule. If a signal matches this query, it is suppressed and not triggered. Same syntax as the queries to search signals in the signal explorer.
        :type suppression_query: str, optional

        :param update_date: A Unix millisecond timestamp given the update date of the suppression rule.
        :type update_date: int, optional

        :param updater: A user.
        :type updater: SecurityMonitoringUser, optional

        :param version: The version of the suppression rule; it starts at 1, and is incremented at each update.
        :type version: int, optional
        """
        if creation_date is not unset:
            kwargs["creation_date"] = creation_date
        if creator is not unset:
            kwargs["creator"] = creator
        if data_exclusion_query is not unset:
            kwargs["data_exclusion_query"] = data_exclusion_query
        if description is not unset:
            kwargs["description"] = description
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if expiration_date is not unset:
            kwargs["expiration_date"] = expiration_date
        if name is not unset:
            kwargs["name"] = name
        if rule_query is not unset:
            kwargs["rule_query"] = rule_query
        if suppression_query is not unset:
            kwargs["suppression_query"] = suppression_query
        if update_date is not unset:
            kwargs["update_date"] = update_date
        if updater is not unset:
            kwargs["updater"] = updater
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
