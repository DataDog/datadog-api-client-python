# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class VercelApiKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "value": (str,),
        }

    attribute_map = {
        "id": "id",
        "value": "value",
    }

    def __init__(self_, id: str, value: str, **kwargs):
        """
        Datadog API key reference used by the Vercel integration to send telemetry.

        :param id: ID of the Datadog API key used by the Vercel integration.
        :type id: str

        :param value: Value of the Datadog API key. Returned as an empty string in read responses.
        :type value: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.value = value
