# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardSearchAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "tags": ([str],),
            "title": (str,),
        }

    attribute_map = {
        "tags": "tags",
        "title": "title",
    }

    def __init__(self_, tags: List[str], title: str, **kwargs):
        """
        Dashboard search result attributes.

        :param tags: List of tags for the dashboard.
        :type tags: [str]

        :param title: Title of the dashboard.
        :type title: str
        """
        super().__init__(kwargs)

        self_.tags = tags
        self_.title = title
