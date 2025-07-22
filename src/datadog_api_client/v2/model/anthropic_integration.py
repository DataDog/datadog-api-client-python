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
    from datadog_api_client.v2.model.anthropic_credentials import AnthropicCredentials
    from datadog_api_client.v2.model.anthropic_integration_type import AnthropicIntegrationType
    from datadog_api_client.v2.model.anthropic_api_key import AnthropicAPIKey


class AnthropicIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.anthropic_credentials import AnthropicCredentials
        from datadog_api_client.v2.model.anthropic_integration_type import AnthropicIntegrationType

        return {
            "credentials": (AnthropicCredentials,),
            "type": (AnthropicIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_, credentials: Union[AnthropicCredentials, AnthropicAPIKey], type: AnthropicIntegrationType, **kwargs
    ):
        """
        The definition of the ``AnthropicIntegration`` object.

        :param credentials: The definition of the ``AnthropicCredentials`` object.
        :type credentials: AnthropicCredentials

        :param type: The definition of the ``AnthropicIntegrationType`` object.
        :type type: AnthropicIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
