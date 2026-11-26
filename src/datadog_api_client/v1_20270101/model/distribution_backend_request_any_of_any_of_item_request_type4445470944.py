# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DistributionBackendRequestAnyOfAnyOfItemRequestType4445470944(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "histogram". Must be one of ["histogram"].
    :type value: str
    """

    allowed_values = {
        "histogram",
    }
    HISTOGRAM: ClassVar["DistributionBackendRequestAnyOfAnyOfItemRequestType4445470944"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DistributionBackendRequestAnyOfAnyOfItemRequestType4445470944.HISTOGRAM = (
    DistributionBackendRequestAnyOfAnyOfItemRequestType4445470944("histogram")
)
