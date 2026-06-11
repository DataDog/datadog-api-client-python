# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class ReportScheduleAuthorAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str, none_type),
            "name": (str, none_type),
        }

    attribute_map = {
        "email": "email",
        "name": "name",
    }

    def __init__(self_, email: Union[str, none_type], name: Union[str, none_type], **kwargs):
        """
        Attributes of the report author.

        :param email: The email address of the report author, or ``null`` if unavailable.
        :type email: str, none_type

        :param name: The display name of the report author, or ``null`` if unavailable.
        :type name: str, none_type
        """
        super().__init__(kwargs)

        self_.email = email
        self_.name = name
