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
    from datadog_api_client.v2.model.gcp_service_account_update_private_key import GCPServiceAccountUpdatePrivateKey
    from datadog_api_client.v2.model.gcp_service_account_update_service_account_email import (
        GCPServiceAccountUpdateServiceAccountEmail,
    )
    from datadog_api_client.v2.model.gcp_service_account_credential_type import GCPServiceAccountCredentialType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class GCPServiceAccountUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_service_account_update_private_key import GCPServiceAccountUpdatePrivateKey
        from datadog_api_client.v2.model.gcp_service_account_update_service_account_email import (
            GCPServiceAccountUpdateServiceAccountEmail,
        )
        from datadog_api_client.v2.model.gcp_service_account_credential_type import GCPServiceAccountCredentialType

        return {
            "private_key": (GCPServiceAccountUpdatePrivateKey,),
            "service_account_email": (GCPServiceAccountUpdateServiceAccountEmail,),
            "type": (GCPServiceAccountCredentialType,),
        }

    attribute_map = {
        "private_key": "private_key",
        "service_account_email": "service_account_email",
        "type": "type",
    }

    def __init__(
        self_,
        type: GCPServiceAccountCredentialType,
        private_key: Union[
            GCPServiceAccountUpdatePrivateKey, str, ActionConnectionAWSSecretsManagerReference, UnsetType
        ] = unset,
        service_account_email: Union[
            GCPServiceAccountUpdateServiceAccountEmail, str, ActionConnectionAWSSecretsManagerReference, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        The definition of the ``GCPServiceAccount`` object.

        :param private_key: The ``GCPServiceAccountUpdate`` ``private_key``.
        :type private_key: GCPServiceAccountUpdatePrivateKey, optional

        :param service_account_email: The ``GCPServiceAccountUpdate`` ``service_account_email``.
        :type service_account_email: GCPServiceAccountUpdateServiceAccountEmail, optional

        :param type: The definition of the ``GCPServiceAccount`` object.
        :type type: GCPServiceAccountCredentialType
        """
        if private_key is not unset:
            kwargs["private_key"] = private_key
        if service_account_email is not unset:
            kwargs["service_account_email"] = service_account_email
        super().__init__(kwargs)

        self_.type = type
