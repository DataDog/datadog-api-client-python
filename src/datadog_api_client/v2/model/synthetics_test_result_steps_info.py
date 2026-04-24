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


class SyntheticsTestResultStepsInfo(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "completed": (int,),
            "errors": (int,),
            "total": (int,),
        }

    attribute_map = {
        "completed": "completed",
        "errors": "errors",
        "total": "total",
    }

    def __init__(
        self_,
        completed: Union[int, UnsetType] = unset,
        errors: Union[int, UnsetType] = unset,
        total: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Step execution summary for a Synthetic test result.

        :param completed: Number of completed steps.
        :type completed: int, optional

        :param errors: Number of steps with errors.
        :type errors: int, optional

        :param total: Total number of steps.
        :type total: int, optional
        """
        if completed is not unset:
            kwargs["completed"] = completed
        if errors is not unset:
            kwargs["errors"] = errors
        if total is not unset:
            kwargs["total"] = total
        super().__init__(kwargs)
