# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

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


class SecurityFindingsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attributes": (
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
            "tags": ([str],),
            "timestamp": (int,),
        }

    attribute_map = {
        "attributes": "attributes",
        "tags": "tags",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        attributes: Union[Dict[str, Any], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        timestamp: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The JSON object containing all attributes of the security finding.

        :param attributes: The custom attributes of the security finding.
        :type attributes: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param tags: List of tags associated with the security finding.
        :type tags: [str], optional

        :param timestamp: The Unix timestamp at which the detection changed for the resource. Same value as @detection_changed_at.
        :type timestamp: int, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if tags is not unset:
            kwargs["tags"] = tags
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)
