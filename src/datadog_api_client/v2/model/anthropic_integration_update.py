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
    from datadog_api_client.v2.model.anthropic_credentials_update import AnthropicCredentialsUpdate
    from datadog_api_client.v2.model.anthropic_integration_type import AnthropicIntegrationType
    from datadog_api_client.v2.model.anthropic_api_key_update import AnthropicAPIKeyUpdate


class AnthropicIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.anthropic_credentials_update import AnthropicCredentialsUpdate
        from datadog_api_client.v2.model.anthropic_integration_type import AnthropicIntegrationType

        return {
            "credentials": (AnthropicCredentialsUpdate,),
            "type": (AnthropicIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: AnthropicIntegrationType,
        credentials: Union[AnthropicCredentialsUpdate, AnthropicAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``AnthropicIntegrationUpdate`` object.

        :param credentials: The definition of the ``AnthropicCredentialsUpdate`` object.
        :type credentials: AnthropicCredentialsUpdate, optional

        :param type: The definition of the ``AnthropicIntegrationType`` object.
        :type type: AnthropicIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
