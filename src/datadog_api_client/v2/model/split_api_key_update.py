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
    from datadog_api_client.v2.model.split_api_key_update_api_key import SplitAPIKeyUpdateApiKey
    from datadog_api_client.v2.model.split_api_key_type import SplitAPIKeyType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class SplitAPIKeyUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.split_api_key_update_api_key import SplitAPIKeyUpdateApiKey
        from datadog_api_client.v2.model.split_api_key_type import SplitAPIKeyType

        return {
            "api_key": (SplitAPIKeyUpdateApiKey,),
            "type": (SplitAPIKeyType,),
        }

    attribute_map = {
        "api_key": "api_key",
        "type": "type",
    }

    def __init__(
        self_,
        type: SplitAPIKeyType,
        api_key: Union[SplitAPIKeyUpdateApiKey, str, ActionConnectionAWSSecretsManagerReference, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``SplitAPIKey`` object.

        :param api_key: The ``SplitAPIKeyUpdate`` ``api_key``.
        :type api_key: SplitAPIKeyUpdateApiKey, optional

        :param type: The definition of the ``SplitAPIKey`` object.
        :type type: SplitAPIKeyType
        """
        if api_key is not unset:
            kwargs["api_key"] = api_key
        super().__init__(kwargs)

        self_.type = type
