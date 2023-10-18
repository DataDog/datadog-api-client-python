# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ContainerGroupAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "tags": (dict,),
        }

    attribute_map = {
        "count": "count",
        "tags": "tags",
    }

    def __init__(self_, count: Union[int, UnsetType] = unset, tags: Union[dict, UnsetType] = unset, **kwargs):
        """
        Attributes for a container group.

        :param count: Number of containers in the group.
        :type count: int, optional

        :param tags: Tags from the group name parsed in key/value format.
        :type tags: dict, optional
        """
        if count is not unset:
            kwargs["count"] = count
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
