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
    from datadog_api_client.v2.model.agent_trigger import AgentTrigger


class AgentTriggerWrapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.agent_trigger import AgentTrigger

        return {
            "agent_trigger": (AgentTrigger,),
            "start_step_names": ([str],),
        }

    attribute_map = {
        "agent_trigger": "agentTrigger",
        "start_step_names": "startStepNames",
    }

    def __init__(self_, agent_trigger: AgentTrigger, start_step_names: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Schema for an agent-based trigger.

        :param agent_trigger: Trigger a workflow from an agent via the MCP execute tool. Workflow can be executed from Bits Chat, Bits Agent Builder, Claude Code, Codex, Cursor, and any other coding agent using the Datadog MCP.
        :type agent_trigger: AgentTrigger

        :param start_step_names: Names of existing workflow steps that run first after a trigger fires.
        :type start_step_names: [str], optional
        """
        if start_step_names is not unset:
            kwargs["start_step_names"] = start_step_names
        super().__init__(kwargs)

        self_.agent_trigger = agent_trigger
