# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.container_image_item import ContainerImageItem
    from datadog_api_client.v2.model.container_image import ContainerImage
    from datadog_api_client.v2.model.container_image_group import ContainerImageGroup


class ContainerImagesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_image_item import ContainerImageItem

        return {
            "data": ([ContainerImageItem],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_,
        data: Union[List[Union[ContainerImageItem, ContainerImage, ContainerImageGroup]], UnsetType] = unset,
        **kwargs,
    ):
        """
        List of Container Images.

        :param data: Array of Container Image objects.
        :type data: [ContainerImageItem], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
