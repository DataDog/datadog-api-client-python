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
    from datadog_api_client.v2.model.experiments_bandit_policy_history_v2_dto_data_attributes import (
        ExperimentsBanditPolicyHistoryV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_bandit_policy_history_v2_dto_data_type import (
        ExperimentsBanditPolicyHistoryV2DTODataType,
    )


class ExperimentsBanditPolicyHistoryV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_policy_history_v2_dto_data_attributes import (
            ExperimentsBanditPolicyHistoryV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_bandit_policy_history_v2_dto_data_type import (
            ExperimentsBanditPolicyHistoryV2DTODataType,
        )

        return {
            "attributes": (ExperimentsBanditPolicyHistoryV2DTODataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsBanditPolicyHistoryV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsBanditPolicyHistoryV2DTODataAttributes,
        id: UUID,
        type: ExperimentsBanditPolicyHistoryV2DTODataType,
        **kwargs,
    ):
        """
        JSON:API resource containing a policy the bandit served.

        :param attributes: A traffic split the bandit served, with the same fields as ``active_policy``.
        :type attributes: ExperimentsBanditPolicyHistoryV2DTODataAttributes

        :param id: The policy ID. Each exposure logs it as ``bandit.policy_id`` , except exposures logged after the bandit ends.
        :type id: UUID

        :param type: Bandit policy resource type.
        :type type: ExperimentsBanditPolicyHistoryV2DTODataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
