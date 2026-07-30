# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class STIXIngestResponseAttributes(ModelNormal):
    validations = {
        "added": {
            "inclusive_minimum": 0,
        },
        "invalid": {
            "inclusive_minimum": 0,
        },
        "unsupported": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "added": (int,),
            "invalid": (int,),
            "unsupported": (int,),
        }

    attribute_map = {
        "added": "added",
        "invalid": "invalid",
        "unsupported": "unsupported",
    }

    def __init__(self_, added: int, invalid: int, unsupported: int, **kwargs):
        """
        Counters describing the result of the STIX ingestion request.

        :param added: The number of supported indicators added.
        :type added: int

        :param invalid: The number of indicators with patterns that could not be parsed.
        :type invalid: int

        :param unsupported: The number of unsupported objects or patterns.
        :type unsupported: int
        """
        super().__init__(kwargs)

        self_.added = added
        self_.invalid = invalid
        self_.unsupported = unsupported
