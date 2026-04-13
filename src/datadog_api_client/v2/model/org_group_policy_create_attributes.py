# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class OrgGroupPolicyCreateAttributes(ModelNormal):
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
            "policy_name": (str,),
        }

    attribute_map = {
        "content": "content",
        "policy_name": "policy_name",
    }

    def __init__(self_, content: Dict[str, Any], policy_name: str, **kwargs):
        """
        Attributes for creating an org group policy.

        :param content: The policy content as key-value pairs.
        :type content: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param policy_name: The name of the policy.
        :type policy_name: str
        """
        super().__init__(kwargs)

        self_.content = content
        self_.policy_name = policy_name
