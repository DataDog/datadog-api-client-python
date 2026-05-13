# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CostAnomalyDismissal(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cause": (str,),
            "dismissal_id": (str,),
            "message": (str,),
            "updated_at": (int,),
            "updated_by": (str,),
        }

    attribute_map = {
        "cause": "cause",
        "dismissal_id": "dismissal_id",
        "message": "message",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(self_, cause: str, dismissal_id: str, message: str, updated_at: int, updated_by: str, **kwargs):
        """
        Resolution metadata for an anomaly that has been dismissed.

        :param cause: Reason the anomaly was dismissed.
        :type cause: str

        :param dismissal_id: Unique identifier of the dismissal record.
        :type dismissal_id: str

        :param message: Optional message explaining the dismissal.
        :type message: str

        :param updated_at: Timestamp of the last dismissal update in Unix milliseconds.
        :type updated_at: int

        :param updated_by: Identifier of the user that last updated the dismissal.
        :type updated_by: str
        """
        super().__init__(kwargs)

        self_.cause = cause
        self_.dismissal_id = dismissal_id
        self_.message = message
        self_.updated_at = updated_at
        self_.updated_by = updated_by
