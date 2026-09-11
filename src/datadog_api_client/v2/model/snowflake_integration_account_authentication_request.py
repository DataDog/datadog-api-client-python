# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.snowflake_integration_account_private_key_auth_type import (
        SnowflakeIntegrationAccountPrivateKeyAuthType,
    )


class SnowflakeIntegrationAccountAuthenticationRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_integration_account_private_key_auth_type import (
            SnowflakeIntegrationAccountPrivateKeyAuthType,
        )

        return {
            "auth_type": (SnowflakeIntegrationAccountPrivateKeyAuthType,),
            "private_key": (str,),
            "private_key_name": (str,),
            "private_key_passphrase": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "private_key": "private_key",
        "private_key_name": "private_key_name",
        "private_key_passphrase": "private_key_passphrase",
    }

    def __init__(
        self_,
        auth_type: SnowflakeIntegrationAccountPrivateKeyAuthType,
        private_key: str,
        private_key_name: str,
        private_key_passphrase: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        RSA key pair authentication, the only method Snowflake integration accounts support. Generate an RSA key pair and assign the public key to the Snowflake user named in ``settings.username``. Because an update replaces this object as a whole, every required field must be sent again on each update, even when only one of them is changing.

        :param auth_type: The authentication method type.
        :type auth_type: SnowflakeIntegrationAccountPrivateKeyAuthType

        :param private_key: The private key, in PEM format.
        :type private_key: str

        :param private_key_name: Name that distinguishes this private key from other keys in Datadog.
        :type private_key_name: str

        :param private_key_passphrase: Passphrase that decrypts the private key. Provide it only when the key is encrypted.
        :type private_key_passphrase: str, optional
        """
        if private_key_passphrase is not unset:
            kwargs["private_key_passphrase"] = private_key_passphrase
        super().__init__(kwargs)

        self_.auth_type = auth_type
        self_.private_key = private_key
        self_.private_key_name = private_key_name
