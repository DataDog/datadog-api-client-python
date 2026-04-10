# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TriggerInvestigationResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "investigation_id": (str,),
        }

    attribute_map = {
        "investigation_id": "investigation_id",
    }

    def __init__(self_, investigation_id: str, **kwargs):
        """
        Attributes for the trigger investigation response.

        :param investigation_id: The ID of the investigation that was created.
        :type investigation_id: str
        """
        super().__init__(kwargs)

        self_.investigation_id = investigation_id
