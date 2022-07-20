# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuthNMappingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.authn_mapping import AuthNMapping
        from datadog_api_client.v2.model.authn_mapping_included import AuthNMappingIncluded
        from datadog_api_client.v2.model.response_meta_attributes import ResponseMetaAttributes

        return {
            "data": ([AuthNMapping],),
            "included": ([AuthNMappingIncluded],),
            "meta": (ResponseMetaAttributes,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(self, *args, **kwargs):
        """
        Array of AuthN Mappings response.

        :param data: Array of returned AuthN Mappings.
        :type data: [AuthNMapping], optional

        :param included: Included data in the AuthN Mapping response.
        :type included: [AuthNMappingIncluded], optional

        :param meta: Object describing meta attributes of response.
        :type meta: ResponseMetaAttributes, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuthNMappingsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
