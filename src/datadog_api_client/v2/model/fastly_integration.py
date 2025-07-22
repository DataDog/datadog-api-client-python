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
    from datadog_api_client.v2.model.fastly_credentials import FastlyCredentials
    from datadog_api_client.v2.model.fastly_integration_type import FastlyIntegrationType
    from datadog_api_client.v2.model.fastly_api_key import FastlyAPIKey


class FastlyIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fastly_credentials import FastlyCredentials
        from datadog_api_client.v2.model.fastly_integration_type import FastlyIntegrationType

        return {
            "credentials": (FastlyCredentials,),
            "type": (FastlyIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(self_, credentials: Union[FastlyCredentials, FastlyAPIKey], type: FastlyIntegrationType, **kwargs):
        """
        The definition of the ``FastlyIntegration`` object.

        :param credentials: The definition of the ``FastlyCredentials`` object.
        :type credentials: FastlyCredentials

        :param type: The definition of the ``FastlyIntegrationType`` object.
        :type type: FastlyIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
