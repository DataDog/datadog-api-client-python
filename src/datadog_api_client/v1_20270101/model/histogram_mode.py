# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HistogramMode(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["distribution_metric", "pre_binned_metric"].
    :type value: str
    """

    allowed_values = {
        "distribution_metric",
        "pre_binned_metric",
    }
    DISTRIBUTION_METRIC: ClassVar["HistogramMode"]
    PRE_BINNED_METRIC: ClassVar["HistogramMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HistogramMode.DISTRIBUTION_METRIC = HistogramMode("distribution_metric")
HistogramMode.PRE_BINNED_METRIC = HistogramMode("pre_binned_metric")
