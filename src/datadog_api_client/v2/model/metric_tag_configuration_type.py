# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class MetricTagConfigurationType(StringEnum):
    """
    The metric tag configuration resource type.

    :param value: If omitted defaults to "manage_tags". Must be one of ["manage_tags"].
    :type value: str
    """

    allowed_values = {
        "manage_tags",
    }
    MANAGE_TAGS: ClassVar["MetricTagConfigurationType"]


MetricTagConfigurationType.MANAGE_TAGS = MetricTagConfigurationType("manage_tags")
