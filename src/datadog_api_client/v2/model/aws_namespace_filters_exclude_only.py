# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSNamespaceFiltersExcludeOnly(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "exclude_only": ([str],),
        }

    attribute_map = {
        "exclude_only": "exclude_only",
    }

    def __init__(self_, exclude_only: List[str], **kwargs):
        """
        Exclude only these namespaces from metrics collection. Defaults to ``["AWS/SQS", "AWS/ElasticMapReduce"]``.
        ``AWS/SQS`` and ``AWS/ElasticMapReduce`` are excluded by default to reduce your AWS CloudWatch costs from ``GetMetricData`` API calls.

        :param exclude_only: Exclude only these namespaces from metrics collection. Defaults to ``["AWS/SQS", "AWS/ElasticMapReduce"]``.
            ``AWS/SQS`` and ``AWS/ElasticMapReduce`` are excluded by default to reduce your AWS CloudWatch costs from ``GetMetricData`` API calls.
        :type exclude_only: [str]
        """
        super().__init__(kwargs)

        self_.exclude_only = exclude_only
