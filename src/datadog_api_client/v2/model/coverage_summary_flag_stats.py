# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class CoverageSummaryFlagStats(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "patch_coverage": (float, none_type),
            "total_coverage": (float, none_type),
        }

    attribute_map = {
        "patch_coverage": "patch_coverage",
        "total_coverage": "total_coverage",
    }

    def __init__(
        self_,
        patch_coverage: Union[float, none_type, UnsetType] = unset,
        total_coverage: Union[float, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Coverage statistics for a specific flag.

        :param patch_coverage: Patch coverage percentage for the flag.
        :type patch_coverage: float, none_type, optional

        :param total_coverage: Total coverage percentage for the flag.
        :type total_coverage: float, none_type, optional
        """
        if patch_coverage is not unset:
            kwargs["patch_coverage"] = patch_coverage
        if total_coverage is not unset:
            kwargs["total_coverage"] = total_coverage
        super().__init__(kwargs)
