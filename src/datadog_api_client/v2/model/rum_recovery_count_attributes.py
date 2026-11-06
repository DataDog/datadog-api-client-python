# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RumRecoveryCountAttributes(ModelNormal):
    validations = {
        "_from": {
            "inclusive_minimum": 1,
        },
        "to": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "_from": (int,),
            "query": (str,),
            "to": (int,),
        }

    attribute_map = {
        "_from": "from",
        "query": "query",
        "to": "to",
    }

    def __init__(self_, _from: int, query: str, to: int, **kwargs):
        """
        Query for a recovery estimate. The range cannot exceed 180 days; from cannot be more than 4 years ago and to cannot be more than 1 hour in the future. Session availability depends on the configured archive retention.

        :param _from: Start of the range in Unix milliseconds. Must be positive and earlier than to.
        :type _from: int

        :param query: RUM search query. Not blank, at most 4096 bytes for batch creation and count.
        :type query: str

        :param to: End of the range in Unix milliseconds.
        :type to: int
        """
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.to = to
