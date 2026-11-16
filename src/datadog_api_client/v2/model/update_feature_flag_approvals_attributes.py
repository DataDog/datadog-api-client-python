# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UpdateFeatureFlagApprovalsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
        }

    attribute_map = {
        "enabled": "enabled",
    }

    def __init__(self_, enabled: bool, **kwargs):
        """
        The approval requirement for the flag.

        :param enabled: Whether approval is required. Disabling requires the Feature Flag Approvals Override permission.
        :type enabled: bool
        """
        super().__init__(kwargs)

        self_.enabled = enabled
