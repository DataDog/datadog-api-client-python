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
    from datadog_api_client.v2.model.container_item import ContainerItem
    from datadog_api_client.v2.model.containers_response_links import ContainersResponseLinks
    from datadog_api_client.v2.model.container_meta import ContainerMeta
    from datadog_api_client.v2.model.container import Container
    from datadog_api_client.v2.model.container_group import ContainerGroup


class ContainersResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_item import ContainerItem
        from datadog_api_client.v2.model.containers_response_links import ContainersResponseLinks
        from datadog_api_client.v2.model.container_meta import ContainerMeta

        return {
            "data": ([ContainerItem],),
            "links": (ContainersResponseLinks,),
            "meta": (ContainerMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[Union[ContainerItem, Container, ContainerGroup]], UnsetType] = unset,
        links: Union[ContainersResponseLinks, UnsetType] = unset,
        meta: Union[ContainerMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        List of containers.

        :param data: Array of Container objects.
        :type data: [ContainerItem], optional

        :param links: Pagination links.
        :type links: ContainersResponseLinks, optional

        :param meta: Response metadata object.
        :type meta: ContainerMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
