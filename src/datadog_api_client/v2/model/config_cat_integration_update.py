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
    from datadog_api_client.v2.model.config_cat_credentials_update import ConfigCatCredentialsUpdate
    from datadog_api_client.v2.model.config_cat_integration_type import ConfigCatIntegrationType
    from datadog_api_client.v2.model.config_cat_sdk_key_update import ConfigCatSDKKeyUpdate


class ConfigCatIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.config_cat_credentials_update import ConfigCatCredentialsUpdate
        from datadog_api_client.v2.model.config_cat_integration_type import ConfigCatIntegrationType

        return {
            "credentials": (ConfigCatCredentialsUpdate,),
            "type": (ConfigCatIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: ConfigCatIntegrationType,
        credentials: Union[ConfigCatCredentialsUpdate, ConfigCatSDKKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``ConfigCatIntegrationUpdate`` object.

        :param credentials: The definition of the ``ConfigCatCredentialsUpdate`` object.
        :type credentials: ConfigCatCredentialsUpdate, optional

        :param type: The definition of the ``ConfigCatIntegrationType`` object.
        :type type: ConfigCatIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
