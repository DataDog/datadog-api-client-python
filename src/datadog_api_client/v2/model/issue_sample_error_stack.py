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
    from datadog_api_client.v2.model.issue_sample_stack_frame import IssueSampleStackFrame


class IssueSampleErrorStack(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_sample_stack_frame import IssueSampleStackFrame

        return {
            "frames": ([IssueSampleStackFrame],),
            "language": (str,),
        }

    attribute_map = {
        "frames": "frames",
        "language": "language",
    }

    def __init__(
        self_,
        frames: Union[List[IssueSampleStackFrame], UnsetType] = unset,
        language: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Parsed stack trace of the error. Only the sample picked by the ``git_metadata`` bias has frames.

        :param frames: Stack frames, from the top of the stack.
        :type frames: [IssueSampleStackFrame], optional

        :param language: Language the stack trace was parsed as.
        :type language: str, optional
        """
        if frames is not unset:
            kwargs["frames"] = frames
        if language is not unset:
            kwargs["language"] = language
        super().__init__(kwargs)
