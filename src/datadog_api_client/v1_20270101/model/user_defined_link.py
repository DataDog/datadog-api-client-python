# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UserDefinedLink(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "label": (str,),
            "link": (str,),
        }

    attribute_map = {
        "label": "label",
        "link": "link",
    }

    def __init__(self_, label: str, link: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param label: Test-only generated schema for the dashboard versioning proof of concept.
        :type label: str

        :param link: Test-only generated schema for the dashboard versioning proof of concept.
        :type link: str
        """
        super().__init__(kwargs)

        self_.label = label
        self_.link = link
