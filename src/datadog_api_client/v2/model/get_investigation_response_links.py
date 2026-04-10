# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GetInvestigationResponseLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "self": (str,),
        }

    attribute_map = {
        "self": "self",
    }

    def __init__(self_, self: str, **kwargs):
        """
        Links related to the investigation.

        :param self: The URL to the investigation in the Datadog app.
        :type self: str
        """
        super().__init__(kwargs)

        self_.self = self
