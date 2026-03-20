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
    from datadog_api_client.v2.model.incident_user_defined_field_field_type import IncidentUserDefinedFieldFieldType
    from datadog_api_client.v2.model.incident_user_defined_field_valid_value import IncidentUserDefinedFieldValidValue


class IncidentUserDefinedFieldAttributesCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_field_category import IncidentUserDefinedFieldCategory
        from datadog_api_client.v2.model.incident_user_defined_field_collected import IncidentUserDefinedFieldCollected
        from datadog_api_client.v2.model.incident_user_defined_field_field_type import IncidentUserDefinedFieldFieldType
        from datadog_api_client.v2.model.incident_user_defined_field_valid_value import (
            IncidentUserDefinedFieldValidValue,
        )

        return {
            "category": (IncidentUserDefinedFieldCategory,),
            "collected": (IncidentUserDefinedFieldCollected,),
            "default_value": (str, none_type),
            "display_name": (str,),
            "name": (str,),
            "ordinal": (str, none_type),
            "required": (bool,),
            "tag_key": (str, none_type),
            "type": (IncidentUserDefinedFieldFieldType,),
            "valid_values": ([IncidentUserDefinedFieldValidValue],),
        }

    attribute_map = {
        "category": "category",
        "collected": "collected",
        "default_value": "default_value",
        "display_name": "display_name",
        "name": "name",
        "ordinal": "ordinal",
        "required": "required",
        "tag_key": "tag_key",
        "type": "type",
        "valid_values": "valid_values",
    }

    def __init__(
        self_,
        name: str,
        type: IncidentUserDefinedFieldFieldType,
        category: Union[IncidentUserDefinedFieldCategory, none_type, UnsetType] = unset,
        collected: Union[IncidentUserDefinedFieldCollected, none_type, UnsetType] = unset,
        default_value: Union[str, none_type, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        ordinal: Union[str, none_type, UnsetType] = unset,
        required: Union[bool, UnsetType] = unset,
        tag_key: Union[str, none_type, UnsetType] = unset,
        valid_values: Union[List[IncidentUserDefinedFieldValidValue], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an incident user-defined field.

        :param category: The section in which the field appears. Use "what_happened" for impact-related fields or "why_it_happened" for root cause fields. When null, the field appears in the Attributes section.
        :type category: IncidentUserDefinedFieldCategory, none_type, optional

        :param collected: The lifecycle stage at which the app prompts users to fill out this field. Cannot be set on required fields.
        :type collected: IncidentUserDefinedFieldCollected, none_type, optional

        :param default_value: The default value for the field. Must be one of the valid values when valid_values is set.
        :type default_value: str, none_type, optional

        :param display_name: The human-readable name shown in the UI. Defaults to a formatted version of the name if not provided.
        :type display_name: str, optional

        :param name: The unique machine-readable name of the field. Must start with a letter or digit and contain only letters, digits, underscores, or periods.
        :type name: str

        :param ordinal: A decimal string representing the field's display order in the UI.
        :type ordinal: str, none_type, optional

        :param required: When true, users must fill out this field on incidents.
        :type required: bool, optional

        :param tag_key: For metric tag-type fields only, the metric tag key that powers the autocomplete options.
        :type tag_key: str, none_type, optional

        :param type: The data type of the field. 1=dropdown, 2=multiselect, 3=textbox, 4=textarray, 5=metrictag, 6=autocomplete, 7=number, 8=datetime.
        :type type: IncidentUserDefinedFieldFieldType

        :param valid_values: The list of allowed values for dropdown, multiselect, and autocomplete fields. Limited to 1000 values.
        :type valid_values: [IncidentUserDefinedFieldValidValue], optional
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
        if tag_key is not unset:
            kwargs["tag_key"] = tag_key
        if valid_values is not unset:
            kwargs["valid_values"] = valid_values
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
