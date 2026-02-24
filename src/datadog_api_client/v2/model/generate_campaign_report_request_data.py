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
    from datadog_api_client.v2.model.generate_campaign_report_request_attributes import (
        GenerateCampaignReportRequestAttributes,
    )
    from datadog_api_client.v2.model.generate_campaign_report_request_data_type import (
        GenerateCampaignReportRequestDataType,
    )


class GenerateCampaignReportRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.generate_campaign_report_request_attributes import (
            GenerateCampaignReportRequestAttributes,
        )
        from datadog_api_client.v2.model.generate_campaign_report_request_data_type import (
            GenerateCampaignReportRequestDataType,
        )

        return {
            "attributes": (GenerateCampaignReportRequestAttributes,),
            "type": (GenerateCampaignReportRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GenerateCampaignReportRequestAttributes,
        type: GenerateCampaignReportRequestDataType,
        **kwargs,
    ):
        """
        Data for generating a campaign report.

        :param attributes: Attributes for generating a campaign report.
        :type attributes: GenerateCampaignReportRequestAttributes

        :param type:
        :type type: GenerateCampaignReportRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
