# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class RumManagedArchiveErrorResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "errors": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type],),
        }

    attribute_map = {
        "errors": "errors",
    }

    def __init__(self_, errors: List[Any], **kwargs):
        """
        API error response.

        :param errors: Errors as plain-text messages or JSON:API error objects containing status, title, and detail.
        :type errors: [bool, date, datetime, dict, float, int, list, str, UUID, none_type]
        """
        super().__init__(kwargs)

        self_.errors = errors
