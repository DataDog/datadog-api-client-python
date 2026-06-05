# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class BudgetWithEntriesDataAttributesEntriesItemsCosts(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "actual": (float, none_type),
            "amount": (float, none_type),
            "custom_forecast": (float, none_type),
            "forecast": (float, none_type),
            "ootb_forecast": (float, none_type),
        }

    attribute_map = {
        "actual": "actual",
        "amount": "amount",
        "custom_forecast": "custom_forecast",
        "forecast": "forecast",
        "ootb_forecast": "ootb_forecast",
    }

    def __init__(
        self_,
        actual: Union[float, none_type, UnsetType] = unset,
        amount: Union[float, none_type, UnsetType] = unset,
        custom_forecast: Union[float, none_type, UnsetType] = unset,
        forecast: Union[float, none_type, UnsetType] = unset,
        ootb_forecast: Union[float, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Cost data for a single budget entry.

        :param actual: The actual cost for this entry. Present only when ``actual=true`` is requested.
        :type actual: float, none_type, optional

        :param amount: The budgeted amount for this entry.
        :type amount: float, none_type, optional

        :param custom_forecast: The custom forecast override for this entry. ``null`` when ``forecast=true`` is requested but no custom forecast has been set for this entry's month. A numeric value, including ``0`` , indicates an explicit custom forecast override. Omitted when ``forecast=false`` or the feature is not available for the organization.
        :type custom_forecast: float, none_type, optional

        :param forecast: The final forecast for this entry, with any custom forecast override applied. Present only when ``forecast=true`` is requested.
        :type forecast: float, none_type, optional

        :param ootb_forecast: The out-of-the-box ML forecast for this entry, before custom overrides. Present only when ``forecast=true`` is requested.
        :type ootb_forecast: float, none_type, optional
        """
        if actual is not unset:
            kwargs["actual"] = actual
        if amount is not unset:
            kwargs["amount"] = amount
        if custom_forecast is not unset:
            kwargs["custom_forecast"] = custom_forecast
        if forecast is not unset:
            kwargs["forecast"] = forecast
        if ootb_forecast is not unset:
            kwargs["ootb_forecast"] = ootb_forecast
        super().__init__(kwargs)
