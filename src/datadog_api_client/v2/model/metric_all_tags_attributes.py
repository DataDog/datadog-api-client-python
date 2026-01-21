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


class MetricAllTagsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ingested_tags": ([str],),
            "tags": ([str],),
        }

    attribute_map = {
        "ingested_tags": "ingested_tags",
        "tags": "tags",
    }

    def __init__(
        self_, ingested_tags: Union[List[str], UnsetType] = unset, tags: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Object containing the definition of a metric's indexed and ingested tags.

        :param ingested_tags: List of ingested tags that are not indexed.
        :type ingested_tags: [str], optional

        :param tags: List of indexed tags.
        :type tags: [str], optional
        """
        if ingested_tags is not unset:
            kwargs["ingested_tags"] = ingested_tags
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
