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
    from datadog_api_client.v2.model.rum_sdk_config_serialized_regex_type import RumSdkConfigSerializedRegexType


class RumSdkConfigSerializedRegex(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_sdk_config_serialized_regex_type import RumSdkConfigSerializedRegexType

        return {
            "rc_serialized_type": (RumSdkConfigSerializedRegexType,),
            "value": (str,),
        }

    attribute_map = {
        "rc_serialized_type": "rc_serialized_type",
        "value": "value",
    }

    def __init__(self_, rc_serialized_type: RumSdkConfigSerializedRegexType, value: str, **kwargs):
        """
        A serialized regex used as an extractor in dynamic options.

        :param rc_serialized_type: The type identifier for a serialized regex. Always ``regex``.
        :type rc_serialized_type: RumSdkConfigSerializedRegexType

        :param value: The regex pattern used for extraction.
        :type value: str
        """
        super().__init__(kwargs)

        self_.rc_serialized_type = rc_serialized_type
        self_.value = value
