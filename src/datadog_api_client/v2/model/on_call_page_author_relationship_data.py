# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OnCallPageAuthorRelationshipData(ModelNormal):
    _nullable = True

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
        Reference to the author of a Page action.

        :param id: The ID of the author.
        :type id: str

        :param type: The resource type of the author, for example ``users`` , ``monitors`` ,
            ``incident_authors`` , or ``security_signal``.
        :type type: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
