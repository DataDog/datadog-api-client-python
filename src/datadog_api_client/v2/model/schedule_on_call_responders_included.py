# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ScheduleOnCallRespondersIncluded(ModelComposed):
    def __init__(self, **kwargs):
        """
        Represents a union of related resources included in the response, such as responder groups, shifts, schedules, and users.

        :param attributes: Attributes for one position's (previous, current, or next) group of on-call responder shifts.
        :type attributes: ScheduleOnCallResponderDataAttributes, optional

        :param id: Unique identifier of this responder group.
        :type id: str, optional

        :param relationships: Relationships for a single position's (previous, current, or next) responder group.
        :type relationships: ScheduleOnCallResponderDataRelationships, optional

        :param type: Represents the resource type for a single position's (previous, current, or next) group of on-call responder shifts.
        :type type: ScheduleOnCallResponderDataType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.schedule_on_call_responder_data import ScheduleOnCallResponderData
        from datadog_api_client.v2.model.shift_data import ShiftData
        from datadog_api_client.v2.model.schedule_data import ScheduleData
        from datadog_api_client.v2.model.user import User

        return {
            "oneOf": [
                ScheduleOnCallResponderData,
                ShiftData,
                ScheduleData,
                User,
            ],
        }
