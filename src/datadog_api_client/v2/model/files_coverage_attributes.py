# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.file_coverage_lines import FileCoverageLines


class FilesCoverageAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.file_coverage_lines import FileCoverageLines

        return {
            "base_commit_sha": (str,),
            "event_timestamp": (int,),
            "files": ({str: (FileCoverageLines,)},),
            "head_commit_sha": (str,),
            "report_count": (int,),
        }

    attribute_map = {
        "base_commit_sha": "base_commit_sha",
        "event_timestamp": "event_timestamp",
        "files": "files",
        "head_commit_sha": "head_commit_sha",
        "report_count": "report_count",
    }

    def __init__(
        self_,
        base_commit_sha: Union[str, UnsetType] = unset,
        event_timestamp: Union[int, UnsetType] = unset,
        files: Union[Dict[str, FileCoverageLines], UnsetType] = unset,
        head_commit_sha: Union[str, UnsetType] = unset,
        report_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the per-file code coverage response.

        :param base_commit_sha: The SHA of the base commit used for comparison (for example, the merge base for a PR).
        :type base_commit_sha: str, optional

        :param event_timestamp: Unix timestamp (milliseconds) of the coverage event.
        :type event_timestamp: int, optional

        :param files: Map of file paths to per-file coverage line data.
        :type files: {str: (FileCoverageLines,)}, optional

        :param head_commit_sha: The SHA of the head commit for which coverage was evaluated.
        :type head_commit_sha: str, optional

        :param report_count: Number of coverage reports evaluated.
        :type report_count: int, optional
        """
        if base_commit_sha is not unset:
            kwargs["base_commit_sha"] = base_commit_sha
        if event_timestamp is not unset:
            kwargs["event_timestamp"] = event_timestamp
        if files is not unset:
            kwargs["files"] = files
        if head_commit_sha is not unset:
            kwargs["head_commit_sha"] = head_commit_sha
        if report_count is not unset:
            kwargs["report_count"] = report_count
        super().__init__(kwargs)
