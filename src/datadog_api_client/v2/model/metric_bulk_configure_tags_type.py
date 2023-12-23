# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class MetricBulkConfigureTagsType(StringEnum):
    """
    The metric bulk configure tags resource.

    :param value: If omitted defaults to "metric_bulk_configure_tags". Must be one of ["metric_bulk_configure_tags"].
    :type value: str
    """

    allowed_values = {
        "metric_bulk_configure_tags",
    }
    BULK_MANAGE_TAGS: ClassVar["MetricBulkConfigureTagsType"]


MetricBulkConfigureTagsType.BULK_MANAGE_TAGS = MetricBulkConfigureTagsType("metric_bulk_configure_tags")
