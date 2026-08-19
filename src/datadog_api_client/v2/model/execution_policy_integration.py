# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExecutionPolicyIntegration(ModelSimple):
    """
    The integration the action pattern applies to.

    :param value: Must be one of ["INTEGRATION_KUBERNETES", "INTEGRATION_SCRIPT", "INTEGRATION_REMOTE_ACTION"].
    :type value: str
    """

    allowed_values = {
        "INTEGRATION_KUBERNETES",
        "INTEGRATION_SCRIPT",
        "INTEGRATION_REMOTE_ACTION",
    }
    INTEGRATION_KUBERNETES: ClassVar["ExecutionPolicyIntegration"]
    INTEGRATION_SCRIPT: ClassVar["ExecutionPolicyIntegration"]
    INTEGRATION_REMOTE_ACTION: ClassVar["ExecutionPolicyIntegration"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExecutionPolicyIntegration.INTEGRATION_KUBERNETES = ExecutionPolicyIntegration("INTEGRATION_KUBERNETES")
ExecutionPolicyIntegration.INTEGRATION_SCRIPT = ExecutionPolicyIntegration("INTEGRATION_SCRIPT")
ExecutionPolicyIntegration.INTEGRATION_REMOTE_ACTION = ExecutionPolicyIntegration("INTEGRATION_REMOTE_ACTION")
