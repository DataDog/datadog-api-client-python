# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AIGuardSdsFindingLocation(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end_index_exclusive": (int,),
            "path": (str,),
            "start_index": (int,),
        }

    attribute_map = {
        "end_index_exclusive": "end_index_exclusive",
        "path": "path",
        "start_index": "start_index",
    }

    def __init__(self_, end_index_exclusive: int, path: str, start_index: int, **kwargs):
        """
        The location of a sensitive data match within the evaluated request.

        :param end_index_exclusive: The end character index (exclusive) of the sensitive data match.
        :type end_index_exclusive: int

        :param path: The JSON path to the field containing the sensitive data.
        :type path: str

        :param start_index: The start character index of the sensitive data match.
        :type start_index: int
        """
        super().__init__(kwargs)

        self_.end_index_exclusive = end_index_exclusive
        self_.path = path
        self_.start_index = start_index
