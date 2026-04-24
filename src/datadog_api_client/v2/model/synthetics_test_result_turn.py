# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_bucket_keys import SyntheticsTestResultBucketKeys
    from datadog_api_client.v2.model.synthetics_test_result_turn_step import SyntheticsTestResultTurnStep


class SyntheticsTestResultTurn(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_bucket_keys import SyntheticsTestResultBucketKeys
        from datadog_api_client.v2.model.synthetics_test_result_turn_step import SyntheticsTestResultTurnStep

        return {
            "bucket_keys": (SyntheticsTestResultBucketKeys,),
            "name": (str,),
            "reasoning": (str,),
            "status": (str,),
            "steps": ([SyntheticsTestResultTurnStep],),
            "turn_finished_at": (int,),
            "turn_started_at": (int,),
        }

    attribute_map = {
        "bucket_keys": "bucket_keys",
        "name": "name",
        "reasoning": "reasoning",
        "status": "status",
        "steps": "steps",
        "turn_finished_at": "turn_finished_at",
        "turn_started_at": "turn_started_at",
    }

    def __init__(
        self_,
        bucket_keys: Union[SyntheticsTestResultBucketKeys, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        reasoning: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        steps: Union[List[SyntheticsTestResultTurnStep], UnsetType] = unset,
        turn_finished_at: Union[int, UnsetType] = unset,
        turn_started_at: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A turn in a goal-based browser test, grouping steps and reasoning.

        :param bucket_keys: Storage bucket keys for artifacts produced during a step or test.
        :type bucket_keys: SyntheticsTestResultBucketKeys, optional

        :param name: Name of the turn.
        :type name: str, optional

        :param reasoning: Agent reasoning produced for this turn.
        :type reasoning: str, optional

        :param status: Status of the turn (for example, ``passed`` , ``failed`` ).
        :type status: str, optional

        :param steps: Steps executed during the turn.
        :type steps: [SyntheticsTestResultTurnStep], optional

        :param turn_finished_at: Unix timestamp (ms) of when the turn finished.
        :type turn_finished_at: int, optional

        :param turn_started_at: Unix timestamp (ms) of when the turn started.
        :type turn_started_at: int, optional
        """
        if bucket_keys is not unset:
            kwargs["bucket_keys"] = bucket_keys
        if name is not unset:
            kwargs["name"] = name
        if reasoning is not unset:
            kwargs["reasoning"] = reasoning
        if status is not unset:
            kwargs["status"] = status
        if steps is not unset:
            kwargs["steps"] = steps
        if turn_finished_at is not unset:
            kwargs["turn_finished_at"] = turn_finished_at
        if turn_started_at is not unset:
            kwargs["turn_started_at"] = turn_started_at
        super().__init__(kwargs)
