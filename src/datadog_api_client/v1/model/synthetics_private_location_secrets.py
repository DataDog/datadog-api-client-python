# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsPrivateLocationSecrets(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_private_location_secrets_authentication import (
            SyntheticsPrivateLocationSecretsAuthentication,
        )
        from datadog_api_client.v1.model.synthetics_private_location_secrets_config_decryption import (
            SyntheticsPrivateLocationSecretsConfigDecryption,
        )

        return {
            "authentication": (SyntheticsPrivateLocationSecretsAuthentication,),
            "config_decryption": (SyntheticsPrivateLocationSecretsConfigDecryption,),
        }

    attribute_map = {
        "authentication": "authentication",
        "config_decryption": "config_decryption",
    }

    def __init__(self, *args, **kwargs):
        """
        Secrets for the private location. Only present in the response when creating the private location.

        :param authentication: Authentication part of the secrets.
        :type authentication: SyntheticsPrivateLocationSecretsAuthentication, optional

        :param config_decryption: Private key for the private location.
        :type config_decryption: SyntheticsPrivateLocationSecretsConfigDecryption, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsPrivateLocationSecrets, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
