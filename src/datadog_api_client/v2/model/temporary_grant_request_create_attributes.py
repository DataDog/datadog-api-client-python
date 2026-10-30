# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class TemporaryGrantRequestCreateAttributes(ModelNormal):
    validations = {
        "justification": {
            "max_length": 4096,
            "min_length": 1,
        },
        "total": {
            "inclusive_maximum": 9223372036854,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "expires_at": (datetime, none_type),
            "justification": (str,),
            "total": (int,),
        }

    attribute_map = {
        "expires_at": "expires_at",
        "justification": "justification",
        "total": "total",
    }

    def __init__(
        self_, justification: str, total: int, expires_at: Union[datetime, none_type, UnsetType] = unset, **kwargs
    ):
        """
        Immutable terms and justification for a temporary grant request.

        :param expires_at: Exclusive expiry. Must be a future timestamp with a timezone. Date-only values are rejected. If omitted or null, defaults to the next UTC month boundary. Approval accepts this deadline unchanged.
        :type expires_at: datetime, none_type, optional

        :param justification: Reason for requesting temporary credits. Trimmed and limited to 4096 UTF-8 bytes.
        :type justification: str

        :param total: Target monthly AI credit limit in positive whole credits, not additional credits. Fractional credits are not accepted.
        :type total: int
        """
        if expires_at is not unset:
            kwargs["expires_at"] = expires_at
        super().__init__(kwargs)

        self_.justification = justification
        self_.total = total
