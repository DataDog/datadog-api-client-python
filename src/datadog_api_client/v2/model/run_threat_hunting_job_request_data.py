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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.run_threat_hunting_job_request_attributes import (
        RunThreatHuntingJobRequestAttributes,
    )
    from datadog_api_client.v2.model.run_threat_hunting_job_request_data_type import RunThreatHuntingJobRequestDataType


class RunThreatHuntingJobRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.run_threat_hunting_job_request_attributes import (
            RunThreatHuntingJobRequestAttributes,
        )
        from datadog_api_client.v2.model.run_threat_hunting_job_request_data_type import (
            RunThreatHuntingJobRequestDataType,
        )

        return {
            "attributes": (RunThreatHuntingJobRequestAttributes,),
            "type": (RunThreatHuntingJobRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RunThreatHuntingJobRequestAttributes, UnsetType] = unset,
        type: Union[RunThreatHuntingJobRequestDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for running a threat hunting job request.

        :param attributes: Run a threat hunting job request.
        :type attributes: RunThreatHuntingJobRequestAttributes, optional

        :param type: Type of data.
        :type type: RunThreatHuntingJobRequestDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
