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
    from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data import (
        ExperimentsCreateExposureSQLModelV2RequestData,
    )


class ExperimentsCreateExposureSQLModelV2Request(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data import (
            ExperimentsCreateExposureSQLModelV2RequestData,
        )

        return {
            "data": (ExperimentsCreateExposureSQLModelV2RequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsCreateExposureSQLModelV2RequestData, **kwargs):
        """
        Request to create a SQL model for experiment assignment data.

        :param data: Exposure SQL model resource to create.
        :type data: ExperimentsCreateExposureSQLModelV2RequestData
        """
        super().__init__(kwargs)

        self_.data = data
