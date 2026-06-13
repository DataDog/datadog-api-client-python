# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

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


class LLMObsPatternsRunSummary(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_config_snapshot import LLMObsPatternsConfigSnapshot

        return {
            "completed_at": (datetime, none_type),
            "config_snapshot": (LLMObsPatternsConfigSnapshot,),
            "created_at": (datetime,),
            "id": (str,),
            "status": (str,),
        }

    attribute_map = {
        "completed_at": "completed_at",
        "config_snapshot": "config_snapshot",
        "created_at": "created_at",
        "id": "id",
        "status": "status",
    }

    def __init__(
        self_,
        created_at: datetime,
        id: str,
        status: str,
        completed_at: Union[datetime, none_type, UnsetType] = unset,
        config_snapshot: Union[LLMObsPatternsConfigSnapshot, UnsetType] = unset,
        **kwargs,
    ):
        """
        Summary of an LLM Observability patterns run.

        :param completed_at: Timestamp when the run completed. Null if the run has not completed.
        :type completed_at: datetime, none_type, optional

        :param config_snapshot: Snapshot of the configuration used for a patterns run.
        :type config_snapshot: LLMObsPatternsConfigSnapshot, optional

        :param created_at: Timestamp when the run was created.
        :type created_at: datetime

        :param id: Unique identifier of the run.
        :type id: str

        :param status: Status of the run.
        :type status: str
        """
        if completed_at is not unset:
            kwargs["completed_at"] = completed_at
        if config_snapshot is not unset:
            kwargs["config_snapshot"] = config_snapshot
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.id = id
        self_.status = status
