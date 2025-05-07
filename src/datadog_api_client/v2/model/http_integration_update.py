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
    from datadog_api_client.v2.model.http_credentials_update import HTTPCredentialsUpdate
    from datadog_api_client.v2.model.http_integration_type import HTTPIntegrationType
    from datadog_api_client.v2.model.http_token_auth_update import HTTPTokenAuthUpdate


class HTTPIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_credentials_update import HTTPCredentialsUpdate
        from datadog_api_client.v2.model.http_integration_type import HTTPIntegrationType

        return {
            "base_url": (str,),
            "credentials": (HTTPCredentialsUpdate,),
            "type": (HTTPIntegrationType,),
        }

    attribute_map = {
        "base_url": "base_url",
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: HTTPIntegrationType,
        base_url: Union[str, UnsetType] = unset,
        credentials: Union[HTTPCredentialsUpdate, HTTPTokenAuthUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``HTTPIntegrationUpdate`` object.

        :param base_url: Base HTTP url for the integration
        :type base_url: str, optional

        :param credentials: The definition of ``HTTPCredentialsUpdate`` object.
        :type credentials: HTTPCredentialsUpdate, optional

        :param type: The definition of ``HTTPIntegrationType`` object.
        :type type: HTTPIntegrationType
        """
        if base_url is not unset:
            kwargs["base_url"] = base_url
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
