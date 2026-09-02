# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductCatalogSKUOnDemandOption(ModelSimple):
    """
    The billing frequency applied to on-demand usage of the SKU by default.

    :param value: Must be one of ["hourly", "monthly"].
    :type value: str
    """

    allowed_values = {
        "hourly",
        "monthly",
    }
    HOURLY: ClassVar["ProductCatalogSKUOnDemandOption"]
    MONTHLY: ClassVar["ProductCatalogSKUOnDemandOption"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductCatalogSKUOnDemandOption.HOURLY = ProductCatalogSKUOnDemandOption("hourly")
ProductCatalogSKUOnDemandOption.MONTHLY = ProductCatalogSKUOnDemandOption("monthly")
