# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class ApplicationSecurityWafCustomRuleMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "added_at": (datetime,),
            "added_by": (str,),
            "added_by_name": (str,),
            "modified_at": (datetime,),
            "modified_by": (str,),
            "modified_by_name": (str,),
        }

    attribute_map = {
        "added_at": "added_at",
        "added_by": "added_by",
        "added_by_name": "added_by_name",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "modified_by_name": "modified_by_name",
    }

    def __init__(
        self_,
        added_at: Union[datetime, UnsetType] = unset,
        added_by: Union[str, UnsetType] = unset,
        added_by_name: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        modified_by: Union[str, UnsetType] = unset,
        modified_by_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata associated with the WAF Custom Rule.

        :param added_at: The date and time the WAF custom rule was created.
        :type added_at: datetime, optional

        :param added_by: The handle of the user who created the WAF custom rule.
        :type added_by: str, optional

        :param added_by_name: The name of the user who created the WAF custom rule.
        :type added_by_name: str, optional

        :param modified_at: The date and time the WAF custom rule was last updated.
        :type modified_at: datetime, optional

        :param modified_by: The handle of the user who last updated the WAF custom rule.
        :type modified_by: str, optional

        :param modified_by_name: The name of the user who last updated the WAF custom rule.
        :type modified_by_name: str, optional
        """
        if added_at is not unset:
            kwargs["added_at"] = added_at
        if added_by is not unset:
            kwargs["added_by"] = added_by
        if added_by_name is not unset:
            kwargs["added_by_name"] = added_by_name
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if modified_by is not unset:
            kwargs["modified_by"] = modified_by
        if modified_by_name is not unset:
            kwargs["modified_by_name"] = modified_by_name
        super().__init__(kwargs)
