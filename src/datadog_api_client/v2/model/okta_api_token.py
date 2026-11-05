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
    from datadog_api_client.v2.model.okta_api_token_api_token import OktaAPITokenApiToken
    from datadog_api_client.v2.model.okta_api_token_domain import OktaAPITokenDomain
    from datadog_api_client.v2.model.okta_api_token_type import OktaAPITokenType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class OktaAPIToken(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.okta_api_token_api_token import OktaAPITokenApiToken
        from datadog_api_client.v2.model.okta_api_token_domain import OktaAPITokenDomain
        from datadog_api_client.v2.model.okta_api_token_type import OktaAPITokenType

        return {
            "api_token": (OktaAPITokenApiToken,),
            "domain": (OktaAPITokenDomain,),
            "type": (OktaAPITokenType,),
        }

    attribute_map = {
        "api_token": "api_token",
        "domain": "domain",
        "type": "type",
    }

    def __init__(
        self_,
        api_token: Union[OktaAPITokenApiToken, str, ActionConnectionAWSSecretsManagerReference],
        domain: Union[OktaAPITokenDomain, str, ActionConnectionAWSSecretsManagerReference],
        type: OktaAPITokenType,
        **kwargs,
    ):
        """
        The definition of the ``OktaAPIToken`` object.

        :param api_token: The ``OktaAPIToken`` ``api_token``.
        :type api_token: OktaAPITokenApiToken

        :param domain: The ``OktaAPIToken`` ``domain``.
        :type domain: OktaAPITokenDomain

        :param type: The definition of the ``OktaAPIToken`` object.
        :type type: OktaAPITokenType
        """
        super().__init__(kwargs)

        self_.api_token = api_token
        self_.domain = domain
        self_.type = type
