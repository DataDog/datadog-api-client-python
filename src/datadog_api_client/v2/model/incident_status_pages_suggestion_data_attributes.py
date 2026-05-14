# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentStatusPagesSuggestionDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "status": (str,),
            "update_text": (str,),
        }

    attribute_map = {
        "status": "status",
        "update_text": "update_text",
    }

    def __init__(self_, status: str, update_text: str, **kwargs):
        """
        Attributes of a status pages suggestion.

        :param status: The suggested status for the status page.
        :type status: str

        :param update_text: The suggested update text for the status page notice.
        :type update_text: str
        """
        super().__init__(kwargs)

        self_.status = status
        self_.update_text = update_text
