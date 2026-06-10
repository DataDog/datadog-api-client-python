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
    from datadog_api_client.v2.model.report_schedule_create_request_data import ReportScheduleCreateRequestData


class ReportScheduleCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.report_schedule_create_request_data import ReportScheduleCreateRequestData

        return {
            "data": (ReportScheduleCreateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ReportScheduleCreateRequestData, **kwargs):
        """
        Request body for creating a report schedule.

        :param data: The JSON:API data object for a report schedule creation request.
        :type data: ReportScheduleCreateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
