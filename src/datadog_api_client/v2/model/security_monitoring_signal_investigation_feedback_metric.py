# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SecurityMonitoringSignalInvestigationFeedbackMetric(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "placeholder": (str,),
            "prompt": (str,),
            "response": (str,),
            "type": (str,),
        }

    attribute_map = {
        "placeholder": "placeholder",
        "prompt": "prompt",
        "response": "response",
        "type": "type",
    }

    def __init__(self_, prompt: str, response: str, type: str, placeholder: Union[str, UnsetType] = unset, **kwargs):
        """
        A feedback metric containing user response.

        :param placeholder: Placeholder text for the metric.
        :type placeholder: str, optional

        :param prompt: The question or prompt.
        :type prompt: str

        :param response: The user's response.
        :type response: str

        :param type: The type of metric.
        :type type: str
        """
        if placeholder is not unset:
            kwargs["placeholder"] = placeholder
        super().__init__(kwargs)

        self_.prompt = prompt
        self_.response = response
        self_.type = type
