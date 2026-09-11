# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DatabricksIntegrationAccountPatAuthType(ModelSimple):
    """
    The authentication method type.

    :param value: If omitted defaults to "pat". Must be one of ["pat"].
    :type value: str
    """

    allowed_values = {
        "pat",
    }
    PAT: ClassVar["DatabricksIntegrationAccountPatAuthType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DatabricksIntegrationAccountPatAuthType.PAT = DatabricksIntegrationAccountPatAuthType("pat")
