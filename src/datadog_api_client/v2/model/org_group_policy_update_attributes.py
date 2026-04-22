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


class OrgGroupPolicyUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "content": (
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
        "content": "content",
    }

    def __init__(self_, content: Union[Dict[str, Any], UnsetType] = unset, **kwargs):
        """
        Attributes for updating an org group policy.

        :param content: The policy content as key-value pairs.
        :type content: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if content is not unset:
            kwargs["content"] = content
        super().__init__(kwargs)
