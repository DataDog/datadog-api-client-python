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
    from datadog_api_client.v2.model.parse_json_processor_type import ParseJSONProcessorType


class ParseJSONProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.parse_json_processor_type import ParseJSONProcessorType

        return {
            "field": (str,),
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "type": (ParseJSONProcessorType,),
        }

    attribute_map = {
        "field": "field",
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        field: str,
        id: str,
        inputs: List[str],
        type: ParseJSONProcessorType,
        include: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``parse_json`` processor extracts JSON from a specified field and flattens it into the event. This is useful when logs contain embedded JSON as a string.

        :param field: The ``ParseJSONProcessor`` ``field``.
        :type field: str

        :param id: The ``ParseJSONProcessor`` ``id``.
        :type id: str

        :param include: The ``ParseJSONProcessor`` ``include``.
        :type include: str, optional

        :param inputs: The ``ParseJSONProcessor`` ``inputs``.
        :type inputs: [str]

        :param type: The ``ParseJSONProcessor`` ``type``.
        :type type: ParseJSONProcessorType
        """
        if include is not unset:
            kwargs["include"] = include
        super().__init__(kwargs)

        self_.field = field
        self_.id = id
        self_.inputs = inputs
        self_.type = type
