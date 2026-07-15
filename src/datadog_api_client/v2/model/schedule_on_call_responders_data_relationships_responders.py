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
    from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships_responders_data_items import (
        ScheduleOnCallRespondersDataRelationshipsRespondersDataItems,
    )


class ScheduleOnCallRespondersDataRelationshipsResponders(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.schedule_on_call_responders_data_relationships_responders_data_items import (
            ScheduleOnCallRespondersDataRelationshipsRespondersDataItems,
        )

        return {
            "data": ([ScheduleOnCallRespondersDataRelationshipsRespondersDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_,
        data: Union[List[ScheduleOnCallRespondersDataRelationshipsRespondersDataItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines the list of per-position (previous, current, next) responder groups for the schedule.

        :param data: Array of references to the responder groups included in the response.
        :type data: [ScheduleOnCallRespondersDataRelationshipsRespondersDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
