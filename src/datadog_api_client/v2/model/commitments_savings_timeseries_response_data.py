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
    from datadog_api_client.v2.model.commitments_savings_timeseries_response_attributes import (
        CommitmentsSavingsTimeseriesResponseAttributes,
    )
    from datadog_api_client.v2.model.commitments_savings_timeseries_response_type import (
        CommitmentsSavingsTimeseriesResponseType,
    )


class CommitmentsSavingsTimeseriesResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_savings_timeseries_response_attributes import (
            CommitmentsSavingsTimeseriesResponseAttributes,
        )
        from datadog_api_client.v2.model.commitments_savings_timeseries_response_type import (
            CommitmentsSavingsTimeseriesResponseType,
        )

        return {
            "attributes": (CommitmentsSavingsTimeseriesResponseAttributes,),
            "id": (str,),
            "type": (CommitmentsSavingsTimeseriesResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CommitmentsSavingsTimeseriesResponseAttributes,
        id: str,
        type: CommitmentsSavingsTimeseriesResponseType,
        **kwargs,
    ):
        """
        The timeseries savings resource.

        :param attributes: Attributes of a timeseries savings response.
        :type attributes: CommitmentsSavingsTimeseriesResponseAttributes

        :param id: The identifier of the timeseries savings response.
        :type id: str

        :param type: Type of the timeseries savings response resource.
        :type type: CommitmentsSavingsTimeseriesResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
