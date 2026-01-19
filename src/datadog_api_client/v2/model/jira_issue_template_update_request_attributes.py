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


class JiraIssueTemplateUpdateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "fields": (
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
            "name": (str,),
        }

    attribute_map = {
        "fields": "fields",
        "name": "name",
    }

    def __init__(
        self_, fields: Union[Dict[str, Any], UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Attributes for updating a Jira issue template

        :param fields: Custom fields for the Jira issue template
        :type fields: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param name: The name of the issue template
        :type name: str, optional
        """
        if fields is not unset:
            kwargs["fields"] = fields
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
