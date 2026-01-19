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


class WebIntegrationAccountUpdateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "secrets": (
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
            ),
            "settings": (
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
            ),
        }

    attribute_map = {
        "name": "name",
        "secrets": "secrets",
        "settings": "settings",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        secrets: Union[Dict[str, Any], UnsetType] = unset,
        settings: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating a web integration account. All fields are optional -
        only provide the fields you want to update. Partial updates are supported,
        allowing you to modify specific settings or secrets without providing all fields.

        :param name: The name of the account.
        :type name: str, optional

        :param secrets: Sensitive credentials to update. Only the secrets provided will be updated.
            These values are write-only and never returned in responses.
        :type secrets: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param settings: Integration-specific settings to update. Only the fields provided will be updated.
            The structure varies by integration type. Refer to the integration's schema for available fields.
        :type settings: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if secrets is not unset:
            kwargs["secrets"] = secrets
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)
