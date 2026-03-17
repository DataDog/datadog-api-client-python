# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RumSegmentReferenceTableJoinCondition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "column_name": (str,),
            "facet": (str,),
        }

    attribute_map = {
        "column_name": "column_name",
        "facet": "facet",
    }

    def __init__(self_, column_name: str, facet: str, **kwargs):
        """
        The join condition for a reference table query block.

        :param column_name: The reference table column to join on.
        :type column_name: str

        :param facet: The RUM facet to join on.
        :type facet: str
        """
        super().__init__(kwargs)

        self_.column_name = column_name
        self_.facet = facet
