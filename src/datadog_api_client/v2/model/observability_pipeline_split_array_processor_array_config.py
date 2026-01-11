# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineSplitArrayProcessorArrayConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "field": (str,),
            "include": (str,),
        }

    attribute_map = {
        "field": "field",
        "include": "include",
    }

    def __init__(self_, field: str, include: str, **kwargs):
        """
        Configuration for a single array split operation.

        :param field: The path to the array field to split.
        :type field: str

        :param include: A Datadog search query used to determine which logs this array split operation targets.
        :type include: str
        """
        super().__init__(kwargs)

        self_.field = field
        self_.include = include
