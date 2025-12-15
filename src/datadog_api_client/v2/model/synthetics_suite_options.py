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


class SyntheticsSuiteOptions(ModelNormal):
    validations = {
        "alerting_threshold": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "alerting_threshold": (float,),
        }

    attribute_map = {
        "alerting_threshold": "alerting_threshold",
    }

    def __init__(self_, alerting_threshold: Union[float, UnsetType] = unset, **kwargs):
        """
        Object describing the extra options for a Synthetic suite.

        :param alerting_threshold: Percentage of critical tests failure needed for a suite to fail.
        :type alerting_threshold: float, optional
        """
        if alerting_threshold is not unset:
            kwargs["alerting_threshold"] = alerting_threshold
        super().__init__(kwargs)
