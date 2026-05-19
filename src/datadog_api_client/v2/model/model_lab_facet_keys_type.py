# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ModelLabFacetKeysType(ModelSimple):
    """
    The JSON:API type for a facet keys resource.

    :param value: If omitted defaults to "facet_keys". Must be one of ["facet_keys"].
    :type value: str
    """

    allowed_values = {
        "facet_keys",
    }
    FACET_KEYS: ClassVar["ModelLabFacetKeysType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ModelLabFacetKeysType.FACET_KEYS = ModelLabFacetKeysType("facet_keys")
