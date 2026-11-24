# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_sdk_config_dynamic_option import RUMSdkConfigDynamicOption


class RUMSdkConfigDynamicOptionPair(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_sdk_config_dynamic_option import RUMSdkConfigDynamicOption

        return {
            "key": (str,),
            "value": (RUMSdkConfigDynamicOption,),
        }

    attribute_map = {
        "key": "key",
        "value": "value",
    }

    def __init__(self_, key: str, value: RUMSdkConfigDynamicOption, **kwargs):
        """
        A key-value pair where the value is a dynamic configuration option.

        :param key: The key name for this dynamic configuration pair.
        :type key: str

        :param value: A dynamic configuration option that extracts a value at runtime using a specified strategy.
        :type value: RUMSdkConfigDynamicOption
        """
        super().__init__(kwargs)

        self_.key = key
        self_.value = value
