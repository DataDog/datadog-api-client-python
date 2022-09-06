# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ChargebackBreakdown(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "charge_type": (str,),
            "cost": (float,),
            "product_name": (str,),
        }

    attribute_map = {
        "charge_type": "charge_type",
        "cost": "cost",
        "product_name": "product_name",
    }

    def __init__(self_, *args, **kwargs):
        """
        Charges breakdown.

        :param charge_type: The type of charge for a particular product.
        :type charge_type: str, optional

        :param cost: The cost for a particular product and charge type during a given month.
        :type cost: float, optional

        :param product_name: The product for which cost is being reported.
        :type product_name: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
