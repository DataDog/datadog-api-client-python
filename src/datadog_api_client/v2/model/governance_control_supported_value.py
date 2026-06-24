# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GovernanceControlSupportedValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "label": (str,),
            "value": (str,),
        }

    attribute_map = {
        "label": "label",
        "value": "value",
    }

    def __init__(self_, label: str, value: str, **kwargs):
        """
        A supported value for an enumerated parameter.

        :param label: The human-readable label for the value.
        :type label: str

        :param value: The machine-readable value.
        :type value: str
        """
        super().__init__(kwargs)

        self_.label = label
        self_.value = value
