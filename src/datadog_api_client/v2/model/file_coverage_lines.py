# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class FileCoverageLines(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "added_lines": ([int],),
            "covered_lines": ([int],),
            "executable_lines": ([int],),
        }

    attribute_map = {
        "added_lines": "added_lines",
        "covered_lines": "covered_lines",
        "executable_lines": "executable_lines",
    }

    def __init__(
        self_,
        added_lines: Union[List[int], UnsetType] = unset,
        covered_lines: Union[List[int], UnsetType] = unset,
        executable_lines: Union[List[int], UnsetType] = unset,
        **kwargs,
    ):
        """
        Per-file line coverage data including executable, covered, and added lines.

        :param added_lines: Line numbers that were added in the specified scope (for example, in a PR diff).
        :type added_lines: [int], optional

        :param covered_lines: Line numbers that were covered by tests.
        :type covered_lines: [int], optional

        :param executable_lines: Line numbers that are executable (can be covered).
        :type executable_lines: [int], optional
        """
        if added_lines is not unset:
            kwargs["added_lines"] = added_lines
        if covered_lines is not unset:
            kwargs["covered_lines"] = covered_lines
        if executable_lines is not unset:
            kwargs["executable_lines"] = executable_lines
        super().__init__(kwargs)
