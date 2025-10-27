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
    from datadog_api_client.v2.model.threat_hunting_job_response_data import ThreatHuntingJobResponseData
    from datadog_api_client.v2.model.threat_hunting_job_list_meta import ThreatHuntingJobListMeta


class ListThreatHuntingJobsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.threat_hunting_job_response_data import ThreatHuntingJobResponseData
        from datadog_api_client.v2.model.threat_hunting_job_list_meta import ThreatHuntingJobListMeta

        return {
            "data": ([ThreatHuntingJobResponseData],),
            "meta": (ThreatHuntingJobListMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[ThreatHuntingJobResponseData], UnsetType] = unset,
        meta: Union[ThreatHuntingJobListMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        List of threat hunting jobs.

        :param data: Array containing the list of threat hunting jobs.
        :type data: [ThreatHuntingJobResponseData], optional

        :param meta: Metadata about the list of jobs.
        :type meta: ThreatHuntingJobListMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
