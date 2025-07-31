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
    from datadog_api_client.v2.model.gemini_credentials import GeminiCredentials
    from datadog_api_client.v2.model.gemini_integration_type import GeminiIntegrationType
    from datadog_api_client.v2.model.gemini_api_key import GeminiAPIKey


class GeminiIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gemini_credentials import GeminiCredentials
        from datadog_api_client.v2.model.gemini_integration_type import GeminiIntegrationType

        return {
            "credentials": (GeminiCredentials,),
            "type": (GeminiIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(self_, credentials: Union[GeminiCredentials, GeminiAPIKey], type: GeminiIntegrationType, **kwargs):
        """
        The definition of the ``GeminiIntegration`` object.

        :param credentials: The definition of the ``GeminiCredentials`` object.
        :type credentials: GeminiCredentials

        :param type: The definition of the ``GeminiIntegrationType`` object.
        :type type: GeminiIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
