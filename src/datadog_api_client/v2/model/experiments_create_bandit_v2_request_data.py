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
    from datadog_api_client.v2.model.experiments_create_bandit_v2_request_data_attributes import (
        ExperimentsCreateBanditV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_bandit_v2_dto_data_type import ExperimentsBanditV2DTODataType


class ExperimentsCreateBanditV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_bandit_v2_request_data_attributes import (
            ExperimentsCreateBanditV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_bandit_v2_dto_data_type import ExperimentsBanditV2DTODataType

        return {
            "attributes": (ExperimentsCreateBanditV2RequestDataAttributes,),
            "type": (ExperimentsBanditV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsCreateBanditV2RequestDataAttributes,
        type: ExperimentsBanditV2DTODataType,
        **kwargs,
    ):
        """
        Bandit resource to create.

        :param attributes: The new draft's setup. Only ``name`` is required. Whether the draft is ready to run is checked when it starts.
        :type attributes: ExperimentsCreateBanditV2RequestDataAttributes

        :param type: Bandit resource type.
        :type type: ExperimentsBanditV2DTODataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
