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
    from datadog_api_client.v2.model.open_ai_credentials_update import OpenAICredentialsUpdate
    from datadog_api_client.v2.model.open_ai_integration_type import OpenAIIntegrationType
    from datadog_api_client.v2.model.open_aiapi_key_update import OpenAIAPIKeyUpdate


class OpenAIIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_credentials_update import OpenAICredentialsUpdate
        from datadog_api_client.v2.model.open_ai_integration_type import OpenAIIntegrationType

        return {
            "credentials": (OpenAICredentialsUpdate,),
            "type": (OpenAIIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: OpenAIIntegrationType,
        credentials: Union[OpenAICredentialsUpdate, OpenAIAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``OpenAIIntegrationUpdate`` object.

        :param credentials: The definition of the ``OpenAICredentialsUpdate`` object.
        :type credentials: OpenAICredentialsUpdate, optional

        :param type: The definition of the ``OpenAIIntegrationType`` object.
        :type type: OpenAIIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
