# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.microsoft_sentinel_destination_type import MicrosoftSentinelDestinationType


class MicrosoftSentinelDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.microsoft_sentinel_destination_type import MicrosoftSentinelDestinationType

        return {
            "client_id": (str,),
            "dcr_immutable_id": (str,),
            "id": (str,),
            "inputs": ([str],),
            "table": (str,),
            "tenant_id": (str,),
            "type": (MicrosoftSentinelDestinationType,),
        }

    attribute_map = {
        "client_id": "client_id",
        "dcr_immutable_id": "dcr_immutable_id",
        "id": "id",
        "inputs": "inputs",
        "table": "table",
        "tenant_id": "tenant_id",
        "type": "type",
    }

    def __init__(
        self_,
        client_id: str,
        dcr_immutable_id: str,
        id: str,
        inputs: List[str],
        table: str,
        tenant_id: str,
        type: MicrosoftSentinelDestinationType,
        **kwargs,
    ):
        """
        The ``microsoft_sentinel`` destination forwards logs to Microsoft Sentinel.

        :param client_id: Azure AD client ID used for authentication.
        :type client_id: str

        :param dcr_immutable_id: The immutable ID of the Data Collection Rule (DCR).
        :type dcr_immutable_id: str

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param table: The name of the Log Analytics table where logs are sent.
        :type table: str

        :param tenant_id: Azure AD tenant ID.
        :type tenant_id: str

        :param type: The destination type. The value should always be ``microsoft_sentinel``.
        :type type: MicrosoftSentinelDestinationType
        """
        super().__init__(kwargs)

        self_.client_id = client_id
        self_.dcr_immutable_id = dcr_immutable_id
        self_.id = id
        self_.inputs = inputs
        self_.table = table
        self_.tenant_id = tenant_id
        self_.type = type
