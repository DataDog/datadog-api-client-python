# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
        CreateDegradationRequestDataAttributesStatus,
    )


class DegradationTemplateDataAttributesUpdatesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
            CreateDegradationRequestDataAttributesStatus,
        )

        return {
            "message": (str,),
            "status": (CreateDegradationRequestDataAttributesStatus,),
        }

    attribute_map = {
        "message": "message",
        "status": "status",
    }

    def __init__(
        self_, status: CreateDegradationRequestDataAttributesStatus, message: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        A pre-filled update for a degradation created from this template.

        :param message: The message of the update.
        :type message: str, optional

        :param status: The status of the degradation.
        :type status: CreateDegradationRequestDataAttributesStatus
        """
        if message is not unset:
            kwargs["message"] = message
        super().__init__(kwargs)

        self_.status = status
