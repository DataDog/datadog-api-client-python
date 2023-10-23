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
    from datadog_api_client.v2.model.container_image_attributes import ContainerImageAttributes
    from datadog_api_client.v2.model.container_image_type import ContainerImageType


class ContainerImage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_image_attributes import ContainerImageAttributes
        from datadog_api_client.v2.model.container_image_type import ContainerImageType

        return {
            "attributes": (ContainerImageAttributes,),
            "id": (str,),
            "type": (ContainerImageType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ContainerImageAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[ContainerImageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Container Image object.

        :param attributes: Attributes for a Container Image.
        :type attributes: ContainerImageAttributes, optional

        :param id: Container Image ID.
        :type id: str, optional

        :param type: Type of Container Image.
        :type type: ContainerImageType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
