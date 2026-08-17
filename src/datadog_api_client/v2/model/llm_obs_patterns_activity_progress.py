# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class LLMObsPatternsActivityProgress(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "nb_completed": (int,),
            "started_at": (datetime, none_type),
            "status": (str,),
            "sub_step": (str,),
            "target": (int,),
        }

    attribute_map = {
        "name": "name",
        "nb_completed": "nb_completed",
        "started_at": "started_at",
        "status": "status",
        "sub_step": "sub_step",
        "target": "target",
    }

    def __init__(
        self_,
        name: str,
        status: str,
        nb_completed: Union[int, UnsetType] = unset,
        started_at: Union[datetime, none_type, UnsetType] = unset,
        sub_step: Union[str, UnsetType] = unset,
        target: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Progress information for a single step of a patterns run.

        :param name: Name of the step.
        :type name: str

        :param nb_completed: Number of completed work items.
        :type nb_completed: int, optional

        :param started_at: Timestamp when the step started. Null if the step has not started.
        :type started_at: datetime, none_type, optional

        :param status: Status of the step.
        :type status: str

        :param sub_step: Label of the current sub-step.
        :type sub_step: str, optional

        :param target: Total number of work items.
        :type target: int, optional
        """
        if nb_completed is not unset:
            kwargs["nb_completed"] = nb_completed
        if started_at is not unset:
            kwargs["started_at"] = started_at
        if sub_step is not unset:
            kwargs["sub_step"] = sub_step
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.name = name
        self_.status = status
