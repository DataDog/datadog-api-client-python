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
    from datadog_api_client.v2.model.http_credentials import HTTPCredentials
    from datadog_api_client.v2.model.http_integration_type import HTTPIntegrationType
    from datadog_api_client.v2.model.http_token_auth import HTTPTokenAuth


class HTTPIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_credentials import HTTPCredentials
        from datadog_api_client.v2.model.http_integration_type import HTTPIntegrationType

        return {
            "base_url": (str,),
            "credentials": (HTTPCredentials,),
            "type": (HTTPIntegrationType,),
        }

    attribute_map = {
        "base_url": "base_url",
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_, base_url: str, credentials: Union[HTTPCredentials, HTTPTokenAuth], type: HTTPIntegrationType, **kwargs
    ):
        """
        The definition of ``HTTPIntegration`` object.

        :param base_url: Base HTTP url for the integration
        :type base_url: str

        :param credentials: The definition of ``HTTPCredentials`` object.
        :type credentials: HTTPCredentials

        :param type: The definition of ``HTTPIntegrationType`` object.
        :type type: HTTPIntegrationType
        """
        super().__init__(kwargs)

        self_.base_url = base_url
        self_.credentials = credentials
        self_.type = type
