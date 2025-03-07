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
    from datadog_api_client.v2.model.filter_processor_type import FilterProcessorType


class FilterProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.filter_processor_type import FilterProcessorType

        return {
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "type": (FilterProcessorType,),
        }

    attribute_map = {
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_, id: str, include: str, type: FilterProcessorType, inputs: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        A filter processor component.

        :param id: The unique ID of the processor.
        :type id: str

        :param include: Inclusion filter for the processor.
        :type include: str

        :param inputs: The inputs for the processor.
        :type inputs: [str], optional

        :param type: The type of processor.
        :type type: FilterProcessorType
        """
        if inputs is not unset:
            kwargs["inputs"] = inputs
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.type = type
