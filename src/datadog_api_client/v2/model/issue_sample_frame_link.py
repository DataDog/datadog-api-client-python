# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue_sample_git_file_location import IssueSampleGitFileLocation


class IssueSampleFrameLink(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_sample_git_file_location import IssueSampleGitFileLocation

        return {
            "code_location": (IssueSampleGitFileLocation,),
            "frame_id": (int,),
        }

    attribute_map = {
        "code_location": "code_location",
        "frame_id": "frame_id",
    }

    def __init__(self_, code_location: IssueSampleGitFileLocation, frame_id: int, **kwargs):
        """
        Source code location of a stack frame.

        :param code_location: Location of a stack frame in a repository file. Empty when the source code is unavailable.
        :type code_location: IssueSampleGitFileLocation

        :param frame_id: Index of the frame in the stack trace, starting at 0.
        :type frame_id: int
        """
        super().__init__(kwargs)

        self_.code_location = code_location
        self_.frame_id = frame_id
