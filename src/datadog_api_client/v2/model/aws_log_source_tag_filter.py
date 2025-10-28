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


class AWSLogSourceTagFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "source": (str,),
            "tags": ([str], none_type),
        }

    attribute_map = {
        "source": "source",
        "tags": "tags",
    }

    def __init__(
        self_, source: Union[str, UnsetType] = unset, tags: Union[List[str], none_type, UnsetType] = unset, **kwargs
    ):
        """
        AWS log source tag filter list. Defaults to ``[]``.
        Array of log source to AWS resource tag mappings. Each mapping contains a log source and its
        associated AWS resource tags (in ``key:value`` format) used to filter logs submitted to Datadog.
        Tag filters are applied for tags on the AWS resource emitting logs; tags associated with the
        log storage entity (such as a CloudWatch Log Group or S3 Bucket) are not considered.
        For more information on resource tag filter syntax,
        `see AWS resource exclusion <https://docs.datadoghq.com/account_management/billing/aws/#aws-resource-exclusion>`_
        in the AWS integration billing page.

        :param source: The AWS log source to which the tag filters defined in ``tags`` are applied.
        :type source: str, optional

        :param tags: The AWS resource tags to filter on for the log source specified by ``source``.
        :type tags: [str], none_type, optional
        """
        if source is not unset:
            kwargs["source"] = source
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
