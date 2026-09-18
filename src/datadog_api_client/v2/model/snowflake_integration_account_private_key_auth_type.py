# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SnowflakeIntegrationAccountPrivateKeyAuthType(ModelSimple):
    """
    The authentication method type.

    :param value: If omitted defaults to "snowflake_private_key". Must be one of ["snowflake_private_key"].
    :type value: str
    """

    allowed_values = {
        "snowflake_private_key",
    }
    SNOWFLAKE_PRIVATE_KEY: ClassVar["SnowflakeIntegrationAccountPrivateKeyAuthType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SnowflakeIntegrationAccountPrivateKeyAuthType.SNOWFLAKE_PRIVATE_KEY = SnowflakeIntegrationAccountPrivateKeyAuthType(
    "snowflake_private_key"
)
