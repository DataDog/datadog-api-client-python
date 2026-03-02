# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class EventEmailAddressUserData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: str, **kwargs):
        """
        A user data reference in a relationship.

        :param id: The UUID of the user.
        :type id: str

        :param type: The type of the resource.
        :type type: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
