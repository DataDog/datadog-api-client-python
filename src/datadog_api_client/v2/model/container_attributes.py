# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ContainerAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "container_id": (str,),
            "created_at": (str,),
            "host": (str,),
            "image_digest": (str, none_type),
            "image_name": (str,),
            "image_tags": ([str], none_type),
            "name": (str,),
            "started_at": (str,),
            "state": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "container_id": "container_id",
        "created_at": "created_at",
        "host": "host",
        "image_digest": "image_digest",
        "image_name": "image_name",
        "image_tags": "image_tags",
        "name": "name",
        "started_at": "started_at",
        "state": "state",
        "tags": "tags",
    }

    def __init__(
        self_,
        container_id: Union[str, UnsetType] = unset,
        created_at: Union[str, UnsetType] = unset,
        host: Union[str, UnsetType] = unset,
        image_digest: Union[str, none_type, UnsetType] = unset,
        image_name: Union[str, UnsetType] = unset,
        image_tags: Union[List[str], none_type, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        started_at: Union[str, UnsetType] = unset,
        state: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for a container.

        :param container_id: The ID of the container.
        :type container_id: str, optional

        :param created_at: Time the container was created.
        :type created_at: str, optional

        :param host: Hostname of the host running the container.
        :type host: str, optional

        :param image_digest: Digest of the compressed image manifest.
        :type image_digest: str, none_type, optional

        :param image_name: Name of the associated container image.
        :type image_name: str, optional

        :param image_tags: List of image tags associated with the container image.
        :type image_tags: [str], none_type, optional

        :param name: Name of the container.
        :type name: str, optional

        :param started_at: Time the container was started.
        :type started_at: str, optional

        :param state: State of the container. This depends on the container runtime.
        :type state: str, optional

        :param tags: List of tags associated with the container.
        :type tags: [str], optional
        """
        if container_id is not unset:
            kwargs["container_id"] = container_id
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if host is not unset:
            kwargs["host"] = host
        if image_digest is not unset:
            kwargs["image_digest"] = image_digest
        if image_name is not unset:
            kwargs["image_name"] = image_name
        if image_tags is not unset:
            kwargs["image_tags"] = image_tags
        if name is not unset:
            kwargs["name"] = name
        if started_at is not unset:
            kwargs["started_at"] = started_at
        if state is not unset:
            kwargs["state"] = state
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
