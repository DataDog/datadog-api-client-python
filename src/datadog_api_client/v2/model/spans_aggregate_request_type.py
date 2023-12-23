# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SpansAggregateRequestType(StringEnum):
    """
    The type of resource. The value should always be aggregate_request.

    :param value: If omitted defaults to "aggregate_request". Must be one of ["aggregate_request"].
    :type value: str
    """

    allowed_values = {
        "aggregate_request",
    }
    AGGREGATE_REQUEST: ClassVar["SpansAggregateRequestType"]


SpansAggregateRequestType.AGGREGATE_REQUEST = SpansAggregateRequestType("aggregate_request")
