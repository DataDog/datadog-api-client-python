# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.quota_limit_enforce_type import QuotaLimitEnforceType


class QuotaLimit(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.quota_limit_enforce_type import QuotaLimitEnforceType

        return {
            "enforce": (QuotaLimitEnforceType,),
            "limit": (int,),
        }

    attribute_map = {
        "enforce": "enforce",
        "limit": "limit",
    }

    def __init__(self_, enforce: QuotaLimitEnforceType, limit: int, **kwargs):
        """
        Unified definition of ``QuotaLimit`` object.

        :param enforce: The definition of ``QuotaLimitEnforceType`` object.
        :type enforce: QuotaLimitEnforceType

        :param limit: The limit for quota enforcement.
        :type limit: int
        """
        super().__init__(kwargs)

        self_.enforce = enforce
        self_.limit = limit
