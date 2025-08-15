# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class PutAppsDatastoreItemRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "value": (
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
        "value": "value",
    }

    def __init__(self_, value: Dict[str, Any], **kwargs):
        """
        The definition of ``PutAppsDatastoreItemRequestDataAttributes`` object.

        :param value: The ``attributes`` ``value``.
        :type value: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}
        """
        super().__init__(kwargs)

        self_.value = value
