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
    from datadog_api_client.v2.model.experiments_exposure_sql_model_v2_dto_data import (
        ExperimentsExposureSQLModelV2DTOData,
    )


class ExperimentsExposureSQLModelV2DTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_exposure_sql_model_v2_dto_data import (
            ExperimentsExposureSQLModelV2DTOData,
        )

        return {
            "data": (ExperimentsExposureSQLModelV2DTOData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsExposureSQLModelV2DTOData, **kwargs):
        """
        Response containing a SQL model for experiment assignment data.

        :param data: Exposure SQL model resource with its identifier and configuration.
        :type data: ExperimentsExposureSQLModelV2DTOData
        """
        super().__init__(kwargs)

        self_.data = data
