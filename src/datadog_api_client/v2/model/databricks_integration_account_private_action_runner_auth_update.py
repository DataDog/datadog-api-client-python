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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.databricks_integration_account_private_action_runner_auth_type import (
        DatabricksIntegrationAccountPrivateActionRunnerAuthType,
    )


class DatabricksIntegrationAccountPrivateActionRunnerAuthUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_private_action_runner_auth_type import (
            DatabricksIntegrationAccountPrivateActionRunnerAuthType,
        )

        return {
            "auth_type": (DatabricksIntegrationAccountPrivateActionRunnerAuthType,),
            "connection_id": (UUID,),
            "secret_path": (str, none_type),
            "user_uuid": (UUID,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "connection_id": "connection_id",
        "secret_path": "secret_path",
        "user_uuid": "user_uuid",
    }

    def __init__(
        self_,
        auth_type: DatabricksIntegrationAccountPrivateActionRunnerAuthType,
        connection_id: Union[UUID, UnsetType] = unset,
        secret_path: Union[str, none_type, UnsetType] = unset,
        user_uuid: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Private Action Runner authentication. The runner holds the Databricks credentials, so this method carries no secrets. Only the fields provided are changed.

        :param auth_type: The authentication method type.
        :type auth_type: DatabricksIntegrationAccountPrivateActionRunnerAuthType

        :param connection_id: Unique identifier of the Private Action Runner connection holding the credentials.
        :type connection_id: UUID, optional

        :param secret_path: Path of the credential inside the secret backend configured on the runner. Omit it to keep the stored path, send ``null`` or an empty string to remove it, or send a value to replace it.
        :type secret_path: str, none_type, optional

        :param user_uuid: Unique identifier of the user the Private Action Runner connection belongs to.
        :type user_uuid: UUID, optional
        """
        if connection_id is not unset:
            kwargs["connection_id"] = connection_id
        if secret_path is not unset:
            kwargs["secret_path"] = secret_path
        if user_uuid is not unset:
            kwargs["user_uuid"] = user_uuid
        super().__init__(kwargs)

        self_.auth_type = auth_type
