# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CustomCostsFileLineItem(ModelNormal):
    validations = {
        "charge_period_end": {},
        "charge_period_start": {},
    }

    @cached_property
    def openapi_types(_):
        return {
            "billed_cost": (float,),
            "billing_currency": (str,),
            "charge_description": (str,),
            "charge_period_end": (str,),
            "charge_period_start": (str,),
            "provider_name": (str,),
            "tags": ({str: (str,)},),
        }

    attribute_map = {
        "billed_cost": "BilledCost",
        "billing_currency": "BillingCurrency",
        "charge_description": "ChargeDescription",
        "charge_period_end": "ChargePeriodEnd",
        "charge_period_start": "ChargePeriodStart",
        "provider_name": "ProviderName",
        "tags": "Tags",
    }

    def __init__(
        self_,
        billed_cost: Union[float, UnsetType] = unset,
        billing_currency: Union[str, UnsetType] = unset,
        charge_description: Union[str, UnsetType] = unset,
        charge_period_end: Union[str, UnsetType] = unset,
        charge_period_start: Union[str, UnsetType] = unset,
        provider_name: Union[str, UnsetType] = unset,
        tags: Union[Dict[str, str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Line item details from a Custom Costs file.

        :param billed_cost: Total cost in the cost file.
        :type billed_cost: float, optional

        :param billing_currency: Currency used in the Custom Costs file.
        :type billing_currency: str, optional

        :param charge_description: Description for the line item cost.
        :type charge_description: str, optional

        :param charge_period_end: End date of the usage charge.
        :type charge_period_end: str, optional

        :param charge_period_start: Start date of the usage charge.
        :type charge_period_start: str, optional

        :param provider_name: Name of the provider for the line item.
        :type provider_name: str, optional

        :param tags: Additional tags for the line item.
        :type tags: {str: (str,)}, optional
        """
        if billed_cost is not unset:
            kwargs["billed_cost"] = billed_cost
        if billing_currency is not unset:
            kwargs["billing_currency"] = billing_currency
        if charge_description is not unset:
            kwargs["charge_description"] = charge_description
        if charge_period_end is not unset:
            kwargs["charge_period_end"] = charge_period_end
        if charge_period_start is not unset:
            kwargs["charge_period_start"] = charge_period_start
        if provider_name is not unset:
            kwargs["provider_name"] = provider_name
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
