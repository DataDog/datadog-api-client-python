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
    from datadog_api_client.v2.model.execution_step_status import ExecutionStepStatus


class ExecutionStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.execution_step_status import ExecutionStepStatus

        return {
            "completed_at": (datetime, none_type),
            "error": (str,),
            "id": (str,),
            "name": (str,),
            "started_at": (datetime, none_type),
            "status": (ExecutionStepStatus,),
        }

    attribute_map = {
        "completed_at": "completed_at",
        "error": "error",
        "id": "id",
        "name": "name",
        "started_at": "started_at",
        "status": "status",
    }

    def __init__(
        self_,
        id: str,
        name: str,
        status: ExecutionStepStatus,
        completed_at: Union[datetime, none_type, UnsetType] = unset,
        error: Union[str, UnsetType] = unset,
        started_at: Union[datetime, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single step in a workflow execution.

        :param completed_at: Timestamp when the step completed. Null if not yet completed.
        :type completed_at: datetime, none_type, optional

        :param error: Error message if the step failed.
        :type error: str, optional

        :param id: The unique identifier of the execution step.
        :type id: str

        :param name: The name of the step.
        :type name: str

        :param started_at: Timestamp when the step started. Null if not yet started.
        :type started_at: datetime, none_type, optional

        :param status: The current status of the step.
        :type status: ExecutionStepStatus
        """
        if completed_at is not unset:
            kwargs["completed_at"] = completed_at
        if error is not unset:
            kwargs["error"] = error
        if started_at is not unset:
            kwargs["started_at"] = started_at
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
        self_.status = status
