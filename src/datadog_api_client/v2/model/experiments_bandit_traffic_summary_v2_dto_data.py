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
    from datadog_api_client.v2.model.experiments_bandit_traffic_summary_v2_dto_data_attributes import (
        ExperimentsBanditTrafficSummaryV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_bandit_traffic_summary_v2_dto_data_type import (
        ExperimentsBanditTrafficSummaryV2DTODataType,
    )


class ExperimentsBanditTrafficSummaryV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_traffic_summary_v2_dto_data_attributes import (
            ExperimentsBanditTrafficSummaryV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_bandit_traffic_summary_v2_dto_data_type import (
            ExperimentsBanditTrafficSummaryV2DTODataType,
        )

        return {
            "attributes": (ExperimentsBanditTrafficSummaryV2DTODataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsBanditTrafficSummaryV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsBanditTrafficSummaryV2DTODataAttributes,
        id: UUID,
        type: ExperimentsBanditTrafficSummaryV2DTODataType,
        **kwargs,
    ):
        """
        JSON:API resource containing a bandit's traffic summary.

        :param attributes: What the bandit has observed, as of its latest saved refresh.
        :type attributes: ExperimentsBanditTrafficSummaryV2DTODataAttributes

        :param id: The bandit ID.
        :type id: UUID

        :param type: Bandit traffic summary resource type.
        :type type: ExperimentsBanditTrafficSummaryV2DTODataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
