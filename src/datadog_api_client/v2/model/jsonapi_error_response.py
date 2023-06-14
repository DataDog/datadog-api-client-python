# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.jsonapi_error_item import JSONAPIErrorItem


class JSONAPIErrorResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jsonapi_error_item import JSONAPIErrorItem

        return {
            "errors": ([JSONAPIErrorItem],),
        }

    attribute_map = {
        "errors": "errors",
    }

    def __init__(self_, errors: List[JSONAPIErrorItem], **kwargs):
        """
        API error response.

        :param errors: A list of errors.
        :type errors: [JSONAPIErrorItem]
        """
        super().__init__(kwargs)

        self_.errors = errors
