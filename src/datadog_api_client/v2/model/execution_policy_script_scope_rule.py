# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExecutionPolicyScriptScopeRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "target_script_names": ([str],),
        }

    attribute_map = {
        "target_script_names": "target_script_names",
    }

    def __init__(self_, target_script_names: List[str], **kwargs):
        """
        A rule restricting a script scope to specific script names.

        :param target_script_names: The script names this rule applies to.
        :type target_script_names: [str]
        """
        super().__init__(kwargs)

        self_.target_script_names = target_script_names
