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
        AWS Metrics Collection tag filters list. Defaults to ``[]``.
        The array of custom AWS resource tags (in the form ``key:value`` ) defines a filter that Datadog uses when collecting metrics from a specified service.
        Wildcards, such as ``?`` (match a single character) and ``*`` (match multiple characters), and exclusion using ``!`` before the tag are supported.
        For EC2, only hosts that match one of the defined tags will be imported into Datadog. The rest will be ignored.
        For example, ``env:production,instance-type:c?.*,!region:us-east-1``.

        :param namespace: The AWS service for which the tag filters defined in ``tags`` will be applied.
        :type namespace: str, optional

        :param tags: The AWS resource tags to filter on for the service specified by ``namespace``.
        :type tags: [str], none_type, optional
        """
        if namespace is not unset:
            kwargs["namespace"] = namespace
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
