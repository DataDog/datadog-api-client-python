# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class UsageQuotaUpdateAttributes(ModelNormal):
    validations = {
        "usage_limit": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "enforced": (bool, none_type),
            "usage_limit": (int, none_type),
        }

    attribute_map = {
        "enforced": "enforced",
        "usage_limit": "usage_limit",
    }

    def __init__(
        self_,
        enforced: Union[bool, none_type, UnsetType] = unset,
        usage_limit: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes to update on a usage quota. Omitting a property leaves its current value unchanged.

        :param enforced: Whether to actively block usage above the limit. Omit this field to leave the current enforcement setting unchanged.
        :type enforced: bool, none_type, optional

        :param usage_limit: The new quota limit in the usage units defined by the quota namespace. For an organization-wide quota (empty scope), the limit must be greater than the usage already recorded in the current period. Omit this field to leave the current limit unchanged.
        :type usage_limit: int, none_type, optional
        """
        if enforced is not unset:
            kwargs["enforced"] = enforced
        if usage_limit is not unset:
            kwargs["usage_limit"] = usage_limit
        super().__init__(kwargs)
