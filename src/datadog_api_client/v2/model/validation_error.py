# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.validation_error_meta import ValidationErrorMeta


class ValidationError(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.validation_error_meta import ValidationErrorMeta

        return {
            "meta": (ValidationErrorMeta,),
            "title": (str,),
        }

    attribute_map = {
        "meta": "meta",
        "title": "title",
    }

    def __init__(self_, meta: ValidationErrorMeta, title: str, **kwargs):
        """
        Represents a single validation error, including a human-readable title and metadata.

        :param meta: Describes additional metadata for validation errors, including field names and error messages.
        :type meta: ValidationErrorMeta

        :param title: A short, human-readable summary of the error.
        :type title: str
        """
        super().__init__(kwargs)

        self_.meta = meta
        self_.title = title
