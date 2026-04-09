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


class TestOptimizationFlakyTestsManagementPoliciesAttemptToFix(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "retries": (int,),
        }

    attribute_map = {
        "retries": "retries",
    }

    def __init__(self_, retries: Union[int, UnsetType] = unset, **kwargs):
        """
        Configuration for the attempt-to-fix Flaky Tests Management policy.

        :param retries: Number of retries when attempting to fix a flaky test. Must be greater than 0.
        :type retries: int, optional
        """
        if retries is not unset:
            kwargs["retries"] = retries
        super().__init__(kwargs)
