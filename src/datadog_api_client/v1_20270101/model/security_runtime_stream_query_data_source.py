# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityRuntimeStreamQueryDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "security_runtime_stream". Must be one of ["security_runtime_stream"].
    :type value: str
    """

    allowed_values = {
        "security_runtime_stream",
    }
    SECURITY_RUNTIME_STREAM: ClassVar["SecurityRuntimeStreamQueryDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityRuntimeStreamQueryDataSource.SECURITY_RUNTIME_STREAM = SecurityRuntimeStreamQueryDataSource(
    "security_runtime_stream"
)
