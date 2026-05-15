# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CommitmentsUtilizationScalarProductBreakdownEntry(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "product": (str,),
            "utilization": (float,),
        }

    attribute_map = {
        "product": "product",
        "utilization": "utilization",
    }

    def __init__(self_, product: str, utilization: float, **kwargs):
        """
        Per-product utilization data in a scalar utilization response.

        :param product: The cloud product name.
        :type product: str

        :param utilization: The utilization percentage for the product.
        :type utilization: float
        """
        super().__init__(kwargs)

        self_.product = product
        self_.utilization = utilization
