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


class IncidentConfigurationDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "execute_integrations": (bool,),
            "execute_notification_rules": (bool,),
            "include_in_analytics": (bool,),
            "include_in_search": (bool,),
        }

    attribute_map = {
        "execute_integrations": "execute_integrations",
        "execute_notification_rules": "execute_notification_rules",
        "include_in_analytics": "include_in_analytics",
        "include_in_search": "include_in_search",
    }

    def __init__(
        self_,
        execute_integrations: Union[bool, UnsetType] = unset,
        execute_notification_rules: Union[bool, UnsetType] = unset,
        include_in_analytics: Union[bool, UnsetType] = unset,
        include_in_search: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an incident configuration.

        :param execute_integrations: Whether to execute integrations for this incident.
        :type execute_integrations: bool, optional

        :param execute_notification_rules: Whether to execute notification rules for this incident.
        :type execute_notification_rules: bool, optional

        :param include_in_analytics: Whether to include this incident in analytics.
        :type include_in_analytics: bool, optional

        :param include_in_search: Whether to include this incident in search results.
        :type include_in_search: bool, optional
        """
        if execute_integrations is not unset:
            kwargs["execute_integrations"] = execute_integrations
        if execute_notification_rules is not unset:
            kwargs["execute_notification_rules"] = execute_notification_rules
        if include_in_analytics is not unset:
            kwargs["include_in_analytics"] = include_in_analytics
        if include_in_search is not unset:
            kwargs["include_in_search"] = include_in_search
        super().__init__(kwargs)
