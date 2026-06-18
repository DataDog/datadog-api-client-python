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
    from datadog_api_client.v2.model.rum_sdk_config_match_option_serialized_type import (
        RumSdkConfigMatchOptionSerializedType,
    )


class RumSdkConfigMatchOption(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_sdk_config_match_option_serialized_type import (
            RumSdkConfigMatchOptionSerializedType,
        )

        return {
            "rc_serialized_type": (RumSdkConfigMatchOptionSerializedType,),
            "value": (str,),
        }

    attribute_map = {
        "rc_serialized_type": "rc_serialized_type",
        "value": "value",
    }

    def __init__(self_, rc_serialized_type: RumSdkConfigMatchOptionSerializedType, value: str, **kwargs):
        """
        A match option used for URL or origin pattern matching.

        :param rc_serialized_type: The type of match pattern, either a literal string or a regex.
        :type rc_serialized_type: RumSdkConfigMatchOptionSerializedType

        :param value: The value to match against.
        :type value: str
        """
        super().__init__(kwargs)

        self_.rc_serialized_type = rc_serialized_type
        self_.value = value
