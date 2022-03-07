# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.slo_list_response_metadata_page import SLOListResponseMetadataPage

    globals()["SLOListResponseMetadataPage"] = SLOListResponseMetadataPage


class SLOListResponseMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "page": (SLOListResponseMetadataPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self, *args, **kwargs):
        """
        The metadata object containing additional information about the list of SLOs.

        :param page: The object containing information about the pages of the list of SLOs.
        :type page: SLOListResponseMetadataPage, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOListResponseMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
