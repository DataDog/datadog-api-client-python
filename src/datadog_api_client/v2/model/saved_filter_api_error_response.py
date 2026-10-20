# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SavedFilterAPIErrorResponse(ModelNormal):
    validations = {
        "errors": {
            "min_items": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "errors": ([str],),
        }

    attribute_map = {
        "errors": "errors",
    }

    def __init__(self_, errors: List[str], **kwargs):
        """
        A saved filter authorization error containing at least one error message.

        :param errors: The authorization error messages.
        :type errors: [str]
        """
        super().__init__(kwargs)

        self_.errors = errors
