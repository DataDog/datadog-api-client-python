# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UpdateAppTagsRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "tags": ([str],),
        }

    attribute_map = {
        "tags": "tags",
    }

    def __init__(self_, tags: List[str], **kwargs):
        """
        Attributes for replacing an app's tags.

        :param tags: The full list of tags that should be set on the app. Existing tags not present in this list are removed.
        :type tags: [str]
        """
        super().__init__(kwargs)

        self_.tags = tags
