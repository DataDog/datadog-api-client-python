# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class CostSettingDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (str,),
            "created_by": (str,),
            "data": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
                none_type,
            ),
            "description": (str,),
            "last_modified_by": (str,),
            "setting_name": (str,),
            "updated_at": (str,),
            "version": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "data": "data",
        "description": "description",
        "last_modified_by": "last_modified_by",
        "setting_name": "setting_name",
        "updated_at": "updated_at",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: str,
        created_by: str,
        description: str,
        last_modified_by: str,
        setting_name: str,
        updated_at: str,
        version: str,
        data: Union[Dict[str, Any], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for a cost setting.

        :param created_at: The timestamp when the setting was created.
        :type created_at: str

        :param created_by: The UUID of the user who created the setting.
        :type created_by: str

        :param data: The setting data as a flexible key-value map.
        :type data: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param description: A human-readable description of the setting.
        :type description: str

        :param last_modified_by: The UUID of the user who last modified the setting.
        :type last_modified_by: str

        :param setting_name: The name of the setting.
        :type setting_name: str

        :param updated_at: The timestamp when the setting was last updated.
        :type updated_at: str

        :param version: The version of the setting.
        :type version: str
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.description = description
        self_.last_modified_by = last_modified_by
        self_.setting_name = setting_name
        self_.updated_at = updated_at
        self_.version = version
