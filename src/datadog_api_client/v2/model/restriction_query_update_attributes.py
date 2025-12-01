# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RestrictionQueryUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "restriction_query": (str,),
        }

    attribute_map = {
        "restriction_query": "restriction_query",
    }

    def __init__(self_, restriction_query: str, **kwargs):
        """
        Attributes of the edited restriction query.

        :param restriction_query: The restriction query.
        :type restriction_query: str
        """
        super().__init__(kwargs)

        self_.restriction_query = restriction_query
