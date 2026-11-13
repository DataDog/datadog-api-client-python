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


class DeploymentGatesBitsDeploymentAnalysisRuleOptions(ModelNormal):
    validations = {
        "duration": {
            "inclusive_maximum": 7200,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "duration": (int,),
        }

    attribute_map = {
        "duration": "duration",
    }

    def __init__(self_, duration: Union[int, UnsetType] = unset, **kwargs):
        """
        Options for a ``bits_deployment_analysis`` rule.

        :param duration: Evaluation window in seconds. Maximum 7200 (2 hours).
        :type duration: int, optional
        """
        if duration is not unset:
            kwargs["duration"] = duration
        super().__init__(kwargs)
