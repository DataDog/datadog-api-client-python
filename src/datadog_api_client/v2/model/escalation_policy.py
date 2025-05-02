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
    from datadog_api_client.v2.model.escalation_policy_data import EscalationPolicyData
    from datadog_api_client.v2.model.escalation_policy_included import EscalationPolicyIncluded
    from datadog_api_client.v2.model.team_reference import TeamReference
    from datadog_api_client.v2.model.escalation_policy_step import EscalationPolicyStep
    from datadog_api_client.v2.model.escalation_policy_user import EscalationPolicyUser
    from datadog_api_client.v2.model.schedule_data import ScheduleData


class EscalationPolicy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_data import EscalationPolicyData
        from datadog_api_client.v2.model.escalation_policy_included import EscalationPolicyIncluded

        return {
            "data": (EscalationPolicyData,),
            "included": ([EscalationPolicyIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[EscalationPolicyData, UnsetType] = unset,
        included: Union[
            List[
                Union[EscalationPolicyIncluded, TeamReference, EscalationPolicyStep, EscalationPolicyUser, ScheduleData]
            ],
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Represents a complete escalation policy response, including policy data and optionally included related resources.

        :param data: Represents the data for a single escalation policy, including its attributes, ID, relationships, and resource type.
        :type data: EscalationPolicyData, optional

        :param included: Provides any included related resources, such as steps or targets, returned with the policy.
        :type included: [EscalationPolicyIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
