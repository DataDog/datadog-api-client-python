# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProductCatalogSKUAllotment(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "child_sku_code": (str,),
            "hourly_quantity": (float,),
            "monthly_quantity": (int,),
            "parent_sku_code": (str,),
        }

    attribute_map = {
        "child_sku_code": "child_sku_code",
        "hourly_quantity": "hourly_quantity",
        "monthly_quantity": "monthly_quantity",
        "parent_sku_code": "parent_sku_code",
    }

    def __init__(
        self_, child_sku_code: str, hourly_quantity: float, monthly_quantity: int, parent_sku_code: str, **kwargs
    ):
        """
        A quantity of one SKU that is included with, and consumed before, the billable usage of
        another SKU.

        :param child_sku_code: The code of the SKU that receives the allotment.
        :type child_sku_code: str

        :param hourly_quantity: The quantity allotted per hour. Fractional for some allotments, and equal to
            ``monthly_quantity`` for others, depending on how the child SKU meters usage.
        :type hourly_quantity: float

        :param monthly_quantity: The quantity allotted per month.
        :type monthly_quantity: int

        :param parent_sku_code: The code of the SKU that provides the allotment. Always the code of the SKU the
            allotment is returned under.
        :type parent_sku_code: str
        """
        super().__init__(kwargs)

        self_.child_sku_code = child_sku_code
        self_.hourly_quantity = hourly_quantity
        self_.monthly_quantity = monthly_quantity
        self_.parent_sku_code = parent_sku_code
