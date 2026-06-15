# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MaxSessionDurationUpdateAttributes(ModelNormal):
    validations = {
        "max_session_duration": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "max_session_duration": (int,),
        }

    attribute_map = {
        "max_session_duration": "max_session_duration",
    }

    def __init__(self_, max_session_duration: int, **kwargs):
        """
        Attributes for the maximum session duration update request.

        :param max_session_duration: The maximum session duration, in seconds.
        :type max_session_duration: int
        """
        super().__init__(kwargs)

        self_.max_session_duration = max_session_duration
