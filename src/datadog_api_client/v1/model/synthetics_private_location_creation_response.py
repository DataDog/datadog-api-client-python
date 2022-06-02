# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsPrivateLocationCreationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_private_location import SyntheticsPrivateLocation
        from datadog_api_client.v1.model.synthetics_private_location_creation_response_result_encryption import (
            SyntheticsPrivateLocationCreationResponseResultEncryption,
        )

        return {
            "config": (dict,),
            "private_location": (SyntheticsPrivateLocation,),
            "result_encryption": (SyntheticsPrivateLocationCreationResponseResultEncryption,),
        }

    attribute_map = {
        "config": "config",
        "private_location": "private_location",
        "result_encryption": "result_encryption",
    }

    def __init__(self, *args, **kwargs):
        """
        Object that contains the new private location, the public key for result encryption, and the configuration skeleton.

        :param config: Configuration skeleton for the private location. See installation instructions of the private location on how to use this configuration.
        :type config: dict, optional

        :param private_location: Object containing information about the private location to create.
        :type private_location: SyntheticsPrivateLocation, optional

        :param result_encryption: Public key for the result encryption.
        :type result_encryption: SyntheticsPrivateLocationCreationResponseResultEncryption, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsPrivateLocationCreationResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
