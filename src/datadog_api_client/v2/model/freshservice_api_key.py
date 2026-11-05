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
    from datadog_api_client.v2.model.freshservice_api_key_api_key import FreshserviceAPIKeyApiKey
    from datadog_api_client.v2.model.freshservice_api_key_domain import FreshserviceAPIKeyDomain
    from datadog_api_client.v2.model.freshservice_api_key_type import FreshserviceAPIKeyType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class FreshserviceAPIKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.freshservice_api_key_api_key import FreshserviceAPIKeyApiKey
        from datadog_api_client.v2.model.freshservice_api_key_domain import FreshserviceAPIKeyDomain
        from datadog_api_client.v2.model.freshservice_api_key_type import FreshserviceAPIKeyType

        return {
            "api_key": (FreshserviceAPIKeyApiKey,),
            "domain": (FreshserviceAPIKeyDomain,),
            "type": (FreshserviceAPIKeyType,),
        }

    attribute_map = {
        "api_key": "api_key",
        "domain": "domain",
        "type": "type",
    }

    def __init__(
        self_,
        api_key: Union[FreshserviceAPIKeyApiKey, str, ActionConnectionAWSSecretsManagerReference],
        domain: Union[FreshserviceAPIKeyDomain, str, ActionConnectionAWSSecretsManagerReference],
        type: FreshserviceAPIKeyType,
        **kwargs,
    ):
        """
        The definition of the ``FreshserviceAPIKey`` object.

        :param api_key: The ``FreshserviceAPIKey`` ``api_key``.
        :type api_key: FreshserviceAPIKeyApiKey

        :param domain: The ``FreshserviceAPIKey`` ``domain``.
        :type domain: FreshserviceAPIKeyDomain

        :param type: The definition of the ``FreshserviceAPIKey`` object.
        :type type: FreshserviceAPIKeyType
        """
        super().__init__(kwargs)

        self_.api_key = api_key
        self_.domain = domain
        self_.type = type
