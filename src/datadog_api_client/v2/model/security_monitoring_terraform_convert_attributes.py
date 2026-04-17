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


class SecurityMonitoringTerraformConvertAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "resource_json": (
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
        "resource_json": "resource_json",
    }

    def __init__(self_, resource_json: Dict[str, Any], **kwargs):
        """
        Attributes for the convert request.

        :param resource_json: The resource attributes as a JSON object, matching the structure returned by the corresponding Datadog API (for example, the attributes of a suppression rule).
        :type resource_json: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}
        """
        super().__init__(kwargs)

        self_.resource_json = resource_json
