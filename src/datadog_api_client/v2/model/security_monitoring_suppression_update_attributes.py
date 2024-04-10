# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class SecurityMonitoringSuppressionUpdateAttributes(ModelNormal):
    validations = {
        "version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "data_exclusion_query": (str,),
            "description": (str,),
            "enabled": (bool,),
            "expiration_date": (int, none_type),
            "name": (str,),
            "rule_query": (str,),
            "suppression_query": (str,),
            "version": (int,),
        }

    attribute_map = {
        "data_exclusion_query": "data_exclusion_query",
        "description": "description",
        "enabled": "enabled",
        "expiration_date": "expiration_date",
        "name": "name",
        "rule_query": "rule_query",
        "suppression_query": "suppression_query",
        "version": "version",
    }

    def __init__(
        self_,
        data_exclusion_query: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        expiration_date: Union[int, none_type, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        rule_query: Union[str, UnsetType] = unset,
        suppression_query: Union[str, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The suppression rule properties to be updated.

        :param data_exclusion_query: An exclusion query on the input data of the security rules, which could be logs, Agent events, or other types of data based on the security rule. Events matching this query are ignored by any detection rules referenced in the suppression rule.
        :type data_exclusion_query: str, optional

        :param description: A description for the suppression rule.
        :type description: str, optional

        :param enabled: Whether the suppression rule is enabled.
        :type enabled: bool, optional

        :param expiration_date: A Unix millisecond timestamp giving an expiration date for the suppression rule. After this date, it won't suppress signals anymore. If unset, the expiration date of the suppression rule is left untouched. If set to ``null`` , the expiration date is removed.
        :type expiration_date: int, none_type, optional

        :param name: The name of the suppression rule.
        :type name: str, optional

        :param rule_query: The rule query of the suppression rule, with the same syntax as the search bar for detection rules.
        :type rule_query: str, optional

        :param suppression_query: The suppression query of the suppression rule. If a signal matches this query, it is suppressed and not triggered. Same syntax as the queries to search signals in the signal explorer.
        :type suppression_query: str, optional

        :param version: The current version of the suppression. This is optional, but it can help prevent concurrent modifications.
        :type version: int, optional
        """
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
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
