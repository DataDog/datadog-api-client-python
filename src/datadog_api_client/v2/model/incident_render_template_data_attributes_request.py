# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class IncidentRenderTemplateDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "content": (str,),
            "datetime_format": (str,),
            "timezone": (str,),
            "validate_links": (bool, none_type),
            "validate_variables": (bool, none_type),
        }

    attribute_map = {
        "content": "content",
        "datetime_format": "datetime_format",
        "timezone": "timezone",
        "validate_links": "validate_links",
        "validate_variables": "validate_variables",
    }

    def __init__(
        self_,
        content: str,
        datetime_format: Union[str, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        validate_links: Union[bool, none_type, UnsetType] = unset,
        validate_variables: Union[bool, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for rendering a template.

        :param content: The template content to render.
        :type content: str

        :param datetime_format: The date-time format to use for rendering.
        :type datetime_format: str, optional

        :param timezone: The timezone to use for rendering.
        :type timezone: str, optional

        :param validate_links: Whether to validate links in the rendered template.
        :type validate_links: bool, none_type, optional

        :param validate_variables: Whether to validate variables in the template.
        :type validate_variables: bool, none_type, optional
        """
        if datetime_format is not unset:
            kwargs["datetime_format"] = datetime_format
        if timezone is not unset:
            kwargs["timezone"] = timezone
        if validate_links is not unset:
            kwargs["validate_links"] = validate_links
        if validate_variables is not unset:
            kwargs["validate_variables"] = validate_variables
        super().__init__(kwargs)

        self_.content = content
