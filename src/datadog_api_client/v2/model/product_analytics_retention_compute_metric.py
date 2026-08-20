# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsRetentionComputeMetric(ModelSimple):
    """
    The retention metric to compute, either an absolute count or a rate.

    :param value: Must be one of ["__dd.retention", "__dd.retention_rate"].
    :type value: str
    """

    allowed_values = {
        "__dd.retention",
        "__dd.retention_rate",
    }
    RETENTION: ClassVar["ProductAnalyticsRetentionComputeMetric"]
    RETENTION_RATE: ClassVar["ProductAnalyticsRetentionComputeMetric"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsRetentionComputeMetric.RETENTION = ProductAnalyticsRetentionComputeMetric("__dd.retention")
ProductAnalyticsRetentionComputeMetric.RETENTION_RATE = ProductAnalyticsRetentionComputeMetric("__dd.retention_rate")
