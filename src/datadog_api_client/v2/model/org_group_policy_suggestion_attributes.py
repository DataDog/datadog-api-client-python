# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_group_policy_suggestion_status import OrgGroupPolicySuggestionStatus


class OrgGroupPolicySuggestionAttributes(ModelNormal):
    validations = {
        "consensus_ratio": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_suggestion_status import OrgGroupPolicySuggestionStatus

        return {
            "consensus_ratio": (float,),
            "policy_name": (str,),
            "recommended_value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "status": (OrgGroupPolicySuggestionStatus,),
        }

    attribute_map = {
        "consensus_ratio": "consensus_ratio",
        "policy_name": "policy_name",
        "recommended_value": "recommended_value",
        "status": "status",
    }

    def __init__(
        self_,
        consensus_ratio: float,
        policy_name: str,
        recommended_value: Any,
        status: OrgGroupPolicySuggestionStatus,
        **kwargs,
    ):
        """
        Attributes of an org group policy suggestion.

        :param consensus_ratio: The ratio of member orgs whose configuration agrees on the recommended value.
        :type consensus_ratio: float

        :param policy_name: The name of the suggested policy.
        :type policy_name: str

        :param recommended_value: The recommended value for the policy, based on member org consensus.
        :type recommended_value: bool, date, datetime, dict, float, int, list, str, UUID, none_type

        :param status: The status of the policy suggestion.
        :type status: OrgGroupPolicySuggestionStatus
        """
        super().__init__(kwargs)

        self_.consensus_ratio = consensus_ratio
        self_.policy_name = policy_name
        self_.recommended_value = recommended_value
        self_.status = status
