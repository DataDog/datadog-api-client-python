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


class CustomAttributeConfigResourceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType

        return {
            "case_type_id": (str,),
            "description": (str,),
            "display_name": (str,),
            "is_multi": (bool,),
            "key": (str,),
            "type": (CustomAttributeType,),
        }

    attribute_map = {
        "case_type_id": "case_type_id",
        "description": "description",
        "display_name": "display_name",
        "is_multi": "is_multi",
        "key": "key",
        "type": "type",
    }

    def __init__(
        self_,
        case_type_id: str,
        display_name: str,
        is_multi: bool,
        key: str,
        type: CustomAttributeType,
        description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a custom attribute configuration, defining an organization-specific metadata field that can be added to cases of a given type.

        :param case_type_id: The UUID of the case type this custom attribute belongs to.
        :type case_type_id: str

        :param description: A description explaining the purpose and expected values for this custom attribute.
        :type description: str, optional

        :param display_name: The human-readable label shown in the Case Management UI for this custom attribute.
        :type display_name: str

        :param is_multi: If ``true`` , this attribute accepts an array of values. If ``false`` , only a single value is allowed.
        :type is_multi: bool

        :param key: The programmatic key used to reference this custom attribute in search queries and API calls.
        :type key: str

        :param type: The data type of the custom attribute, which determines the allowed values and UI input control.
        :type type: CustomAttributeType
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.case_type_id = case_type_id
        self_.display_name = display_name
        self_.is_multi = is_multi
        self_.key = key
        self_.type = type
