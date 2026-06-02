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
    from datadog_api_client.v2.model.assignment_result import AssignmentResult


class AssigneeResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.assignment_result import AssignmentResult

        return {
            "failures": ([AssignmentResult],),
            "warnings": ([AssignmentResult],),
        }

    attribute_map = {
        "failures": "failures",
        "warnings": "warnings",
    }

    def __init__(
        self_,
        failures: Union[List[AssignmentResult], UnsetType] = unset,
        warnings: Union[List[AssignmentResult], UnsetType] = unset,
        **kwargs,
    ):
        """
        Per-finding warnings and failures produced while processing the bulk assignee request.

        :param failures: Findings that could not be assigned or unassigned.
        :type failures: [AssignmentResult], optional

        :param warnings: Findings for which the assignment succeeded but a non-critical error occurred during processing.
        :type warnings: [AssignmentResult], optional
        """
        if failures is not unset:
            kwargs["failures"] = failures
        if warnings is not unset:
            kwargs["warnings"] = warnings
        super().__init__(kwargs)
