# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OrgAuthorizedClientRelationshipUserAuthorizedClientsLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "related": (str,),
        }

    attribute_map = {
        "related": "related",
    }

    def __init__(self_, related: str, **kwargs):
        """
        Links for the user authorized clients relationship.

        :param related: Link to the user authorized clients for this org authorized client.
        :type related: str
        """
        super().__init__(kwargs)

        self_.related = related
