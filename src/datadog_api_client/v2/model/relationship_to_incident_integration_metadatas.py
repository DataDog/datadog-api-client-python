# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RelationshipToIncidentIntegrationMetadatas(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_incident_integration_metadata_data import (
            RelationshipToIncidentIntegrationMetadataData,
        )

        return {
            "data": ([RelationshipToIncidentIntegrationMetadataData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data, *args, **kwargs):
        """
        A relationship reference for multiple integration metadata objects.

        :param data: The integration metadata relationship array
        :type data: [RelationshipToIncidentIntegrationMetadataData]
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.data = data
