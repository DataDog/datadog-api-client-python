# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ReplayAnalysisLLMDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "intent": (str,),
            "user_pattern": ([str],),
        }

    attribute_map = {
        "intent": "intent",
        "user_pattern": "user_pattern",
    }

    def __init__(self_, intent: str, user_pattern: List[str], **kwargs):
        """
        AI-generated analysis details for a replay issue.

        :param intent: Interpreted user intent derived from session analysis.
        :type intent: str

        :param user_pattern: List of user behavior steps observed in the session.
        :type user_pattern: [str]
        """
        super().__init__(kwargs)

        self_.intent = intent
        self_.user_pattern = user_pattern
