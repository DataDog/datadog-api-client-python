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


class BudgetAttributesCosts(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "actual": (float, none_type),
            "amount": (float, none_type),
            "forecast": (float, none_type),
            "ootb_forecast": (float, none_type),
        }

    attribute_map = {
        "actual": "actual",
        "amount": "amount",
        "forecast": "forecast",
        "ootb_forecast": "ootb_forecast",
    }

    def __init__(
        self_,
        actual: Union[float, none_type, UnsetType] = unset,
        amount: Union[float, none_type, UnsetType] = unset,
        forecast: Union[float, none_type, UnsetType] = unset,
        ootb_forecast: Union[float, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Aggregated cost data for the budget over the requested period.

        :param actual: The total actual cost. Present only when ``actual=true`` is requested.
        :type actual: float, none_type, optional

        :param amount: The total budgeted amount over the requested period.
        :type amount: float, none_type, optional

        :param forecast: The total forecast cost, with any custom forecast overrides applied. Present only when ``forecast=true`` is requested.
        :type forecast: float, none_type, optional

        :param ootb_forecast: The out-of-the-box ML forecast before custom overrides. Present only when ``forecast=true`` is requested.
        :type ootb_forecast: float, none_type, optional
        """
        if actual is not unset:
            kwargs["actual"] = actual
        if amount is not unset:
            kwargs["amount"] = amount
        if forecast is not unset:
            kwargs["forecast"] = forecast
        if ootb_forecast is not unset:
            kwargs["ootb_forecast"] = ootb_forecast
        super().__init__(kwargs)
