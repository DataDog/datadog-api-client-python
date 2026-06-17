# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.io_c_triage_write_request_attributes import IoCTriageWriteRequestAttributes


class IoCTriageWriteRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.io_c_triage_write_request_attributes import IoCTriageWriteRequestAttributes

        return {
            "attributes": (IoCTriageWriteRequestAttributes,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: IoCTriageWriteRequestAttributes, **kwargs):
        """
        Data object for the triage write request.

        :param attributes: Attributes for setting an indicator's triage state.
        :type attributes: IoCTriageWriteRequestAttributes

        :param type: Triage state resource type.
        :type type: str
        """
        super().__init__(kwargs)
        type = kwargs.get("type", "ioc_triage_state")

        self_.attributes = attributes
        self_.type = type
