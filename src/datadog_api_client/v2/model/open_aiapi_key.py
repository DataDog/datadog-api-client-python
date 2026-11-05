# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.open_aiapi_key_api_token import OpenAIAPIKeyApiToken
    from datadog_api_client.v2.model.open_aiapi_key_type import OpenAIAPIKeyType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class OpenAIAPIKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_aiapi_key_api_token import OpenAIAPIKeyApiToken
        from datadog_api_client.v2.model.open_aiapi_key_type import OpenAIAPIKeyType

        return {
            "api_token": (OpenAIAPIKeyApiToken,),
            "type": (OpenAIAPIKeyType,),
        }

    attribute_map = {
        "api_token": "api_token",
        "type": "type",
    }

    def __init__(
        self_,
        api_token: Union[OpenAIAPIKeyApiToken, str, ActionConnectionAWSSecretsManagerReference],
        type: OpenAIAPIKeyType,
        **kwargs,
    ):
        """
        The definition of the ``OpenAIAPIKey`` object.

        :param api_token: The ``OpenAIAPIKey`` ``api_token``.
        :type api_token: OpenAIAPIKeyApiToken

        :param type: The definition of the ``OpenAIAPIKey`` object.
        :type type: OpenAIAPIKeyType
        """
        super().__init__(kwargs)

        self_.api_token = api_token
        self_.type = type
