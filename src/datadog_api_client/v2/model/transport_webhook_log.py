# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.transport_webhook_log_attributes import TransportWebhookLogAttributes


class TransportWebhookLog(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.transport_webhook_log_attributes import TransportWebhookLogAttributes

        return {
            "attributes": (TransportWebhookLogAttributes,),
            "date": (datetime,),
            "log_id": (str,),
            "source": (str,),
            "status": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "attributes": "attributes",
        "date": "date",
        "log_id": "log_id",
        "source": "source",
        "status": "status",
        "tags": "tags",
    }

    def __init__(
        self_,
        attributes: TransportWebhookLogAttributes,
        date: datetime,
        log_id: str,
        source: str,
        status: str,
        tags: List[str],
        **kwargs,
    ):
        """
        A single email transport webhook log event.

        :param attributes: Top-level attributes for the webhook log event, including delivery status, recipient details, and provider metadata.
        :type attributes: TransportWebhookLogAttributes

        :param date: The ISO 8601 timestamp of the event.
        :type date: datetime

        :param log_id: The unique log event identifier.
        :type log_id: str

        :param source: The email transport provider.
        :type source: str

        :param status: The log status level.
        :type status: str

        :param tags: A list of tags associated with the event.
        :type tags: [str]
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.date = date
        self_.log_id = log_id
        self_.source = source
        self_.status = status
        self_.tags = tags
