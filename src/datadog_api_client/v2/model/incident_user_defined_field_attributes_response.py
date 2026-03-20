# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_user_defined_field_category import IncidentUserDefinedFieldCategory
    from datadog_api_client.v2.model.incident_user_defined_field_collected import IncidentUserDefinedFieldCollected
    from datadog_api_client.v2.model.incident_user_defined_field_metadata import IncidentUserDefinedFieldMetadata
    from datadog_api_client.v2.model.incident_user_defined_field_valid_value import IncidentUserDefinedFieldValidValue


class IncidentUserDefinedFieldAttributesResponse(ModelNormal):
    validations = {
        "type": {
            "inclusive_maximum": 8,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_field_category import IncidentUserDefinedFieldCategory
        from datadog_api_client.v2.model.incident_user_defined_field_collected import IncidentUserDefinedFieldCollected
        from datadog_api_client.v2.model.incident_user_defined_field_metadata import IncidentUserDefinedFieldMetadata
        from datadog_api_client.v2.model.incident_user_defined_field_valid_value import (
            IncidentUserDefinedFieldValidValue,
        )

        return {
            "attached_to": (str,),
            "category": (IncidentUserDefinedFieldCategory,),
            "collected": (IncidentUserDefinedFieldCollected,),
            "created": (datetime,),
            "default_value": (str, none_type),
            "deleted": (datetime, none_type),
            "display_name": (str,),
            "metadata": (IncidentUserDefinedFieldMetadata,),
            "modified": (datetime, none_type),
            "name": (str,),
            "ordinal": (str, none_type),
            "prerequisite": (str, none_type),
            "required": (bool,),
            "reserved": (bool,),
            "table_id": (int,),
            "tag_key": (str, none_type),
            "type": (int, none_type),
            "valid_values": ([IncidentUserDefinedFieldValidValue], none_type),
        }

    attribute_map = {
        "attached_to": "attached_to",
        "category": "category",
        "collected": "collected",
        "created": "created",
        "default_value": "default_value",
        "deleted": "deleted",
        "display_name": "display_name",
        "metadata": "metadata",
        "modified": "modified",
        "name": "name",
        "ordinal": "ordinal",
        "prerequisite": "prerequisite",
        "required": "required",
        "reserved": "reserved",
        "table_id": "table_id",
        "tag_key": "tag_key",
        "type": "type",
        "valid_values": "valid_values",
    }
    read_only_vars = {
        "attached_to",
        "created",
        "deleted",
        "modified",
        "prerequisite",
        "reserved",
        "table_id",
    }

    def __init__(
        self_,
        attached_to: str,
        category: Union[IncidentUserDefinedFieldCategory, none_type],
        collected: Union[IncidentUserDefinedFieldCollected, none_type],
        created: datetime,
        default_value: Union[str, none_type],
        deleted: Union[datetime, none_type],
        display_name: str,
        metadata: Union[IncidentUserDefinedFieldMetadata, none_type],
        modified: Union[datetime, none_type],
        name: str,
        ordinal: Union[str, none_type],
        prerequisite: Union[str, none_type],
        required: bool,
        reserved: bool,
        table_id: int,
        tag_key: Union[str, none_type],
        type: Union[int, none_type],
        valid_values: Union[List[IncidentUserDefinedFieldValidValue], none_type],
        **kwargs,
    ):
        """
        Attributes of an incident user-defined field.

        :param attached_to: The resource type this field is attached to. Always "incidents".
        :type attached_to: str

        :param category: The section in which the field appears. Use "what_happened" for impact-related fields or "why_it_happened" for root cause fields. When null, the field appears in the Attributes section.
        :type category: IncidentUserDefinedFieldCategory, none_type

        :param collected: The lifecycle stage at which the app prompts users to fill out this field. Cannot be set on required fields.
        :type collected: IncidentUserDefinedFieldCollected, none_type

        :param created: Timestamp when the field was created.
        :type created: datetime

        :param default_value: The default value for the field.
        :type default_value: str, none_type

        :param deleted: Timestamp when the field was soft-deleted, or null if not deleted.
        :type deleted: datetime, none_type

        :param display_name: The human-readable name shown in the UI.
        :type display_name: str

        :param metadata: Metadata for autocomplete-type user-defined fields, describing how to populate autocomplete options.
        :type metadata: IncidentUserDefinedFieldMetadata, none_type

        :param modified: Timestamp when the field was last modified.
        :type modified: datetime, none_type

        :param name: The unique machine-readable name of the field.
        :type name: str

        :param ordinal: A decimal string representing the field's display order in the UI.
        :type ordinal: str, none_type

        :param prerequisite: Reserved for future use. Always null.
        :type prerequisite: str, none_type

        :param required: When true, users must fill out this field on incidents.
        :type required: bool

        :param reserved: When true, this field is reserved for system use and cannot be deleted.
        :type reserved: bool

        :param table_id: Reserved for internal use. Always 0.
        :type table_id: int

        :param tag_key: For metric tag-type fields only, the metric tag key that powers the autocomplete options.
        :type tag_key: str, none_type

        :param type: The data type of the field. 1=dropdown, 2=multiselect, 3=textbox, 4=textarray, 5=metrictag, 6=autocomplete, 7=number, 8=datetime.
        :type type: int, none_type

        :param valid_values: The list of allowed values for dropdown, multiselect, and autocomplete fields.
        :type valid_values: [IncidentUserDefinedFieldValidValue], none_type
        """
        super().__init__(kwargs)

        self_.attached_to = attached_to
        self_.category = category
        self_.collected = collected
        self_.created = created
        self_.default_value = default_value
        self_.deleted = deleted
        self_.display_name = display_name
        self_.metadata = metadata
        self_.modified = modified
        self_.name = name
        self_.ordinal = ordinal
        self_.prerequisite = prerequisite
        self_.required = required
        self_.reserved = reserved
        self_.table_id = table_id
        self_.tag_key = tag_key
        self_.type = type
        self_.valid_values = valid_values
