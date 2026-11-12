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
    from datadog_api_client.v2.model.agent_health_remediation_script import AgentHealthRemediationScript
    from datadog_api_client.v2.model.agent_health_remediation_step import AgentHealthRemediationStep


class AgentHealthRemediation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.agent_health_remediation_script import AgentHealthRemediationScript
        from datadog_api_client.v2.model.agent_health_remediation_step import AgentHealthRemediationStep

        return {
            "script": (AgentHealthRemediationScript,),
            "steps": ([AgentHealthRemediationStep],),
            "summary": (str,),
        }

    attribute_map = {
        "script": "script",
        "steps": "steps",
        "summary": "summary",
    }

    def __init__(
        self_,
        script: Union[AgentHealthRemediationScript, UnsetType] = unset,
        steps: Union[List[AgentHealthRemediationStep], UnsetType] = unset,
        summary: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Remediation for the issue. Omitted when no remediation is available.

        :param script: A script that can be used to remediate the issue.
        :type script: AgentHealthRemediationScript, optional

        :param steps: Steps to remediate the issue.
        :type steps: [AgentHealthRemediationStep], optional

        :param summary: A summary of how to remediate the issue.
        :type summary: str, optional
        """
        if script is not unset:
            kwargs["script"] = script
        if steps is not unset:
            kwargs["steps"] = steps
        if summary is not unset:
            kwargs["summary"] = summary
        super().__init__(kwargs)
