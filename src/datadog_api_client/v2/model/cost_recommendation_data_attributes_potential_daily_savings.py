# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CostRecommendationDataAttributesPotentialDailySavings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "amount": (float,),
            "currency": (str,),
        }

    attribute_map = {
        "amount": "amount",
        "currency": "currency",
    }

    def __init__(self_, amount: Union[float, UnsetType] = unset, currency: Union[str, UnsetType] = unset, **kwargs):
        """
        Estimated daily savings if the recommendation is applied.

        :param amount: Numeric amount of the potential daily savings.
        :type amount: float, optional

        :param currency: ISO 4217 currency code for the savings amount.
        :type currency: str, optional
        """
        if amount is not unset:
            kwargs["amount"] = amount
        if currency is not unset:
            kwargs["currency"] = currency
        super().__init__(kwargs)
