# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTriggerTest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_ci_batch_metadata import SyntheticsCIBatchMetadata

        return {
            "metadata": (SyntheticsCIBatchMetadata,),
            "public_id": (str,),
        }

    attribute_map = {
        "metadata": "metadata",
        "public_id": "public_id",
    }

    def __init__(self, public_id, *args, **kwargs):
        """
        Test configuration for Synthetics

        :param metadata: Metadata for the Synthetics tests run.
        :type metadata: SyntheticsCIBatchMetadata, optional

        :param public_id: The public ID of the Synthetics test to trigger.
        :type public_id: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.public_id = public_id

    @classmethod
    def _from_openapi_data(cls, public_id, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTriggerTest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.public_id = public_id
        return self
