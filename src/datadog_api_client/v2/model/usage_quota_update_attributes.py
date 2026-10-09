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
        "pending_usage_limit": {
            "inclusive_minimum": 0,
        },
        "usage_limit": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "enforced": (bool, none_type),
            "pending_usage_limit": (int, none_type),
            "usage_limit": (int, none_type),
        }

    attribute_map = {
        "enforced": "enforced",
        "pending_usage_limit": "pending_usage_limit",
        "usage_limit": "usage_limit",
    }

    def __init__(
        self_,
        enforced: Union[bool, none_type, UnsetType] = unset,
        pending_usage_limit: Union[int, none_type, UnsetType] = unset,
        usage_limit: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes to update on a usage quota. At least one of ``usage_limit`` , ``enforced`` , or ``pending_usage_limit`` must be provided. Omitting a property leaves its current value unchanged.

        :param enforced: Whether to actively block usage above the limit. Omit this field to leave the current enforcement setting unchanged.
        :type enforced: bool, none_type, optional

        :param pending_usage_limit: The non-negative, whole-number limit to schedule for the organization-wide quota in the usage units defined by the quota namespace. It is not checked against current usage. Each write schedules the value for 00:00 UTC on the first day of the next calendar month and replaces any previously scheduled change; the server computes ``pending_effective_from``. Omit this field to leave any scheduled change unchanged, including when raising ``usage_limit`` ; use ``DELETE /api/v2/usage/quotas/{quota_namespace}/{id}/pending`` to cancel one.
        :type pending_usage_limit: int, none_type, optional

        :param usage_limit: The new quota limit in the usage units defined by the quota namespace. For an organization-wide quota (empty scope), the limit must be greater than the usage already recorded in the current period. Omit this field to leave the current limit unchanged.
        :type usage_limit: int, none_type, optional
        """
        if enforced is not unset:
            kwargs["enforced"] = enforced
        if pending_usage_limit is not unset:
            kwargs["pending_usage_limit"] = pending_usage_limit
        if usage_limit is not unset:
            kwargs["usage_limit"] = usage_limit
        super().__init__(kwargs)
