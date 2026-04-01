# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_user_defined_field_category import IncidentUserDefinedFieldCategory
    from datadog_api_client.v2.model.incident_user_defined_field_collected import IncidentUserDefinedFieldCollected
    from datadog_api_client.v2.model.incident_user_defined_field_valid_value import IncidentUserDefinedFieldValidValue


class IncidentUserDefinedFieldAttributesUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_field_category import IncidentUserDefinedFieldCategory
        from datadog_api_client.v2.model.incident_user_defined_field_collected import IncidentUserDefinedFieldCollected
        from datadog_api_client.v2.model.incident_user_defined_field_valid_value import (
            IncidentUserDefinedFieldValidValue,
        )

        return {
            "category": (IncidentUserDefinedFieldCategory,),
            "collected": (IncidentUserDefinedFieldCollected,),
            "default_value": (str, none_type),
            "display_name": (str,),
            "ordinal": (str, none_type),
            "required": (bool, none_type),
            "valid_values": ([IncidentUserDefinedFieldValidValue], none_type),
        }

    attribute_map = {
        "category": "category",
        "collected": "collected",
        "default_value": "default_value",
        "display_name": "display_name",
        "ordinal": "ordinal",
        "required": "required",
        "valid_values": "valid_values",
    }

    def __init__(
        self_,
        category: Union[IncidentUserDefinedFieldCategory, none_type, UnsetType] = unset,
        collected: Union[IncidentUserDefinedFieldCollected, none_type, UnsetType] = unset,
        default_value: Union[str, none_type, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        ordinal: Union[str, none_type, UnsetType] = unset,
        required: Union[bool, none_type, UnsetType] = unset,
        valid_values: Union[List[IncidentUserDefinedFieldValidValue], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating an incident user-defined field. All fields are optional.

        :param category: The section in which the field appears: "what_happened" or "why_it_happened". When null, the field appears in the Attributes section.
        :type category: IncidentUserDefinedFieldCategory, none_type, optional

        :param collected: The lifecycle stage at which the app prompts users to fill out this field. Cannot be set on required fields.
        :type collected: IncidentUserDefinedFieldCollected, none_type, optional

        :param default_value: The default value for the field. Must be one of the valid values when valid_values is set.
        :type default_value: str, none_type, optional

        :param display_name: The human-readable name shown in the UI.
        :type display_name: str, optional

        :param ordinal: A decimal string representing the field's display order in the UI.
        :type ordinal: str, none_type, optional

        :param required: When true, users must fill out this field on incidents.
        :type required: bool, none_type, optional

        :param valid_values: The list of allowed values for dropdown and multiselect fields. Limited to 1000 values.
        :type valid_values: [IncidentUserDefinedFieldValidValue], none_type, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if collected is not unset:
            kwargs["collected"] = collected
        if default_value is not unset:
            kwargs["default_value"] = default_value
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if ordinal is not unset:
            kwargs["ordinal"] = ordinal
        if required is not unset:
            kwargs["required"] = required
        if valid_values is not unset:
            kwargs["valid_values"] = valid_values
        super().__init__(kwargs)
