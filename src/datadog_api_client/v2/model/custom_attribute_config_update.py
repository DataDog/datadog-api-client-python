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
    from datadog_api_client.v2.model.custom_attribute_config_update_attributes import (
        CustomAttributeConfigUpdateAttributes,
    )
    from datadog_api_client.v2.model.custom_attribute_config_resource_type import CustomAttributeConfigResourceType


class CustomAttributeConfigUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_attribute_config_update_attributes import (
            CustomAttributeConfigUpdateAttributes,
        )
        from datadog_api_client.v2.model.custom_attribute_config_resource_type import CustomAttributeConfigResourceType

        return {
            "attributes": (CustomAttributeConfigUpdateAttributes,),
            "type": (CustomAttributeConfigResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: CustomAttributeConfigResourceType,
        attributes: Union[CustomAttributeConfigUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating a custom attribute configuration.

        :param attributes: Attributes that can be updated on a custom attribute configuration. All fields are optional; only provided fields are changed.
        :type attributes: CustomAttributeConfigUpdateAttributes, optional

        :param type: JSON:API resource type for custom attribute configurations.
        :type type: CustomAttributeConfigResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
