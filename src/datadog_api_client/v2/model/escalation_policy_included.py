# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class EscalationPolicyIncluded(ModelComposed):
    def __init__(self, **kwargs):
        """
        Represents included related resources when retrieving an escalation policy, such as teams, steps, or targets.

        :param attributes: Encapsulates the basic attributes of a Team reference, such as name, handle, and an optional avatar or description.
        :type attributes: TeamReferenceAttributes, optional

        :param id: The team's unique identifier.
        :type id: str, optional

        :param type: Teams resource type.
        :type type: TeamReferenceType

        :param relationships: Represents the relationship of an escalation policy step to its targets.
        :type relationships: EscalationPolicyStepRelationships, optional
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
        from datadog_api_client.v2.model.escalation_policy_step import EscalationPolicyStep
        from datadog_api_client.v2.model.escalation_policy_user import EscalationPolicyUser
        from datadog_api_client.v2.model.schedule_data import ScheduleData

        return {
            "oneOf": [
                TeamReference,
                EscalationPolicyStep,
                EscalationPolicyUser,
                ScheduleData,
            ],
        }
