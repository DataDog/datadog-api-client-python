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


class CustomForecastResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_forecast_entry import CustomForecastEntry

        return {
            "budget_uid": (str,),
            "created_at": (int,),
            "created_by": (str,),
            "entries": ([CustomForecastEntry],),
            "updated_at": (int,),
            "updated_by": (str,),
        }

    attribute_map = {
        "budget_uid": "budget_uid",
        "created_at": "created_at",
        "created_by": "created_by",
        "entries": "entries",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        budget_uid: str,
        created_at: int,
        created_by: str,
        entries: List[CustomForecastEntry],
        updated_at: int,
        updated_by: str,
        **kwargs,
    ):
        """
        Attributes of a custom forecast.

        :param budget_uid: The UUID of the budget that this custom forecast belongs to.
        :type budget_uid: str

        :param created_at: Timestamp the custom forecast was created, in Unix milliseconds.
        :type created_at: int

        :param created_by: The id of the user that created the custom forecast.
        :type created_by: str

        :param entries: Monthly custom forecast entries.
        :type entries: [CustomForecastEntry]

        :param updated_at: Timestamp the custom forecast was last updated, in Unix milliseconds.
        :type updated_at: int

        :param updated_by: The id of the user that last updated the custom forecast.
        :type updated_by: str
        """
        super().__init__(kwargs)

        self_.budget_uid = budget_uid
        self_.created_at = created_at
        self_.created_by = created_by
        self_.entries = entries
        self_.updated_at = updated_at
        self_.updated_by = updated_by
