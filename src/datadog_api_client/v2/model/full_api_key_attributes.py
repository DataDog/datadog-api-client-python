# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.full_api_key_last_used_date import FullAPIKeyLastUsedDate


class FullAPIKeyAttributes(ModelNormal):
    validations = {
        "last4": {
            "max_length": 4,
            "min_length": 4,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.full_api_key_last_used_date import FullAPIKeyLastUsedDate

        return {
            "category": (str,),
            "created_at": (str,),
            "date_last_used": (str, none_type),
            "key": (str,),
            "last4": (str,),
            "last_used_date": (FullAPIKeyLastUsedDate,),
            "modified_at": (str,),
            "name": (str,),
            "remote_config_read_enabled": (bool,),
            "used_in_last_24_hours": (bool,),
        }

    attribute_map = {
        "category": "category",
        "created_at": "created_at",
        "date_last_used": "date_last_used",
        "key": "key",
        "last4": "last4",
        "last_used_date": "last_used_date",
        "modified_at": "modified_at",
        "name": "name",
        "remote_config_read_enabled": "remote_config_read_enabled",
        "used_in_last_24_hours": "used_in_last_24_hours",
    }
    read_only_vars = {
        "created_at",
        "key",
        "last4",
        "modified_at",
    }

    def __init__(
        self_,
        category: Union[str, UnsetType] = unset,
        created_at: Union[str, UnsetType] = unset,
        date_last_used: Union[str, none_type, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        last4: Union[str, UnsetType] = unset,
        last_used_date: Union[FullAPIKeyLastUsedDate, UnsetType] = unset,
        modified_at: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        remote_config_read_enabled: Union[bool, UnsetType] = unset,
        used_in_last_24_hours: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a full API key.

        :param category: The category of the API key.
        :type category: str, optional

        :param created_at: Creation date of the API key.
        :type created_at: str, optional

        :param date_last_used: The date and time the API key was last used.
        :type date_last_used: str, none_type, optional

        :param key: The API key.
        :type key: str, optional

        :param last4: The last four characters of the API key.
        :type last4: str, optional

        :param last_used_date: Attributes for the last time the specific API key was used.
        :type last_used_date: FullAPIKeyLastUsedDate, optional

        :param modified_at: Date the API key was last modified.
        :type modified_at: str, optional

        :param name: Name of the API key.
        :type name: str, optional

        :param remote_config_read_enabled: The remote config read enabled status.
        :type remote_config_read_enabled: bool, optional

        :param used_in_last_24_hours: If the API key was used within the last 24 hours.
        :type used_in_last_24_hours: bool, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if date_last_used is not unset:
            kwargs["date_last_used"] = date_last_used
        if key is not unset:
            kwargs["key"] = key
        if last4 is not unset:
            kwargs["last4"] = last4
        if last_used_date is not unset:
            kwargs["last_used_date"] = last_used_date
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if name is not unset:
            kwargs["name"] = name
        if remote_config_read_enabled is not unset:
            kwargs["remote_config_read_enabled"] = remote_config_read_enabled
        if used_in_last_24_hours is not unset:
            kwargs["used_in_last_24_hours"] = used_in_last_24_hours
        super().__init__(kwargs)
