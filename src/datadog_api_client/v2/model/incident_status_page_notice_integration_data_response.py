# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_status_page_notice_integration_data_attributes import (
        IncidentStatusPageNoticeIntegrationDataAttributes,
    )
    from datadog_api_client.v2.model.incident_status_page_notice_integration_type import (
        IncidentStatusPageNoticeIntegrationType,
    )


class IncidentStatusPageNoticeIntegrationDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_status_page_notice_integration_data_attributes import (
            IncidentStatusPageNoticeIntegrationDataAttributes,
        )
        from datadog_api_client.v2.model.incident_status_page_notice_integration_type import (
            IncidentStatusPageNoticeIntegrationType,
        )

        return {
            "attributes": (IncidentStatusPageNoticeIntegrationDataAttributes,),
            "id": (UUID,),
            "type": (IncidentStatusPageNoticeIntegrationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentStatusPageNoticeIntegrationDataAttributes,
        id: UUID,
        type: IncidentStatusPageNoticeIntegrationType,
        **kwargs,
    ):
        """
        Status page notice integration data in a response.

        :param attributes: Attributes of a status page notice integration.
        :type attributes: IncidentStatusPageNoticeIntegrationDataAttributes

        :param id: The integration identifier.
        :type id: UUID

        :param type: Incident integration resource type.
        :type type: IncidentStatusPageNoticeIntegrationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
