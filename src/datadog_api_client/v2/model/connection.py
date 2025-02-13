# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class Connection(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "connection_id": (str,),
            "label": (str,),
        }

    attribute_map = {
        "connection_id": "connectionId",
        "label": "label",
    }

    def __init__(self_, connection_id: str, label: str, **kwargs):
        """
        The definition of ``Connection`` object.

        :param connection_id: The ``Connection`` ``connectionId``.
        :type connection_id: str

        :param label: The ``Connection`` ``label``.
        :type label: str
        """
        super().__init__(kwargs)

        self_.connection_id = connection_id
        self_.label = label
