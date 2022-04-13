# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    file_type,
)


class IdPMetadataFormData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "idp_file": (file_type,),
        }

    attribute_map = {
        "idp_file": "idp_file",
    }

    def __init__(self, *args, **kwargs):
        """
        The form data submitted to upload IdP metadata

        :param idp_file: The IdP metadata XML file
        :type idp_file: file_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IdPMetadataFormData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
