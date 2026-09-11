# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.snowflake_integration_account_private_key_auth_type import (
        SnowflakeIntegrationAccountPrivateKeyAuthType,
    )


class SnowflakeIntegrationAccountAuthenticationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_integration_account_private_key_auth_type import (
            SnowflakeIntegrationAccountPrivateKeyAuthType,
        )

        return {
            "auth_type": (SnowflakeIntegrationAccountPrivateKeyAuthType,),
            "private_key_name": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "private_key_name": "private_key_name",
    }

    def __init__(self_, auth_type: SnowflakeIntegrationAccountPrivateKeyAuthType, private_key_name: str, **kwargs):
        """
        Authentication configured on the Snowflake integration account.

        :param auth_type: The authentication method type.
        :type auth_type: SnowflakeIntegrationAccountPrivateKeyAuthType

        :param private_key_name: Name that distinguishes this private key from other keys in Datadog.
        :type private_key_name: str
        """
        super().__init__(kwargs)

        self_.auth_type = auth_type
        self_.private_key_name = private_key_name
