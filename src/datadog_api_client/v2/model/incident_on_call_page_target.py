# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentOnCallPageTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "identifier": (str,),
            "type": (str,),
        }

    attribute_map = {
        "identifier": "identifier",
        "type": "type",
    }

    def __init__(self_, identifier: str, type: str, **kwargs):
        """
        The target of an on-call page.

        :param identifier: The identifier of the page target.
        :type identifier: str

        :param type: The type of the page target.
        :type type: str
        """
        super().__init__(kwargs)

        self_.identifier = identifier
        self_.type = type
