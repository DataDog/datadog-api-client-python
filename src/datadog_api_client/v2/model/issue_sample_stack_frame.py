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
    from datadog_api_client.v2.model.issue_sample_code_snippet import IssueSampleCodeSnippet
    from datadog_api_client.v2.model.issue_sample_git_file_location import IssueSampleGitFileLocation


class IssueSampleStackFrame(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_sample_code_snippet import IssueSampleCodeSnippet
        from datadog_api_client.v2.model.issue_sample_git_file_location import IssueSampleGitFileLocation

        return {
            "code_snippet": (IssueSampleCodeSnippet,),
            "git_file_location": (IssueSampleGitFileLocation,),
            "text": (str,),
        }

    attribute_map = {
        "code_snippet": "code_snippet",
        "git_file_location": "git_file_location",
        "text": "text",
    }

    def __init__(
        self_,
        code_snippet: Union[IssueSampleCodeSnippet, UnsetType] = unset,
        git_file_location: Union[IssueSampleGitFileLocation, UnsetType] = unset,
        text: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A stack frame.

        :param code_snippet: Source code around a stack frame. Empty when the source code is unavailable.
        :type code_snippet: IssueSampleCodeSnippet, optional

        :param git_file_location: Location of a stack frame in a repository file. Empty when the source code is unavailable.
        :type git_file_location: IssueSampleGitFileLocation, optional

        :param text: Text of the frame, as it appears in the stack trace.
        :type text: str, optional
        """
        if code_snippet is not unset:
            kwargs["code_snippet"] = code_snippet
        if git_file_location is not unset:
            kwargs["git_file_location"] = git_file_location
        if text is not unset:
            kwargs["text"] = text
        super().__init__(kwargs)
