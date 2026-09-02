# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductCatalogSKUType(ModelSimple):
    """
    The SKU resource type.

    :param value: If omitted defaults to "Sku". Must be one of ["Sku"].
    :type value: str
    """

    allowed_values = {
        "Sku",
    }
    SKU: ClassVar["ProductCatalogSKUType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductCatalogSKUType.SKU = ProductCatalogSKUType("Sku")
