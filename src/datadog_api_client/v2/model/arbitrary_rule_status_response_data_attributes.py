# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ArbitraryRuleStatusResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "processing_status": (str,),
        }

    attribute_map = {
        "processing_status": "processing_status",
    }

    def __init__(self_, processing_status: str, **kwargs):
        """
        The definition of ``ArbitraryRuleStatusResponseDataAttributes`` object.

        :param processing_status: The processing status of the custom allocation rule.
        :type processing_status: str
        """
        super().__init__(kwargs)

        self_.processing_status = processing_status
