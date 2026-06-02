# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SignalsProblemsSampleMetadata(ModelNormal):
    validations = {
        "failed": {
            "inclusive_maximum": 2147483647,
        },
        "requested": {
            "inclusive_maximum": 2147483647,
        },
        "succeeded": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "failed": (int,),
            "requested": (int,),
            "sampled_view_ids": ([str],),
            "succeeded": (int,),
            "success_rate": (float,),
        }

    attribute_map = {
        "failed": "failed",
        "requested": "requested",
        "sampled_view_ids": "sampled_view_ids",
        "succeeded": "succeeded",
        "success_rate": "success_rate",
    }

    def __init__(
        self_, failed: int, requested: int, sampled_view_ids: List[str], succeeded: int, success_rate: float, **kwargs
    ):
        """
        Metadata about the sampling quality for a signals and problems query.

        :param failed: Number of view instances that failed to process.
        :type failed: int

        :param requested: Number of view instances requested for sampling.
        :type requested: int

        :param sampled_view_ids: List of RUM view IDs that were sampled.
        :type sampled_view_ids: [str]

        :param succeeded: Number of view instances successfully processed.
        :type succeeded: int

        :param success_rate: Ratio of successfully processed views to requested views.
        :type success_rate: float
        """
        super().__init__(kwargs)

        self_.failed = failed
        self_.requested = requested
        self_.sampled_view_ids = sampled_view_ids
        self_.succeeded = succeeded
        self_.success_rate = success_rate
