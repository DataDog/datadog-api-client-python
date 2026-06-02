# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class IncidentConfigurationDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "execute_integrations": (bool,),
            "execute_notification_rules": (bool,),
            "incident_id": (str,),
            "include_in_analytics": (bool,),
            "include_in_search": (bool,),
            "modified_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "execute_integrations": "execute_integrations",
        "execute_notification_rules": "execute_notification_rules",
        "incident_id": "incident_id",
        "include_in_analytics": "include_in_analytics",
        "include_in_search": "include_in_search",
        "modified_at": "modified_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        incident_id: str,
        modified_at: datetime,
        execute_integrations: Union[bool, UnsetType] = unset,
        execute_notification_rules: Union[bool, UnsetType] = unset,
        include_in_analytics: Union[bool, UnsetType] = unset,
        include_in_search: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an incident configuration in a response.

        :param created_at: Timestamp when the configuration was created.
        :type created_at: datetime

        :param execute_integrations: Whether integrations are executed for this incident.
        :type execute_integrations: bool, optional

        :param execute_notification_rules: Whether notification rules are executed for this incident.
        :type execute_notification_rules: bool, optional

        :param incident_id: The incident identifier.
        :type incident_id: str

        :param include_in_analytics: Whether this incident is included in analytics.
        :type include_in_analytics: bool, optional

        :param include_in_search: Whether this incident is included in search results.
        :type include_in_search: bool, optional

        :param modified_at: Timestamp when the configuration was last modified.
        :type modified_at: datetime
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

        self_.created_at = created_at
        self_.incident_id = incident_id
        self_.modified_at = modified_at
