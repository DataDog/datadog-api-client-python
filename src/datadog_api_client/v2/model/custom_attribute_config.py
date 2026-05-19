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
    from datadog_api_client.v2.model.custom_attribute_config_resource_attributes import (
        CustomAttributeConfigResourceAttributes,
    )
    from datadog_api_client.v2.model.custom_attribute_config_resource_type import CustomAttributeConfigResourceType


class CustomAttributeConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_attribute_config_resource_attributes import (
            CustomAttributeConfigResourceAttributes,
        )
        from datadog_api_client.v2.model.custom_attribute_config_resource_type import CustomAttributeConfigResourceType

        return {
            "attributes": (CustomAttributeConfigResourceAttributes,),
            "id": (str,),
            "type": (CustomAttributeConfigResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[CustomAttributeConfigResourceAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CustomAttributeConfigResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``CustomAttributeConfig`` object.

        :param attributes: Custom attribute resource attributes
        :type attributes: CustomAttributeConfigResourceAttributes, optional

        :param id: Custom attribute configs identifier
        :type id: str, optional

        :param type: Custom attributes config JSON:API resource type
        :type type: CustomAttributeConfigResourceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
