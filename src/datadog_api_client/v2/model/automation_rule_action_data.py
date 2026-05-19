# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AutomationRuleActionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "agent_type": (str,),
            "assigned_agent_id": (str,),
            "handle": (str,),
        }

    attribute_map = {
        "agent_type": "agent_type",
        "assigned_agent_id": "assigned_agent_id",
        "handle": "handle",
    }

    def __init__(
        self_,
        agent_type: Union[str, UnsetType] = unset,
        assigned_agent_id: Union[str, UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for the action to execute, dependent on the action type.

        :param agent_type: The type of AI agent to assign. Required when the action type is ``assign_agent``.
        :type agent_type: str, optional

        :param assigned_agent_id: The identifier of the AI agent to assign to the case. Required when the action type is ``assign_agent``.
        :type assigned_agent_id: str, optional

        :param handle: The handle of the Datadog workflow to execute. Required when the action type is ``execute_workflow``.
        :type handle: str, optional
        """
        if agent_type is not unset:
            kwargs["agent_type"] = agent_type
        if assigned_agent_id is not unset:
            kwargs["assigned_agent_id"] = assigned_agent_id
        if handle is not unset:
            kwargs["handle"] = handle
        super().__init__(kwargs)
