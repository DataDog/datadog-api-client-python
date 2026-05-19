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


class CustomAttributeConfigAttributesCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType

        return {
            "description": (str,),
            "display_name": (str,),
            "is_multi": (bool,),
            "key": (str,),
            "type": (CustomAttributeType,),
        }

    attribute_map = {
        "description": "description",
        "display_name": "display_name",
        "is_multi": "is_multi",
        "key": "key",
        "type": "type",
    }

    def __init__(
        self_,
        display_name: str,
        is_multi: bool,
        key: str,
        type: CustomAttributeType,
        description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Custom attribute config resource attributes

        :param description: Custom attribute description.
        :type description: str, optional

        :param display_name: Custom attribute name.
        :type display_name: str

        :param is_multi: Whether multiple values can be set
        :type is_multi: bool

        :param key: Custom attribute key. This will be the value use to search on this custom attribute
        :type key: str

        :param type: Custom attributes type
        :type type: CustomAttributeType
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.display_name = display_name
        self_.is_multi = is_multi
        self_.key = key
        self_.type = type
