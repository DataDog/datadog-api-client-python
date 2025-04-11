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
    from datadog_api_client.v2.model.schedule_create_request_data import ScheduleCreateRequestData


class ScheduleCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_create_request_data import ScheduleCreateRequestData

        return {
            "data": (ScheduleCreateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ScheduleCreateRequestData, **kwargs):
        """
        The top-level request body for schedule creation, wrapping a ``data`` object.

        :param data: The core data wrapper for creating a schedule, encompassing attributes, relationships, and the resource type.
        :type data: ScheduleCreateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
