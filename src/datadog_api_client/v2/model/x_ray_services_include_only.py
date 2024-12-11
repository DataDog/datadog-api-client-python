# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class XRayServicesIncludeOnly(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "include_only": ([str],),
        }

    attribute_map = {
        "include_only": "include_only",
    }

    def __init__(self_, include_only: List[str], **kwargs):
        """
        Include only these services. Defaults to ``[]``.

        :param include_only: Include only these services.
        :type include_only: [str]
        """
        super().__init__(kwargs)

        self_.include_only = include_only
