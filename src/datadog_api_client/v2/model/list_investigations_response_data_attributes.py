# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ListInvestigationsResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "status": (str,),
            "title": (str,),
        }

    attribute_map = {
        "status": "status",
        "title": "title",
    }

    def __init__(self_, status: str, title: str, **kwargs):
        """
        Attributes of an investigation list item.

        :param status: The current status of the investigation.
        :type status: str

        :param title: The title of the investigation.
        :type title: str
        """
        super().__init__(kwargs)

        self_.status = status
        self_.title = title
