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
    from datadog_api_client.v2.model.escalation_policy_list_item import EscalationPolicyListItem
    from datadog_api_client.v2.model.escalation_policy_included import EscalationPolicyIncluded
    from datadog_api_client.v2.model.escalation_policies_response_meta import EscalationPoliciesResponseMeta
    from datadog_api_client.v2.model.escalation_policy_step import EscalationPolicyStep
    from datadog_api_client.v2.model.escalation_policy_user import EscalationPolicyUser
    from datadog_api_client.v2.model.schedule_data import ScheduleData
    from datadog_api_client.v2.model.configured_schedule import ConfiguredSchedule
    from datadog_api_client.v2.model.team_reference import TeamReference


class EscalationPolicies(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_list_item import EscalationPolicyListItem
        from datadog_api_client.v2.model.escalation_policy_included import EscalationPolicyIncluded
        from datadog_api_client.v2.model.escalation_policies_response_meta import EscalationPoliciesResponseMeta

        return {
            "data": ([EscalationPolicyListItem],),
            "included": ([EscalationPolicyIncluded],),
            "meta": (EscalationPoliciesResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[EscalationPolicyListItem],
        included: Union[
            List[
                Union[
                    EscalationPolicyIncluded,
                    EscalationPolicyStep,
                    EscalationPolicyUser,
                    ScheduleData,
                    ConfiguredSchedule,
                    TeamReference,
                ]
            ],
            UnsetType,
        ] = unset,
        meta: Union[EscalationPoliciesResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        A paginated list of escalation policies, with any related resources requested through ``include``.

        :param data: A list of escalation policies.
        :type data: [EscalationPolicyListItem]

        :param included: Provides any included related resources, such as teams, steps, or targets, returned with the policies.
        :type included: [EscalationPolicyIncluded], optional

        :param meta: Metadata included in the response when listing escalation policies.
        :type meta: EscalationPoliciesResponseMeta, optional
        """
        if included is not unset:
            kwargs["included"] = included
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
