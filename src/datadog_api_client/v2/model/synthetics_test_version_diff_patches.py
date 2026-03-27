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
    from datadog_api_client.v2.model.synthetics_test_version_diff_patch_diff import SyntheticsTestVersionDiffPatchDiff


class SyntheticsTestVersionDiffPatches(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_version_diff_patch_diff import (
            SyntheticsTestVersionDiffPatchDiff,
        )

        return {
            "diffs": ([SyntheticsTestVersionDiffPatchDiff],),
            "length1": (int,),
            "length2": (int,),
            "start1": (int,),
            "start2": (int,),
        }

    attribute_map = {
        "diffs": "diffs",
        "length1": "length1",
        "length2": "length2",
        "start1": "start1",
        "start2": "start2",
    }

    def __init__(
        self_,
        diffs: Union[List[SyntheticsTestVersionDiffPatchDiff], UnsetType] = unset,
        length1: Union[int, UnsetType] = unset,
        length2: Union[int, UnsetType] = unset,
        start1: Union[int, UnsetType] = unset,
        start2: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing a patch in the diff.

        :param diffs: List of individual diff operations.
        :type diffs: [SyntheticsTestVersionDiffPatchDiff], optional

        :param length1: Length of the original text segment.
        :type length1: int, optional

        :param length2: Length of the modified text segment.
        :type length2: int, optional

        :param start1: Start position in the original text.
        :type start1: int, optional

        :param start2: Start position in the modified text.
        :type start2: int, optional
        """
        if diffs is not unset:
            kwargs["diffs"] = diffs
        if length1 is not unset:
            kwargs["length1"] = length1
        if length2 is not unset:
            kwargs["length2"] = length2
        if start1 is not unset:
            kwargs["start1"] = start1
        if start2 is not unset:
            kwargs["start2"] = start2
        super().__init__(kwargs)
