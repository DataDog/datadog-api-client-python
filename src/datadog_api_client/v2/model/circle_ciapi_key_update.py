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
    from datadog_api_client.v2.model.circle_ciapi_key_update_api_token import CircleCIAPIKeyUpdateApiToken
    from datadog_api_client.v2.model.circle_ciapi_key_type import CircleCIAPIKeyType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class CircleCIAPIKeyUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.circle_ciapi_key_update_api_token import CircleCIAPIKeyUpdateApiToken
        from datadog_api_client.v2.model.circle_ciapi_key_type import CircleCIAPIKeyType

        return {
            "api_token": (CircleCIAPIKeyUpdateApiToken,),
            "type": (CircleCIAPIKeyType,),
        }

    attribute_map = {
        "api_token": "api_token",
        "type": "type",
    }

    def __init__(
        self_,
        type: CircleCIAPIKeyType,
        api_token: Union[
            CircleCIAPIKeyUpdateApiToken, str, ActionConnectionAWSSecretsManagerReference, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        The definition of the ``CircleCIAPIKey`` object.

        :param api_token: The ``CircleCIAPIKeyUpdate`` ``api_token``.
        :type api_token: CircleCIAPIKeyUpdateApiToken, optional

        :param type: The definition of the ``CircleCIAPIKey`` object.
        :type type: CircleCIAPIKeyType
        """
        if api_token is not unset:
            kwargs["api_token"] = api_token
        super().__init__(kwargs)

        self_.type = type
