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


class AiGatewayModelAutomaticPricingRate(ModelNormal):
    validations = {
        "amount": {},
        "context_max_tokens": {
            "inclusive_minimum": 1,
        },
        "context_min_tokens": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "amount": (str,),
            "component": (str,),
            "context_max_tokens": (int,),
            "context_min_tokens": (int,),
            "currency": (str,),
            "mode": (str,),
            "operation": (str,),
            "service_tier": (str,),
            "unit": (str,),
        }

    attribute_map = {
        "amount": "amount",
        "component": "component",
        "context_max_tokens": "context_max_tokens",
        "context_min_tokens": "context_min_tokens",
        "currency": "currency",
        "mode": "mode",
        "operation": "operation",
        "service_tier": "service_tier",
        "unit": "unit",
    }

    def __init__(
        self_,
        amount: str,
        component: str,
        currency: str,
        mode: str,
        unit: str,
        context_max_tokens: Union[int, UnsetType] = unset,
        context_min_tokens: Union[int, UnsetType] = unset,
        operation: Union[str, UnsetType] = unset,
        service_tier: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        One published price. Prices can differ by operation, mode, service tier, and input length.

        :param amount: Exact decimal amount per unit, zero or greater, represented as a string to preserve precision. Supports fixed decimal and exponent notation.
        :type amount: str

        :param component: Token category priced, such as ``input`` , ``output`` , ``cache_read`` , or ``cache_write``.
        :type component: str

        :param context_max_tokens: Largest input length covered by this price. Omitted when there is no upper bound.
        :type context_max_tokens: int, optional

        :param context_min_tokens: Input length above which this price applies. Omitted for the base tier.
        :type context_min_tokens: int, optional

        :param currency: Currency of the price. The only supported value is USD.
        :type currency: str

        :param mode: Source mode name. ``standard`` is the base mode. Other values, such as ``fast`` , are source-defined and
            selected by ``mode_triggers``.
        :type mode: str

        :param operation: Operation the price applies to. Omitted when it applies to every operation.
        :type operation: str, optional

        :param service_tier: Provider service tier explicitly associated with this mode by the source. Omitted when unknown.
        :type service_tier: str, optional

        :param unit: Unit of the quoted amount. The only supported value is million_tokens.
        :type unit: str
        """
        if context_max_tokens is not unset:
            kwargs["context_max_tokens"] = context_max_tokens
        if context_min_tokens is not unset:
            kwargs["context_min_tokens"] = context_min_tokens
        if operation is not unset:
            kwargs["operation"] = operation
        if service_tier is not unset:
            kwargs["service_tier"] = service_tier
        super().__init__(kwargs)

        self_.amount = amount
        self_.component = component
        self_.currency = currency
        self_.mode = mode
        self_.unit = unit
