# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ModelLabFacetValuesType(ModelSimple):
    """
    The JSON:API type for a facet values resource.

    :param value: If omitted defaults to "facet_values". Must be one of ["facet_values"].
    :type value: str
    """

    allowed_values = {
        "facet_values",
    }
    FACET_VALUES: ClassVar["ModelLabFacetValuesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ModelLabFacetValuesType.FACET_VALUES = ModelLabFacetValuesType("facet_values")
