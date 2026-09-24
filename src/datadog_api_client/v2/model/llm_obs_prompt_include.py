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


class LLMObsPromptInclude(ModelNormal):
    validations = {
        "items": {
            "min_items": 1,
        },
        "prompt_id": {
            "min_length": 1,
        },
        "version": {
            "inclusive_maximum": 2147483647,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "items": ([int],),
            "prompt_id": (str,),
            "version": (int,),
        }

    attribute_map = {
        "items": "items",
        "prompt_id": "prompt_id",
        "version": "version",
    }

    def __init__(self_, prompt_id: str, version: int, items: Union[List[int], UnsetType] = unset, **kwargs):
        """
        Includes messages from a specific version of another prompt. Omitting ``items`` includes every message from that version in its original order. When ``items`` is present, messages are included in the specified order, including repetitions.

        :param items: Zero-based indexes of messages from the included prompt. For example, ``[2, 0, 0]`` includes the third message, followed by the first message twice. Omit this field to include all messages in their original order.
        :type items: [int], optional

        :param prompt_id: Customer-provided identifier of the included prompt.
        :type prompt_id: str

        :param version: Positive sequential version number of the included prompt.
        :type version: int
        """
        if items is not unset:
            kwargs["items"] = items
        super().__init__(kwargs)

        self_.prompt_id = prompt_id
        self_.version = version
