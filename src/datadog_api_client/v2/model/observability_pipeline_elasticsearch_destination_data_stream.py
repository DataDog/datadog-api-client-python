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


class ObservabilityPipelineElasticsearchDestinationDataStream(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "auto_routing": (bool,),
            "dataset": (str,),
            "dtype": (str,),
            "namespace": (str,),
            "sync_fields": (bool,),
        }

    attribute_map = {
        "auto_routing": "auto_routing",
        "dataset": "dataset",
        "dtype": "dtype",
        "namespace": "namespace",
        "sync_fields": "sync_fields",
    }

    def __init__(
        self_,
        auto_routing: Union[bool, UnsetType] = unset,
        dataset: Union[str, UnsetType] = unset,
        dtype: Union[str, UnsetType] = unset,
        namespace: Union[str, UnsetType] = unset,
        sync_fields: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration options for writing to Elasticsearch Data Streams instead of a fixed index.

        :param auto_routing: When ``true`` , automatically routes events to the appropriate data stream based on the event content.
        :type auto_routing: bool, optional

        :param dataset: The data stream dataset. This groups events by their source or application.
        :type dataset: str, optional

        :param dtype: The data stream type. This determines how events are categorized within the data stream.
        :type dtype: str, optional

        :param namespace: The data stream namespace. This separates events into different environments or domains.
        :type namespace: str, optional

        :param sync_fields: When ``true`` , synchronizes data stream fields with the Elasticsearch index mapping.
        :type sync_fields: bool, optional
        """
        if auto_routing is not unset:
            kwargs["auto_routing"] = auto_routing
        if dataset is not unset:
            kwargs["dataset"] = dataset
        if dtype is not unset:
            kwargs["dtype"] = dtype
        if namespace is not unset:
            kwargs["namespace"] = namespace
        if sync_fields is not unset:
            kwargs["sync_fields"] = sync_fields
        super().__init__(kwargs)
