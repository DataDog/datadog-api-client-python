# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAddEnvVarsProcessorType(ModelSimple):
    """
    The processor type. The value should always be `add_env_vars`.

    :param value: If omitted defaults to "add_env_vars". Must be one of ["add_env_vars"].
    :type value: str
    """

    allowed_values = {
        "add_env_vars",
    }
    ADD_ENV_VARS: ClassVar["ObservabilityPipelineAddEnvVarsProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAddEnvVarsProcessorType.ADD_ENV_VARS = ObservabilityPipelineAddEnvVarsProcessorType("add_env_vars")
