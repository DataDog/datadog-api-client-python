# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorConfigPolicyDowntimePolicyCreateRequest(ModelNormal):
    validations = {
        "max_duration_ms": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "max_duration_ms": (int,),
        }

    attribute_map = {
        "max_duration_ms": "max_duration_ms",
    }

    def __init__(self_, max_duration_ms: int, **kwargs):
        """
        Downtime duration attributes of a monitor configuration policy.

        :param max_duration_ms: The maximum allowed downtime duration, in milliseconds.
        :type max_duration_ms: int
        """
        super().__init__(kwargs)

        self_.max_duration_ms = max_duration_ms
