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


class ObservabilityPipelineAmazonS3GenericBatchSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "batch_size": (int,),
            "timeout_secs": (int,),
        }

    attribute_map = {
        "batch_size": "batch_size",
        "timeout_secs": "timeout_secs",
    }

    def __init__(
        self_, batch_size: Union[int, UnsetType] = unset, timeout_secs: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        Event batching settings

        :param batch_size: Maximum batch size in bytes.
        :type batch_size: int, optional

        :param timeout_secs: Maximum number of seconds to wait before flushing the batch.
        :type timeout_secs: int, optional
        """
        if batch_size is not unset:
            kwargs["batch_size"] = batch_size
        if timeout_secs is not unset:
            kwargs["timeout_secs"] = timeout_secs
        super().__init__(kwargs)
