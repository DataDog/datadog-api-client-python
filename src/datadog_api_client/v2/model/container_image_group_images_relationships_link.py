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
    from datadog_api_client.v2.model.container_image_group_relationships_links import (
        ContainerImageGroupRelationshipsLinks,
    )


class ContainerImageGroupImagesRelationshipsLink(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_image_group_relationships_links import (
            ContainerImageGroupRelationshipsLinks,
        )

        return {
            "data": ([str],),
            "links": (ContainerImageGroupRelationshipsLinks,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
    }

    def __init__(
        self_,
        data: Union[List[str], UnsetType] = unset,
        links: Union[ContainerImageGroupRelationshipsLinks, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships to Container Images inside a Container Image Group.

        :param data: Links data.
        :type data: [str], optional

        :param links: Links attributes.
        :type links: ContainerImageGroupRelationshipsLinks, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        super().__init__(kwargs)
