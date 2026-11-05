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
    from datadog_api_client.v2.model.grey_noise_api_key_api_key import GreyNoiseAPIKeyApiKey
    from datadog_api_client.v2.model.grey_noise_api_key_type import GreyNoiseAPIKeyType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class GreyNoiseAPIKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.grey_noise_api_key_api_key import GreyNoiseAPIKeyApiKey
        from datadog_api_client.v2.model.grey_noise_api_key_type import GreyNoiseAPIKeyType

        return {
            "api_key": (GreyNoiseAPIKeyApiKey,),
            "type": (GreyNoiseAPIKeyType,),
        }

    attribute_map = {
        "api_key": "api_key",
        "type": "type",
    }

    def __init__(
        self_,
        api_key: Union[GreyNoiseAPIKeyApiKey, str, ActionConnectionAWSSecretsManagerReference],
        type: GreyNoiseAPIKeyType,
        **kwargs,
    ):
        """
        The definition of the ``GreyNoiseAPIKey`` object.

        :param api_key: The ``GreyNoiseAPIKey`` ``api_key``.
        :type api_key: GreyNoiseAPIKeyApiKey

        :param type: The definition of the ``GreyNoiseAPIKey`` object.
        :type type: GreyNoiseAPIKeyType
        """
        super().__init__(kwargs)

        self_.api_key = api_key
        self_.type = type
