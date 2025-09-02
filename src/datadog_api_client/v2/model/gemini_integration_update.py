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
    from datadog_api_client.v2.model.gemini_credentials_update import GeminiCredentialsUpdate
    from datadog_api_client.v2.model.gemini_integration_type import GeminiIntegrationType
    from datadog_api_client.v2.model.gemini_api_key_update import GeminiAPIKeyUpdate


class GeminiIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gemini_credentials_update import GeminiCredentialsUpdate
        from datadog_api_client.v2.model.gemini_integration_type import GeminiIntegrationType

        return {
            "credentials": (GeminiCredentialsUpdate,),
            "type": (GeminiIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: GeminiIntegrationType,
        credentials: Union[GeminiCredentialsUpdate, GeminiAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``GeminiIntegrationUpdate`` object.

        :param credentials: The definition of the ``GeminiCredentialsUpdate`` object.
        :type credentials: GeminiCredentialsUpdate, optional

        :param type: The definition of the ``GeminiIntegrationType`` object.
        :type type: GeminiIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
