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


class DeploymentRuleOptionsFaultyDeploymentDetection(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "duration": (int,),
            "excluded_resources": ([str],),
        }

    attribute_map = {
        "duration": "duration",
        "excluded_resources": "excluded_resources",
    }

    def __init__(
        self_,
        duration: Union[int, UnsetType] = unset,
        excluded_resources: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Faulty deployment detection options for deployment rules.

        :param duration: The duration for faulty deployment detection.
        :type duration: int, optional

        :param excluded_resources: Resources to exclude from faulty deployment detection.
        :type excluded_resources: [str], optional
        """
        if duration is not unset:
            kwargs["duration"] = duration
        if excluded_resources is not unset:
            kwargs["excluded_resources"] = excluded_resources
        super().__init__(kwargs)
