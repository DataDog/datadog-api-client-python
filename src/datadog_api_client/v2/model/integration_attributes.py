# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IntegrationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "categories": ([str],),
            "description": (str,),
            "installed": (bool,),
            "title": (str,),
        }

    attribute_map = {
        "categories": "categories",
        "description": "description",
        "installed": "installed",
        "title": "title",
    }

    def __init__(self_, categories: List[str], description: str, installed: bool, title: str, **kwargs):
        """
        Attributes for an integration.

        :param categories: List of categories associated with the integration.
        :type categories: [str]

        :param description: A description of the integration.
        :type description: str

        :param installed: Whether the integration is installed.
        :type installed: bool

        :param title: The name of the integration.
        :type title: str
        """
        super().__init__(kwargs)

        self_.categories = categories
        self_.description = description
        self_.installed = installed
        self_.title = title
