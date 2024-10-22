# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class AWSNamespaceTagFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "namespace": (str,),
            "tags": ([str], none_type),
        }

    attribute_map = {
        "namespace": "namespace",
        "tags": "tags",
    }

    def __init__(
        self_, namespace: Union[str, UnsetType] = unset, tags: Union[List[str], none_type, UnsetType] = unset, **kwargs
    ):
        """
        AWS Metrics tag filters

        :param namespace: The AWS Namespace to apply the tag filters against
        :type namespace: str, optional

        :param tags: The tags to filter based on
        :type tags: [str], none_type, optional
        """
        if namespace is not unset:
            kwargs["namespace"] = namespace
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
