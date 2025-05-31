# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.schedule_update_request_data import ScheduleUpdateRequestData


class ScheduleUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_update_request_data import ScheduleUpdateRequestData

        return {
            "data": (ScheduleUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ScheduleUpdateRequestData, **kwargs):
        """
        A top-level wrapper for a schedule update request, referring to the ``data`` object with the new details.

        :param data: Contains all data needed to update an existing schedule, including its attributes (such as name and time zone) and any relationships to teams.
        :type data: ScheduleUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
