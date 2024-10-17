# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSNamespaceFiltersExcludeAll(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "exclude_all": (bool,),
        }

    attribute_map = {
        "exclude_all": "exclude_all",
    }

    def __init__(self_, exclude_all: bool, **kwargs):
        """
        Exclude all namespaces

        :param exclude_all: Exclude all namespaces
        :type exclude_all: bool
        """
        super().__init__(kwargs)

        self_.exclude_all = exclude_all
