# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_bucket_keys import SyntheticsTestResultBucketKeys


class SyntheticsTestResultTurnStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_bucket_keys import SyntheticsTestResultBucketKeys

        return {
            "bucket_keys": (SyntheticsTestResultBucketKeys,),
            "config": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
        }

    attribute_map = {
        "bucket_keys": "bucket_keys",
        "config": "config",
    }

    def __init__(
        self_,
        bucket_keys: Union[SyntheticsTestResultBucketKeys, UnsetType] = unset,
        config: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        A step executed during a goal-based browser test turn.

        :param bucket_keys: Storage bucket keys for artifacts produced during a step or test.
        :type bucket_keys: SyntheticsTestResultBucketKeys, optional

        :param config: Browser step configuration for this turn step.
        :type config: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if bucket_keys is not unset:
            kwargs["bucket_keys"] = bucket_keys
        if config is not unset:
            kwargs["config"] = config
        super().__init__(kwargs)
