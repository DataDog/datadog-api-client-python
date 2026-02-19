# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RumSegmentStaticEntry(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "name": (str,),
            "user_count": (int,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "user_count": "user_count",
    }

    def __init__(self_, id: str, name: str, user_count: int, **kwargs):
        """
        A static user list entry within a segment data query.

        :param id: The identifier of the static list.
        :type id: str

        :param name: The name of the static list.
        :type name: str

        :param user_count: The number of users in the static list.
        :type user_count: int
        """
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
        self_.user_count = user_count
