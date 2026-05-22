# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SampleLogGenerationSubscriptionsResponseMeta(ModelNormal):
    validations = {
        "total_subscriptions": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "total_subscriptions": (int,),
        }

    attribute_map = {
        "total_subscriptions": "total_subscriptions",
    }

    def __init__(self_, total_subscriptions: int, **kwargs):
        """
        Metadata returned alongside a list of sample log generation subscriptions.

        :param total_subscriptions: The total number of subscriptions matching the request, irrespective of pagination.
        :type total_subscriptions: int
        """
        super().__init__(kwargs)

        self_.total_subscriptions = total_subscriptions
