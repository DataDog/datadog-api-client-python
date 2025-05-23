# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ScheduleDataIncludedItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        Any additional resources related to this schedule, such as teams and layers.

        :param attributes: Encapsulates the basic attributes of a Team reference, such as name, handle, and an optional avatar or description.
        :type attributes: TeamReferenceAttributes, optional

        :param id: The team's unique identifier.
        :type id: str, optional

        :param type: Teams resource type.
        :type type: TeamReferenceType

        :param relationships: Holds references to objects related to the Layer entity, such as its members.
        :type relationships: LayerRelationships, optional
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
        from datadog_api_client.v2.model.team_reference import TeamReference
        from datadog_api_client.v2.model.layer import Layer
        from datadog_api_client.v2.model.schedule_member import ScheduleMember
        from datadog_api_client.v2.model.schedule_user import ScheduleUser

        return {
            "oneOf": [
                TeamReference,
                Layer,
                ScheduleMember,
                ScheduleUser,
            ],
        }
