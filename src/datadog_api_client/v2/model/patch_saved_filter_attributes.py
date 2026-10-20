# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.saved_filter_targeting_rule_request import SavedFilterTargetingRuleRequest


class PatchSavedFilterAttributes(ModelNormal):
    validations = {
        "name": {
            "min_length": 1,
        },
        "targeting_rules": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saved_filter_targeting_rule_request import SavedFilterTargetingRuleRequest

        return {
            "description": (str, none_type),
            "last_updated_at": (datetime, none_type),
            "name": (str, none_type),
            "targeting_rules": ([SavedFilterTargetingRuleRequest], none_type),
        }

    attribute_map = {
        "description": "description",
        "last_updated_at": "last_updated_at",
        "name": "name",
        "targeting_rules": "targeting_rules",
    }

    def __init__(
        self_,
        description: Union[str, none_type, UnsetType] = unset,
        last_updated_at: Union[datetime, none_type, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        targeting_rules: Union[List[SavedFilterTargetingRuleRequest], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Fields to update. At least one of ``name`` , ``description`` , or ``targeting_rules`` must have a non-null value. Omitted or null fields are preserved. The creation type cannot be changed.

        :param description: The new description. Send an empty string to clear the description. If omitted or null, the existing description is preserved.
        :type description: str, none_type, optional

        :param last_updated_at: The ``updated_at`` value returned by a previous read, as an RFC 3339 timestamp. If it differs from the stored update time, truncated to seconds, the request returns a 409 response. For metadata-only updates, this check does not prevent all concurrent writes. This field alone does not constitute an update.
        :type last_updated_at: datetime, none_type, optional

        :param name: The new name of the saved filter. Must not be empty.
        :type name: str, none_type, optional

        :param targeting_rules: The complete replacement targeting rules, combined with OR. Conditions within each rule are combined with AND. Replaces all existing rules. Values are not appended. Must contain at least one rule. Saved filters cannot reference other saved filters.
        :type targeting_rules: [SavedFilterTargetingRuleRequest], none_type, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if last_updated_at is not unset:
            kwargs["last_updated_at"] = last_updated_at
        if name is not unset:
            kwargs["name"] = name
        if targeting_rules is not unset:
            kwargs["targeting_rules"] = targeting_rules
        super().__init__(kwargs)
