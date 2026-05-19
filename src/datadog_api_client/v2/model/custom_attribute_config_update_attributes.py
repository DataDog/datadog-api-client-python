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
    from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType
    from datadog_api_client.v2.model.custom_attribute_type_data import CustomAttributeTypeData


class CustomAttributeConfigUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType
        from datadog_api_client.v2.model.custom_attribute_type_data import CustomAttributeTypeData

        return {
            "description": (str,),
            "display_name": (str,),
            "map_from": (str,),
            "type": (CustomAttributeType,),
            "type_data": (CustomAttributeTypeData,),
        }

    attribute_map = {
        "description": "description",
        "display_name": "display_name",
        "map_from": "map_from",
        "type": "type",
        "type_data": "type_data",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        map_from: Union[str, UnsetType] = unset,
        type: Union[CustomAttributeType, UnsetType] = unset,
        type_data: Union[CustomAttributeTypeData, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes that can be updated on a custom attribute configuration. All fields are optional; only provided fields are changed.

        :param description: A description explaining the purpose and expected values for this custom attribute.
        :type description: str, optional

        :param display_name: The human-readable label shown in the Case Management UI for this custom attribute.
        :type display_name: str, optional

        :param map_from: An external field identifier to auto-populate this attribute from (used for integrations with external systems).
        :type map_from: str, optional

        :param type: The data type of the custom attribute, which determines the allowed values and UI input control.
        :type type: CustomAttributeType, optional

        :param type_data: Type-specific configuration for the custom attribute. For SELECT-type attributes, this contains the list of allowed options.
        :type type_data: CustomAttributeTypeData, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if map_from is not unset:
            kwargs["map_from"] = map_from
        if type is not unset:
            kwargs["type"] = type
        if type_data is not unset:
            kwargs["type_data"] = type_data
        super().__init__(kwargs)
