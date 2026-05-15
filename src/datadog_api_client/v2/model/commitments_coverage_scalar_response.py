# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.commitments_scalar_column import CommitmentsScalarColumn


class CommitmentsCoverageScalarResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_scalar_column import CommitmentsScalarColumn

        return {
            "columns": ([CommitmentsScalarColumn],),
        }

    attribute_map = {
        "columns": "columns",
    }

    def __init__(self_, columns: List[CommitmentsScalarColumn], **kwargs):
        """
        Response containing scalar coverage metrics for cloud commitment programs.

        :param columns: Array of scalar columns in the response.
        :type columns: [CommitmentsScalarColumn]
        """
        super().__init__(kwargs)

        self_.columns = columns
