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
    from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request_data_attributes import (
        ExperimentsAnalysisPlanWriteV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request_data_type import (
        ExperimentsAnalysisPlanWriteV2RequestDataType,
    )


class ExperimentsAnalysisPlanWriteV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request_data_attributes import (
            ExperimentsAnalysisPlanWriteV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request_data_type import (
            ExperimentsAnalysisPlanWriteV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsAnalysisPlanWriteV2RequestDataAttributes,),
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
        type: ExperimentsAnalysisPlanWriteV2RequestDataType,
        attributes: Union[ExperimentsAnalysisPlanWriteV2RequestDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Analysis plan resource to update.

        :param attributes: Statistical settings and duration targets to apply to the experiment.
        :type attributes: ExperimentsAnalysisPlanWriteV2RequestDataAttributes, optional

        :param id: Identifier of the experiment. If supplied, it must match experiment_id in the path.
        :type id: UUID, optional

        :param type: Analysis plans resource type.
        :type type: ExperimentsAnalysisPlanWriteV2RequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
