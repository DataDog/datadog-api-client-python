# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


class ActionQuerySpecConnectionGroup(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (UUID,),
            "tags": ([str],),
        }

    attribute_map = {
        "id": "id",
        "tags": "tags",
    }

    def __init__(self_, id: Union[UUID, UnsetType] = unset, tags: Union[List[str], UnsetType] = unset, **kwargs):
        """
        The connection group to use for an action query.

        :param id: The ID of the connection group.
        :type id: UUID, optional

        :param tags: The tags of the connection group.
        :type tags: [str], optional
        """
        if id is not unset:
            kwargs["id"] = id
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
