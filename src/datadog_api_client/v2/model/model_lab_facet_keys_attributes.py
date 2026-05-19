# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class ModelLabFacetKeysAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "metrics": ([str], none_type),
            "parameters": ([str],),
            "tags": ([str],),
        }

    attribute_map = {
        "metrics": "metrics",
        "parameters": "parameters",
        "tags": "tags",
    }

    def __init__(self_, metrics: Union[List[str], none_type], parameters: List[str], tags: List[str], **kwargs):
        """
        Available facet key names for filtering resources.

        :param metrics: The list of available metric facet keys.
        :type metrics: [str], none_type

        :param parameters: The list of available parameter facet keys.
        :type parameters: [str]

        :param tags: The list of available tag facet keys.
        :type tags: [str]
        """
        super().__init__(kwargs)

        self_.metrics = metrics
        self_.parameters = parameters
        self_.tags = tags
