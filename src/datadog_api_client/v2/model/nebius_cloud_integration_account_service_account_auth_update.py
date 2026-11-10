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
    from datadog_api_client.v2.model.nebius_cloud_integration_account_service_account_auth_type import (
        NebiusCloudIntegrationAccountServiceAccountAuthType,
    )


class NebiusCloudIntegrationAccountServiceAccountAuthUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_integration_account_service_account_auth_type import (
            NebiusCloudIntegrationAccountServiceAccountAuthType,
        )

        return {
            "auth_type": (NebiusCloudIntegrationAccountServiceAccountAuthType,),
            "private_key": (str,),
            "public_key_id": (str, none_type),
            "service_account_id": (str,),
            "static_api_key": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "private_key": "private_key",
        "public_key_id": "public_key_id",
        "service_account_id": "service_account_id",
        "static_api_key": "static_api_key",
    }

    def __init__(
        self_,
        auth_type: NebiusCloudIntegrationAccountServiceAccountAuthType,
        private_key: Union[str, UnsetType] = unset,
        public_key_id: Union[str, none_type, UnsetType] = unset,
        service_account_id: Union[str, UnsetType] = unset,
        static_api_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Service-account key pair authentication, the only method Nebius Cloud integration accounts support. Only the fields provided are changed; omit ``private_key`` and ``static_api_key`` to keep the stored ones.

        :param auth_type: The authentication method type.
        :type auth_type: NebiusCloudIntegrationAccountServiceAccountAuthType

        :param private_key: The private key of the authorized key pair, in PEM format. Omit it to keep the stored one; an empty string is rejected with a ``422`` response.
        :type private_key: str, optional

        :param public_key_id: ID of the public key half of the authorized key pair. Omit it to keep the stored public key ID, send ``null`` or an empty string to remove it, or send a value to replace it. Removing it is rejected with a ``422`` response while log, resource, or service-quota collection is enabled.
        :type public_key_id: str, none_type, optional

        :param service_account_id: Non-secret ID of the Nebius service account the account authenticates as. It cannot be cleared; sending ``null`` or an empty string is rejected with a ``422`` response.
        :type service_account_id: str, optional

        :param static_api_key: Nebius static API key with the OBSERVABILITY scope. Omit it to keep the stored one; an empty string is rejected with a ``422`` response.
        :type static_api_key: str, optional
        """
        if private_key is not unset:
            kwargs["private_key"] = private_key
        if public_key_id is not unset:
            kwargs["public_key_id"] = public_key_id
        if service_account_id is not unset:
            kwargs["service_account_id"] = service_account_id
        if static_api_key is not unset:
            kwargs["static_api_key"] = static_api_key
        super().__init__(kwargs)

        self_.auth_type = auth_type
