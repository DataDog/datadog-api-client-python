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


class DeploymentGatesFDDRuleOptions(ModelNormal):
    validations = {
        "duration": {
            "inclusive_maximum": 7200,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "allowed_resources": ([str],),
            "duration": (int,),
            "excluded_resources": ([str],),
        }

    attribute_map = {
        "allowed_resources": "allowed_resources",
        "duration": "duration",
        "excluded_resources": "excluded_resources",
    }

    def __init__(
        self_,
        allowed_resources: Union[List[str], UnsetType] = unset,
        duration: Union[int, UnsetType] = unset,
        excluded_resources: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Options for a ``faulty_deployment_detection`` rule.

        :param allowed_resources: APM resource names to include in analysis. Mutually exclusive with ``excluded_resources``.
        :type allowed_resources: [str], optional

        :param duration: Evaluation window in seconds. Maximum 7200 (2 hours).
        :type duration: int, optional

        :param excluded_resources: APM resource names to exclude from analysis.
        :type excluded_resources: [str], optional
        """
        if allowed_resources is not unset:
            kwargs["allowed_resources"] = allowed_resources
        if duration is not unset:
            kwargs["duration"] = duration
        if excluded_resources is not unset:
            kwargs["excluded_resources"] = excluded_resources
        super().__init__(kwargs)
