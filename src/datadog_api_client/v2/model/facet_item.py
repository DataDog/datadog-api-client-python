# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FacetItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "value": (int,),
        }

    attribute_map = {
        "name": "name",
        "value": "value",
    }

    def __init__(self_, name: str, value: int, **kwargs):
        """
        Facet item with count.

        :param name: The name of the facet value.
        :type name: str

        :param value: The count for this facet value.
        :type value: int
        """
        super().__init__(kwargs)

        self_.name = name
        self_.value = value
