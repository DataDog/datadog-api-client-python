# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.escalation_relationships_responders_data_items import (
        EscalationRelationshipsRespondersDataItems,
    )


class EscalationRelationshipsResponders(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_relationships_responders_data_items import (
            EscalationRelationshipsRespondersDataItems,
        )

        return {
            "data": ([EscalationRelationshipsRespondersDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[EscalationRelationshipsRespondersDataItems], UnsetType] = unset, **kwargs):
        """
        Lists the users involved in a specific step of the escalation policy.

        :param data: Array of user references assigned as responders for this escalation step.
        :type data: [EscalationRelationshipsRespondersDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
