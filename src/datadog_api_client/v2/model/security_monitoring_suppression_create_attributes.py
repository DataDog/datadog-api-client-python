# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SecurityMonitoringSuppressionCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "enabled": (bool,),
            "expiration_date": (int,),
            "name": (str,),
            "rule_query": (str,),
            "suppression_query": (str,),
        }

    attribute_map = {
        "description": "description",
        "enabled": "enabled",
        "expiration_date": "expiration_date",
        "name": "name",
        "rule_query": "rule_query",
        "suppression_query": "suppression_query",
    }

    def __init__(
        self_,
        enabled: bool,
        name: str,
        rule_query: str,
        suppression_query: str,
        description: Union[str, UnsetType] = unset,
        expiration_date: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the attributes of the suppression rule to be created.

        :param description: A description for the suppression rule.
        :type description: str, optional

        :param enabled: Whether the suppression rule is enabled.
        :type enabled: bool

        :param expiration_date: A Unix millisecond timestamp giving an expiration date for the suppression rule. After this date, it won't suppress signals anymore.
        :type expiration_date: int, optional

        :param name: The name of the suppression rule.
        :type name: str

        :param rule_query: The rule query of the suppression rule, with the same syntax as the search bar for detection rules.
        :type rule_query: str

        :param suppression_query: The suppression query of the suppression rule. If a signal matches this query, it is suppressed and is not triggered . Same syntax as the queries to search signals in the signal explorer.
        :type suppression_query: str
        """
        if description is not unset:
            kwargs["description"] = description
        if expiration_date is not unset:
            kwargs["expiration_date"] = expiration_date
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.name = name
        self_.rule_query = rule_query
        self_.suppression_query = suppression_query
