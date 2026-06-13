# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_patterns_activity_progress import LLMObsPatternsActivityProgress


class LLMObsPatternsRunStatusResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_activity_progress import LLMObsPatternsActivityProgress

        return {
            "created_at": (datetime,),
            "progress": ([LLMObsPatternsActivityProgress],),
            "status": (str,),
            "step": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "progress": "progress",
        "status": "status",
        "step": "step",
    }

    def __init__(
        self_, created_at: datetime, progress: List[LLMObsPatternsActivityProgress], status: str, step: str, **kwargs
    ):
        """
        Attributes of an LLM Observability patterns run status.

        :param created_at: Timestamp when the run was created.
        :type created_at: datetime

        :param progress: List of step-by-step progress entries for a patterns run.
        :type progress: [LLMObsPatternsActivityProgress]

        :param status: Overall status of the run.
        :type status: str

        :param step: The current step of the run.
        :type step: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.progress = progress
        self_.status = status
        self_.step = step
