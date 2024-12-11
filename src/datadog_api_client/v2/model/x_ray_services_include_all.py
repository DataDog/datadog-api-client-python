# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class XRayServicesIncludeAll(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "include_all": (bool,),
        }

    attribute_map = {
        "include_all": "include_all",
    }

    def __init__(self_, include_all: bool, **kwargs):
        """
        Include all services.

        :param include_all: Include all services.
        :type include_all: bool
        """
        super().__init__(kwargs)

        self_.include_all = include_all
