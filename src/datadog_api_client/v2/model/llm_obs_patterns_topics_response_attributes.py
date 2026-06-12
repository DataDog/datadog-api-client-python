# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_patterns_config_snapshot import LLMObsPatternsConfigSnapshot
    from datadog_api_client.v2.model.llm_obs_patterns_topic import LLMObsPatternsTopic


class LLMObsPatternsTopicsResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_config_snapshot import LLMObsPatternsConfigSnapshot
        from datadog_api_client.v2.model.llm_obs_patterns_topic import LLMObsPatternsTopic

        return {
            "completed_at": (datetime, none_type),
            "config_id": (str,),
            "config_snapshot": (LLMObsPatternsConfigSnapshot,),
            "created_at": (datetime,),
            "previous_run_id": (str,),
            "run_id": (str,),
            "topics": ([LLMObsPatternsTopic],),
        }

    attribute_map = {
        "completed_at": "completed_at",
        "config_id": "config_id",
        "config_snapshot": "config_snapshot",
        "created_at": "created_at",
        "previous_run_id": "previous_run_id",
        "run_id": "run_id",
        "topics": "topics",
    }

    def __init__(
        self_,
        config_id: str,
        created_at: datetime,
        previous_run_id: str,
        run_id: str,
        topics: List[LLMObsPatternsTopic],
        completed_at: Union[datetime, none_type, UnsetType] = unset,
        config_snapshot: Union[LLMObsPatternsConfigSnapshot, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an LLM Observability patterns topics response.

        :param completed_at: Timestamp when the run completed. Null if the run has not completed.
        :type completed_at: datetime, none_type, optional

        :param config_id: Identifier of the configuration that produced the run.
        :type config_id: str

        :param config_snapshot: Snapshot of the configuration used for a patterns run.
        :type config_snapshot: LLMObsPatternsConfigSnapshot, optional

        :param created_at: Timestamp when the run was created.
        :type created_at: datetime

        :param previous_run_id: Identifier of the run that completed immediately before this one. Empty if none.
        :type previous_run_id: str

        :param run_id: Identifier of the run that produced the topics.
        :type run_id: str

        :param topics: List of discovered topics.
        :type topics: [LLMObsPatternsTopic]
        """
        if completed_at is not unset:
            kwargs["completed_at"] = completed_at
        if config_snapshot is not unset:
            kwargs["config_snapshot"] = config_snapshot
        super().__init__(kwargs)

        self_.config_id = config_id
        self_.created_at = created_at
        self_.previous_run_id = previous_run_id
        self_.run_id = run_id
        self_.topics = topics
