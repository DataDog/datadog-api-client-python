# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsPrivateLocationCreationResponseResultEncryption(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "id": (str,),
            "key": (str,),
        }

    attribute_map = {
        "id": "id",
        "key": "key",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Public key for the result encryption.

        :param id: Fingerprint for the encryption key.
        :type id: str, optional

        :param key: Public key for result encryption.
        :type key: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsPrivateLocationCreationResponseResultEncryption, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
