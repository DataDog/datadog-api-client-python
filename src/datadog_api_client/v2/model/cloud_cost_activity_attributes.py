# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CloudCostActivityAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "is_enabled": (bool,),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
    }

    def __init__(self_, is_enabled: bool, **kwargs):
        """
        Attributes for Cloud Cost activity.

        :param is_enabled: Whether or not the cloud account is enabled.
        :type is_enabled: bool
        """
        super().__init__(kwargs)

        self_.is_enabled = is_enabled
