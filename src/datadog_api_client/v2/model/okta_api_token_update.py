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
    from datadog_api_client.v2.model.okta_api_token_update_api_token import OktaAPITokenUpdateApiToken
    from datadog_api_client.v2.model.okta_api_token_update_domain import OktaAPITokenUpdateDomain
    from datadog_api_client.v2.model.okta_api_token_type import OktaAPITokenType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class OktaAPITokenUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.okta_api_token_update_api_token import OktaAPITokenUpdateApiToken
        from datadog_api_client.v2.model.okta_api_token_update_domain import OktaAPITokenUpdateDomain
        from datadog_api_client.v2.model.okta_api_token_type import OktaAPITokenType

        return {
            "api_token": (OktaAPITokenUpdateApiToken,),
            "domain": (OktaAPITokenUpdateDomain,),
            "type": (OktaAPITokenType,),
        }

    attribute_map = {
        "api_token": "api_token",
        "domain": "domain",
        "type": "type",
    }

    def __init__(
        self_,
        type: OktaAPITokenType,
        api_token: Union[
            OktaAPITokenUpdateApiToken, str, ActionConnectionAWSSecretsManagerReference, UnsetType
        ] = unset,
        domain: Union[OktaAPITokenUpdateDomain, str, ActionConnectionAWSSecretsManagerReference, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``OktaAPIToken`` object.

        :param api_token: The ``OktaAPITokenUpdate`` ``api_token``.
        :type api_token: OktaAPITokenUpdateApiToken, optional

        :param domain: The ``OktaAPITokenUpdate`` ``domain``.
        :type domain: OktaAPITokenUpdateDomain, optional

        :param type: The definition of the ``OktaAPIToken`` object.
        :type type: OktaAPITokenType
        """
        if api_token is not unset:
            kwargs["api_token"] = api_token
        if domain is not unset:
            kwargs["domain"] = domain
        super().__init__(kwargs)

        self_.type = type
