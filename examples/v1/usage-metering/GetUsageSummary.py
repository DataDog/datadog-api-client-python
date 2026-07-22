"""
Get usage across your account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi as UsageMeteringApiV2
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
with ApiClient(configuration) as api_client:
    # Step 1: fetch the canonical field lists from the v2 discovery endpoint.
    v2_instance = UsageMeteringApiV2(api_client)
    fields_response = v2_instance.get_usage_summary_available_fields()
    attrs = fields_response.data.attributes
    response_fields = attrs.response_fields  # Layer 1 keys
    date_fields = attrs.date_fields  # Layer 2 keys
    date_org_fields = attrs.date_org_fields  # Layer 3 keys

    # Step 2: call the v1 summary endpoint with org details included.
    v1_instance = UsageMeteringApi(api_client)
    resp = v1_instance.get_usage_summary(
        start_month=datetime(2021, 11, 11, 11, 11, 11, 111000, tzinfo=tzutc()),
        include_org_details=True,
    )

    # Layer 1 – top-level UsageSummaryResponse additionalProperties
    print("=== Layer 1: UsageSummaryResponse ===")
    for field in response_fields:
        value = resp.get(field)
        if value is not None:
            print(f"  {field}: {value}")

    # Layer 2 – per-date UsageSummaryDate additionalProperties
    print("=== Layer 2: UsageSummaryDate (usage[]) ===")
    for date_entry in resp.get("usage") or []:
        date_label = date_entry.get("date", "unknown")
        for field in date_fields:
            value = date_entry.get(field)
            if value is not None:
                print(f"  [{date_label}] {field}: {value}")

        # Layer 3 – per-org UsageSummaryDateOrg additionalProperties
        print(f"  === Layer 3: UsageSummaryDateOrg (usage[].orgs[]) for {date_label} ===")
        for org in date_entry.get("orgs") or []:
            org_label = org.get("name", org.get("id", "unknown"))
            for field in date_org_fields:
                value = org.get(field)
                if value is not None:
                    print(f"    [{org_label}] {field}: {value}")
