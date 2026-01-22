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


class ObservabilityPipelineOpenSearchDestinationDataStream(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dataset": (str,),
            "dtype": (str,),
            "namespace": (str,),
        }

    attribute_map = {
        "dataset": "dataset",
        "dtype": "dtype",
        "namespace": "namespace",
    }

    def __init__(
        self_,
        dataset: Union[str, UnsetType] = unset,
        dtype: Union[str, UnsetType] = unset,
        namespace: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration options for writing to OpenSearch Data Streams instead of a fixed index.

        :param dataset: The data stream dataset for your logs. This groups logs by their source or application.
        :type dataset: str, optional

        :param dtype: The data stream type for your logs. This determines how logs are categorized within the data stream.
        :type dtype: str, optional

        :param namespace: The data stream namespace for your logs. This separates logs into different environments or domains.
        :type namespace: str, optional
        """
        if dataset is not unset:
            kwargs["dataset"] = dataset
        if dtype is not unset:
            kwargs["dtype"] = dtype
        if namespace is not unset:
            kwargs["namespace"] = namespace
        super().__init__(kwargs)
