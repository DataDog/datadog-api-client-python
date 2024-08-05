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


class ListTagsResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "tags": ([str],),
        }

    attribute_map = {
        "tags": "tags",
    }

    def __init__(self_, tags: Union[List[str], UnsetType] = unset, **kwargs):
        """
        The definition of ListTagsResponseDataAttributes object.

        :param tags: The list of tags
        :type tags: [str], optional
        """
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
