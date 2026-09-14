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
)


class DeviceTagsBySource(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "source": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "source": "source",
        "tags": "tags",
    }

    def __init__(self_, source: Union[str, UnsetType] = unset, tags: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Tags associated with a device from a specific source.

        :param source: The source of the tags.
        :type source: str, optional

        :param tags: The list of tags for the source.
        :type tags: [str], optional
        """
        if source is not unset:
            kwargs["source"] = source
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
