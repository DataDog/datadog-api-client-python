# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CloudWorkloadSecurityAgentPolicyCreateAttributes(ModelNormal):
    validations = {
        "priority": {
            "inclusive_maximum": 1000000000,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "enabled": (bool,),
            "host_tags": ([str],),
            "name": (str,),
            "priority": (int,),
        }

    attribute_map = {
        "description": "description",
        "enabled": "enabled",
        "host_tags": "hostTags",
        "name": "name",
        "priority": "priority",
    }

    def __init__(
        self_,
        name: str,
        description: Union[str, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        host_tags: Union[List[str], UnsetType] = unset,
        priority: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Create a new Cloud Workload Security Agent policy

        :param description: The description of the policy
        :type description: str, optional

        :param enabled: Whether the policy is enabled
        :type enabled: bool, optional

        :param host_tags: The host tags defining where this policy is deployed
        :type host_tags: [str], optional

        :param name: The name of the policy
        :type name: str

        :param priority: The priority of the policy
        :type priority: int, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if host_tags is not unset:
            kwargs["host_tags"] = host_tags
        if priority is not unset:
            kwargs["priority"] = priority
        super().__init__(kwargs)

        self_.name = name
