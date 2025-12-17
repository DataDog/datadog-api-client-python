# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersSegmentsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "segment_id": (str,),
        }

    attribute_map = {
        "name": "name",
        "segment_id": "segment_id",
    }

    def __init__(self_, name: str, segment_id: str, **kwargs):
        """


        :param name:
        :type name: str

        :param segment_id:
        :type segment_id: str
        """
        super().__init__(kwargs)

        self_.name = name
        self_.segment_id = segment_id
