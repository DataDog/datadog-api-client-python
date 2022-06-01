# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.service_level_objective import ServiceLevelObjective
        from datadog_api_client.v1.model.slo_list_response_metadata import SLOListResponseMetadata

        return {
            "data": ([ServiceLevelObjective],),
            "errors": ([str],),
            "metadata": (SLOListResponseMetadata,),
        }

    attribute_map = {
        "data": "data",
        "errors": "errors",
        "metadata": "metadata",
    }

    def __init__(self, *args, **kwargs):
        """
        A response with one or more service level objective.

        :param data: An array of service level objective objects.
        :type data: [ServiceLevelObjective], optional

        :param errors: An array of error messages. Each endpoint documents how/whether this field is
            used.
        :type errors: [str], optional

        :param metadata: The metadata object containing additional information about the list of SLOs.
        :type metadata: SLOListResponseMetadata, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
