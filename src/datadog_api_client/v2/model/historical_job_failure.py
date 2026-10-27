# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.historical_job_failure_reason import HistoricalJobFailureReason


class HistoricalJobFailure(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.historical_job_failure_reason import HistoricalJobFailureReason

        return {
            "hint": (str,),
            "reason": (HistoricalJobFailureReason,),
        }

    attribute_map = {
        "hint": "hint",
        "reason": "reason",
    }

    def __init__(
        self_,
        hint: Union[str, UnsetType] = unset,
        reason: Union[HistoricalJobFailureReason, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details about why the job failed. Only present when the job has failed and won't be retried.

        :param hint: A suggestion to fix the failure.
        :type hint: str, optional

        :param reason: The reason why the job failed.
        :type reason: HistoricalJobFailureReason, optional
        """
        if hint is not unset:
            kwargs["hint"] = hint
        if reason is not unset:
            kwargs["reason"] = reason
        super().__init__(kwargs)
