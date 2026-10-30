# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TopologyRequestCustomProjectionDimension(ModelNormal):
    validations = {
        "dimension": {},
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "column": (str,),
            "dimension": (str,),
        }

    attribute_map = {
        "column": "column",
        "dimension": "dimension",
    }

    def __init__(self_, column: str, dimension: str, **kwargs):
        """
        Mapping from one result column to one node field.

        :param column: Column name from the result. Must be a group-by tag key or a formula.
        :type column: str

        :param dimension: Node field that receives the column's value: ``id`` , ``title`` , ``subtitle`` , or ``values[N]`` for the value at position N. When ``id`` is not set, each node's ID is derived from the group-by tags (for example, ``env:prod,service:web`` ). When ``title`` is not set, the title is the node's ID. When several rows set the same non- ``id`` field on a node, the last non-null value wins.
        :type dimension: str
        """
        super().__init__(kwargs)

        self_.column = column
        self_.dimension = dimension
