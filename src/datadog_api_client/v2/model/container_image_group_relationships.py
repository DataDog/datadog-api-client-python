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
    from datadog_api_client.v2.model.container_image_group_images_relationships_link import (
        ContainerImageGroupImagesRelationshipsLink,
    )


class ContainerImageGroupRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_image_group_images_relationships_link import (
            ContainerImageGroupImagesRelationshipsLink,
        )

        return {
            "container_images": (ContainerImageGroupImagesRelationshipsLink,),
        }

    attribute_map = {
        "container_images": "container_images",
    }

    def __init__(
        self_, container_images: Union[ContainerImageGroupImagesRelationshipsLink, UnsetType] = unset, **kwargs
    ):
        """
        Relationships inside a Container Image Group.

        :param container_images: Relationships to Container Images inside a Container Image Group.
        :type container_images: ContainerImageGroupImagesRelationshipsLink, optional
        """
        if container_images is not unset:
            kwargs["container_images"] = container_images
        super().__init__(kwargs)
