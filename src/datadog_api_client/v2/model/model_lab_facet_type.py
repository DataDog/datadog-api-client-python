# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ModelLabFacetType(ModelSimple):
    """
    The type of facet for filtering Model Lab runs.

    :param value: Must be one of ["parameter", "attribute", "tag", "metric"].
    :type value: str
    """

    allowed_values = {
        "parameter",
        "attribute",
        "tag",
        "metric",
    }
    PARAMETER: ClassVar["ModelLabFacetType"]
    ATTRIBUTE: ClassVar["ModelLabFacetType"]
    TAG: ClassVar["ModelLabFacetType"]
    METRIC: ClassVar["ModelLabFacetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ModelLabFacetType.PARAMETER = ModelLabFacetType("parameter")
ModelLabFacetType.ATTRIBUTE = ModelLabFacetType("attribute")
ModelLabFacetType.TAG = ModelLabFacetType("tag")
ModelLabFacetType.METRIC = ModelLabFacetType("metric")
