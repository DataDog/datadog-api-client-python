# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class StatuspageAccountCreateAttributes(ModelNormal):
    validations = {
        "api_key": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "api_key": (str,),
        }

    attribute_map = {
        "api_key": "api_key",
    }

    def __init__(self_, api_key: str, **kwargs):
        """
        The Statuspage account attributes for a create request.

        :param api_key: The Statuspage API key for your Statuspage account.
        :type api_key: str
        """
        super().__init__(kwargs)

        self_.api_key = api_key
