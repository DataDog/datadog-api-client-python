# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentAttachmentsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_attachment_data import IncidentAttachmentData
        from datadog_api_client.v2.model.incident_attachments_response_included_item import (
            IncidentAttachmentsResponseIncludedItem,
        )

        return {
            "data": ([IncidentAttachmentData],),
            "included": ([IncidentAttachmentsResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(self_, data, *args, **kwargs):
        """
        The response object containing an incident's attachments.

        :param data: An array of incident attachments.
        :type data: [IncidentAttachmentData]

        :param included: Included related resources that the user requested.
        :type included: [IncidentAttachmentsResponseIncludedItem], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.data = data
