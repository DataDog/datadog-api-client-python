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
    from datadog_api_client.v2.model.config_cat_credentials import ConfigCatCredentials
    from datadog_api_client.v2.model.config_cat_integration_type import ConfigCatIntegrationType
    from datadog_api_client.v2.model.config_cat_sdk_key import ConfigCatSDKKey


class ConfigCatIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.config_cat_credentials import ConfigCatCredentials
        from datadog_api_client.v2.model.config_cat_integration_type import ConfigCatIntegrationType

        return {
            "credentials": (ConfigCatCredentials,),
            "type": (ConfigCatIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_, credentials: Union[ConfigCatCredentials, ConfigCatSDKKey], type: ConfigCatIntegrationType, **kwargs
    ):
        """
        The definition of the ``ConfigCatIntegration`` object.

        :param credentials: The definition of the ``ConfigCatCredentials`` object.
        :type credentials: ConfigCatCredentials

        :param type: The definition of the ``ConfigCatIntegrationType`` object.
        :type type: ConfigCatIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
