# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductCatalogSKUPricingType(ModelSimple):
    """
    How the SKU is priced. `usage` prices each billable usage unit, and `percent` prices a
        percentage; percent-priced SKUs have no `billing_units`.

    :param value: Must be one of ["usage", "percent"].
    :type value: str
    """

    allowed_values = {
        "usage",
        "percent",
    }
    USAGE: ClassVar["ProductCatalogSKUPricingType"]
    PERCENT: ClassVar["ProductCatalogSKUPricingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductCatalogSKUPricingType.USAGE = ProductCatalogSKUPricingType("usage")
ProductCatalogSKUPricingType.PERCENT = ProductCatalogSKUPricingType("percent")
