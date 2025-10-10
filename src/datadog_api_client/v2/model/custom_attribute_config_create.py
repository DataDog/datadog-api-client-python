# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_attribute_config_attributes_create import (
        CustomAttributeConfigAttributesCreate,
    )
    from datadog_api_client.v2.model.custom_attribute_config_resource_type import CustomAttributeConfigResourceType


class CustomAttributeConfigCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_attribute_config_attributes_create import (
            CustomAttributeConfigAttributesCreate,
        )
        from datadog_api_client.v2.model.custom_attribute_config_resource_type import CustomAttributeConfigResourceType

        return {
            "attributes": (CustomAttributeConfigAttributesCreate,),
            "type": (CustomAttributeConfigResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: CustomAttributeConfigAttributesCreate, type: CustomAttributeConfigResourceType, **kwargs
    ):
        """
        Custom attribute config

        :param attributes: Custom attribute config resource attributes
        :type attributes: CustomAttributeConfigAttributesCreate

        :param type: Custom attributes config JSON:API resource type
        :type type: CustomAttributeConfigResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
