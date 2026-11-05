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
    from datadog_api_client.v2.model.clickup_api_key_update_api_token import ClickupAPIKeyUpdateApiToken
    from datadog_api_client.v2.model.clickup_api_key_type import ClickupAPIKeyType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class ClickupAPIKeyUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.clickup_api_key_update_api_token import ClickupAPIKeyUpdateApiToken
        from datadog_api_client.v2.model.clickup_api_key_type import ClickupAPIKeyType

        return {
            "api_token": (ClickupAPIKeyUpdateApiToken,),
            "type": (ClickupAPIKeyType,),
        }

    attribute_map = {
        "api_token": "api_token",
        "type": "type",
    }

    def __init__(
        self_,
        type: ClickupAPIKeyType,
        api_token: Union[
            ClickupAPIKeyUpdateApiToken, str, ActionConnectionAWSSecretsManagerReference, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        The definition of the ``ClickupAPIKey`` object.

        :param api_token: The ``ClickupAPIKeyUpdate`` ``api_token``.
        :type api_token: ClickupAPIKeyUpdateApiToken, optional

        :param type: The definition of the ``ClickupAPIKey`` object.
        :type type: ClickupAPIKeyType
        """
        if api_token is not unset:
            kwargs["api_token"] = api_token
        super().__init__(kwargs)

        self_.type = type
