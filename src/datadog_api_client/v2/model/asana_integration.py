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
    from datadog_api_client.v2.model.asana_credentials import AsanaCredentials
    from datadog_api_client.v2.model.asana_integration_type import AsanaIntegrationType
    from datadog_api_client.v2.model.asana_access_token import AsanaAccessToken


class AsanaIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asana_credentials import AsanaCredentials
        from datadog_api_client.v2.model.asana_integration_type import AsanaIntegrationType

        return {
            "credentials": (AsanaCredentials,),
            "type": (AsanaIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(self_, credentials: Union[AsanaCredentials, AsanaAccessToken], type: AsanaIntegrationType, **kwargs):
        """
        The definition of the ``AsanaIntegration`` object.

        :param credentials: The definition of the ``AsanaCredentials`` object.
        :type credentials: AsanaCredentials

        :param type: The definition of the ``AsanaIntegrationType`` object.
        :type type: AsanaIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
