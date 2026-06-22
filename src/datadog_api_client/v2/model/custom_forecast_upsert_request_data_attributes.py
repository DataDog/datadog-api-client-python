# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_forecast_entry import CustomForecastEntry


class CustomForecastUpsertRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_forecast_entry import CustomForecastEntry

        return {
            "budget_uid": (str,),
            "entries": ([CustomForecastEntry],),
        }

    attribute_map = {
        "budget_uid": "budget_uid",
        "entries": "entries",
    }

    def __init__(self_, budget_uid: str, entries: List[CustomForecastEntry], **kwargs):
        """
        Attributes of a custom forecast upsert request.

        :param budget_uid: The UUID of the budget that this custom forecast belongs to.
        :type budget_uid: str

        :param entries: Monthly custom forecast entries. An empty list deletes any existing
            custom forecast for the budget.
        :type entries: [CustomForecastEntry]
        """
        super().__init__(kwargs)

        self_.budget_uid = budget_uid
        self_.entries = entries
