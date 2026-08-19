# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ExecutionPolicyTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "agent_tags": ([str],),
            "name": (str, none_type),
        }

    attribute_map = {
        "agent_tags": "agent_tags",
        "name": "name",
    }

    def __init__(self_, agent_tags: List[str], name: Union[str, none_type, UnsetType] = unset, **kwargs):
        """
        A target this policy is scoped to, expressed as a set of Agent tags.

        :param agent_tags: The Agent tags identifying the target.
        :type agent_tags: [str]

        :param name: A human-readable name for the target.
        :type name: str, none_type, optional
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.agent_tags = agent_tags
