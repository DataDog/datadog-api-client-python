# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentStatuspageSubscriptionDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
        }

    attribute_map = {
        "email": "email",
    }

    def __init__(self_, email: str, **kwargs):
        """
        Attributes for creating an email subscription.

        :param email: The email address to subscribe.
        :type email: str
        """
        super().__init__(kwargs)

        self_.email = email
