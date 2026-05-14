# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class IncidentJiraTemplateFieldConfiguration(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "custom_outbound_value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "incident_field": (str, none_type),
            "jira_field_key": (str,),
            "jira_field_type": (str, none_type),
            "sync_direction": (str,),
            "value_mapping": ({str: (str,)},),
        }

    attribute_map = {
        "custom_outbound_value": "custom_outbound_value",
        "incident_field": "incident_field",
        "jira_field_key": "jira_field_key",
        "jira_field_type": "jira_field_type",
        "sync_direction": "sync_direction",
        "value_mapping": "value_mapping",
    }

    def __init__(
        self_,
        jira_field_key: str,
        sync_direction: str,
        custom_outbound_value: Union[Any, UnsetType] = unset,
        incident_field: Union[str, none_type, UnsetType] = unset,
        jira_field_type: Union[str, none_type, UnsetType] = unset,
        value_mapping: Union[Dict[str, str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for a Jira field mapping.

        :param custom_outbound_value: Custom value for outbound synchronization.
        :type custom_outbound_value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param incident_field: The incident field to map to.
        :type incident_field: str, none_type, optional

        :param jira_field_key: The Jira field key.
        :type jira_field_key: str

        :param jira_field_type: The type of the Jira field.
        :type jira_field_type: str, none_type, optional

        :param sync_direction: The direction of synchronization.
        :type sync_direction: str

        :param value_mapping: Mapping of values between incident and Jira fields.
        :type value_mapping: {str: (str,)}, optional
        """
        if custom_outbound_value is not unset:
            kwargs["custom_outbound_value"] = custom_outbound_value
        if incident_field is not unset:
            kwargs["incident_field"] = incident_field
        if jira_field_type is not unset:
            kwargs["jira_field_type"] = jira_field_type
        if value_mapping is not unset:
            kwargs["value_mapping"] = value_mapping
        super().__init__(kwargs)

        self_.jira_field_key = jira_field_key
        self_.sync_direction = sync_direction
