# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class OnCallPagesIncluded(ModelComposed):
    def __init__(self, **kwargs):
        """
        A resource related to a page.

        :param attributes: Provides basic user information for a schedule, including a name and email address.
        :type attributes: ScheduleUserAttributes, optional

        :param id: The unique user identifier.
        :type id: str

        :param type: Users resource type.
        :type type: ScheduleUserType

        :param relationships: The relationships of a scheduled action.
        :type relationships: OnCallPageScheduledActionRelationships, optional
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
        from datadog_api_client.v2.model.schedule_user import ScheduleUser
        from datadog_api_client.v2.model.team_reference import TeamReference
        from datadog_api_client.v2.model.on_call_page_scheduled_action import OnCallPageScheduledAction
        from datadog_api_client.v2.model.on_call_page_link import OnCallPageLink

        return {
            "oneOf": [
                ScheduleUser,
                TeamReference,
                OnCallPageScheduledAction,
                OnCallPageLink,
            ],
        }
