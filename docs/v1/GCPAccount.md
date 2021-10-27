# GCPAccount

Your Google Cloud Platform Account.

## Properties

| Name                            | Type      | Description                                                                                                                                                                              | Notes      |
| ------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **auth_provider_x509_cert_url** | **str**   | Should be &#x60;https://www.googleapis.com/oauth2/v1/certs&#x60;.                                                                                                                        | [optional] |
| **auth_uri**                    | **str**   | Should be &#x60;https://accounts.google.com/o/oauth2/auth&#x60;.                                                                                                                         | [optional] |
| **automute**                    | **bool**  | Silence monitors for expected GCE instance shutdowns.                                                                                                                                    | [optional] |
| **client_email**                | **str**   | Your email found in your JSON service account key.                                                                                                                                       | [optional] |
| **client_id**                   | **str**   | Your ID found in your JSON service account key.                                                                                                                                          | [optional] |
| **client_x509_cert_url**        | **str**   | Should be &#x60;https://www.googleapis.com/robot/v1/metadata/x509/&lt;CLIENT_EMAIL&gt;&#x60; where &#x60;&lt;CLIENT_EMAIL&gt;&#x60; is the email found in your JSON service account key. | [optional] |
| **errors**                      | **[str]** | An array of errors.                                                                                                                                                                      | [optional] |
| **host_filters**                | **str**   | Limit the GCE instances that are pulled into Datadog by using tags. Only hosts that match one of the defined tags are imported into Datadog.                                             | [optional] |
| **private_key**                 | **str**   | Your private key name found in your JSON service account key.                                                                                                                            | [optional] |
| **private_key_id**              | **str**   | Your private key ID found in your JSON service account key.                                                                                                                              | [optional] |
| **project_id**                  | **str**   | Your Google Cloud project ID found in your JSON service account key.                                                                                                                     | [optional] |
| **token_uri**                   | **str**   | Should be &#x60;https://accounts.google.com/o/oauth2/token&#x60;.                                                                                                                        | [optional] |
| **type**                        | **str**   | The value for service_account found in your JSON service account key.                                                                                                                    | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
