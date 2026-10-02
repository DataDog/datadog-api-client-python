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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_analysis_plan_v2_mutation_response_data_attributes import (
        ExperimentsAnalysisPlanV2MutationResponseDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request_data_type import (
        ExperimentsAnalysisPlanWriteV2RequestDataType,
    )


class ExperimentsAnalysisPlanV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_analysis_plan_v2_mutation_response_data_attributes import (
            ExperimentsAnalysisPlanV2MutationResponseDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request_data_type import (
            ExperimentsAnalysisPlanWriteV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsAnalysisPlanV2MutationResponseDataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsAnalysisPlanWriteV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: ExperimentsAnalysisPlanWriteV2RequestDataType,
        attributes: Union[ExperimentsAnalysisPlanV2MutationResponseDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Analysis plan resource with its identifier and settings.

        :param attributes: Statistical settings and duration targets in the saved analysis plan.
        :type attributes: ExperimentsAnalysisPlanV2MutationResponseDataAttributes, optional

        :param id: Identifier of the experiment whose analysis plan is returned.
        :type id: UUID

        :param type: Analysis plans resource type.
        :type type: ExperimentsAnalysisPlanWriteV2RequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
