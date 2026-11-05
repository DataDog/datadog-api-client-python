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
    from datadog_api_client.v2.model.config_cat_sdk_key_api_password import ConfigCatSDKKeyApiPassword
    from datadog_api_client.v2.model.config_cat_sdk_key_api_username import ConfigCatSDKKeyApiUsername
    from datadog_api_client.v2.model.config_cat_sdk_key_sdk_key import ConfigCatSDKKeySdkKey
    from datadog_api_client.v2.model.config_cat_sdk_key_type import ConfigCatSDKKeyType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class ConfigCatSDKKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.config_cat_sdk_key_api_password import ConfigCatSDKKeyApiPassword
        from datadog_api_client.v2.model.config_cat_sdk_key_api_username import ConfigCatSDKKeyApiUsername
        from datadog_api_client.v2.model.config_cat_sdk_key_sdk_key import ConfigCatSDKKeySdkKey
        from datadog_api_client.v2.model.config_cat_sdk_key_type import ConfigCatSDKKeyType

        return {
            "api_password": (ConfigCatSDKKeyApiPassword,),
            "api_username": (ConfigCatSDKKeyApiUsername,),
            "sdk_key": (ConfigCatSDKKeySdkKey,),
            "type": (ConfigCatSDKKeyType,),
        }

    attribute_map = {
        "api_password": "api_password",
        "api_username": "api_username",
        "sdk_key": "sdk_key",
        "type": "type",
    }

    def __init__(
        self_,
        api_password: Union[ConfigCatSDKKeyApiPassword, str, ActionConnectionAWSSecretsManagerReference],
        api_username: Union[ConfigCatSDKKeyApiUsername, str, ActionConnectionAWSSecretsManagerReference],
        sdk_key: Union[ConfigCatSDKKeySdkKey, str, ActionConnectionAWSSecretsManagerReference],
        type: ConfigCatSDKKeyType,
        **kwargs,
    ):
        """
        The definition of the ``ConfigCatSDKKey`` object.

        :param api_password: The ``ConfigCatSDKKey`` ``api_password``.
        :type api_password: ConfigCatSDKKeyApiPassword

        :param api_username: The ``ConfigCatSDKKey`` ``api_username``.
        :type api_username: ConfigCatSDKKeyApiUsername

        :param sdk_key: The ``ConfigCatSDKKey`` ``sdk_key``.
        :type sdk_key: ConfigCatSDKKeySdkKey

        :param type: The definition of the ``ConfigCatSDKKey`` object.
        :type type: ConfigCatSDKKeyType
        """
        super().__init__(kwargs)

        self_.api_password = api_password
        self_.api_username = api_username
        self_.sdk_key = sdk_key
        self_.type = type
