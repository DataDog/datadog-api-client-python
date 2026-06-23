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
    from datadog_api_client.v1.model.logs_category_processor_category import LogsCategoryProcessorCategory
    from datadog_api_client.v1.model.logs_category_processor_type import LogsCategoryProcessorType


class LogsArrayMapCategorySubProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_category_processor_category import LogsCategoryProcessorCategory
        from datadog_api_client.v1.model.logs_category_processor_type import LogsCategoryProcessorType

        return {
            "categories": ([LogsCategoryProcessorCategory],),
            "name": (str,),
            "target": (str,),
            "type": (LogsCategoryProcessorType,),
        }

    attribute_map = {
        "categories": "categories",
        "name": "name",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        categories: List[LogsCategoryProcessorCategory],
        target: str,
        type: LogsCategoryProcessorType,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A category sub-processor for use inside an array-map processor.
        Unlike the top-level category processor, ``is_enabled`` is not supported.

        :param categories: Array of filters to match against a log and the corresponding value to assign.
        :type categories: [LogsCategoryProcessorCategory]

        :param name: Name of the sub-processor.
        :type name: str, optional

        :param target: Target attribute path for the category value.
        :type target: str

        :param type: Type of logs category processor.
        :type type: LogsCategoryProcessorType
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.categories = categories
        self_.target = target
        self_.type = type
