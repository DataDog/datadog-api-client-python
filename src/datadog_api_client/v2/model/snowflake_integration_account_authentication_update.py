# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SnowflakeIntegrationAccountAuthenticationUpdate(ModelComposed):
    def __init__(self, **kwargs):
        """
        Authentication for updating the Snowflake integration account. Exactly one method is set.

        :param auth_type: The authentication method type.
        :type auth_type: SnowflakeIntegrationAccountPrivateKeyAuthType

        :param private_key: The private key, in PEM format.
        :type private_key: str, optional

        :param private_key_name: Name that distinguishes this private key from other keys in Datadog.
        :type private_key_name: str, optional

        :param private_key_passphrase: Passphrase that decrypts the private key. Provide it only when the key is encrypted. Omit it to keep the stored passphrase, send `null` or an empty string to remove it, or send a value to replace it.
        :type private_key_passphrase: str, none_type, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.snowflake_integration_account_private_key_auth_update import (
            SnowflakeIntegrationAccountPrivateKeyAuthUpdate,
        )

        return {
            "oneOf": [
                SnowflakeIntegrationAccountPrivateKeyAuthUpdate,
            ],
        }
