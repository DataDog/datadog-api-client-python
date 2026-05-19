# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType
    from datadog_api_client.v2.model.custom_attribute_values_union import CustomAttributeValuesUnion


class CustomAttributeValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType
        from datadog_api_client.v2.model.custom_attribute_values_union import CustomAttributeValuesUnion

        return {
            "is_multi": (bool,),
            "type": (CustomAttributeType,),
            "value": (CustomAttributeValuesUnion,),
        }

    attribute_map = {
        "is_multi": "is_multi",
        "type": "type",
        "value": "value",
    }

    def __init__(
        self_,
        is_multi: bool,
        type: CustomAttributeType,
        value: Union[CustomAttributeValuesUnion, str, List[str], float, List[float]],
        **kwargs,
    ):
        """
        Custom attribute values

        :param is_multi: If true, value must be an array
        :type is_multi: bool

        :param type: Custom attributes type
        :type type: CustomAttributeType

        :param value: Union of supported value for a custom attribute
        :type value: CustomAttributeValuesUnion
        """
        super().__init__(kwargs)

        self_.is_multi = is_multi
        self_.type = type
        self_.value = value
