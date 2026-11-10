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
    from datadog_api_client.v2.model.nebius_cloud_integration_account_service_account_auth_type import (
        NebiusCloudIntegrationAccountServiceAccountAuthType,
    )


class NebiusCloudIntegrationAccountServiceAccountAuthResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_integration_account_service_account_auth_type import (
            NebiusCloudIntegrationAccountServiceAccountAuthType,
        )

        return {
            "auth_type": (NebiusCloudIntegrationAccountServiceAccountAuthType,),
            "public_key_id": (str,),
            "service_account_id": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "public_key_id": "public_key_id",
        "service_account_id": "service_account_id",
    }

    def __init__(
        self_,
        auth_type: NebiusCloudIntegrationAccountServiceAccountAuthType,
        service_account_id: str,
        public_key_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The service-account key pair authentication method configured on the account.

        :param auth_type: The authentication method type.
        :type auth_type: NebiusCloudIntegrationAccountServiceAccountAuthType

        :param public_key_id: ID of the public key half of the authorized key pair. Omitted when unset.
        :type public_key_id: str, optional

        :param service_account_id: ID of the Nebius service account the account authenticates as.
        :type service_account_id: str
        """
        if public_key_id is not unset:
            kwargs["public_key_id"] = public_key_id
        super().__init__(kwargs)

        self_.auth_type = auth_type
        self_.service_account_id = service_account_id
