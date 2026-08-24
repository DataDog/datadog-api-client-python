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
    from datadog_api_client.v2.model.device_tags_by_source import DeviceTagsBySource


class ListTagsResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.device_tags_by_source import DeviceTagsBySource

        return {
            "by_source": ([DeviceTagsBySource],),
            "tags": ([str],),
        }

    attribute_map = {
        "by_source": "by_source",
        "tags": "tags",
    }
    read_only_vars = {
        "by_source",
    }

    def __init__(
        self_,
        by_source: Union[List[DeviceTagsBySource], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ListTagsResponseDataAttributes object.

        :param by_source: The list of device tags grouped by source.
        :type by_source: [DeviceTagsBySource], optional

        :param tags: The list of tags
        :type tags: [str], optional
        """
        if by_source is not unset:
            kwargs["by_source"] = by_source
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
