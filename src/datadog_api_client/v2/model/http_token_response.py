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
    from datadog_api_client.v2.model.http_token_response_value import HTTPTokenResponseValue
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class HTTPTokenResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_token_response_value import HTTPTokenResponseValue

        return {
            "name": (str,),
            "value": (HTTPTokenResponseValue,),
        }

    attribute_map = {
        "name": "name",
        "value": "value",
    }

    def __init__(
        self_,
        name: str,
        value: Union[HTTPTokenResponseValue, str, ActionConnectionAWSSecretsManagerReference],
        **kwargs,
    ):
        """
        An HTTP authentication token returned by the API. Its type is implicitly ``SECRET``.

        :param name: Name of the HTTP authentication token.
        :type name: str

        :param value: The ``HTTPTokenResponse`` ``value``.
        :type value: HTTPTokenResponseValue
        """
        super().__init__(kwargs)

        self_.name = name
        self_.value = value
