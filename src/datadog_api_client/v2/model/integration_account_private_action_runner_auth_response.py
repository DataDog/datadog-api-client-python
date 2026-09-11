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
    from datadog_api_client.v2.model.integration_account_private_action_runner_auth_type import (
        IntegrationAccountPrivateActionRunnerAuthType,
    )


class IntegrationAccountPrivateActionRunnerAuthResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_account_private_action_runner_auth_type import (
            IntegrationAccountPrivateActionRunnerAuthType,
        )

        return {
            "auth_type": (IntegrationAccountPrivateActionRunnerAuthType,),
            "connection_id": (str,),
            "secret_path": (str,),
            "user_uuid": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "connection_id": "connection_id",
        "secret_path": "secret_path",
        "user_uuid": "user_uuid",
    }

    def __init__(
        self_,
        auth_type: IntegrationAccountPrivateActionRunnerAuthType,
        connection_id: str,
        user_uuid: str,
        secret_path: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The Private Action Runner authentication method configured on the account.

        :param auth_type: The authentication method type.
        :type auth_type: IntegrationAccountPrivateActionRunnerAuthType

        :param connection_id: Unique identifier of the Private Action Runner connection holding the credentials.
        :type connection_id: str

        :param secret_path: Path of the credential inside the secret backend configured on the runner.
        :type secret_path: str, optional

        :param user_uuid: Unique identifier of the user the Private Action Runner connection belongs to.
        :type user_uuid: str
        """
        if secret_path is not unset:
            kwargs["secret_path"] = secret_path
        super().__init__(kwargs)

        self_.auth_type = auth_type
        self_.connection_id = connection_id
        self_.user_uuid = user_uuid
