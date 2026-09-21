# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.snowflake_integration_account_private_key_auth_type import (
        SnowflakeIntegrationAccountPrivateKeyAuthType,
    )


class SnowflakeIntegrationAccountPrivateKeyAuthUpdate(ModelNormal):
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
            "private_key_passphrase": (str, none_type),
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
        private_key: Union[str, UnsetType] = unset,
        private_key_name: Union[str, UnsetType] = unset,
        private_key_passphrase: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        RSA key pair authentication, the only method Snowflake integration accounts support. Only the fields provided are changed; omit ``private_key`` to keep the stored one.

        :param auth_type: The authentication method type.
        :type auth_type: SnowflakeIntegrationAccountPrivateKeyAuthType

        :param private_key: The private key, in PEM format.
        :type private_key: str, optional

        :param private_key_name: Name that distinguishes this private key from other keys in Datadog.
        :type private_key_name: str, optional

        :param private_key_passphrase: Passphrase that decrypts the private key. Provide it only when the key is encrypted. Omit it to keep the stored passphrase, send ``null`` or an empty string to remove it, or send a value to replace it.
        :type private_key_passphrase: str, none_type, optional
        """
        if private_key is not unset:
            kwargs["private_key"] = private_key
        if private_key_name is not unset:
            kwargs["private_key_name"] = private_key_name
        if private_key_passphrase is not unset:
            kwargs["private_key_passphrase"] = private_key_passphrase
        super().__init__(kwargs)

        self_.auth_type = auth_type
