# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TenancyProductsDataType(ModelSimple):
    """
    OCI tenancy product resource type.

    :param value: If omitted defaults to "oci_tenancy_product". Must be one of ["oci_tenancy_product"].
    :type value: str
    """

    allowed_values = {
        "oci_tenancy_product",
    }
    OCI_TENANCY_PRODUCT: ClassVar["TenancyProductsDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TenancyProductsDataType.OCI_TENANCY_PRODUCT = TenancyProductsDataType("oci_tenancy_product")
