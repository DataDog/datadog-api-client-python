# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_call_page_scheduled_action_relationships_schedules_data import (
        OnCallPageScheduledActionRelationshipsSchedulesData,
    )


class OnCallPageScheduledActionRelationshipsSchedules(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_scheduled_action_relationships_schedules_data import (
            OnCallPageScheduledActionRelationshipsSchedulesData,
        )

        return {
            "data": ([OnCallPageScheduledActionRelationshipsSchedulesData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_, data: Union[List[OnCallPageScheduledActionRelationshipsSchedulesData], UnsetType] = unset, **kwargs
    ):
        """
        The schedules the action escalates to.

        :param data: The list of schedules.
        :type data: [OnCallPageScheduledActionRelationshipsSchedulesData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
