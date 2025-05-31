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
    from datadog_api_client.v2.model.custom_framework_without_requirements import CustomFrameworkWithoutRequirements
    from datadog_api_client.v2.model.custom_framework_type import CustomFrameworkType


class CustomFrameworkMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_framework_without_requirements import CustomFrameworkWithoutRequirements
        from datadog_api_client.v2.model.custom_framework_type import CustomFrameworkType

        return {
            "attributes": (CustomFrameworkWithoutRequirements,),
            "id": (str,),
            "type": (CustomFrameworkType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[CustomFrameworkWithoutRequirements, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CustomFrameworkType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata for custom frameworks.

        :param attributes: Framework without requirements.
        :type attributes: CustomFrameworkWithoutRequirements, optional

        :param id: The ID of the custom framework.
        :type id: str, optional

        :param type: The type of the resource. The value must be ``custom_framework``.
        :type type: CustomFrameworkType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
