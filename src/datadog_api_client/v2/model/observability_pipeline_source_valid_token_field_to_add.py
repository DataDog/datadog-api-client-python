# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineSourceValidTokenFieldToAdd(ModelNormal):
    validations = {
        "key": {
            "max_length": 256,
        },
        "value": {
            "max_length": 1024,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "key": (str,),
            "value": (str,),
        }

    attribute_map = {
        "key": "key",
        "value": "value",
    }

    def __init__(self_, key: str, value: str, **kwargs):
        """
        An optional metadata field that is attached to every event authenticated by the
        associated token. Both ``key`` and ``value`` must match ``^[A-Za-z0-9_]+$``.

        :param key: The metadata field name to add to incoming events.
        :type key: str

        :param value: The metadata field value to add to incoming events.
        :type value: str
        """
        super().__init__(kwargs)

        self_.key = key
        self_.value = value
