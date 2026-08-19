# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.execution_policy_integration import ExecutionPolicyIntegration


class ExecutionPolicyActionPattern(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_policy_integration import ExecutionPolicyIntegration

        return {
            "action_fqns": ([str],),
            "integration": (ExecutionPolicyIntegration,),
        }

    attribute_map = {
        "action_fqns": "action_fqns",
        "integration": "integration",
    }

    def __init__(self_, action_fqns: List[str], integration: ExecutionPolicyIntegration, **kwargs):
        """
        The set of actions this policy applies to.

        :param action_fqns: The fully qualified action names this policy matches. Use ``*`` to match all actions
            of the integration, or a fully qualified name prefixed with the integration's action
            namespace (for example ``com.datadoghq.script.*`` for the Script integration).
        :type action_fqns: [str]

        :param integration: The integration the action pattern applies to.
        :type integration: ExecutionPolicyIntegration
        """
        super().__init__(kwargs)

        self_.action_fqns = action_fqns
        self_.integration = integration
