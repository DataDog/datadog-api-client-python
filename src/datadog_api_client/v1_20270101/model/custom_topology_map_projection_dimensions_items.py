# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.custom_topology_map_node_dimension import CustomTopologyMapNodeDimension


class CustomTopologyMapProjectionDimensionsItems(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.custom_topology_map_node_dimension import (
            CustomTopologyMapNodeDimension,
        )

        return {
            "column": (str,),
            "dimension": (CustomTopologyMapNodeDimension,),
        }

    attribute_map = {
        "column": "column",
        "dimension": "dimension",
    }

    def __init__(self_, column: str, dimension: Union[CustomTopologyMapNodeDimension, str], **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param dimension: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimension: CustomTopologyMapNodeDimension
        """
        super().__init__(kwargs)

        self_.column = column
        self_.dimension = dimension
