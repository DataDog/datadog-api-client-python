# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.allocation_exposure_schedule import AllocationExposureSchedule
    from datadog_api_client.v2.model.allocation_exposure_schedule_data_type import AllocationExposureScheduleDataType


class AllocationExposureScheduleData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.allocation_exposure_schedule import AllocationExposureSchedule
        from datadog_api_client.v2.model.allocation_exposure_schedule_data_type import (
            AllocationExposureScheduleDataType,
        )

        return {
            "attributes": (AllocationExposureSchedule,),
            "id": (UUID,),
            "type": (AllocationExposureScheduleDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AllocationExposureSchedule, id: UUID, type: AllocationExposureScheduleDataType, **kwargs
    ):
        """
        Data wrapper for progressive rollout schedule responses.

        :param attributes: Progressive release details for a targeting rule allocation.
        :type attributes: AllocationExposureSchedule

        :param id: The unique identifier of the progressive rollout.
        :type id: UUID

        :param type: The resource type for progressive rollout schedules.
        :type type: AllocationExposureScheduleDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
