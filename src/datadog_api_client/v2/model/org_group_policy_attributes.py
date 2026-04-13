# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class OrgGroupPolicyAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "content": (
                {
                    str: (
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
                    )
                },
            ),
            "enforced_at": (datetime,),
            "modified_at": (datetime,),
            "policy_name": (str,),
        }

    attribute_map = {
        "content": "content",
        "enforced_at": "enforced_at",
        "modified_at": "modified_at",
        "policy_name": "policy_name",
    }

    def __init__(
        self_,
        enforced_at: datetime,
        modified_at: datetime,
        policy_name: str,
        content: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an org group policy.

        :param content: The policy content as key-value pairs.
        :type content: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param enforced_at: Timestamp when the policy was enforced.
        :type enforced_at: datetime

        :param modified_at: Timestamp when the policy was last modified.
        :type modified_at: datetime

        :param policy_name: The name of the policy.
        :type policy_name: str
        """
        if content is not unset:
            kwargs["content"] = content
        super().__init__(kwargs)

        self_.enforced_at = enforced_at
        self_.modified_at = modified_at
        self_.policy_name = policy_name
