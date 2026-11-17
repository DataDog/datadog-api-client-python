# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class NebiusCloudIntegrationAccountAuthenticationRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Authentication for creating the Nebius Cloud integration account. Exactly one method is set.

        :param auth_type: The authentication method type.
        :type auth_type: NebiusCloudIntegrationAccountServiceAccountAuthType

        :param private_key: The private key of the authorized key pair, in PEM format. Required when log, resource, or service-quota collection is enabled; a request that enables one of them without it is rejected with a `422` response.
        :type private_key: str, optional

        :param public_key_id: ID of the public key half of the authorized key pair, such as `publickey-xxxxxxxx`. Required when log, resource, or service-quota collection is enabled; a request that enables one of them without it is rejected with a `422` response.
        :type public_key_id: str, optional

        :param service_account_id: Non-secret ID of the Nebius service account the account authenticates as.
        :type service_account_id: str

        :param static_api_key: Nebius static API key with the OBSERVABILITY scope, used to query logs. Required when log, resource, or service-quota collection is enabled; a request that enables one of them without it is rejected with a `422` response.
        :type static_api_key: str, optional
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
        from datadog_api_client.v2.model.nebius_cloud_integration_account_service_account_auth_request import (
            NebiusCloudIntegrationAccountServiceAccountAuthRequest,
        )

        return {
            "oneOf": [
                NebiusCloudIntegrationAccountServiceAccountAuthRequest,
            ],
        }
