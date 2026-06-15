# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_patterns_run_summary import LLMObsPatternsRunSummary


class LLMObsPatternsRunsResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_run_summary import LLMObsPatternsRunSummary

        return {
            "runs": ([LLMObsPatternsRunSummary],),
        }

    attribute_map = {
        "runs": "runs",
    }

    def __init__(self_, runs: List[LLMObsPatternsRunSummary], **kwargs):
        """
        Attributes of an LLM Observability patterns runs response.

        :param runs: List of patterns runs.
        :type runs: [LLMObsPatternsRunSummary]
        """
        super().__init__(kwargs)

        self_.runs = runs
