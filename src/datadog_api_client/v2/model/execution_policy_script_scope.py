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
    from datadog_api_client.v2.model.execution_policy_script_scope_rule import ExecutionPolicyScriptScopeRule


class ExecutionPolicyScriptScope(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_policy_script_scope_rule import ExecutionPolicyScriptScopeRule

        return {
            "rules": ([ExecutionPolicyScriptScopeRule],),
        }

    attribute_map = {
        "rules": "rules",
    }

    def __init__(self_, rules: List[ExecutionPolicyScriptScopeRule], **kwargs):
        """
        Restricts the policy to specific scripts.

        :param rules: The script scope rules.
        :type rules: [ExecutionPolicyScriptScopeRule]
        """
        super().__init__(kwargs)

        self_.rules = rules
