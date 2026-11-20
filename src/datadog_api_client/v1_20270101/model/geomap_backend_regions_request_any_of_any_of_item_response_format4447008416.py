# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GeomapBackendRegionsRequestAnyOfAnyOfItemResponseFormat4447008416(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "scalar". Must be one of ["scalar"].
    :type value: str
    """

    allowed_values = {
        "scalar",
    }
    SCALAR: ClassVar["GeomapBackendRegionsRequestAnyOfAnyOfItemResponseFormat4447008416"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GeomapBackendRegionsRequestAnyOfAnyOfItemResponseFormat4447008416.SCALAR = (
    GeomapBackendRegionsRequestAnyOfAnyOfItemResponseFormat4447008416("scalar")
)
