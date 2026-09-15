# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IntegrationAccountPrivateActionRunnerAuthType(ModelSimple):
    """
    The authentication method type.

    :param value: If omitted defaults to "private-action-runner". Must be one of ["private-action-runner"].
    :type value: str
    """

    allowed_values = {
        "private-action-runner",
    }
    PRIVATE_ACTION_RUNNER: ClassVar["IntegrationAccountPrivateActionRunnerAuthType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IntegrationAccountPrivateActionRunnerAuthType.PRIVATE_ACTION_RUNNER = IntegrationAccountPrivateActionRunnerAuthType(
    "private-action-runner"
)
