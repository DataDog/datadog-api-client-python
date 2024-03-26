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
    from datadog_api_client.v2.model.slo_report_status_get_response_attributes import (
        SLOReportStatusGetResponseAttributes,
    )


class SLOReportStatusGetResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.slo_report_status_get_response_attributes import (
            SLOReportStatusGetResponseAttributes,
        )

        return {
            "attributes": (SLOReportStatusGetResponseAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SLOReportStatusGetResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data portion of the SLO report status response.

        :param attributes: The attributes portion of the SLO report status response.
        :type attributes: SLOReportStatusGetResponseAttributes, optional

        :param id: The ID of the report job.
        :type id: str, optional

        :param type: The type of ID.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
