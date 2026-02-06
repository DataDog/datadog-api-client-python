# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class JiraIssueFindingId(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "discovered": (int,),
            "id": (str,),
            "resource": (str,),
            "tags": (str,),
        }

    attribute_map = {
        "discovered": "discovered",
        "id": "id",
        "resource": "resource",
        "tags": "tags",
    }

    def __init__(self_, discovered: int, id: str, resource: str, tags: str, **kwargs):
        """


        :param discovered: Timestamp when the finding was discovered.
        :type discovered: int

        :param id: Identifier of the finding.
        :type id: str

        :param resource: Resource associated with the finding.
        :type resource: str

        :param tags: Tags associated with the finding.
        :type tags: str
        """
        super().__init__(kwargs)

        self_.discovered = discovered
        self_.id = id
        self_.resource = resource
        self_.tags = tags
