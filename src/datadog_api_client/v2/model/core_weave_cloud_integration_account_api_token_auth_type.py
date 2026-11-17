# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CoreWeaveCloudIntegrationAccountAPITokenAuthType(ModelSimple):
    """
    The authentication method type.

    :param value: If omitted defaults to "coreweave_api_token". Must be one of ["coreweave_api_token"].
    :type value: str
    """

    allowed_values = {
        "coreweave_api_token",
    }
    COREWEAVE_API_TOKEN: ClassVar["CoreWeaveCloudIntegrationAccountAPITokenAuthType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CoreWeaveCloudIntegrationAccountAPITokenAuthType.COREWEAVE_API_TOKEN = CoreWeaveCloudIntegrationAccountAPITokenAuthType(
    "coreweave_api_token"
)
